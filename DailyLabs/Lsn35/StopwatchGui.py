# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Randall.Bower/Documents/Courses/CS210/Code/Lab35_Threads/StopwatchGui.ui'
#
# Created: Sat Nov 22 17:15:00 2014
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

class Ui_StopwatchGui(object):
    def setupUi(self, StopwatchGui):
        StopwatchGui.setObjectName(_fromUtf8("StopwatchGui"))
        StopwatchGui.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(StopwatchGui)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.main_layout = QtGui.QVBoxLayout()
        self.main_layout.setObjectName(_fromUtf8("main_layout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.main_layout.addItem(spacerItem)
        self.counter_layout = QtGui.QHBoxLayout()
        self.counter_layout.setObjectName(_fromUtf8("counter_layout"))
        self.time_label = QtGui.QLabel(StopwatchGui)
        font = QtGui.QFont()
        font.setPointSize(32)
        self.time_label.setFont(font)
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setObjectName(_fromUtf8("time_label"))
        self.counter_layout.addWidget(self.time_label)
        self.main_layout.addLayout(self.counter_layout)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.main_layout.addItem(spacerItem1)
        self.button_layout = QtGui.QHBoxLayout()
        self.button_layout.setObjectName(_fromUtf8("button_layout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.button_layout.addItem(spacerItem2)
        self.start_stop_button = QtGui.QPushButton(StopwatchGui)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_stop_button.sizePolicy().hasHeightForWidth())
        self.start_stop_button.setSizePolicy(sizePolicy)
        self.start_stop_button.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.start_stop_button.setFont(font)
        self.start_stop_button.setObjectName(_fromUtf8("start_stop_button"))
        self.button_layout.addWidget(self.start_stop_button)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.button_layout.addItem(spacerItem3)
        self.main_layout.addLayout(self.button_layout)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.main_layout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.main_layout)

        self.retranslateUi(StopwatchGui)
        QtCore.QMetaObject.connectSlotsByName(StopwatchGui)

    def retranslateUi(self, StopwatchGui):
        StopwatchGui.setWindowTitle(_translate("StopwatchGui", "Stopwatch", None))
        self.time_label.setText(_translate("StopwatchGui", "0.00", None))
        self.start_stop_button.setText(_translate("StopwatchGui", "Start/Stop", None))

