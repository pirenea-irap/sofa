# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\S.O.F.T.S\PIRENEA\PYTHON\sofa\src\gui\sequence_qt.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtWidgets


class Ui_DockWidget_Sequence(object):

    def setupUi(self, DockWidget_Sequence):
        DockWidget_Sequence.setObjectName("DockWidget_Sequence")
        DockWidget_Sequence.resize(340, 200)
        DockWidget_Sequence.setMinimumSize(QtCore.QSize(340, 200))
        DockWidget_Sequence.setFeatures(
            QtWidgets.QDockWidget.DockWidgetFloatable | QtWidgets.QDockWidget.DockWidgetMovable)
        DockWidget_Sequence.setAllowedAreas(
            QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView_Sequence = QtWidgets.QTableView(self.dockWidgetContents)
        self.tableView_Sequence.setObjectName("tableView_Sequence")
        self.verticalLayout.addWidget(self.tableView_Sequence)
        DockWidget_Sequence.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget_Sequence)
        QtCore.QMetaObject.connectSlotsByName(DockWidget_Sequence)

    def retranslateUi(self, DockWidget_Sequence):
        _translate = QtCore.QCoreApplication.translate
        DockWidget_Sequence.setWindowTitle(_translate("DockWidget_Sequence", "Sequence"))
