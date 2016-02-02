#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#        Copyright (c) IRAP CNRS
#        Odile Coeur-Joly, Toulouse, France
#
"""
This module manages the dictionary of XML parameters.
"""


class Dictionary(object):

    """
    classdocs
    """

    def __init__(self):
        """
        Constructor
        If necessary, change only the values in this dictionary (right part).
        Tags (left part) are fixed and should not be modified.

        """
        self.parameters_dict = {
            'pulse': 'pulse',
            'channel': 'channel',
            "start_time": "start_time",
            "duration": "duration",
            "function": "function",
            "trapping": "trapping",
            "emptying": "emptying",
            "adiabatic_low": "adiabatic_low",
            "adiabatic_high": "adiabatic_high",
            "Laser_aut": "Laser_aut",
            "Cryostat": "Cryostat",
            "Filter_int": "Filter_int",
            "Filter_ext": "Filter_ext",
            "Axial_up": "Axial_up",
            "Axial_down": "Axial_down",
            "Gain_int": "Gain_int",
            "Gain_ext": "Gain_ext",
            "Excitation": "Excitation",
            "Acquisition": "Acquisition",
            "Gin": "PAS BIEN",
            "GI_in": "GI_in",
            "GI_out": "GI_out",
            "Gout": "Gout",
            "ok1": "ok1",
            "ok2": "ok2",
            "Relay_1": "Relay_1",
            "Relay_2": "Relay_2",
            "Relay_3": "Relay_3",
            "Relay_4": "Relay_4",
            "Relay_5": "Relay_5",
            "Relay_6": "Relay_6",
            "Relay_7": "Relay_7",
            "Relay_8": "Relay_8",
            "Gas_1": "Gas_1",
            "Gas_2": "Gas_2",
            "Gas_3": "Gas_3",
            "Gas_4": "Gas_4",
            "Gas_5": "Gas_5",
            "Gas_6": "Gas_6",
            "Gas_7": "Gas_7",
            "Gas_8": "Gas_8",
            "ref_mass": "300.0939",
            "start_mass": "280.0",
            "end_mass": "310.0",
            "mph": "0.015",
            "mpd": "70",
        }
        print("Parameters have been initialized")

        """Change only the values in this Dictionary. """
        self.channels_dict = {
            self.parameters_dict["Laser_aut"]: "1",
            self.parameters_dict["Cryostat"]: "2",
            self.parameters_dict["Filter_int"]: "3",
            self.parameters_dict["Filter_ext"]: "4",
            self.parameters_dict["Axial_up"]: "5",
            self.parameters_dict["Axial_down"]: "6",
            self.parameters_dict["Gain_int"]: "7",
            self.parameters_dict["Gain_ext"]: "8",
            self.parameters_dict["Excitation"]: "9",
            self.parameters_dict["Acquisition"]: "10",
            self.parameters_dict["Gin"]: "11",
            self.parameters_dict["GI_in"]: "12",
            self.parameters_dict["GI_out"]: "13",
            self.parameters_dict["Gout"]: "14",
            self.parameters_dict["ok1"]: "15",
            self.parameters_dict["ok2"]: "16",
            self.parameters_dict["Relay_1"]: "17",
            self.parameters_dict["Relay_2"]: "18",
            self.parameters_dict["Relay_3"]: "19",
            self.parameters_dict["Relay_4"]: "20",
            self.parameters_dict["Relay_5"]: "21",
            self.parameters_dict["Relay_6"]: "22",
            self.parameters_dict["Relay_7"]: "23",
            self.parameters_dict["Relay_8"]: "24",
            self.parameters_dict["Gas_1"]: "25",
            self.parameters_dict["Gas_2"]: "26",
            self.parameters_dict["Gas_3"]: "27",
            self.parameters_dict["Gas_4"]: "28",
            self.parameters_dict["Gas_5"]: "29",
            self.parameters_dict["Gas_6"]: "30",
            self.parameters_dict["Gas_7"]: "31",
            self.parameters_dict["Gas_8"]: "32",
        }
        print("Channels have been initialized")

if __name__ == '__main__':

    #     print ("dico", Dictionary.pirenea_dict)
    #     d= Dictionary().parameters_dict
    d = Dictionary()
    par = d.parameters_dict
    ch = d.channels_dict

    print("channel gin", ch[par["Gin"]])
    print("channel PAS BIEN", ch["PAS BIEN"])

else:
    print("\nImporting... %s", __name__)
