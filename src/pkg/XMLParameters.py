#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#        Copyright (c) IRAP CNRS
#        Odile Coeur-Joly, Toulouse, France
#
"""
Process XML files for PIRENEA.
"""
from datetime import datetime
import os

from pkg.dictionary import Dictionary
import xml.etree.cElementTree as ET


class XMLFile(object):

    """
    classdocs
    """

    def __init__(self, filename="default"):
        """
        Constructor
        """
        self.XMLfilename = filename + ".xml"
        """ global dict for XML element tags : avoid to modify the strings everywhere """
        di = Dictionary()
        self.d = di.parameters_dict
        self.ch = di.channels_dict

        if os.path.isfile(self.XMLfilename):
            print("XML file already exists")
            tree = ET.parse(self.XMLfilename)
            self.root = tree.getroot()
            self.general = self.root.find("general")
            self.analysis = self.root.find("analysis")
        else:
            print("XML file creation")
            self.__create()
            self.fill_general(
                "Chris", "PIRENEA", filename, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def __create(self):
        self.root = ET.Element("Parameters")
        self.root.set("version", "0.1")
        self.root.text = ("XML file with the full set of PIRENEA parameters")
        self.general = ET.SubElement(self.root, "general")
        self.general.text = ("General parameters set by the user")
        self.analysis = ET.SubElement(self.root, "analysis")
        self.analysis.text = ("Analysis parameters")

    def fill_general(self, user_name, project_name, raw_filename, date_time):
        """ General parameters """
        ET.SubElement(self.general, "user_name").text = str(user_name)
        ET.SubElement(self.general, "project_name").text = str(project_name)
        ET.SubElement(self.general, "raw_filename").text = str(raw_filename)
        ET.SubElement(self.general, "date_time").text = str(date_time)
#             datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def write_to_file(self):
        tree = ET.ElementTree(self.root)
        tree.write(self.XMLfilename, encoding="utf-8")

    def update_analysis_signal(self, points, start, end, duration):
        """ Signal part """
        duration = "{:.1f}".format(float(duration))
        sig = ET.SubElement(self.analysis, "signal")
        ET.SubElement(sig, "signal_length", units="points").text = str(points)
        ET.SubElement(sig, "start_signal", units="points").text = str(start)
        ET.SubElement(sig, "end_signal", units="points").text = str(end)
        ET.SubElement(sig, "excit_duration", units="ms").text = (duration)

    def update_analysis_mass(self, ref_mass, cyc_freq, mag_freq):
        """ Mass part """
        ref_mass = "{:.5f}".format(float(ref_mass))
        cyc_freq = "{:.3f}".format(float(cyc_freq))
        mag_freq = "{:.4f}".format(float(mag_freq))
        mass = ET.SubElement(self.analysis, "mass")
        ET.SubElement(mass, "ref_mass", units="u").text = (ref_mass)
        ET.SubElement(mass, "cyclotron_freq", units="Hz").text = (cyc_freq)
        ET.SubElement(mass, "magnetron_freq", units="Hz").text = (mag_freq)

#         """ Peak part """
#         mph = str(self.d["mph"])
#         mpd = str(self.d["mpd"])
#         pk = ET.SubElement(self.ana, "peaks")
#         ET.SubElement(pk, "mph", units="arb. unit").text = (mph)
#         ET.SubElement(pk, "mpd", units="points").text = (mpd)

    def get_analysis(self, tree):
        root = tree.getroot()
        analysis = root.find("analysis")
        for element in analysis:
            print("tag : ", element.tag, "=", element.text)
        """ Retrieve the duration occurrence """
        for pulse in root.findall("./sequence/pulse"):
            #             if len(pulse):
            if pulse.find(self.d["channel"]) is None:
                print("no channel found")
            else:
                print("text1=", pulse.find(self.d["channel"]).text)


if __name__ == '__main__':

    filename = "G:\\PIRENEA_manips\\2014\\data_2014_07_30\\2014_07_30_003.A00"
    toto = XMLFile(filename)
    toto.update_analysis_mass(300.0939, 255.727, 0.001)

    toto.write_to_file()
#
#     tree = ET.parse(filename + ".xml")
#     toto.get_analysis(tree)


else:
    print("\nImporting... ", __name__)
