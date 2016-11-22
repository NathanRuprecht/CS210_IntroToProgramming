# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CounterGui.ui'
#
# Created: Tue Oct 21 09:15:34 2014
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

class Ui_CounterGui(object):
    def setupUi(self, CounterGui):
        CounterGui.setObjectName(_fromUtf8("CounterGui"))
        CounterGui.resize(400, 300)
        self.verticalLayout_2 = QtGui.QVBoxLayout(CounterGui)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.counter_layout = QtGui.QHBoxLayout()
        self.counter_layout.setObjectName(_fromUtf8("counter_layout"))
        self.count_label = QtGui.QLabel(CounterGui)
        font = QtGui.QFont()
        font.setPointSize(32)
        self.count_label.setFont(font)
        self.count_label.setAlignment(QtCore.Qt.AlignCenter)
        self.count_label.setObjectName(_fromUtf8("count_label"))
        self.counter_layout.addWidget(self.count_label)
        self.verticalLayout.addLayout(self.counter_layout)
        self.btn_layout = QtGui.QHBoxLayout()
        self.btn_layout.setObjectName(_fromUtf8("btn_layout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.btn_layout.addItem(spacerItem)
        self.inc_btn = QtGui.QPushButton(CounterGui)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.inc_btn.setFont(font)
        self.inc_btn.setObjectName(_fromUtf8("inc_btn"))
        self.btn_layout.addWidget(self.inc_btn)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.btn_layout.addItem(spacerItem1)
        self.dec_btn = QtGui.QPushButton(CounterGui)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.dec_btn.setFont(font)
        self.dec_btn.setObjectName(_fromUtf8("dec_btn"))
        self.btn_layout.addWidget(self.dec_btn)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.btn_layout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.btn_layout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(CounterGui)
        QtCore.QMetaObject.connectSlotsByName(CounterGui)

    def retranslateUi(self, CounterGui):
        CounterGui.setWindowTitle(_translate("CounterGui", "Counter", None))
        self.count_label.setText(_translate("CounterGui", "0", None))
        self.inc_btn.setText(_translate("CounterGui", "+", None))
        self.dec_btn.setText(_translate("CounterGui", "-", None))

