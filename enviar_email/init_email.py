from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Config(QDialog):
    def laranja(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowIcon(QIcon("icon.png"))
        Dialog.resize(400, 300)
        Dialog.setMaximumSize(QSize(400, 300))
        Dialog.setMinimumSize(QSize(400, 300))
        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(110, 10, 181, 31))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QLabel(Dialog)
        self.label_2.setGeometry(QRect(20, 80, 71, 31))
        font = QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setGeometry(QRect(100, 80, 291, 26))
        font = QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.textChanged[str].connect(self.ativa_btn)
        self.lineEdit.setStyleSheet("QLineEdit:focus {\n"
        "    border: 2px solid rgb(0, 85, 255);\n"
        "    background-color: rgb(255, 255, 231);\n"
        "}")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QLabel(Dialog)
        self.label_3.setGeometry(QRect(20, 130, 41, 21))
        font = QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QLabel(Dialog)
        self.label_4.setGeometry(QRect(20, 170, 97, 21))
        font = QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QLabel(Dialog)
        self.label_5.setGeometry(QRect(240, 170, 97, 21))
        font = QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QRect(100, 130, 291, 26))
        font = QFont()
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.textChanged[str].connect(self.ativa_btn)
        self.lineEdit_2.setStyleSheet("QLineEdit:focus {\n"
        "    border: 2px solid rgb(0, 85, 255);\n"
        "    background-color: rgb(255, 255, 231);\n"
        "}")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QRect(20, 190, 150, 26))
        font = QFont()
        font.setPointSize(11)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.textChanged[str].connect(self.ativa_btn)
        self.lineEdit_3.setStyleSheet("QLineEdit:focus {\n"
        "    border: 2px solid rgb(0, 85, 255);\n"
        "    background-color: rgb(255, 255, 231);\n"
        "}")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit_4 = QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QRect(240, 190, 150, 26))
        font = QFont()
        font.setPointSize(11)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.textChanged[str].connect(self.ativa_btn)
        self.lineEdit_4.setStyleSheet("QLineEdit:focus {\n"
        "    border: 2px solid rgb(0, 85, 255);\n"
        "    background-color: rgb(255, 255, 231);\n"
        "}")
        self.lineEdit_4.setValidator(QIntValidator())
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setGeometry(QRect(210, 260, 183, 31))
        font = QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.salvar_credenciais)
        self.pushButton.clicked.connect(Dialog.close)
        self.pushButton.setEnabled(False)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setGeometry(QRect(10, 260, 183, 31))
        font = QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.clicked.connect(self.ver_credenciais)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def salvar_credenciais(self):
        self.arquivo = open('config.txt', 'w')
        self.arquivo.write(f'{self.lineEdit.text()}\n')
        self.arquivo.write(f'{self.lineEdit_2.text()}\n')
        self.arquivo.write(f'{self.lineEdit_3.text()}\n')
        self.arquivo.write(self.lineEdit_4.text())
        self.arquivo.close()
        QMessageBox.information(QMessageBox(), 'kaiqueafonsoferreira21@gmail.com', 'CREDENCIAIS SALVAS COM SUCESSO!')
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")

    def ver_credenciais(self):
         try:
             self.arquivo = open('arq.txt', encoding='utf8')
             self.lista = []
             for linha in self.arquivo:
                 linha = linha.strip()
                 self.lista.append(linha)

             self.arquivo.close()
             self.lineEdit.setText(self.lista[0])
             self.lineEdit_2.setText(self.lista[1])
             self.lineEdit_3.setText(self.lista[2])
             self.lineEdit_4.setText(self.lista[3])
         except Exception as ERROR:
             print(ERROR)
             QMessageBox.warning(QMessageBox(), 'ERROR', 'NEMHUM E-MAIL CADASTRADO')
             return None

    def ativa_btn(self):
        if self.lineEdit.text() and self.lineEdit_2.text() and self.lineEdit_3.text() and self.lineEdit_4.text():
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "WX-KL324"))
        self.label.setText(_translate("Dialog", "Editar E-mail"))
        self.label_2.setText(_translate("Dialog", "E-mail\n"
        "Remetente"))
        self.label_3.setText(_translate("Dialog", "Senha"))
        self.label_4.setText(_translate("Dialog", "Servidor SMTP"))
        self.label_5.setText(_translate("Dialog", "Porta"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Inisira Seu E-mail"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Inisira Sua Senha"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "Inisira o Nome SMTP"))
        self.lineEdit_4.setPlaceholderText(_translate("Dialog", "Inisira a Porta"))
        self.pushButton_2.setText(_translate("Dialog", "Ver Credenciais [F1]"))
        self.pushButton_2.setShortcut(_translate("Dialog", "F1"))
        self.pushButton.setText(_translate("Dialog", "SALVAR [Enter]"))
        self.pushButton.setShortcut(_translate("Dialog", "Enter"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = QDialog()
    tela = Config()
    tela.laranja(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
