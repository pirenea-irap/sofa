#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#        Copyright (c) IRAP CNRS
#        Odile Coeur-Joly, Toulouse, France
#
"""
This module manages the PIRENEA filenames.
"""
import logging
import os
log = logging.getLogger('root')


class FilesAndDirs(object):

    """
    Manage to find spectra in data directories
    """

    def __init__(self, folder="D:", year=2014, month=5, day=12):
        """
        Constructor
        """
        self.year = int(year)
        self.month = int(month)
        self.day = int(day)
        self.folder = folder + os.sep + "PIRENEA" + os.sep + "DATA"
        self.files = []

    def get_years(self, folder):
        """
        Returns a list of years, for one folder
        """
        self.folder = folder
        dirname = os.path.abspath(self.folder)
        list_years = []

        if not os.path.isdir(dirname):
            log.error("Not a directory: %s", dirname)
        else:
            li = os.listdir(dirname)
            for y in li:
                if len(y) == 4 and y.isdecimal():
                    list_years.append(y)
        return list_years

    def get_months(self, year):
        """
        Return a list of months for one directory
        """
        self.year = year
        dirname = self.folder + os.sep + '%d' % self.year
        dirname = os.path.join(self.folder, dirname)
        list_months = []

        if not os.path.isdir(dirname):
            log.error("Not a directory: %s", dirname)
        else:
            di = os.listdir(dirname)
            for d in di:
                if len(d) == 15:
                    list_months.append(d[10:12])
            list_months = list(dict().fromkeys(list_months).keys())
            list_months.sort()

        return list_months

    def get_days(self, year, month):
        """
        Return a list of spectrum numbers for one directory
        """
        self.year = year
        self.month = month
        dirname = self.folder + os.sep + '%d' % self.year
        dirname = os.path.join(self.folder, dirname)
        list_days = []

        if not os.path.isdir(dirname):
            log.error("Not a directory: %s", dirname)
        else:
            di = os.listdir(dirname)
            for d in di:
                if len(d) == 15:
                    if (d[10:12] == ('%02d' % self.month)):
                        list_days.append(d[13:15])
            list_days = list(dict().fromkeys(list_days).keys())
            list_days.sort()

        return list_days

    def get_dirname(self, folder, year, month, day):
        """
        Return a full path name of one directory
        """
        self.folder = folder
        self.year = year
        self.month = month
        self.day = day

        # create directory name
        directory = self.folder + os.sep + \
            '%d' % self.year + os.sep + \
            "data_" + '%d' % self.year + \
            "_" + '%02d' % self.month + \
            "_" + '%02d' % self.day

        dirname = os.path.join(self.folder, directory)
#         print("directory=", dirname)

        return dirname

    def get_setup(self, dirname):
        """
        Return a list of setups for one directory
        """
        setups = []

        if not os.path.isdir(dirname):
            log.error("Not a directory: %s", dirname)
        else:
            self.files = os.listdir(dirname)
            for f in self.files:
                if len(f) == 21:
                    setups.append(f[0:2])
            """ remove duplicate names and sort the lists """
            setups = list(dict().fromkeys(setups).keys())
            setups.sort()

        return setups

    def get_spectra(self, dirname, setup):
        """
        Return a list of spectrum numbers for one directory
        """
        spectra = []

        if not os.path.isdir(dirname):
            log.error("Not a directory: %s", dirname)
        else:
            self.files = os.listdir(dirname)
            for f in self.files:
                if len(f) == 21:
                    if (f[0:2] == (setup)):
                        spectra.append(f[14:17])
            """ remove duplicate names and sort the lists """
            spectra = list(dict().fromkeys(spectra).keys())
            spectra.sort()

        return spectra

    def get_acquis(self, directory, setup, specNum):
        """
        Return a list of (acquisitions, accumulations) for one spectrum
        """
        dirname = directory
        acquis = []

        if not os.path.isdir(dirname):
            log.error("Not a directory: %s", dirname)
        else:
            self.files = os.listdir(dirname)
            for f in self.files:
                if len(f) == 21:
                    if (f[0:2] == (setup) and f[14:17] == (specNum)):
                        acquis.append(f[18:19])
            """ remove duplicate names and sort the lists """
            acquis = list(dict().fromkeys(acquis).keys())
            acquis.sort()

        return acquis

    def get_accums(self, directory, setup, specNum, acquis):
        """
        Return a list of (accumulations) for one spectrum
        """
        dirname = directory
        accums = []

        if not os.path.isdir(dirname):
            log.error("Not a directory: %s", dirname)
        else:
            self.files = os.listdir(dirname)
            for f in self.files:
                if len(f) == 21:
                    if (f[0:2] == (setup) and f[14:17] == (specNum) and f[18:19] == (acquis)):
                        accums.append(f[19:21])
            """ remove duplicate names and sort the lists """
            accums = list(dict().fromkeys(accums).keys())
            accums.sort()

        return accums

    def get_spectrumName(self, directory, year, month, day, setup, specNum, acquis, accum):
        """
        Return a spectrum name from a given directory, number, acquis, accum
        """
        dirname = directory
        spectrumName = ""

        if not os.path.isdir(dirname):
            log.error("Not a directory: %s", dirname)
        else:
            # create spectrum name
            spectrumName = dirname + os.sep + \
                '%s' % setup + str("_") + \
                '%d' % int(year) + str("_") + \
                '%02d' % int(month) + str("_") + \
                '%02d' % int(day) + str("_") + \
                '%03d' % int(specNum) + str(".") + \
                str(acquis) + \
                '%02d' % int(accum)
        return spectrumName


if __name__ == '__main__':

    """
    main method to test this script as a unit test.
    """
    fi = FilesAndDirs()
    years = fi.get_years("Y:\\")
    print("years=", years)
    months = fi.get_months(int("2018"))
    print("months=", months)
    days = fi.get_days(2018, int("01"))
    print("days=", days)
    dirname = fi.get_dirname("Y:\\", int("2018"), int("01"), int("23"))
    print("dirname=", dirname)
    setups = fi.get_setup(dirname)
    print("setups=", setups)
    spectra = fi.get_spectra(dirname, str("P1"))
    print("spectra=", spectra)
    acquis = fi.get_acquis(dirname, str("P1"), str("001"))
    print("acquis=", acquis)
    accums = fi.get_accums(dirname, str("P1"), str("001"), str("A"))
    print("accums=", accums)
    specName = fi.get_spectrumName(dirname,
                                   int("2018"),
                                   int("01"),
                                   int("23"),
                                   str("P1"),
                                   str("001"),
                                   str("A"),
                                   str("00")
                                   )
    print("name = ", specName)

else:
    log.info("Importing... %s", __name__)
