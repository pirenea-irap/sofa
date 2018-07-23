#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#        Copyright (c) IRAP CNRS
#        Odile Coeur-Joly, Toulouse, France
#
"""
This module manages the GUI of the data selector.
"""
import logging

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDockWidget

from gui.data_selector_qt import Ui_DockWidget_DataSelector
from pkg.filenames import FilesAndDirs
log = logging.getLogger('root')


class DataSelectorGUI(QDockWidget):

    analysisRaisedSignal = pyqtSignal(str)
    masstabRaisedSignal = pyqtSignal(str)

    def __init__(self, parent=None):
        """
        constructor
        """
        super(DataSelectorGUI, self).__init__(parent)
        self.ui = Ui_DockWidget_DataSelector()
        self.ui.setupUi(self)
        self.filesAndDirs = FilesAndDirs()

    def setup(self):
        self.connect_events()
        self.fill_year()

    def connect_events(self):
        self.ui.lineEdit_Folder.textChanged.connect(self.fill_year)
        self.ui.comboBox_Year.currentIndexChanged.connect(self.fill_month)
        self.ui.comboBox_Month.currentIndexChanged.connect(self.fill_day)
        self.ui.comboBox_Day.currentIndexChanged.connect(self.fill_setup)
        self.ui.comboBox_Setup.currentIndexChanged.connect(self.fill_spectra)
        self.ui.comboBox_Number.currentIndexChanged.connect(self.fill_acquis)
        self.ui.comboBox_Acquis.currentIndexChanged.connect(self.fill_accums)
#         self.ui.checkBox_AutoUpdate.stateChanged.connect(self.toggle_update)
        self.ui.pushButton_StartAnalysis.clicked.connect(self.emit_signals)
        self.ui.pushButton_GetLast.clicked.connect(self.get_last)

    def fill_year(self):
        log.debug("event from %s", self.sender())
        self.ui.pushButton_GetLast.hide()
        self.ui.comboBox_Year.clear()
        self.folder = self.ui.lineEdit_Folder.text()
        li = self.filesAndDirs.get_years(self.folder)
        if li:
            self.ui.comboBox_Year.addItems(li)

    def fill_month(self):
        log.debug("event from %s", self.sender())
        self.ui.pushButton_GetLast.hide()
        self.ui.comboBox_Month.clear()
        self.year = self.ui.comboBox_Year.currentText()
        if self.year:
            months = self.filesAndDirs.get_months(int(self.year))
            if months:
                self.ui.comboBox_Month.addItems(months)

    def fill_day(self):
        log.debug("event from %s", self.sender())
        self.ui.pushButton_GetLast.hide()
        self.ui.comboBox_Day.clear()
        self.ui.lineEdit_Directory.clear()
        self.month = self.ui.comboBox_Month.currentText()
        if self.month:
            days = self.filesAndDirs.get_days(int(self.year), int(self.month))
            if days:
                self.ui.comboBox_Day.addItems(days)

    def fill_setup(self):
        log.debug("event from %s", self.sender())
        self.ui.pushButton_GetLast.hide()
        self.ui.comboBox_Setup.clear()
        self.day = self.ui.comboBox_Day.currentText()
        if self.day:
            self.directory = self.filesAndDirs.get_dirname(self.folder, int(self.year),
                                                           int(self.month), int(self.day))
            self.ui.lineEdit_Directory.setText(self.directory)
            if self.directory:
                setups = self.filesAndDirs.get_setup(self.directory)
                self.ui.comboBox_Setup.addItems(setups)

    def fill_spectra(self, last=False):
        log.debug("event from %s", self.sender())
        self.ui.comboBox_Number.clear()
        self.setup = self.ui.comboBox_Setup.currentText()
        if self.setup:
            spectra = self.filesAndDirs.get_spectra(self.directory, self.setup)
            if spectra:
                self.ui.comboBox_Number.addItems(spectra)
                if last:
                    self.ui.comboBox_Number.setCurrentIndex(len(spectra) - 1)

    def fill_acquis(self):
        log.debug("event from %s", self.sender())
        self.ui.comboBox_Acquis.clear()
        self.specNum = self.ui.comboBox_Number.currentText()
        if self.specNum:
            acquis = self.filesAndDirs.get_acquis(self.directory, self.setup, self.specNum)
            if acquis:
                self.ui.comboBox_Acquis.addItems(acquis)

    def fill_accums(self):
        log.debug("event from %s", self.sender())
        self.ui.comboBox_Accum.clear()
        self.acquis = self.ui.comboBox_Acquis.currentText()
        if self.acquis:
            accums = self.filesAndDirs.get_accums(
                self.directory, self.setup, self.specNum, self.acquis)
            if accums:
                self.ui.comboBox_Accum.addItems(accums)

#     def toggle_update(self):
#         log.debug("event from %s", self.sender())
#         if self.ui.checkBox_AutoUpdate.isChecked():
#             self.ui.pushButton_UpdatePlot.setDisabled(True)
#         else:
#             self.ui.pushButton_UpdatePlot.setEnabled(True)

    def emit_signals(self):
        log.debug("event from %s", self.sender())
        self.accum = self.ui.comboBox_Accum.currentText()
        self.ui.pushButton_GetLast.show()
        if self.accum:
            spectrumName = self.filesAndDirs.get_spectrumName(
                self.directory, self.year, self.month, self.day,
                self.setup, self.specNum, self.acquis, self.accum)
            self.analysisRaisedSignal.emit(spectrumName)
            self.masstabRaisedSignal.emit(spectrumName)
        else:
            log.error("No data, accumulation not selected")

    def get_last(self):
        log.debug("event from %s", self.sender())
        self.fill_spectra(last=True)
        self.fill_acquis()
        self.fill_accums()


if __name__ == '__main__':
    pass
else:
    log.info("Importing... %s", __name__)
