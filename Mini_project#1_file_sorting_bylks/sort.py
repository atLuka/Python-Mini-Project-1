'''

Author:@atLuka


'''


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog,QFileDialog
from src.new_sort import new_sort 




class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setStyleSheet("background-color:#313133;")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 30, 301, 21))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK JP")
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#96be25;\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK JP")
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:#96be25;\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK JP")
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #96be25;\n"
"")
        self.label_3.setObjectName("label_3")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(120, 80, 221, 21))
        self.textBrowser.setStyleSheet("background-color:#a9afb1;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(120, 140, 221, 21))
        self.textBrowser_2.setStyleSheet("background-color:#a9afb1;\n"
"")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(350, 80, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK JP")
        font.setItalic(True)
        self.toolButton.setFont(font)
        self.toolButton.setStyleSheet("background-color:#a9afb1;")
        self.toolButton.setObjectName("toolButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 140, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK JP")
        font.setItalic(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:#a9afb1;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 200, 89, 25))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK JP")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color:#a9afb1;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(300, 260, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK JP")
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:#96be25;")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Mini-project #1"))
        self.label.setText(_translate("Form", "Python file sorting mini-project "))
        self.label_2.setText(_translate("Form", "Source path : "))
        self.label_3.setText(_translate("Form", "Target path : "))
        self.toolButton.setText(_translate("Form", "Open"))
        self.pushButton_2.setText(_translate("Form", "Open"))
        self.pushButton_3.setText(_translate("Form", "Sort"))
        self.label_4.setText(_translate("Form", "By Lks"))
        self.toolButton.setText(_translate("Form", "Open"))
        self.pushButton_2.setText(_translate("Form", "Open"))
        self.pushButton_3.setText(_translate("Form", "Sort"))
        self.toolButton.clicked.connect(self.open_dialog_box)
        self.pushButton_2.clicked.connect(self.open_scd_dialog_box)
        self.pushButton_3.clicked.connect(self.exec_new_sort)

    def open_dialog_box(self):
       filename= QFileDialog.getExistingDirectory()
       path=filename
       self.textBrowser.setPlainText(path)

    def open_scd_dialog_box(self):
        filename= QFileDialog.getExistingDirectory()
        path=filename
        self.textBrowser_2.setPlainText(path)
                
    def get_txt(self,other):
        other.show()
        return other.toPlainText()

    def exec_new_sort(self):
        new_sort(self.get_txt(self.textBrowser),self.get_txt(self.textBrowser_2))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
