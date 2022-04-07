# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import MysqlConn

class Ui_Payment(object):
    def __init__(self, Form): #step 2 init
        self.setupUi( Form )

    def setupUi(self, Obj):
        Form = Obj.page7_holder #step 3 set page #step 4 remove the hoz from main temp
        Form.setObjectName("Form")
        Form.resize(650, 519)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 80))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titlelabel = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titlelabel.sizePolicy().hasHeightForWidth())
        self.titlelabel.setSizePolicy(sizePolicy)
        self.titlelabel.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.titlelabel.setFont(font)
        self.titlelabel.setObjectName("titlelabel")
        self.verticalLayout_2.addWidget(self.titlelabel)
        self.line_5 = QtWidgets.QFrame(self.widget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_2.addWidget(self.line_5)
        self.verticalLayout.addWidget(self.widget)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 8, 1, 1, 1)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 2, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        self.AcYear = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.AcYear.setFont(font)
        self.AcYear.setObjectName("AcYear")
        self.gridLayout.addWidget(self.AcYear, 7, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 7, 1, 1, 1)
        self.Branchlabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Branchlabel.sizePolicy().hasHeightForWidth())
        self.Branchlabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setItalic(False)
        self.Branchlabel.setFont(font)
        self.Branchlabel.setObjectName("Branchlabel")
        self.gridLayout.addWidget(self.Branchlabel, 0, 0, 1, 1)
        self.AcYear_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.AcYear_2.setFont(font)
        self.AcYear_2.setObjectName("AcYear_2")
        self.gridLayout.addWidget(self.AcYear_2, 0, 2, 1, 1)
        self.BranchChoice = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.BranchChoice.setFont(font)
        self.BranchChoice.setObjectName("BranchChoice")
        self.gridLayout.addWidget(self.BranchChoice, 8, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 5, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Comps_but_3 = QtWidgets.QRadioButton(self.groupBox)
        self.Comps_but_3.setObjectName("Comps_but_3")
        self.verticalLayout_4.addWidget(self.Comps_but_3)
        self.Comps_but_2 = QtWidgets.QRadioButton(self.groupBox)
        self.Comps_but_2.setChecked(True)
        self.Comps_but_2.setObjectName("Comps_but_2")
        self.verticalLayout_4.addWidget(self.Comps_but_2)
        self.Comps_but_4 = QtWidgets.QRadioButton(self.groupBox)
        self.Comps_but_4.setObjectName("Comps_but_4")
        self.verticalLayout_4.addWidget(self.Comps_but_4)
        self.gridLayout.addWidget(self.groupBox, 3, 2, 2, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Comps_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.Comps_3.setObjectName("Comps_3")
        self.verticalLayout_5.addWidget(self.Comps_3)
        self.Comps_6 = QtWidgets.QRadioButton(self.groupBox_2)
        self.Comps_6.setObjectName("Comps_6")
        self.verticalLayout_5.addWidget(self.Comps_6)
        self.Comps_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.Comps_4.setObjectName("Comps_4")
        self.verticalLayout_5.addWidget(self.Comps_4)
        self.It_button = QtWidgets.QRadioButton(self.groupBox_2)
        self.It_button.setChecked(True)
        self.It_button.setObjectName("It_button")
        self.verticalLayout_5.addWidget(self.It_button)
        self.Comps_but = QtWidgets.QRadioButton(self.groupBox_2)
        self.Comps_but.setObjectName("Comps_but")
        self.verticalLayout_5.addWidget(self.Comps_but)
        self.gridLayout.addWidget(self.groupBox_2, 3, 0, 2, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.widget_2 = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(200, 10))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.widget_2, 0, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
        self.BackBtn = QtWidgets.QPushButton(self.widget_2)
        self.BackBtn.setObjectName("BackBtn")

        self.verticalLayout_3.addWidget(self.BackBtn)
        
        self.verticalLayout.addItem(spacerItem2)
        self.pushButton.clicked.connect(lambda: self.insertSQL(Obj))
        self.BackBtn.clicked.connect(lambda: MysqlConn.Backward(Obj, Obj.stackedWidget.currentIndex()) )
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.titlelabel.setText(_translate("Form", "<html><head/><body><p align=\"center\">Form Details</p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("Form", "F.E"))
        self.comboBox_2.setItemText(1, _translate("Form", "D.S.E"))
        self.AcYear.setText(_translate("Form", "Academic Year"))
        self.comboBox.setItemText(0, _translate("Form", "2020-24"))
        self.comboBox.setItemText(1, _translate("Form", "2021-25"))
        self.comboBox.setItemText(2, _translate("Form", "2022-26"))
        self.Branchlabel.setText(_translate("Form", "Branch"))
        self.AcYear_2.setText(_translate("Form", "Form Method"))
        self.BranchChoice.setText(_translate("Form", "Course"))
        self.Comps_but_3.setText(_translate("Form", "Credit/Debit"))
        self.Comps_but_2.setText(_translate("Form", "UPI"))
        self.Comps_but_4.setText(_translate("Form", "Cash "))
        self.Comps_3.setText(_translate("Form", "Civil Engineering"))
        self.Comps_6.setText(_translate("Form", "Mechanical Engineering"))
        self.It_button.setText(_translate("Form", "Information Technology"))
        self.Comps_but.setText(_translate("Form", "Computer Science"))
        self.pushButton.setText(_translate("Form", "Print"))
        self.BackBtn.setText(_translate("Payment", "Back"))

    def checkAcademic(self):
        if self.Comps_3.isChecked()    : return self.Comps_3.text()
        if self.Comps_6.isChecked() : return self.Comps_6.text()
        if self.Comps_4.isChecked() : return self.Comps_4.text()
        if self.It_button.isChecked() : return self.It_button.text()
        if self.Comps_but.isChecked() : return self.Comps_but.text()

    def checkPayment(self):
        if self.Comps_but_3.isChecked()    : return self.Comps_but_3.text()
        if self.Comps_but_2.isChecked() : return self.Comps_but_2.text()
        if self.Comps_but_4.isChecked() : return self.Comps_but_4.text()
        
    def insertSQL(self, Obj):
        sql = " INSERT INTO `Branch_details` (`Std_ID`, `Branch`, `PaymentMethod`, `AcademicYear`, `Course`) VALUES (%s, %s, %s, %s, %s)  "
        val = (
            MysqlConn.RowCount() + 1,
            self.checkAcademic(),
            self.checkPayment(),
            self.comboBox.currentText(),
            self.comboBox_2.currentText()
             )
        if MysqlConn.UploadForm(sql, val, True) == True: 
            Obj.stackedWidget.setCurrentIndex(2)
        else: MysqlConn.AlertPop("Wrong Or Empty Data!")