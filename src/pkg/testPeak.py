# -*- coding: utf-8 -*-
"""Detect peaks in data based on their amplitude and other features."""

import matplotlib.pyplot as plt
import numpy as np
from pkg.dataset import RawDataset
from pkg.spectrum import FrequencySpectrum
from pkg.spectrum import MassSpectrum


def detect_peaks(x, mph=None, mpd=1, threshold=0, edge='rising',
                 kpsh=False, valley=False, show=False, ax=None):
    """Detect peaks in data based on their amplitude and other features.

    Parameters
    ----------
    x : 1D array_like
        data.
    mph : {None, number}, optional (default = None)
        detect peaks that are greater than minimum peak height.
    mpd : positive integer, optional (default = 1)
        detect peaks that are at least separated by minimum peak distance (in
        number of data).
    threshold : positive number, optional (default = 0)
        detect peaks (valleys) that are greater (smaller) than `threshold`
        in relation to their immediate neighbors.
    edge : {None, 'rising', 'falling', 'both'}, optional (default = 'rising')
        for a flat peak, keep only the rising edge ('rising'), only the
        falling edge ('falling'), both edges ('both'), or don't detect a
        flat peak (None).
    kpsh : bool, optional (default = False)
        keep peaks with same height even if they are closer than `mpd`.
    valley : bool, optional (default = False)
        if True (1), detect valleys (local minima) instead of peaks.
    show : bool, optional (default = False)
        if True (1), plot data in matplotlib figure.
    ax : a matplotlib.axes.Axes instance, optional (default = None).

    Returns
    -------
    ind : 1D array_like
        indeces of the peaks in `x`.

    Notes
    -----
    The detection of valleys instead of peaks is performed internally by simply
    negating the data: `ind_valleys = detect_peaks(-x)`

    The function can handle NaN's

    See this IPython Notebook [1]_.

    References
    ----------
    .. [1] http://nbviewer.ipython.org/github/demotu/BMC/blob/master/notebooks/DetectPeaks.ipynb

    Examples
    --------
    >>> from detect_peaks import detect_peaks
    >>> x = np.random.randn(100)
    >>> x[60:81] = np.nan
    >>> # detect all peaks and plot data
    >>> ind = detect_peaks(x, show=True)
    >>> print(ind)

    >>> x = np.sin(2*np.pi*5*np.linspace(0, 1, 200)) + np.random.randn(200)/5
    >>> # set minimum peak height = 0 and minimum peak distance = 20
    >>> detect_peaks(x, mph=0, mpd=20, show=True)

    >>> x = [0, 1, 0, 2, 0, 3, 0, 2, 0, 1, 0]
    >>> # set minimum peak distance = 2
    >>> detect_peaks(x, mpd=2, show=True)

    >>> x = np.sin(2*np.pi*5*np.linspace(0, 1, 200)) + np.random.randn(200)/5
    >>> # detection of valleys instead of peaks
    >>> detect_peaks(x, mph=0, mpd=20, valley=True, show=True)

    >>> x = [0, 1, 1, 0, 1, 1, 0]
    >>> # detect both edges
    >>> detect_peaks(x, edge='both', show=True)

    >>> x = [-2, 1, -2, 2, 1, 1, 3, 0]
    >>> # set threshold = 2
    >>> detect_peaks(x, threshold = 2, show=True)
    """

    x = np.atleast_1d(x).astype('float64')
    if x.size < 3:
        return np.array([], dtype=int)
    if valley:
        x = -x
    # find indices of all peaks
    dx = x[1:] - x[:-1]
    # handle NaN's
    indnan = np.where(np.isnan(x))[0]
    if indnan.size:
        x[indnan] = np.inf
        dx[np.where(np.isnan(dx))[0]] = np.inf
    ine, ire, ife = np.array([[], [], []], dtype=int)
    if not edge:
        ine = np.where((np.hstack((dx, 0)) < 0) & (np.hstack((0, dx)) > 0))[0]
    else:
        if edge.lower() in ['rising', 'both']:
            ire = np.where(
                (np.hstack((dx, 0)) <= 0) & (np.hstack((0, dx)) > 0))[0]
        if edge.lower() in ['falling', 'both']:
            ife = np.where(
                (np.hstack((dx, 0)) < 0) & (np.hstack((0, dx)) >= 0))[0]
    ind = np.unique(np.hstack((ine, ire, ife)))
    # handle NaN's
    if ind.size and indnan.size:
        # NaN's and values close to NaN's cannot be peaks
        ind = ind[np.in1d(
            ind, np.unique(np.hstack((indnan, indnan - 1, indnan + 1))), invert=True)]
    # first and last values of x cannot be peaks
    if ind.size and ind[0] == 0:
        ind = ind[1:]
    if ind.size and ind[-1] == x.size - 1:
        ind = ind[:-1]
    # remove peaks < minimum peak height
    if ind.size and mph is not None:
        ind = ind[x[ind] >= mph]
    # remove peaks - neighbors < threshold
    if ind.size and threshold > 0:
        dx = np.min(
            np.vstack([x[ind] - x[ind - 1], x[ind] - x[ind + 1]]), axis=0)
        ind = np.delete(ind, np.where(dx < threshold)[0])
    # detect small peaks closer than minimum peak distance
    if ind.size and mpd > 1:
        ind = ind[np.argsort(x[ind])][::-1]  # sort ind by peak height
        idel = np.zeros(ind.size, dtype=bool)
        for i in range(ind.size):
            if not idel[i]:
                # keep peaks with the same height if kpsh is True
                idel = idel | (ind >= ind[i] - mpd) & (ind <= ind[i] + mpd) \
                    & (x[ind[i]] > x[ind] if kpsh else True)
                idel[i] = 0  # Keep current peak
        # remove the small peaks and sort back the indices by their occurrence
        ind = np.sort(ind[~idel])

    if show:
        if indnan.size:
            x[indnan] = np.nan
        if valley:
            x = -x
        _plot(x, mph, mpd, threshold, edge, valley, ax, ind)

    return ind


