#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#        Copyright (c) IRAP CNRS
#        Odile Coeur-Joly, Toulouse, France
#
"""
Process PIRENEA data.
"""
import logging
import numpy as np
from pkg.dataset import RawDataset
from pkg.peaks import Peaks
from pkg.script import Script
from pkg.spectrum import FrequencySpectrum
from pkg.spectrum import MassSpectrum
log = logging.getLogger('root')


class Pipeline(object):

    """
    classdocs
    """

    def __init__(self, filename=""):
        """
        Constructor
        """
        self.filename = filename
        self.__process_file()

    def __process_file(self):
        """ operations on files """
        self.raw = RawDataset(self.filename)
        self.step = self.raw.step
        self.points = self.raw.points
        self.scr = None
        # if script is available, get limits according excitation length
        if self.raw.scriptable:
            self.scr = Script(self.filename)
            duration = self.scr.get_excit_duration()
            self.start = round(duration / self.step)
            self.end = self.points
        # if script is not available, fix arbitrary limits
        else:
            self.start = 0
            self.end = self.points

    def process_signal(self, start=0, end=0, hann=False, half=False, zero=False, zero_twice=False):
        self.signal = self.raw.truncate(start, end)
        if hann:
            self.signal = self.raw.hann(self.signal, half=False)
        if half:
            self.signal = self.raw.hann(self.signal, half=True)
        if zero:
            dummy = np.zeros(self.points)
            if (end > self.points):
                end = self.points
            dummy[0:(end - start)] = self.signal
            self.signal = dummy
        if zero_twice:
            dummy = np.zeros(self.points * 2)
            if (end > self.points):
                end = self.points
            dummy[0:(end - start)] = self.signal
            self.signal = dummy

    def process_spectrum(self, factor=1000.0, ref_mass=0.0, cyclo_freq=0.0, mag_freq=0.0):
        #         t = time.time()
        fs = FrequencySpectrum(self.signal, self.step)
#         t1 = time.time() - t
        self.spectrum = fs.spectrum * factor
        self.freq = fs.freq  # in Hz
        ms = MassSpectrum(self.freq, ref_mass, cyclo_freq, mag_freq)
        self.mass = ms.mass

#     def get_excit_duration(self):
#         buffer, excitation = self.scr.get_excit()
#         if excitation:
#             return buffer[0][3]
#         else:
#             return 0.0

    def mass_recalibrate(self, ref_mass=0.0, accuracy=0.1):
        # Auto calib
        self.ref_mass = ref_mass
        self.accuracy = accuracy
        if ref_mass > 0.0:
            self.ms.basic_recalibrate(self.ref_mass, self.accuracy)

    def process_peaks(self, mph=0.0, mpd=0, startx=0.0, endx=0.0):

        if mph > 0:
            self.mph = mph
        if mpd > 0:
            self.mpd = mpd
        x = self.mass
        y = self.spectrum
        p = Peaks()
        ref = startx + (abs(endx - startx) / 2)
        delta = 1.0

        mph, mpd, mask = p.prepare_detect(ref, delta, x, y, startx, endx)

        # Detect peak on rising edge
        edge = 'rising'
        # Detect peak greater than threshold
        threshold = 0.0
        # Don't use default plot
        ind = p.detect_peaks(y[mask], self.mph, self.mpd, threshold, edge)
#             print("mass =", x[mask][ind])
#             print("inten=", y[mask][ind])

        self.mph = mph
        self.mpd = mpd
        self.mask = mask
        self.ind = ind


if __name__ == '__main__':

    import matplotlib.pyplot as plt

#     filename = "G:\\PIRENEA_manips\\2014\\data_2014_06_26\\2014_06_26_011.A00"
    filename = "D:\\PIRENEA\\DATA\\2018\\data_2018_07_20\\P1_2018_07_20_025.A00"

    pip = Pipeline(filename)
    pip.process_signal(pip.start, pip.end, False, False, False, False)
    pip.process_spectrum(factor=1000.0, ref_mass=300.0939, cyclo_freq=255.692e3, mag_freq=0.001e3)
    pip.process_peaks(mph=0.02, mpd=20.0, startx=290.0, endx=310.0)

    mask = pip.mask
    ind = pip.ind

    x = np.asarray(pip.mass)
    y = np.asarray(pip.spectrum)

    fig, ax = plt.subplots(1, 1)
    line1, = ax.plot(x[mask], y[mask], 'b', lw=1)

    line2, = ax.plot(
        x[mask][ind], y[mask][ind], '+', mfc=None, mec='r', mew=2, ms=8)

    ax.set_title("%s (mph=%.3f, mpd=%d)" % 
                 ('Peak detection', pip.mph, pip.mpd))
    # test annotations
    x = x[mask][ind]
    y = y[mask][ind]
    for i, j in zip(x, y):
        text = "{:.3f}".format(float(j)) + " (" + \
            "{:.4f}".format(float(i)) + ")"
        ax.annotate(text, xy=(i, j), xytext=(i, j), size=8)

    plt.show()

else:
    log.info("Importing... %s", __name__)
