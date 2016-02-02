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

from pkg.dictionary import Dictionary
import xml.etree.cElementTree as ET


class XMLFile(object):
    """
    classdocs
    """

    def __init__(self, XMLfilename="default.xml"):
        """
        Constructor
        """
        self.XMLfilename = XMLfilename

        """ global dict for XML element tags : avoid to modify the strings everywhere """
        di = Dictionary()
        self.d = di.parameters_dict
        self.ch = di.channels_dict

        root = ET.Element("Parameters")
        root.set("version", "0.1")
        root.text = (
            "XML file which contains the full set of PIRENEA parameters")

        self.fill_general(root)
        self.fill_sequence(root)

    def fill_general(self, root):
        """ 1 General parameters """
        parent = ET.SubElement(root, "general")
        parent.text = ("General parameters set by the user")
        ET.SubElement(parent, "user_name").text = ("Odile")
        ET.SubElement(parent, "project_name").text = ("PIRENEA")
        ET.SubElement(parent, "XML_filename").text = str(self.XMLfilename)
        ET.SubElement(parent, "date_time").text = str(
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def add_pulse(self, parent, channel, start_time, duration, function):

        child = ET.SubElement(parent, self.d["pulse"])
        ET.SubElement(
            child, self.d["channel"], number=self.ch[channel]).text = channel
        ET.SubElement(child, self.d["start_time"], units="ms").text = "{:.1f}".format(
            float(start_time))
        ET.SubElement(child, self.d["duration"], units="ms").text = "{:.1f}".format(
            float(duration))
        ET.SubElement(child, self.d["function"]).text = function

        return child

    def fill_sequence(self, root):
        """ Sequence Header"""
        parent = ET.SubElement(root, "sequence")
        parent.text = ("Sequence of pulses")
        ET.SubElement(parent, "sequence_filename").text = (
            "NationalInstruments.bin")

        """ Trapping  Pulses """
        self.add_pulse(parent, self.d["Gin"], "400", "500", self.d["trapping"])
        self.add_pulse(
            parent, self.d["GI_in"], "600", "700", self.d["trapping"])

        """ 2.2 Adiabatic pulse """
        child = ET.SubElement(parent, "pulse")
        ET.SubElement(child, self.d["channel"]).text = ("1")
        ET.SubElement(child, "start_time", units="ms").text = ("600")
        ET.SubElement(child, "duration", units="ms").text = ("0")
        ET.SubElement(child, "function").text = ("adiabatic")
#         baby = ET.SubElement(child, "adiabatic").text = ("Adiabatic low")
        baby = ET.SubElement(child, "adiabatic", units="Adiabatic low")
        ET.SubElement(baby, "start_value", units="V").text = ("4.0")
        ET.SubElement(baby, "end_value", units="V").text = ("-0.5")
        ET.SubElement(baby, "duration", units="ms").text = ("100")
        ET.SubElement(baby, "step_time", units="µs").text = ("10")

        """ Excitation pulse """
        child = ET.SubElement(parent, "pulse")
        ET.SubElement(child, self.d["channel"]).text = ("1")
        ET.SubElement(child, "start_time", units="ms").text = ("600")
        ET.SubElement(child, "duration", units="ms").text = ("0")
        ET.SubElement(child, "function").text = ("excitation")
#         baby = ET.SubElement(child, "buffer").text = ("Excitation Buffer")
        baby = ET.SubElement(child, "buffer", units="Excitation Buffer")
        ET.SubElement(baby, "buffer_filename").text = (
            "swift_1.2_80_250_300.buf")
        ET.SubElement(baby, "duration", units="ms").text = ("1.2")
        ET.SubElement(baby, "intensity", units="%").text = ("80")
        ET.SubElement(baby, "start_frequency", units="kHz").text = ("250")
        ET.SubElement(baby, "end_frequency", units="kHz").text = ("350")

        """ Detection pulse """
        child = ET.SubElement(parent, "pulse")
        ET.SubElement(child, self.d["channel"]).text = ("1")
        ET.SubElement(child, "start_time", units="ms").text = ("600")
        ET.SubElement(child, "duration", units="ms").text = ("0")
        ET.SubElement(child, "function").text = ("detection")

        """ Empty pulse for testing"""
        child = ET.SubElement(parent, "pulse")
        child.text = ("toto est beau")
        child.set("version", "3.3")

        for parent in root:
            print("parent.tag", parent.text)
            for child in parent:
                print("child.tag : ", child.tag, "=", child.text)
                for baby in child:
                    print("baby.tag : ", baby.tag, "=", baby.text)

        """ Find all occurrences of channel in root document """
        for channel in root.iter("channel"):
            print("text iter=", channel.text)

        """ Retrieve an empty occurrence """
        for pulse in root.findall("./sequence/pulse"):
            #             if len(pulse):
            if pulse.find(self.d["channel"]) is None:
                print("no channel found")
            else:
                print("text1=", pulse.find(self.d["channel"]).text)

        comment = ET.Comment("Second test of XML, héhé")
        root.append(comment)

        tree = ET.ElementTree(root)
        tree.write(self.XMLfilename, encoding="utf-8")

    def remove_pulse(self, tree, channel):

        root = tree.getroot()
        sequence = root.find('sequence')
        for pulse in sequence.iter("pulse"):
            print("pulse", pulse)
            for i in range(len(pulse)):
                if pulse[i].text == "adiabatic":
                    sequence.remove(pulse)
                print("i", i, pulse[i].text)

        liste = list(sequence.iter("pulse"))
        print("liste", liste)
        for channel in root.findall("./sequence/pulse/" + str(self.d["channel"])):
            print("channel", channel.text)
#         b = ET.SubElement(a, 'b')
#         c = ET.SubElement(b, 'c')
#         c.text = 'text3'
        tree = ET.ElementTree(root)
        tree.write("tata.xml", encoding="utf-8")

if __name__ == '__main__':
    #     import xml.etree.cElementTree as ET

    toto = XMLFile()
    tree = ET.parse("toto.xml")
    toto.remove_pulse(tree, 1)
else:
    print("\nImporting... ", __name__)
