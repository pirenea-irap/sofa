# -*- coding: utf-8 -*-
"""
This module manages the display of the data selector.
Created on 02 dec. 2014
@author: Odile
"""
from PyQt5 import QtCore
from PyQt5 import QtWidgets

from gui.main_window_qt import Ui_MainWindow


class MainWindowGUI(QtWidgets.QMainWindow):

    """ constructor """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def add_data_selector(self):
        self.ds = self.ui.dockWidget_DataSelector
        self.ds.ui.setupUi(self.ui.dockWidget_DataSelector)
        self.ds.setup()

    def add_analysis(self):
        self.ana = self.ui.dockWidget_Analysis
        self.ana.ui.setupUi(self.ui.dockWidget_Analysis)
        self.ana.setup(self.ds)

    def add_parameters(self):
        self.par = self.ui.dockWidget_Parameters
        self.par.ui.setupUi(self.ui.dockWidget_Parameters)
        self.par.setup(self.ana)

    def add_sequence(self):
        self.seq = self.ui.dockWidget_Sequence
        self.seq.ui.setupUi(self.ui.dockWidget_Sequence)
        self.seq.setup()

    def add_plots(self):
        """ Signal tab """
        self.plo = self.ui.tabWidget_Plots
        self.plo.setup(self.ana)

    def add_masstab_selector(self):
        self.sel = self.ui.dockWidget_MassTabSelector
        self.sel.ui.setupUi(self.ui.dockWidget_MassTabSelector)
        self.sel.setup()

    def add_masstab_viewer(self):
        self.view = self.ui.dockWidget_MassTabViewer
        self.view.ui.setupUi(self.ui.dockWidget_MassTabViewer)
        self.view.setup(self.sel, self.ana)


if __name__ == '__main__':

    import sys

    app = QtWidgets.QApplication(sys.argv)

    """ remove translator ==> switch to english for qt"""
    """ both qt messages and application messages are written in english """
    translator = QtCore.QTranslator()
    app.removeTranslator(translator)

    """ Load app specific translator """
    locale = QtCore.QLocale.system().name()
    if translator.load("main_window_qt-" + locale):
        app.installTranslator(translator)

    """ Load general translator for QT, for example : (cancel ==> annuler) """
    translatorQT = QtCore.QTranslator()
    path = QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.TranslationsPath)
    if translatorQT.load("qt_" + "fr", path):
        app.installTranslator(translatorQT)

    """ Logging"""
    from pkg.logs import Logs
    log = Logs("sofa").setup_debug_logger()
#     log = Logs("sofa").setup_error_logger()
    log.debug("debug test1")

    """ START here..."""
    """ START here..."""
    win = MainWindowGUI()
    log.info("debug test2")
    win.add_data_selector()
    win.add_analysis()
    win.add_parameters()
#     win.add_sequence()
    win.add_plots()
    win.add_masstab_selector()
    win.add_masstab_viewer()

    win.show()
    sys.exit(app.exec_())

else:
    print("\nImporting... ", __name__)
