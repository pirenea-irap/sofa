# -*- coding: utf-8 -*-
"""
This module manages the display of the data selector.

Created on 02 dec. 2014
@author: Odile
$Source$

"""
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal

from gui.data_selector_qt import Ui_DockWidget_DataSelector
from pkg.filenames import FilesAndDirs


class DataSelectorGUI(QtWidgets.QDockWidget):

    analysisRaisedSignal = pyqtSignal(str)
    masstabRaisedSignal = pyqtSignal(str)

    """ constructor """

    def __init__(self, parent=None):
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
        self.ui.comboBox_Day.currentIndexChanged.connect(self.fill_spectra)
        self.ui.comboBox_Number.currentIndexChanged.connect(self.fill_acquis)
        self.ui.comboBox_Acquis.currentIndexChanged.connect(self.fill_accums)
#         self.ui.checkBox_AutoUpdate.stateChanged.connect(self.toggle_update)
        self.ui.pushButton_StartAnalysis.clicked.connect(self.emit_signals)

    """ Fill input widgets with default values """

    def fill_year(self):
        # Year
        #         print("sender fill_year", self.sender())
        self.ui.comboBox_Year.clear()
        self.folder = self.ui.lineEdit_Folder.text()
        li = self.filesAndDirs.get_years(self.folder)
        if li:
            self.ui.comboBox_Year.addItems(li)

    """ Fill input widgets with default values """

    def fill_month(self):
        #         print("sender fill_month", self.sender())
        self.ui.comboBox_Month.clear()
        self.year = self.ui.comboBox_Year.currentText()
        if self.year:
            months = self.filesAndDirs.get_months(int(self.year))
            if months:
                self.ui.comboBox_Month.addItems(months)

    """ Fill input widgets with default values """

    def fill_day(self):
        #         print("sender fill_day", self.sender())
        self.ui.comboBox_Day.clear()
        self.ui.lineEdit_Directory.clear()
        self.month = self.ui.comboBox_Month.currentText()
        if self.month:
            days = self.filesAndDirs.get_days(int(self.year), int(self.month))
            if days:
                self.ui.comboBox_Day.addItems(days)

    """ update list of spectra """

    def fill_spectra(self):
        #         print("sender fill_spectra", self.sender())
        self.ui.comboBox_Number.clear()
        self.day = self.ui.comboBox_Day.currentText()
        if self.day:
            self.directory = self.filesAndDirs.get_dirname(self.folder, int(self.year),
                                                           int(self.month), int(self.day))
            self.ui.lineEdit_Directory.setText(self.directory)
            if self.directory:
                spectra = self.filesAndDirs.get_spectra(self.directory)
                self.ui.comboBox_Number.addItems(spectra)

    """ update list of acquis """

    def fill_acquis(self):
        #         print("sender fill_acquis", self.sender())
        self.ui.comboBox_Acquis.clear()
        self.specNum = self.ui.comboBox_Number.currentText()
        if self.specNum:
            acquis = self.filesAndDirs.get_acquis(self.directory, self.specNum)
            if acquis:
                self.ui.comboBox_Acquis.addItems(acquis)

    """ update list of spectra """

    def fill_accums(self):
        #         print("sender fill_accums", self.sender())
        self.ui.comboBox_Accum.clear()
        self.acquis = self.ui.comboBox_Acquis.currentText()
        if self.acquis:
            accums = self.filesAndDirs.get_accums(
                self.directory, self.specNum, self.acquis)
            if accums:
                self.ui.comboBox_Accum.addItems(accums)

#     def toggle_update(self):
#         print("sender toggle update", self.sender())
#         if self.ui.checkBox_AutoUpdate.isChecked():
#             self.ui.pushButton_UpdatePlot.setDisabled(True)
#         else:
#             self.ui.pushButton_UpdatePlot.setEnabled(True)

    def emit_signals(self):
        #         print("sender emit_signals", self.sender())
        self.accum = self.ui.comboBox_Accum.currentText()
        if self.accum:
            spectrumName = self.filesAndDirs.get_spectrumName(self.directory,
                                                              self.year, self.month, self.day,
                                                              self.specNum, self.acquis, self.accum)
            self.analysisRaisedSignal.emit(spectrumName)
            self.masstabRaisedSignal.emit(spectrumName)
        else:
            print("ERROR in: ", __name__)

if __name__ == '__main__':
    pass
else:
    print("\nImporting... ", __name__)
