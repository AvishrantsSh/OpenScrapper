# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loader.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Loader(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(150, 80)
        Dialog.setMinimumSize(QtCore.QSize(150, 80))
        Dialog.setMaximumSize(QtCore.QSize(150, 80))
        self.movie_label = QtWidgets.QLabel(Dialog)
        self.movie_label.setGeometry(QtCore.QRect(50, 30, 50, 50))
        self.movie_label.setMinimumSize(QtCore.QSize(50, 50))
        self.movie_label.setMaximumSize(QtCore.QSize(50, 50))
        self.movie_label.setText("")
        self.movie_label.setAlignment(QtCore.Qt.AlignCenter)
        self.movie_label.setObjectName("movie_label")
        self.tag = QtWidgets.QLabel(Dialog)
        self.tag.setGeometry(QtCore.QRect(30, 10, 91, 17))
        self.tag.setMaximumSize(QtCore.QSize(16777215, 20))
        self.tag.setText("")
        self.tag.setAlignment(QtCore.Qt.AlignCenter)
        self.tag.setObjectName("tag")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
