#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#        Copyright (c) IRAP CNRS
#        Odile Coeur-Joly, Toulouse, France
#
"""
This module manages the GUI of the sequence viewer.
"""

from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QDockWidget

from gui.sequence_qt import Ui_DockWidget_Sequence
import logging
log = logging.getLogger('root')


class SequenceGUI(QDockWidget):

    """
    classdocs
    """

    def __init__(self, **kwds):
        super().__init__(**kwds)
        self.ui = Ui_DockWidget_Sequence()
        self.ui.setupUi(self)

    def setup(self):
        self.model = QStandardItemModel(2, 5)
        self.ui.tableView_Sequence.setModel(self.model)


if __name__ == '__main__':
    pass
else:
    log.info("Importing... %s", __name__)
