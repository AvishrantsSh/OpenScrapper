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
        Dialog.setMaximumSize(QtCore.QSize(532, 528))
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(70, 100, 391, 431))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(150, 20, 101, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 320, 351, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sign_up = QtWidgets.QPushButton(self.layoutWidget)
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
        self.login = QtWidgets.QPushButton(self.layoutWidget)
        self.login.setMinimumSize(QtCore.QSize(0, 35))
        self.login.setDefault(False)
        self.login.setObjectName("login")
        self.horizontalLayout.addWidget(self.login)
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(20, 90, 351, 61))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.uname = QtWidgets.QLineEdit(self.widget)
        self.uname.setObjectName("uname")
        self.verticalLayout.addWidget(self.uname)
        self.widget1 = QtWidgets.QWidget(self.frame)
        self.widget1.setGeometry(QtCore.QRect(20, 190, 351, 61))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.pwd = QtWidgets.QLineEdit(self.widget1)
        self.pwd.setInputMask("")
        self.pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd.setObjectName("pwd")
        self.verticalLayout_2.addWidget(self.pwd)
        self.error_frm = QtWidgets.QFrame(Dialog)
        self.error_frm.setGeometry(QtCore.QRect(70, 49, 391, 41))
        self.error_frm.setStyleSheet("    padding: 15px 20px;\n"
"    background-color: #ffe3e6;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: rgba(158,28,35,0.2);\n"
"    text-align: center;")
        self.error_frm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.error_frm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.error_frm.setObjectName("error_frm")
        self.label_4 = QtWidgets.QLabel(self.error_frm)
        self.label_4.setGeometry(QtCore.QRect(90, 10, 211, 21))
        self.label_4.setStyleSheet("border:none;\n"
"margin:0;\n"
"padding:0;\n"
"color:black;")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.error_frm)
        self.pushButton.setGeometry(QtCore.QRect(350, 10, 21, 21))
        self.pushButton.setStyleSheet("#pushButton{\n"
"padding:0;\n"
"margin:0;\n"
"border:none;\n"
"border-radius: 0;\n"
"color: rgba(158,28,35,.6);\n"
"background-color:transparent;\n"
"}\n"
"#pushButton:hover{\n"
"color:rgb(158,28,35);\n"
"}")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Project X"))
        self.sign_up.setText(_translate("Dialog", "New User?"))
        self.login.setText(_translate("Dialog", "Login"))
        self.label.setText(_translate("Dialog", "UserName"))
        self.uname.setPlaceholderText(_translate("Dialog", "Username"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.pwd.setPlaceholderText(_translate("Dialog", "Password"))
        self.label_4.setText(_translate("Dialog", "Invalid Login Credentials"))
        self.pushButton.setText(_translate("Dialog", "X"))
