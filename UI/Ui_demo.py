# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Code\pythonCode\Difffolder\UI\demo.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(716, 483)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_ip = QtWidgets.QLabel(Form)
        self.label_ip.setObjectName("label_ip")
        self.horizontalLayout_3.addWidget(self.label_ip)
        self.lineEdit_ip = QtWidgets.QLineEdit(Form)
        self.lineEdit_ip.setObjectName("lineEdit_ip")
        self.horizontalLayout_3.addWidget(self.lineEdit_ip)
        self.label_folder_path = QtWidgets.QLabel(Form)
        self.label_folder_path.setObjectName("label_folder_path")
        self.horizontalLayout_3.addWidget(self.label_folder_path)
        self.lineEdit_folder_path = QtWidgets.QLineEdit(Form)
        self.lineEdit_folder_path.setObjectName("lineEdit_folder_path")
        self.horizontalLayout_3.addWidget(self.lineEdit_folder_path)
        self.label_download_name = QtWidgets.QLabel(Form)
        self.label_download_name.setObjectName("label_download_name")
        self.horizontalLayout_3.addWidget(self.label_download_name)
        self.lineEdit_download_name = QtWidgets.QLineEdit(Form)
        self.lineEdit_download_name.setObjectName("lineEdit_download_name")
        self.horizontalLayout_3.addWidget(self.lineEdit_download_name)
        self.pushButton_download = QtWidgets.QPushButton(Form)
        self.pushButton_download.setObjectName("pushButton_download")
        self.horizontalLayout_3.addWidget(self.pushButton_download)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_ip.setText(_translate("Form", "IP"))
        self.label_folder_path.setText(_translate("Form", "目录路径"))
        self.label_download_name.setText(_translate("Form", "下载名称"))
        self.pushButton_download.setText(_translate("Form", "下载"))
        self.pushButton.setText(_translate("Form", "输出差异"))