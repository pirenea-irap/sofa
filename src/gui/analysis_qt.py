# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file
'D:\S.O.F.T.S\PIRENEA\PYTHON\sofa\src\gui\analysis_qt.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DockWidget_Analysis(object):

    def setupUi(self, DockWidget_Analysis):
        DockWidget_Analysis.setObjectName("DockWidget_Analysis")
        DockWidget_Analysis.resize(1050, 200)
        DockWidget_Analysis.setMinimumSize(QtCore.QSize(1050, 200))
        DockWidget_Analysis.setMaximumSize(QtCore.QSize(1050, 200))
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.groupBox_Signal = QtWidgets.QGroupBox(self.dockWidgetContents)
        self.groupBox_Signal.setGeometry(QtCore.QRect(10, 30, 311, 131))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.groupBox_Signal.setFont(font)
        self.groupBox_Signal.setObjectName("groupBox_Signal")
        self.label_ExcitTruncate = QtWidgets.QLabel(self.groupBox_Signal)
        self.label_ExcitTruncate.setGeometry(QtCore.QRect(160, 10, 70, 16))
        self.label_ExcitTruncate.setObjectName("label_ExcitTruncate")
        self.label_EndTruncate = QtWidgets.QLabel(self.groupBox_Signal)
        self.label_EndTruncate.setGeometry(QtCore.QRect(240, 10, 70, 16))
        self.label_EndTruncate.setObjectName("label_EndTruncate")
        self.label_Step = QtWidgets.QLabel(self.groupBox_Signal)
        self.label_Step.setGeometry(QtCore.QRect(10, 30, 60, 16))
        self.label_Step.setObjectName("label_Step")
        self.label_Points = QtWidgets.QLabel(self.groupBox_Signal)
        self.label_Points.setGeometry(QtCore.QRect(10, 60, 65, 16))
        self.label_Points.setObjectName("label_Points")
        self.spinBox_StartSignal = QtWidgets.QSpinBox(self.groupBox_Signal)
        self.spinBox_StartSignal.setGeometry(QtCore.QRect(160, 60, 60, 20))
        self.spinBox_StartSignal.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.spinBox_StartSignal.setButtonSymbols(
            QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_StartSignal.setMaximum(10000000)
        self.spinBox_StartSignal.setProperty("value", 0)
        self.spinBox_StartSignal.setObjectName("spinBox_StartSignal")
        self.spinBox_DefEndSignal = QtWidgets.QSpinBox(self.groupBox_Signal)
        self.spinBox_DefEndSignal.setEnabled(False)
        self.spinBox_DefEndSignal.setGeometry(QtCore.QRect(240, 30, 60, 20))
        self.spinBox_DefEndSignal.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.spinBox_DefEndSignal.setButtonSymbols(
            QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_DefEndSignal.setMaximum(10000000)
        self.spinBox_DefEndSignal.setObjectName("spinBox_DefEndSignal")
        self.spinBox_EndSignal = QtWidgets.QSpinBox(self.groupBox_Signal)
        self.spinBox_EndSignal.setGeometry(QtCore.QRect(240, 60, 60, 20))
        self.spinBox_EndSignal.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.spinBox_EndSignal.setButtonSymbols(
            QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_EndSignal.setMaximum(10000000)
        self.spinBox_EndSignal.setObjectName("spinBox_EndSignal")
        self.spinBox_DefStartSignal = QtWidgets.QSpinBox(self.groupBox_Signal)
        self.spinBox_DefStartSignal.setEnabled(False)
        self.spinBox_DefStartSignal.setGeometry(QtCore.QRect(160, 30, 60, 20))
        self.spinBox_DefStartSignal.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.spinBox_DefStartSignal.setButtonSymbols(
            QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_DefStartSignal.setMaximum(10000000)
        self.spinBox_DefStartSignal.setObjectName("spinBox_DefStartSignal")
        self.doubleSpinBox_Step = QtWidgets.QDoubleSpinBox(
            self.groupBox_Signal)
        self.doubleSpinBox_Step.setEnabled(False)
        self.doubleSpinBox_Step.setGeometry(QtCore.QRect(80, 30, 60, 20))
        self.doubleSpinBox_Step.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_Step.setButtonSymbols(
            QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_Step.setDecimals(3)
        self.doubleSpinBox_Step.setMaximum(10.0)
        self.doubleSpinBox_Step.setObjectName("doubleSpinBox_Step")
        self.spinBox_Points = QtWidgets.QSpinBox(self.groupBox_Signal)
        self.spinBox_Points.setEnabled(False)
        self.spinBox_Points.setGeometry(QtCore.QRect(80, 60, 60, 20))
        self.spinBox_Points.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.spinBox_Points.setButtonSymbols(
            QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_Points.setMaximum(100000000)
        self.spinBox_Points.setProperty("value", 0)
        self.spinBox_Points.setObjectName("spinBox_Points")
        self.checkBox_Hann = QtWidgets.QCheckBox(self.groupBox_Signal)
        self.checkBox_Hann.setGeometry(QtCore.QRect(10, 95, 60, 17))
        self.checkBox_Hann.setChecked(True)
        self.checkBox_Hann.setObjectName("checkBox_Hann")
        self.buttonGroup_Hann = QtWidgets.QButtonGroup(DockWidget_Analysis)
        self.buttonGroup_Hann.setObjectName("buttonGroup_Hann")
        self.buttonGroup_Hann.addButton(self.checkBox_Hann)
        self.checkBox_ZeroFill = QtWidgets.QCheckBox(self.groupBox_Signal)
        self.checkBox_ZeroFill.setGeometry(QtCore.QRect(230, 90, 80, 17))
        self.checkBox_ZeroFill.setChecked(False)
        self.checkBox_ZeroFill.setObjectName("checkBox_ZeroFill")
        self.buttonGroup_Zero = QtWidgets.QButtonGroup(DockWidget_Analysis)
        self.buttonGroup_Zero.setObjectName("buttonGroup_Zero")
        self.buttonGroup_Zero.addButton(self.checkBox_ZeroFill)
        self.checkBox_HalfHann = QtWidgets.QCheckBox(self.groupBox_Signal)
        self.checkBox_HalfHann.setGeometry(QtCore.QRect(60, 95, 80, 17))
        self.checkBox_HalfHann.setChecked(False)
        self.checkBox_HalfHann.setObjectName("checkBox_HalfHann")
        self.buttonGroup_Hann.addButton(self.checkBox_HalfHann)
        self.checkBox_ZeroFillTwice = QtWidgets.QCheckBox(self.groupBox_Signal)
        self.checkBox_ZeroFillTwice.setGeometry(QtCore.QRect(230, 110, 90, 17))
        self.checkBox_ZeroFillTwice.setChecked(True)
        self.checkBox_ZeroFillTwice.setObjectName("checkBox_ZeroFillTwice")
        self.buttonGroup_Zero.addButton(self.checkBox_ZeroFillTwice)
        self.checkBox_NoZero = QtWidgets.QCheckBox(self.groupBox_Signal)
        self.checkBox_NoZero.setGeometry(QtCore.QRect(150, 100, 70, 17))
        self.checkBox_NoZero.setChecked(False)
        self.checkBox_NoZero.setObjectName("checkBox_NoZero")
        self.buttonGroup_Zero.addButton(self.checkBox_NoZero)
        self.groupBox_Mass = QtWidgets.QGroupBox(self.dockWidgetContents)
        self.groupBox_Mass.setGeometry(QtCore.QRect(340, 10, 340, 150))
        self.groupBox_Mass.setObjectName("groupBox_Mass")
        self.label_RefMass = QtWidgets.QLabel(self.groupBox_Mass)
        self.label_RefMass.setGeometry(QtCore.QRect(10, 31, 95, 16))
        self.label_RefMass.setObjectName("label_RefMass")
        self.label_CycloFreq = QtWidgets.QLabel(self.groupBox_Mass)
        self.label_CycloFreq.setGeometry(QtCore.QRect(10, 60, 95, 16))
        self.label_CycloFreq.setObjectName("label_CycloFreq")
        self.label_MagFreq = QtWidgets.QLabel(self.groupBox_Mass)
        self.label_MagFreq.setGeometry(QtCore.QRect(10, 90, 95, 16))
        self.label_MagFreq.setObjectName("label_MagFreq")
        self.label_PlotStartMass = QtWidgets.QLabel(self.groupBox_Mass)
        self.label_PlotStartMass.setGeometry(QtCore.QRect(10, 120, 95, 16))
        self.label_PlotStartMass.setObjectName("label_PlotStartMass")
        self.checkBox_Hold = QtWidgets.QCheckBox(self.groupBox_Mass)
        self.checkBox_Hold.setGeometry(QtCore.QRect(260, 120, 70, 17))
        self.checkBox_Hold.setObjectName("checkBox_Hold")
        self.doubleSpinBox_RefMass = QtWidgets.QDoubleSpinBox(
            self.groupBox_Mass)
        self.doubleSpinBox_RefMass.setGeometry(QtCore.QRect(110, 30, 70, 20))
        self.doubleSpinBox_RefMass.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_RefMass.setButtonSymbols(
            QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_RefMass.setDecimals(5)
        self.doubleSpinBox_RefMass.setMaximum(1000.0)
        self.doubleSpinBox_RefMass.setProperty("value", 303.0939)
        self.doubleSpinBox_RefMass.setObjectName("doubleSpinBox_RefMass")
        self.doubleSpinBox_CycloFreq = QtWidgets.QDoubleSpinBox(
            self.groupBox_Mass)
        self.doubleSpinBox_CycloFreq.setGeometry(QtCore.QRect(110, 60, 70, 20))
        self.doubleSpinBox_CycloFreq.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_CycloFreq.setButtonSymbols(
            QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_CycloFreq.setDecimals(5)
        self.doubleSpinBox_CycloFreq.setMaximum(1000.0)
        self.doubleSpinBox_CycloFreq.setProperty("value", 255.727)
        self.doubleSpinBox_CycloFreq.setObjectName("doubleSpinBox_CycloFreq")
        self.doubleSpinBox_MagFreq = QtWidgets.QDoubleSpinBox(
            self.groupBox_Mass)
        self.doubleSpinBox_MagFreq.setGeometry(QtCore.QRect(110, 90, 70, 20))
        self.doubleSpinBox_MagFreq.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_MagFreq.setButtonSymbols(
            QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_MagFreq.setDecimals(5)
        self.doubleSpinBox_MagFreq.setMaximum(100.0)
        self.doubleSpinBox_MagFreq.setProperty("value", 0.001)
        self.doubleSpinBox_MagFreq.setObjectName("doubleSpinBox_MagFreq")
        self.doubleSpinBox_PlotMassX1 = QtWidgets.QDoubleSpinBox(
            self.groupBox_Mass)
        self.doubleSpinBox_PlotMassX1.setGeometry(
            QtCore.QRect(110, 120, 60, 20))
        self.doubleSpinBox_PlotMassX1.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_PlotMassX1.setButtonSymbols(
            QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_PlotMassX1.setDecimals(1)
        self.doubleSpinBox_PlotMassX1.setMaximum(1000.0)
        self.doubleSpinBox_PlotMassX1.setProperty("value", 10.0)
        self.doubleSpinBox_PlotMassX1.setObjectName("doubleSpinBox_PlotMassX1")
        self.doubleSpinBox_PlotMassX2 = QtWidgets.QDoubleSpinBox(
            self.groupBox_Mass)
        self.doubleSpinBox_PlotMassX2.setGeometry(
            QtCore.QRect(180, 120, 60, 20))
        self.doubleSpinBox_PlotMassX2.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_PlotMassX2.setButtonSymbols(
            QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_PlotMassX2.setDecimals(1)
        self.doubleSpinBox_PlotMassX2.setMaximum(3000.0)
        self.doubleSpinBox_PlotMassX2.setProperty("value", 600.0)
        self.doubleSpinBox_PlotMassX2.setObjectName("doubleSpinBox_PlotMassX2")
        self.groupBox_Peak = QtWidgets.QGroupBox(self.dockWidgetContents)
        self.groupBox_Peak.setGeometry(QtCore.QRect(700, 40, 340, 81))
        self.groupBox_Peak.setObjectName("groupBox_Peak")
        self.label_PeakHeight = QtWidgets.QLabel(self.groupBox_Peak)
        self.label_PeakHeight.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.label_PeakHeight.setObjectName("label_PeakHeight")
        self.label_PeakDistance = QtWidgets.QLabel(self.groupBox_Peak)
        self.label_PeakDistance.setGeometry(QtCore.QRect(10, 55, 81, 16))
        self.label_PeakDistance.setObjectName("label_PeakDistance")
        self.label_StartMass = QtWidgets.QLabel(self.groupBox_Peak)
        self.label_StartMass.setGeometry(QtCore.QRect(190, 30, 70, 16))
        self.label_StartMass.setObjectName("label_StartMass")
        self.label_EndMass = QtWidgets.QLabel(self.groupBox_Peak)
        self.label_EndMass.setGeometry(QtCore.QRect(190, 55, 70, 16))
        self.label_EndMass.setObjectName("label_EndMass")
        self.doubleSpinBox_PeakHeight = QtWidgets.QDoubleSpinBox(
            self.groupBox_Peak)
        self.doubleSpinBox_PeakHeight.setGeometry(
            QtCore.QRect(100, 30, 60, 20))
        self.doubleSpinBox_PeakHeight.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_PeakHeight.setButtonSymbols(
            QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_PeakHeight.setDecimals(3)
        self.doubleSpinBox_PeakHeight.setObjectName("doubleSpinBox_PeakHeight")
        self.spinBox_PeakDistance = QtWidgets.QSpinBox(self.groupBox_Peak)
        self.spinBox_PeakDistance.setGeometry(QtCore.QRect(100, 55, 30, 20))
        self.spinBox_PeakDistance.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.spinBox_PeakDistance.setButtonSymbols(
            QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_PeakDistance.setMaximum(10000)
        self.spinBox_PeakDistance.setProperty("value", 0)
        self.spinBox_PeakDistance.setObjectName("spinBox_PeakDistance")
        self.doubleSpinBox_StartMass = QtWidgets.QDoubleSpinBox(
            self.groupBox_Peak)
        self.doubleSpinBox_StartMass.setGeometry(QtCore.QRect(260, 30, 60, 20))
        self.doubleSpinBox_StartMass.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_StartMass.setButtonSymbols(
            QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_StartMass.setDecimals(1)
        self.doubleSpinBox_StartMass.setMaximum(1000.0)
        self.doubleSpinBox_StartMass.setObjectName("doubleSpinBox_StartMass")
        self.doubleSpinBox_EndMass = QtWidgets.QDoubleSpinBox(
            self.groupBox_Peak)
        self.doubleSpinBox_EndMass.setGeometry(QtCore.QRect(260, 55, 60, 20))
        self.doubleSpinBox_EndMass.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_EndMass.setButtonSymbols(
            QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_EndMass.setDecimals(1)
        self.doubleSpinBox_EndMass.setMaximum(1000.0)
        self.doubleSpinBox_EndMass.setObjectName("doubleSpinBox_EndMass")
        self.spinBox_PeakDistanceFound = QtWidgets.QSpinBox(self.groupBox_Peak)
        self.spinBox_PeakDistanceFound.setEnabled(False)
        self.spinBox_PeakDistanceFound.setGeometry(
            QtCore.QRect(135, 55, 30, 20))
        self.spinBox_PeakDistanceFound.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.spinBox_PeakDistanceFound.setButtonSymbols(
            QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_PeakDistanceFound.setMaximum(10000)
        self.spinBox_PeakDistanceFound.setProperty("value", 0)
        self.spinBox_PeakDistanceFound.setObjectName(
            "spinBox_PeakDistanceFound")
        self.pushButton_UpdatePlots = QtWidgets.QPushButton(
            self.dockWidgetContents)
        self.pushButton_UpdatePlots.setEnabled(False)
        self.pushButton_UpdatePlots.setGeometry(
            QtCore.QRect(920, 130, 110, 23))
        self.pushButton_UpdatePlots.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_UpdatePlots.setFont(font)
        self.pushButton_UpdatePlots.setObjectName("pushButton_UpdatePlots")
        self.lineEdit_File = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.lineEdit_File.setEnabled(False)
        self.lineEdit_File.setGeometry(QtCore.QRect(140, 10, 133, 20))
        self.lineEdit_File.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setItalic(False)
        self.lineEdit_File.setFont(font)
        self.lineEdit_File.setText("")
        self.lineEdit_File.setReadOnly(False)
        self.lineEdit_File.setObjectName("lineEdit_File")
        self.label_Filename = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_Filename.setGeometry(QtCore.QRect(70, 10, 60, 16))
        self.label_Filename.setObjectName("label_Filename")
        self.checkBox_AutoUpdate = QtWidgets.QCheckBox(self.dockWidgetContents)
        self.checkBox_AutoUpdate.setEnabled(False)
        self.checkBox_AutoUpdate.setGeometry(QtCore.QRect(770, 130, 101, 20))
        self.checkBox_AutoUpdate.setObjectName("checkBox_AutoUpdate")
        DockWidget_Analysis.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget_Analysis)
        QtCore.QMetaObject.connectSlotsByName(DockWidget_Analysis)

    def retranslateUi(self, DockWidget_Analysis):
        _translate = QtCore.QCoreApplication.translate
        DockWidget_Analysis.setWindowTitle(
            _translate("DockWidget_Analysis", "Analysis"))
        self.groupBox_Signal.setTitle(
            _translate("DockWidget_Analysis", "Signal"))
        self.label_ExcitTruncate.setText(
            _translate("DockWidget_Analysis", "Start Signal"))
        self.label_EndTruncate.setText(
            _translate("DockWidget_Analysis", "Stop Signal"))
        self.label_Step.setText(_translate("DockWidget_Analysis", "Step (µs)"))
        self.label_Points.setText(
            _translate("DockWidget_Analysis", "Max Points"))
        self.checkBox_Hann.setText(_translate("DockWidget_Analysis", "Hann"))
        self.checkBox_ZeroFill.setText(
            _translate("DockWidget_Analysis", "Zero (1*N)"))
        self.checkBox_HalfHann.setText(
            _translate("DockWidget_Analysis", "1/2 Hann"))
        self.checkBox_ZeroFillTwice.setText(
            _translate("DockWidget_Analysis", "Zero (2*N)"))
        self.checkBox_NoZero.setText(
            _translate("DockWidget_Analysis", "No Zero"))
        self.groupBox_Mass.setTitle(
            _translate("DockWidget_Analysis", "Mass Calibration"))
        self.label_RefMass.setText(
            _translate("DockWidget_Analysis", "Ref. mass (u)"))
        self.label_CycloFreq.setText(
            _translate("DockWidget_Analysis", "Cycl. Freq. (kHz)"))
        self.label_MagFreq.setText(
            _translate("DockWidget_Analysis", "Mag. Freq (kHz)"))
        self.label_PlotStartMass.setText(
            _translate("DockWidget_Analysis", "Plot mass limits"))
        self.checkBox_Hold.setText(_translate("DockWidget_Analysis", "Hold"))
        self.groupBox_Peak.setTitle(
            _translate("DockWidget_Analysis", "Peak Detection"))
        self.label_PeakHeight.setText(
            _translate("DockWidget_Analysis", "Peak Height"))
        self.label_PeakDistance.setText(
            _translate("DockWidget_Analysis", "Peak Distance"))
        self.label_StartMass.setText(
            _translate("DockWidget_Analysis", "Start Mass"))
        self.label_EndMass.setText(
            _translate("DockWidget_Analysis", "End Mass"))
        self.pushButton_UpdatePlots.setText(
            _translate("DockWidget_Analysis", "Update Plots"))
        self.label_Filename.setText(
            _translate("DockWidget_Analysis", "FILENAME"))
        self.checkBox_AutoUpdate.setText(
            _translate("DockWidget_Analysis", "Auto Update"))
