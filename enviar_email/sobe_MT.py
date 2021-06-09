from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 300)
        Dialog.setMaximumSize(QSize(450, 300))
        Dialog.setMinimumSize(QSize(450, 300))
        Dialog.setWindowIcon(QIcon("icon.png"))

        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(200, 10, 61, 21))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QLabel(Dialog)
        self.label_2.setGeometry(QRect(20, 40, 421, 25))
        font = QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QLabel(Dialog)
        self.label_3.setGeometry(QRect(20, 270, 421, 21))
        font = QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QLabel(Dialog)
        self.label_4.setGeometry(QRect(20, 130, 421, 61))
        font = QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sobre"))
        self.label.setText(_translate("Dialog", "Sobre"))
        self.label_2.setText(_translate("Dialog", "WSE V1.0 | Copyright © 2021 Kaique Afonso | Todos os Direitos Reservados.\nWindows Send Email"))
        self.label_3.setText(_translate("Dialog", "kaiqueafonsoferreira21@gmail.com                                            Oi: (75)98172-9111"))
        self.label_4.setText(_translate("Dialog",  "\"O maldizente não acredita em ninguém por não acredita em si próprio\""))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
