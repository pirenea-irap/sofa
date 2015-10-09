#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#        Copyright (c) IRAP CNRS
#        Odile Coeur-Joly, Toulouse, France
#
"""
Define a global logger for the project.
Picked up from http://stackoverflow.com/questions/7621897/python-logging-module-globally
pkg.log Created on 9 oct. 2015
"""
import logging


class Logs(object):
    """
    Define a global logger.
    """

    def __init__(self, name):
        """
        Constructor
        """
        self.name = name

    def setup_debug_logger(self):
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(module)s - %(message)s", "%Y-%m-%d %H:%M:%S")

        handler = logging.StreamHandler()
        handler.setFormatter(formatter)

        logger = logging.getLogger(self.name)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
        return logger

    def setup_error_logger(self):
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(module)s - %(message)s", "%Y-%m-%d %H:%M:%S")

        handler = logging.StreamHandler()
        handler.setFormatter(formatter)

        logger = logging.getLogger(self.name)
        logger.setLevel(logging.ERROR)
        logger.addHandler(handler)
        return logger
