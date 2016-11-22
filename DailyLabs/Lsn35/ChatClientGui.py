# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Randall.Bower/Documents/Courses/CS210/Code/Lab35_Threads/ChatClientGui.ui'
#
# Created: Sun Nov 23 09:33:30 2014
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

class Ui_ChatClient(object):
    def setupUi(self, ChatClient):
        ChatClient.setObjectName(_fromUtf8("ChatClient"))
        ChatClient.resize(480, 640)
        self.centralwidget = QtGui.QWidget(ChatClient)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.listen_editor = QtGui.QTextEdit(self.centralwidget)
        self.listen_editor.setFocusPolicy(QtCore.Qt.NoFocus)
        self.listen_editor.setReadOnly(True)
        self.listen_editor.setObjectName(_fromUtf8("listen_editor"))
        self.verticalLayout.addWidget(self.listen_editor)
        self.transmit_editor = QtGui.QLineEdit(self.centralwidget)
        self.transmit_editor.setObjectName(_fromUtf8("transmit_editor"))
        self.verticalLayout.addWidget(self.transmit_editor)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        ChatClient.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ChatClient)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.chat_menu = QtGui.QMenu(self.menubar)
        self.chat_menu.setObjectName(_fromUtf8("chat_menu"))
        ChatClient.setMenuBar(self.menubar)
        self.status_bar = QtGui.QStatusBar(ChatClient)
        self.status_bar.setObjectName(_fromUtf8("status_bar"))
        ChatClient.setStatusBar(self.status_bar)
        self.menu_connect = QtGui.QAction(ChatClient)
        self.menu_connect.setObjectName(_fromUtf8("menu_connect"))
        self.menu_disconnect = QtGui.QAction(ChatClient)
        self.menu_disconnect.setObjectName(_fromUtf8("menu_disconnect"))
        self.menu_save = QtGui.QAction(ChatClient)
        self.menu_save.setObjectName(_fromUtf8("menu_save"))
        self.menu_exit = QtGui.QAction(ChatClient)
        self.menu_exit.setObjectName(_fromUtf8("menu_exit"))
        self.chat_menu.addAction(self.menu_connect)
        self.chat_menu.addAction(self.menu_disconnect)
        self.chat_menu.addSeparator()
        self.chat_menu.addAction(self.menu_save)
        self.chat_menu.addAction(self.menu_exit)
        self.menubar.addAction(self.chat_menu.menuAction())

        self.retranslateUi(ChatClient)
        QtCore.QMetaObject.connectSlotsByName(ChatClient)

    def retranslateUi(self, ChatClient):
        ChatClient.setWindowTitle(_translate("ChatClient", "Chat Client", None))
        self.chat_menu.setTitle(_translate("ChatClient", "Chat", None))
        self.menu_connect.setText(_translate("ChatClient", "Connect", None))
        self.menu_disconnect.setText(_translate("ChatClient", "Disconnect", None))
        self.menu_save.setText(_translate("ChatClient", "Save", None))
        self.menu_exit.setText(_translate("ChatClient", "Exit", None))

