# -*- coding: utf-8 -*-
"""
Created on 6 janv. 2015
@author: Odile

gui.sequence
"""

from PyQt5 import QtGui
from PyQt5 import QtWidgets

from gui.sequence_qt import Ui_DockWidget_Sequence


class SequenceGUI(QtWidgets.QDockWidget):

    """
    classdocs
    """

    def __init__(self, **kwds):
        super().__init__(**kwds)
        self.ui = Ui_DockWidget_Sequence()
        self.ui.setupUi(self)

    def setup(self):
        self.model = QtGui.QStandardItemModel(2, 5)
        self.ui.tableView_Sequence.setModel(self.model)


if __name__ == '__main__':
    pass
else:
    print("\nImporting... ", __name__)
