# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PolygonGui.ui'
#
# Created: Thu Oct 23 09:10:55 2014
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

class Ui_PolygonGui(object):
    def setupUi(self, PolygonGui):
        PolygonGui.setObjectName(_fromUtf8("PolygonGui"))
        PolygonGui.resize(527, 384)
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
        PolygonGui.setPalette(palette)
        PolygonGui.setAutoFillBackground(True)
        self.verticalLayout_2 = QtGui.QVBoxLayout(PolygonGui)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.WindowLayout = QtGui.QVBoxLayout()
        self.WindowLayout.setObjectName(_fromUtf8("WindowLayout"))
        self.TopLayout = QtGui.QVBoxLayout()
        self.TopLayout.setObjectName(_fromUtf8("TopLayout"))
        self.widget = QtGui.QWidget(PolygonGui)
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
        self.widget.setPalette(palette)
        self.widget.setAutoFillBackground(True)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.TopLayout.addWidget(self.widget)
        self.WindowLayout.addLayout(self.TopLayout)
        self.BottomLayout = QtGui.QVBoxLayout()
        self.BottomLayout.setObjectName(_fromUtf8("BottomLayout"))
        self.LayoutForBtns = QtGui.QHBoxLayout()
        self.LayoutForBtns.setObjectName(_fromUtf8("LayoutForBtns"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.LayoutForBtns.addItem(spacerItem)
        self.Triangle_Btn = QtGui.QPushButton(PolygonGui)
        self.Triangle_Btn.setObjectName(_fromUtf8("Triangle_Btn"))
        self.LayoutForBtns.addWidget(self.Triangle_Btn)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.LayoutForBtns.addItem(spacerItem1)
        self.Square_Btn = QtGui.QPushButton(PolygonGui)
        self.Square_Btn.setObjectName(_fromUtf8("Square_Btn"))
        self.LayoutForBtns.addWidget(self.Square_Btn)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.LayoutForBtns.addItem(spacerItem2)
        self.Parellelogram = QtGui.QPushButton(PolygonGui)
        self.Parellelogram.setObjectName(_fromUtf8("Parellelogram"))
        self.LayoutForBtns.addWidget(self.Parellelogram)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.LayoutForBtns.addItem(spacerItem3)
        self.Radio_Btns = QtGui.QVBoxLayout()
        self.Radio_Btns.setObjectName(_fromUtf8("Radio_Btns"))
        self.Insert_Btn = QtGui.QRadioButton(PolygonGui)
        self.Insert_Btn.setObjectName(_fromUtf8("Insert_Btn"))
        self.Radio_Btns.addWidget(self.Insert_Btn)
        self.Replace_Btn = QtGui.QRadioButton(PolygonGui)
        self.Replace_Btn.setObjectName(_fromUtf8("Replace_Btn"))
        self.Radio_Btns.addWidget(self.Replace_Btn)
        self.LayoutForBtns.addLayout(self.Radio_Btns)
        self.BottomLayout.addLayout(self.LayoutForBtns)
        self.WindowLayout.addLayout(self.BottomLayout)
        self.verticalLayout_2.addLayout(self.WindowLayout)

        self.retranslateUi(PolygonGui)
        QtCore.QMetaObject.connectSlotsByName(PolygonGui)

    def retranslateUi(self, PolygonGui):
        PolygonGui.setWindowTitle(_translate("PolygonGui", "MyGui", None))
        self.Triangle_Btn.setText(_translate("PolygonGui", "Traingle", None))
        self.Square_Btn.setText(_translate("PolygonGui", "Square", None))
        self.Parellelogram.setText(_translate("PolygonGui", "Parellelogram", None))
        self.Insert_Btn.setText(_translate("PolygonGui", "Insert before closest point", None))
        self.Replace_Btn.setText(_translate("PolygonGui", "Replace closest point", None))

