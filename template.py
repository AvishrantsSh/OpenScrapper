# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scraper.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1099, 812)
        Dialog.setStyleSheet("background-color: #333;\n"
"color:white;")
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(0, 27))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)
        self.Info = QtWidgets.QLabel(Dialog)
        self.Info.setMinimumSize(QtCore.QSize(0, 31))
        self.Info.setText("")
        self.Info.setObjectName("Info")
        self.gridLayout_2.addWidget(self.Info, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.ctrl_frame = QtWidgets.QFrame(Dialog)
        self.ctrl_frame.setEnabled(True)
        self.ctrl_frame.setMinimumSize(QtCore.QSize(0, 500))
        self.ctrl_frame.setStyleSheet("background-color: #222;")
        self.ctrl_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ctrl_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ctrl_frame.setObjectName("ctrl_frame")
        self.Controls = QtWidgets.QLabel(self.ctrl_frame)
        self.Controls.setGeometry(QtCore.QRect(10, 10, 381, 20))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(16)
        self.Controls.setFont(font)
        self.Controls.setStyleSheet("")
        self.Controls.setAlignment(QtCore.Qt.AlignCenter)
        self.Controls.setObjectName("Controls")
        self.SiteType = QtWidgets.QLabel(self.ctrl_frame)
        self.SiteType.setGeometry(QtCore.QRect(10, 60, 171, 17))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(12)
        self.SiteType.setFont(font)
        self.SiteType.setObjectName("SiteType")
        self.Output = QtWidgets.QLabel(self.ctrl_frame)
        self.Output.setGeometry(QtCore.QRect(10, 260, 171, 17))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(12)
        self.Output.setFont(font)
        self.Output.setObjectName("Output")
        self.layoutWidget = QtWidgets.QWidget(self.ctrl_frame)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 320, 331, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.Format = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.Format.setContentsMargins(0, 0, 0, 0)
        self.Format.setObjectName("Format")
        self.json = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(12)
        self.json.setFont(font)
        self.json.setObjectName("json")
        self.Format.addWidget(self.json)
        self.csv = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(12)
        self.csv.setFont(font)
        self.csv.setObjectName("csv")
        self.Format.addWidget(self.csv)
        self.fmt = QtWidgets.QLabel(self.ctrl_frame)
        self.fmt.setGeometry(QtCore.QRect(30, 290, 81, 17))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(12)
        self.fmt.setFont(font)
        self.fmt.setObjectName("fmt")
        self.layoutWidget_8 = QtWidgets.QWidget(self.ctrl_frame)
        self.layoutWidget_8.setGeometry(QtCore.QRect(30, 190, 331, 27))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.Tabletype = QtWidgets.QHBoxLayout(self.layoutWidget_8)
        self.Tabletype.setContentsMargins(0, 0, 0, 0)
        self.Tabletype.setObjectName("Tabletype")
        self.stic = QtWidgets.QRadioButton(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(12)
        self.stic.setFont(font)
        self.stic.setObjectName("stic")
        self.Tabletype.addWidget(self.stic)
        self.dynamic = QtWidgets.QRadioButton(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(12)
        self.dynamic.setFont(font)
        self.dynamic.setObjectName("dynamic")
        self.Tabletype.addWidget(self.dynamic)
        self.TableType = QtWidgets.QLabel(self.ctrl_frame)
        self.TableType.setGeometry(QtCore.QRect(10, 160, 171, 17))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(12)
        self.TableType.setFont(font)
        self.TableType.setObjectName("TableType")
        self.layoutWidget1 = QtWidgets.QWidget(self.ctrl_frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 90, 331, 27))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.Iter = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.Iter.setContentsMargins(0, 0, 0, 0)
        self.Iter.setObjectName("Iter")
        self.single = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(12)
        self.single.setFont(font)
        self.single.setObjectName("single")
        self.Iter.addWidget(self.single)
        self.complete = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(12)
        self.complete.setFont(font)
        self.complete.setObjectName("complete")
        self.Iter.addWidget(self.complete)
        self.gridLayout.addWidget(self.ctrl_frame, 1, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setStyleSheet("#pushButton{\n"
"  background-color: #4CAF50; /* Green */\n"
"  border-radius: 10px;\n"
"  color: #FFFFFF;\n"
"  padding: 12px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  font-size: 16px;\n"
"  margin: 4px 2px;\n"
"}\n"
"#pushButton:hover{\n"
"    background-color: #6CCF70;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 2)
        self.fetch = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fetch.sizePolicy().hasHeightForWidth())
        self.fetch.setSizePolicy(sizePolicy)
        self.fetch.setStyleSheet("#fetch {\n"
"background-color: #4CAF50; /* Green */\n"
"  border-radius: 5px;\n"
"  color: white;\n"
"  padding: 2px 10px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  font-size: 16px;\n"
"  margin: 4px 2px;\n"
"}\n"
"#fetch:hover{\n"
"    background-color: #6CCF70;\n"
"}\n"
"")
        self.fetch.setObjectName("fetch")
        self.gridLayout.addWidget(self.fetch, 0, 1, 1, 1)
        self.URL = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.URL.sizePolicy().hasHeightForWidth())
        self.URL.setSizePolicy(sizePolicy)
        self.URL.setMinimumSize(QtCore.QSize(300, 0))
        self.URL.setStyleSheet("")
        self.URL.setObjectName("URL")
        self.gridLayout.addWidget(self.URL, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 5, 1)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_2.addWidget(self.tableWidget, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Preview (Note: Only first 5 records will be visible in preview)"))
        self.Controls.setText(_translate("Dialog", "Controls"))
        self.SiteType.setText(_translate("Dialog", "Search for Table In:"))
        self.Output.setText(_translate("Dialog", "Output Options:"))
        self.json.setText(_translate("Dialog", "JSON"))
        self.csv.setText(_translate("Dialog", "CSV"))
        self.fmt.setText(_translate("Dialog", "Format"))
        self.stic.setToolTip(_translate("Dialog", "Select if table data does not change over time"))
        self.stic.setText(_translate("Dialog", "Static"))
        self.dynamic.setToolTip(_translate("Dialog", "Select if table data changes with time"))
        self.dynamic.setText(_translate("Dialog", "Dynamic"))
        self.TableType.setText(_translate("Dialog", "Table Type"))
        self.single.setText(_translate("Dialog", "Single Page"))
        self.complete.setText(_translate("Dialog", "Whole Site"))
        self.pushButton.setText(_translate("Dialog", "Get Link !"))
        self.fetch.setText(_translate("Dialog", "Submit"))
        self.URL.setPlaceholderText(_translate("Dialog", "Site URL"))
