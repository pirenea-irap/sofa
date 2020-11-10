#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#        Copyright (c) IRAP CNRS
#        Odile Coeur-Joly, Toulouse, France
#
"""
This module manages the PIRENEA raw datasets.
"""
import logging
import os.path
import struct

from numpy.core import numeric as num
from numpy.core import umath as math

import numpy as np
from pkg.script import Script

log = logging.getLogger('root')


class RawDataset(object):

    """
    Manage PIRENEA old files (big-endian).

    :Example:

    >>> from pkg.dataset import RawDataset
    >>> filename = "Y:\\2018\\data_2018_07_20\\P1_2018_07_20_001.A00"
    >>> s = RawDataset(filename)
    """

    def __init__(self, filename=""):
        """
        Constructor
        """
        self.filename = filename
        self.points = 0
        self.signal = []
        self.step = 0.0
        self.start = 0
        self.end = 0
        self.scriptable = False
        self.text = ""

        self.__read_file()
#         self.__find_limits()

    def __read_file(self):
        """
        Read a PIRENEA binary file, in big-endian format.
        Populate signal[] with the raw signal values and step in microseconds.
        """
        try:
            # Read first integer with number of points
            dt = np.dtype([('points', '>i4')])
            data = np.fromfile(self.filename, dtype=dt, count=1)
            self.points = data['points'][0]
            filesize = os.path.getsize(self.filename)
            # new PIRENEA setup : samples written as long integer
            if (filesize < self.points * 4):
                dt = np.dtype([('points', '>i4'), ('samples', '>i2', self.points),
                               ('step', '>f4'), ('gain', '>f4'), ('offset', '>f4')])
                data = np.fromfile(self.filename, dtype=dt)
                self.signal = data['samples'].ravel() * data['gain'] + data['offset']
                self.step = data['step'][0]  # step in seconds

                # No script for new PIRENEA setup
                self.text = ""

            else:
                # old PIRENEA setup : samples written as float
                dt = np.dtype([('points', '>i4'), ('samples', '>f', (self.points,)),
                               ('step', '>f')])
                data = np.fromfile(self.filename, dtype=dt)
                self.signal = data['samples'].ravel()
                self.step = data['step'][0] * 1e-6  # step in microseconds

                # Skip the binary part and read the script (readlines is faster)
                with open(self.filename, mode="rb") as fir:
                    fir.read(4 + (4 * self.points) + 4)
                    self.text = fir.readlines()

            if len(self.text) > 0:
                self.scriptable = True
                if os.path.isfile(self.filename + "_sc.txt"):
                    pass
                else:
                    with open(self.filename + "_sc.txt", mode="w", encoding='utf_8') as file:
                        log.info("Script file creation...")
                        for line in self.text:
                            # strip removes all whitespace characters
                            if line.strip():
                                linew = line.decode('utf_8')
                                if linew[0] != '/' and linew[0] != '':
                                    file.write(linew)
            else:
                self.scriptable = False

        except (IOError) as error:
            log.error("Unable to open : %s", error)
        except (struct.error) as error:
            log.error("Not a valid binary file : %s", error)

    def __find_limits(self):
        """
        Find the beginning and the end of signal just after excitation buffer

        """
        # if script is available, get limits according excitation length
        if self.scriptable:
            s = Script(self.filename)
            duration = s.get_excit_duration()
            self.start = round(duration / self.step)
            self.end = round(self.points / 2)
        # if script is not available, fix arbitrary limits
        else:
            self.start = 0
            self.end = round(self.points / 2)

    def truncate(self, start=0, end=0):
        """
        Truncate the signal before start to remove excitation

        :param start: first interesting point of signal

        """
        if start < end:
            self.start = start
        if end > 0:
            self.end = end
        truncated = self.signal[self.start:self.end]

        return truncated

    def hann(self, signal, half=False):
        """
        Apply a Hann windowing on raw signal, before FFT.

        """
        points = len(signal)

        # Hanning from Herschel (half window)"""
        # hann = 0.5 * (1.0 + cos ((PI*i) / channels))"""
        if half:
            iarr = num.arange(points) * math.pi / points
            iarr = 0.5 + 0.5 * math.cos(iarr)
        # Hanning from numpy (full window)"""
        else:
            iarr = np.hanning(points)
        hann = signal * iarr

        return hann


if __name__ == '__main__':

    """
    main method to test this script as a unit test.
    """
    import matplotlib.pyplot as plt

#     filename = "D:\\PIRENEA\\PIRENEA_manips\\2014\\data_2014_05_12\\2014_05_12_004.A00"
#     filename = "F:\\PIRENEA_manips\\2015\\data_2015_02_11\\2015_02_11_001.A00"
    filename = "D:\\PIRENEA\\DATA\\2018\\data_2018_07_20\\P1_2018_07_20_025.A00"

    raw = RawDataset(filename)
    print("Number of points: ", raw.points)
    print("Step time: ", raw.step)
    print("first points:", raw.signal[0:8])
    print("last points:", raw.signal[:-4])

    truncated = raw.truncate(10, 100)
    print("length of truncated=", len(truncated), "length of signal=", len(raw.signal))

    hann = raw.hann(raw.signal, True)

    signal = raw.signal
#     signal = hann
#     signal = truncated
    points = len(signal)

    x = np.arange(points)
    # convert time in milliseconds
    x = x * raw.step * 1.e3
    plt.plot(x, signal)
    plt.show()

else:
    log.info("Importing... %s", __name__)
