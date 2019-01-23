#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#        Copyright (c) IRAP CNRS
#        Odile Coeur-Joly, Toulouse, France
#
"""

pkg.masstab_file Created on 23 jan. 2018
"""
import logging
log = logging.getLogger("root")

if __name__ == '__main__':

    import numpy as np
    import os
    from pkg.pipeline import Pipeline
    from pkg.peaks import Peaks

    out_filename = "D:\\PIRENEA\\DATA\\MASS\\My_Masstab_File.txt"

    # Put your own path here
    fpath = "D:\\PIRENEA\\DATA\\2019\\data_2019_01_21"
    num = input("PATH = " + fpath + ": \n" + "==> spectrum number ? (ex: 070): ")

    # For Gabi: howto take a list of spectra (here 10 accumulations)
    filename_list = [f for f in os.listdir(fpath)
                     if f[-4:] != ".xml"
                     if f[-7:-4] == str(num)]
    for i, filename in enumerate(filename_list):
        filename_list[i] = os.path.join(fpath, filename)

    # # Put your own settings here
    mass_list = [89.0, 151.0, 152.0, 176.0, 177.0, 178.0]

    mass_list = sorted(mass_list)
    acc = 0.2  # This is accuracy for peak search, in mass unit
    list_i = [[0] * len(filename_list) for i in range(len(mass_list))]

    # File header
    text = "\n" + " " * 24
    for mass in mass_list:
        text = text + (str(mass) + "_M").ljust(9) + (str(mass) + "_I").ljust(9)
    text = text + "\n" + "=" * 21

    # Loop for filenames
    for i, filename in enumerate(filename_list):
        # Signal processing
        pip = Pipeline(filename)
        # Put your own settings here: start signal, end signal and Hanning
        start = pip.start
        start = 10000
        end = pip.end
        end = 1010000
        hann = False
        pip.process_signal(start, end, hann, False, False, False)
        pip.process_spectrum(factor=1000.0, ref_mass=300.0939, cyclo_freq=255.692e3,
                             mag_freq=0.001e3)

        x = np.asarray(pip.mass)
        y = np.asarray(pip.spectrum)

        # Peak search
        p = Peaks()
        dict_m, dict_i = p.masstab_peaks(x, y, mass_list, acc)

        short_name = os.path.basename(filename)
        text = text + "\n" + str(short_name).ljust(24)
        for mass in mass_list:
            text = text + \
                "{:.4f}".format(float(dict_m[mass])).ljust(9) + \
                "{:.3f}".format(float(dict_i[mass])).ljust(9)

    # Write result into file: this is the same masstab.txt file as within sofa
    with open(out_filename, mode='w', encoding='utf_8') as file:
        file.write(text)
    # debug
    print(text)

else:
    log.info("Importing... %s", __name__)
