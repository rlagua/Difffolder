#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :main.py
@说明    : difffplder
@时间    :2023/07/11 19:32:36
@作者    :PQJ
'''



from UI.Ui_demo import Ui_Form
from diff_folder import FolderComparator
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QHeaderView, QLabel, QLineEdit, QWidget
from PyQt5.QtGui import QTextCursor

import sys
import json

class UiMain(Ui_Form):
    def __init__(self, MainWindow) -> None:
        super().__init__()
        super().setupUi(MainWindow)
        # 重定向 sys.stdout
        self.stdout_orig = sys.stdout
        sys.stdout = self
        sys.stderr = self
        self.bind()
        self.init_folder_path()
    
    def diff(self):
        folder1, folder2 = self.comboBox.currentText(), self.comboBox_2.currentText()
        self.comparator = FolderComparator(folder1=folder1, folder2=folder2)
        self.comparator.compare_folders()
    
    def init_folder_path(self):
        self.folder_path_dict = ['E:\\diff\\folder1', 'E:\\diff\\folder2', 'E:\\diff\\folder3']
    
    def sync_path(self):
        self.comboBox.clear()
        self.comboBox.addItems(self.folder_path_dict)
        # for item in self.folder_path_dict:
        #     print(item)
        #     self.comboBox.addItem(item)
        self.comboBox_2.clear()
        self.comboBox_2.addItems(self.folder_path_dict)

    def bind(self):
        self.pushButton_download.clicked.connect(self.add_folder_path)
        self.pushButton.clicked.connect(self.diff)
    
    def add_folder_path(self):
        if len(self.lineEdit_download_name.text()) > 2:
            self.folder_path_dict.append(self.lineEdit_download_name.text())
            self.sync_path()

    def write(self, text):
        """输出重定向方法"""
        # self.textEdit.append(str(text))
        self.textEdit.moveCursor(QTextCursor.End)
        self.textEdit.insertPlainText(text)
        self.textEdit.moveCursor(QTextCursor.End)
        self.textEdit.ensureCursorVisible()

    def flush(self):
        """输出重定向方法"""
        pass

    def closeEvent(self, event):
        """恢复sys.stdout"""
        sys.stdout = self.stdout_orig

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindows = QWidget()
    Ui = UiMain(MainWindows)
    MainWindows.show()
    sys.exit(app.exec_())
