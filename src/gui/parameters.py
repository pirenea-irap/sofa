#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#        Copyright (c) IRAP CNRS
#        Odile Coeur-Joly, Toulouse, France
#
"""
This module manages the GUI of the parameters viewer.
"""
from PyQt5.QtWidgets import QDockWidget

from gui.parameters_qt import Ui_DockWidget_Parameters
from pkg.xml import XMLPirenea

import logging
log = logging.getLogger('root')


class ParametersGUI(QDockWidget):

    """
    classdocs
    """

    """ constructor """

    def __init__(self, parent=None):
        super(ParametersGUI, self).__init__(parent)
        self.ui = Ui_DockWidget_Parameters()
        self.ui.setupUi(self)

    """ connect to events emitted by the data_selector """

    def setup(self, analysis):
        self.ana = analysis
        self.ana.parametersRaisedSignal.connect(self.fill_params)
        self.ui.comboBox_EjectName.currentIndexChanged.connect(
            self.toggle_ejection)

    def fill_params(self, filename, pipeline):
        log.debug("event from %s", self.sender())
        short = str(filename).split(sep="\\")
        self.ui.lineEdit_File.setText(short[-1])
        self.filename = filename

        if pipeline.raw.scriptable:
            self.enable_parameters_box()
            self.ui.groupBox_Comment.setVisible(False)
            s = pipeline.scr
            self.excitBuffer, self.excitation = s.get_excit()
            self.ejectBuffer, self.ejection = s.get_eject()
            self.detectBuffer, self.detection = s.get_detect()
            # clear old values
            self.update_excitation()
            self.update_ejections()
            self.update_detection()
        else:
            # clear previous comment
            self.disable_parameters_box()
            self.ui.textEdit_Comment.clear()
            self.ui.groupBox_Comment.setVisible(True)
            xmltree = XMLPirenea(self.filename + ".xml")
            comment = xmltree.get_comment()
            self.ui.textEdit_Comment.append(comment)

    def toggle_ejection(self):
        log.debug("event from %s", self.sender())
        self.ui.lineEdit_EjectType.clear()
        self.ui.lineEdit_EjectDuration.clear()
        self.ui.comboBox_EjectIntensity.clear()
        self.ui.comboBox_EjectStart.clear()
        self.ui.comboBox_EjectEnd.clear()
        index = self.ui.comboBox_EjectName.currentIndex()
        # test if items exist
        if self.ejection and index >= 0:
            intensity = []
            start = []
            end = []
            if len(self.ejectBuffer[index]) > 1:
                wave = self.ejectBuffer[index][2]
                duration = "{:.1f}".format(float(self.ejectBuffer[index][3]))
                intensity.append(
                    "{:.1f}".format(float(self.ejectBuffer[index][4])))
                start.append(
                    "{:.1f}".format(float(self.ejectBuffer[index][5])))
            if len(self.ejectBuffer[index]) > 6:
                end.append("{:.1f}".format(float(self.ejectBuffer[index][6])))
            if len(self.ejectBuffer[index]) > 7:
                intensity.append(
                    "{:.1f}".format(float(self.ejectBuffer[index][7])))
                start.append(
                    "{:.1f}".format(float(self.ejectBuffer[index][8])))
                end.append("{:.1f}".format(float(self.ejectBuffer[index][9])))
            if duration:
                self.ui.lineEdit_EjectDuration.setText(duration)
                self.ui.lineEdit_EjectType.setText(wave)
                self.ui.comboBox_EjectIntensity.addItems(intensity)
                self.ui.comboBox_EjectStart.addItems(start)
                self.ui.comboBox_EjectEnd.addItems(end)

    def enable_parameters_box(self):
        self.ui.groupBox_Detect.setVisible(True)
        self.ui.groupBox_Eject.setVisible(True)
        self.ui.groupBox_Excit.setVisible(True)

    def disable_parameters_box(self):
        self.ui.groupBox_Detect.setVisible(False)
        self.ui.groupBox_Eject.setVisible(False)
        self.ui.groupBox_Excit.setVisible(False)

    def update_excitation(self):
        self.ui.lineEdit_ExcitType.clear()
        self.ui.lineEdit_ExcitDuration.clear()
        self.ui.lineEdit_ExcitIntensity.clear()
        self.ui.lineEdit_ExcitStart.clear()
        self.ui.lineEdit_ExcitEnd.clear()
        if self.excitation:
            if len(self.excitBuffer[0]) >= 7:
                wave = self.excitBuffer[0][2]
                self.ui.lineEdit_ExcitType.setText(wave)
                self.ui.lineEdit_ExcitDuration.setText(
                    "{:.1f}".format(float(self.excitBuffer[0][3])))
                self.ui.lineEdit_ExcitIntensity.setText(
                    "{:.1f}".format(float(self.excitBuffer[0][4])))
                self.ui.lineEdit_ExcitStart.setText(
                    "{:.1f}".format(float(self.excitBuffer[0][5])))
                self.ui.lineEdit_ExcitEnd.setText(
                    "{:.1f}".format(float(self.excitBuffer[0][6])))
            else:
                self.ui.lineEdit_ExcitType.setText(self.excitation)

    def update_ejections(self):
        self.ui.comboBox_EjectName.clear()
        if self.ejection:
            self.ui.comboBox_EjectName.addItems(self.ejection)

    def update_detection(self):
        self.ui.comboBox_DetectName.clear()
        if self.detection:
            self.ui.comboBox_DetectName.addItem(self.detection)


if __name__ == '__main__':
    pass
else:
    log.info("Importing... %s", __name__)
