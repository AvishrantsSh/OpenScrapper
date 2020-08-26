# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(532, 528)
        Dialog.setMinimumSize(QtCore.QSize(532, 528))
        Dialog.setMaximumSize(QtCore.QSize(532, 16777215))
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(70, 100, 391, 431))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.uname = QtWidgets.QLineEdit(self.frame)
        self.uname.setGeometry(QtCore.QRect(20, 120, 351, 31))
        self.uname.setObjectName("uname")
        self.pwd = QtWidgets.QLineEdit(self.frame)
        self.pwd.setGeometry(QtCore.QRect(20, 220, 351, 31))
        self.pwd.setInputMask("")
        self.pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd.setObjectName("pwd")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 90, 81, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 190, 81, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(150, 20, 101, 31))
        self.label_3.setObjectName("label_3")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(20, 320, 351, 71))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sign_up = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sign_up.sizePolicy().hasHeightForWidth())
        self.sign_up.setSizePolicy(sizePolicy)
        self.sign_up.setMinimumSize(QtCore.QSize(0, 35))
        self.sign_up.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.sign_up.setAutoDefault(True)
        self.sign_up.setObjectName("sign_up")
        self.horizontalLayout.addWidget(self.sign_up)
        self.login = QtWidgets.QPushButton(self.widget)
        self.login.setMinimumSize(QtCore.QSize(0, 35))
        self.login.setDefault(False)
        self.login.setObjectName("login")
        self.horizontalLayout.addWidget(self.login)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.uname.setPlaceholderText(_translate("Dialog", "Username"))
        self.pwd.setPlaceholderText(_translate("Dialog", "Password"))
        self.label.setText(_translate("Dialog", "UserName"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.label_3.setText(_translate("Dialog", "Dekhte Jao"))
        self.sign_up.setText(_translate("Dialog", "New User?"))
        self.login.setText(_translate("Dialog", "Login"))
