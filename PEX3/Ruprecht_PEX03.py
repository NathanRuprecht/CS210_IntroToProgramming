# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/C16Nathan.Ruprecht/Documents/Academics/2014-2015/2014Fall/CS210/PEX03/PEX3_ForStudents/Ruprecht_PEX03.ui'
#
# Created: Wed Oct 29 15:49:39 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PEX03Gui(object):
    def setupUi(self, PEX03Gui):
        PEX03Gui.setObjectName(_fromUtf8("PEX03Gui"))
        PEX03Gui.resize(1064, 678)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        PEX03Gui.setPalette(palette)
        PEX03Gui.setAutoFillBackground(True)
        self.verticalLayout_2 = QtGui.QVBoxLayout(PEX03Gui)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.WindowLayout = QtGui.QVBoxLayout()
        self.WindowLayout.setObjectName(_fromUtf8("WindowLayout"))
        self.TopLayout = QtGui.QVBoxLayout()
        self.TopLayout.setObjectName(_fromUtf8("TopLayout"))
        self.drawing_widget = QtGui.QWidget(PEX03Gui)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.drawing_widget.setPalette(palette)
        self.drawing_widget.setAutoFillBackground(True)
        self.drawing_widget.setObjectName(_fromUtf8("drawing_widget"))
        self.TopLayout.addWidget(self.drawing_widget)
        self.WindowLayout.addLayout(self.TopLayout)
        self.BottomLayout = QtGui.QVBoxLayout()
        self.BottomLayout.setObjectName(_fromUtf8("BottomLayout"))
        self.LayoutForBtns = QtGui.QHBoxLayout()
        self.LayoutForBtns.setObjectName(_fromUtf8("LayoutForBtns"))
        self.LoadSaveLayout = QtGui.QVBoxLayout()
        self.LoadSaveLayout.setObjectName(_fromUtf8("LoadSaveLayout"))
        self.LoadPolygon_Btn = QtGui.QPushButton(PEX03Gui)
        self.LoadPolygon_Btn.setObjectName(_fromUtf8("LoadPolygon_Btn"))
        self.LoadSaveLayout.addWidget(self.LoadPolygon_Btn)
        self.SavePolygon_Btn = QtGui.QPushButton(PEX03Gui)
        self.SavePolygon_Btn.setObjectName(_fromUtf8("SavePolygon_Btn"))
        self.LoadSaveLayout.addWidget(self.SavePolygon_Btn)
        self.LayoutForBtns.addLayout(self.LoadSaveLayout)
        self.Reset_Btn = QtGui.QPushButton(PEX03Gui)
        self.Reset_Btn.setObjectName(_fromUtf8("Reset_Btn"))
        self.LayoutForBtns.addWidget(self.Reset_Btn)
        self.DirectionLayout = QtGui.QGridLayout()
        self.DirectionLayout.setObjectName(_fromUtf8("DirectionLayout"))
        self.Right_Btn = QtGui.QPushButton(PEX03Gui)
        self.Right_Btn.setObjectName(_fromUtf8("Right_Btn"))
        self.DirectionLayout.addWidget(self.Right_Btn, 2, 2, 1, 1)
        self.Up_Btn = QtGui.QPushButton(PEX03Gui)
        self.Up_Btn.setObjectName(_fromUtf8("Up_Btn"))
        self.DirectionLayout.addWidget(self.Up_Btn, 1, 1, 1, 1)
        self.Left_Btn = QtGui.QPushButton(PEX03Gui)
        self.Left_Btn.setObjectName(_fromUtf8("Left_Btn"))
        self.DirectionLayout.addWidget(self.Left_Btn, 2, 0, 1, 1)
        self.Down_Btn = QtGui.QPushButton(PEX03Gui)
        self.Down_Btn.setObjectName(_fromUtf8("Down_Btn"))
        self.DirectionLayout.addWidget(self.Down_Btn, 3, 1, 1, 1)
        self.LayoutForBtns.addLayout(self.DirectionLayout)
        self.RollerLayout = QtGui.QVBoxLayout()
        self.RollerLayout.setObjectName(_fromUtf8("RollerLayout"))
        self.Roller = QtGui.QDial(PEX03Gui)
        self.Roller.setObjectName(_fromUtf8("Roller"))
        self.RollerLayout.addWidget(self.Roller)
        self.LayoutForBtns.addLayout(self.RollerLayout)
        self.SliderLayout = QtGui.QVBoxLayout()
        self.SliderLayout.setObjectName(_fromUtf8("SliderLayout"))
        self.Slider = QtGui.QSlider(PEX03Gui)
        self.Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Slider.setObjectName(_fromUtf8("Slider"))
        self.SliderLayout.addWidget(self.Slider)
        self.LayoutForBtns.addLayout(self.SliderLayout)
        self.BottomLayout.addLayout(self.LayoutForBtns)
        self.WindowLayout.addLayout(self.BottomLayout)
        self.verticalLayout_2.addLayout(self.WindowLayout)

        self.retranslateUi(PEX03Gui)
        QtCore.QMetaObject.connectSlotsByName(PEX03Gui)

    def retranslateUi(self, PEX03Gui):
        PEX03Gui.setWindowTitle(_translate("PEX03Gui", "MyGui", None))
        self.LoadPolygon_Btn.setText(_translate("PEX03Gui", "Load Polygon", None))
        self.SavePolygon_Btn.setText(_translate("PEX03Gui", "Save Polygon", None))
        self.Reset_Btn.setText(_translate("PEX03Gui", "Reset", None))
        self.Right_Btn.setText(_translate("PEX03Gui", "Right", None))
        self.Up_Btn.setText(_translate("PEX03Gui", "Up", None))
        self.Left_Btn.setText(_translate("PEX03Gui", "Left", None))
        self.Down_Btn.setText(_translate("PEX03Gui", "Down", None))

