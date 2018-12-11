#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#        Copyright (c) IRAP CNRS
#        Odile Coeur-Joly, Toulouse, France
#
"""

pkg.masstab_loop Created on 10 déc. 2018
"""
import logging
log = logging.getLogger("root")

if __name__ == '__main__':

    import numpy as np
    import os
    import matplotlib.pyplot as plt
    from pkg.pipeline import Pipeline
    from pkg.peaks import Peaks

    out_filename = "D:\\PIRENEA\\My_Masstab_File.txt"

    filename_list = ["Y:\\2018\\data_2018_07_20\\P1_2018_07_20_023.A00",
                     "Y:\\2018\\data_2018_07_20\\P1_2018_07_20_024.A00",
                     "Y:\\2018\\data_2018_07_20\\P1_2018_07_20_025.A00",
                     "Y:\\2018\\data_2018_07_20\\P1_2018_07_20_026.A00"]

    mass_list = [300.0, 298.0, 296.0, 301.0, 302.0]
    mass_list = sorted(mass_list)
    acc = 0.2  # This is accuracy for peak search, in mass unit
    hann = False
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
        pip.process_signal(pip.start, pip.end, hann, False, False, False)
        pip.process_spectrum(factor=1000.0, ref_mass=300.0939, cyclo_freq=255.692e3,
                             mag_freq=0.001e3)

        x = np.asarray(pip.mass)
        y = np.asarray(pip.spectrum)

        # Peak search
        p = Peaks()
        dict_m, dict_i = p.masstab_peaks(x, y, mass_list, acc)

        # Extract dict in list_i for future plots
        for j, mass in enumerate(mass_list):
            list_i[j][i] = float(dict_i[mass])

        short_name = os.path.basename(filename)
        text = text + "\n" + str(short_name).ljust(24)
        for mass in mass_list:
            text = text + \
                "{:.4f}".format(float(dict_m[mass])).ljust(9) + \
                "{:.3f}".format(float(dict_i[mass])).ljust(9)

    # Write result into file
    with open(out_filename, mode='w', encoding='utf_8') as file:
        file.write(text)
    # debug
    print(text)

    # use list_i to plot the peak intensities for each mass :
    xplot = range(len(filename_list))
    fig, ax = plt.subplots(1, 1)
    for i in range(len(mass_list)):
        yplot = list_i[i]
        line1, = ax.plot(xplot, yplot)
        ax.annotate("mass {}".format(mass_list[i]), xy=(xplot[1], yplot[1]), size=8)

    ax.set_title("intensity for one mass")
    plt.show()

else:
    log.info("Importing... %s", __name__)
