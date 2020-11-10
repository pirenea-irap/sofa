#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#        Copyright (c) IRAP CNRS
#        Odile Coeur-Joly, Toulouse, France
#
"""
Process XML files for PIRENEA: retrieve parameters.
"""

import logging
import lxml.etree as etree

log = logging.getLogger("root")


class XMLPirenea(object):
    """
    classdocs
    """

    def __init__(self, filename="default"):
        """
        Constructor
        """
        self.filename = filename
        self.tree = []
        try:
            self.tree = etree.parse(self.filename)
        except (etree.LxmlError) as error:
            log.error("Unable to parse the XML file: %s, %s", self.filename, error)
        except (OSError) as error:
            log.error("%s", error)

    def get_comment(self):
        if self.tree:
            # TODO: absolute path should be checked with check XML version
            comment = self.tree.xpath("//EXPERIMENT_Inputs//Comment")
            # comment is a list
            if comment:
                return comment[0].text


if __name__ == '__main__':

    """
    main method to test this script as a unit test.
    """
    filename = "D:\\PIRENEA\\DATA\\2018\\data_2018_07_20\\P1_2018_07_20_025.A00.xml"
    xml = XMLPirenea(filename)

    # Retrieve the comment entered by user
    print("User comment : \n", xml.get_comment())

else:
    log.info("Importing... %s", __name__)