def prepare_detect_peak(central_mass, delta_mass, distance, x, y):
    # search values to detect peaks around a central value of mass
    m = central_mass
    d = distance
#     mask1 = [(x >= round(m) - a) & (x < round(m) + a)]
    mask1 = [(x >= m - d / 2) & (x < m + d / 2)]
    print("lenx=", len(x[mask1]))
    # take a delta of mass around the known mass
    mask = [(x > (m - delta_mass)) & (xx < (m + delta_mass))]
    # mask = [(xx > 600.0) & (xx < 610.0)]
    print("len=", len(y[mask]))
    print("sum=", np.sum(y[mask]))
    print("moyenne=", np.mean(y[mask]))

    # minimum peak height (to avoid peaks of noise)
    mph = np.mean(y[mask]) * 2.0
    # Minimum peak distance (to avoid edge peaks of same peak)
    mpd = len(x[mask1]) / 1.5

    return mph, mpd, mask


def _plot(x, mph, mpd, threshold, edge, valley, ax, ind):
    """Plot results of the detect_peaks function, see its help."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print('matplotlib is not available.')
    else:
        if ax is None:
            _, ax = plt.subplots(1, 1, figsize=(8, 4))

        ax.plot(x, 'b', lw=1)
        if ind.size:
            label = 'valley' if valley else 'peak'
            label = label + 's' if ind.size > 1 else label
            ax.plot(ind, x[ind], '+', mfc=None, mec='r', mew=2, ms=8,
                    label='%d %s' % (ind.size, label))
            ax.legend(loc='best', framealpha=.5, numpoints=1)
        ax.set_xlim(-.02 * x.size, x.size * 1.02 - 1)
        ymin, ymax = x[np.isfinite(x)].min(), x[np.isfinite(x)].max()
        yrange = ymax - ymin if ymax > ymin else 1
        ax.set_ylim(ymin - 0.1 * yrange, ymax + 0.1 * yrange)
        ax.set_xlabel('Data #', fontsize=14)
        ax.set_ylabel('Amplitude', fontsize=14)
        mode = 'Valley detection' if valley else 'Peak detection'
        ax.set_title("%s (mph=%s, mpd=%d, threshold=%s, edge='%s')"
                     % (mode, str(mph), mpd, str(threshold), edge))
        # plt.grid()
        plt.show()


# Read PIRENEA signal
filename = "G:\\PIRENEA_manips\\2013\\data_2013_03_22\\2013_03_22_003.A00"
# step = 0.5 262144
filename = "G:\\PIRENEA_manips\\2006\\data_2006_06_09\\2006_06_09_001.A01"
# step = 0.5 524288
filename = "G:\\PIRENEA_manips\\2013\\data_2013_03_22\\2013_03_22_003.A00"
# step = 0.1 262144
filename = "G:\\PIRENEA_manips\\2004\\data_2004_01_06\\2004_01_06_001.A01"
# step = 0.2 524288
filename = "G:\\PIRENEA_manips\\2014\\data_2014_07_30\\2014_07_30_001.A00"
# step = 0.5 524288
filename = "G:\\PIRENEA_manips\\2014\\data_2014_06_26\\2014_06_26_012.A00"
# step = 0.2 524288
filename = "G:\\PIRENEA_manips\\2014\\data_2014_05_12\\2014_05_12_005.E00"
# step = 0.2 524288
filename = "G:\\PIRENEA_manips\\2006\\data_2006_07_26\\2006_07_26_001.A00"
# step = 0.5 524288
filename = "G:\\PIRENEA_manips\\2014\\data_2014_06_26\\2014_06_26_013.A00"

data = RawDataset(filename)
data.hann()  # half window

points = len(data.signal)
start = data.start
end = round(points / 2)
data.truncate(start, end)

# data.truncate(data.start*2, round(len(data.signal)/2))
# excit = 1.2 ms / 0.5 micros ==> signal starts after point 2400
signal = data.signal
print("len signal =", len(signal))

# Real FFT on complete signal
step = data.step
print("step=", step)
fs = FrequencySpectrum(signal, step)
y = fs.spectrum * 1000.0        # ??? according to Anthony
# x = fs.freq / 1000.0            # in kHz

# Calculate mass
x = fs.freq
ms = MassSpectrum(x, y)
# Auto calib
ref_mass = 600.187
ref_mass = 300.0939
accuracy = 0.1
# ref_mass = 18.0
ms.auto_calib(ref_mass, accuracy)
xx = np.array(ms.mass)

# search values to detect peaks around a know mass
# mask1 = [(xx >= 26.0) & (xx < 27.0)]
# mask1 = [(xx >= 299.0) & (xx < 300.0)]
# mask1 = [(xx >= 599.0) & (xx < 600.0)]
# print("lenx=", len(xx[mask1]))
#
# mask = [(xx > 22.0) & (xx < 30.0)]
# mask = [(xx > 290.0) & (xx < 310.0)]
# mask = [(xx > 600.0) & (xx < 610.0)]
# print("len=", len(y[mask]))
# print("sum=", np.sum(y[mask]))
# print("moyenne=", np.mean(y[mask]))
#
# minimum peak height (to avoid peaks of noise)
# mph = 0.015
# mph = np.mean(y[mask]) * 2.0
# Minimum peak distance (to avoid edge peaks of same peak)
# 1 uma = 76 MHZ, if 0.2 µs : Fech = 5 MHz : interval = Fech*points = Fech*(end - start) : mpd = interval/76 * 2
# 1 uma = 76 MHZ, if 0.5 µs : 76/5 * 2 = 30
# mpd = round(76e6 / (1 / step) * float((end - start) / points) * 4)
# mpd = len(xx[mask1]) / 1.5
# mpd = round(76e6 / (1 / step) * float((end - start) / points) * 2)
delta = 10.0
distance = 1.0
mph, mpd, mask = prepare_detect_peak(ref_mass, delta, distance, xx, y)
print("mph=", mph, " mpd=", mpd, "len de mask y", len(y[mask]))
# Detect peak on rising edge
edge = 'rising'
# Detect peak greater than threshold
threshold = 0.0
# Don't use default plot
show = False

ind = detect_peaks(y[mask], mph, mpd, threshold, edge)
print("mass =", xx[mask][ind])
print("inten=", y[mask][ind])

fig, ax = plt.subplots(1, 1)
line1, = ax.plot(xx[mask], y[mask], 'b', lw=1)

line2, = ax.plot(
    xx[mask][ind], y[mask][ind], '+', mfc=None, mec='r', mew=2, ms=8)

ax.set_title("%s (mph=%.3f, mpd=%d, threshold=%s, edge='%s')"
             % ('Peak detection', mph, mpd, str(threshold), edge))
# test legende
# fig.legend([line2], ['nnn'])

# test annotations
x = xx[mask][ind]
y = y[mask][ind]
for i, j in zip(x, y):
    #     ax.annotate(str(j), xy=(i, j))
    ax.annotate("{:.3f}".format(float(j)), xy=(i, j))

plt.show()
