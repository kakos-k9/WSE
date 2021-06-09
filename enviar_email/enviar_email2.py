from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import help_dialog
import sobe_MT
import init_email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import sys

class Enviar_Email(QMainWindow):
    def inicio(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QIcon("icon.png"))
        MainWindow.resize(474, 430)
        MainWindow.setMaximumSize(QSize(474, 430))
        MainWindow.setMinimumSize(QSize(474, 430))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setGeometry(QRect(20, 50, 81, 31))
        font = QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QRect(20, 90, 431, 26))
        font = QFont()
        font.setPointSize(11)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("QLineEdit:focus {\n"
        "    border: 2px solid rgb(0, 85, 255);\n"
        "    background-color: rgb(255, 255, 231);\n"
        "}")
        self.lineEdit_3.textChanged[str].connect(self.ativa_btn)
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QRect(20, 150, 431, 26))
        font = QFont()
        font.setPointSize(11)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("QLineEdit:focus {\n"
        "    border: 2px solid rgb(0, 85, 255);\n"
        "    background-color: rgb(255, 255, 231);\n"
        "}")
        self.lineEdit_4.textChanged[str].connect(self.ativa_btn)
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QRect(20, 210, 431, 111))
        font = QFont()
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("QTextEdit:focus {\n"
        "    border: 2px solid rgb(0, 85, 255);\n"
        "    background-color: rgb(255, 255, 231);\n"
        "}")
        self.textEdit.setObjectName("textEdit")

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setGeometry(QRect(60, 330, 135, 31))
        font = QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setGeometry(QRect(20, 185, 71, 21))
        font = QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setGeometry(QRect(20, 125, 71, 21))
        font = QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setGeometry(QRect(150, 330, 260, 31))
        font = QFont()
        font.setPointSize(7)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QRect(180, 330, 271, 36))
        font = QFont()
        font.setPointSize(7)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setStyleSheet("QTextEdit:focus {\n"
        "    border: 2px solid rgb(0, 85, 255);\n"
        "    background-color: rgb(255, 255, 231);\n"
        "}")
        self.textEdit_2.setObjectName("textEdit_2")

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QRect(20, 380, 441, 34))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.clicked.connect(self.enviar_email)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setGeometry(QRect(150, 20, 171, 21))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QRect(410, 30, 31, 31))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border: 2px solid rgb(240, 240, 240);")
        self.pushButton.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap("config.png"))
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(32, 32))
        self.pushButton.clicked.connect(self.chamar_config)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QRect(20, 330, 31, 41))
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("border: 2px solid rgb(240, 240, 240);")
        self.pushButton_5.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap("clip.png"))
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QSize(32, 32))
        self.pushButton_5.clicked.connect(self.anexar_arquivo)
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QRect(75, 14, 60, 16))
        font = QFont()
        font.setPointSize(7)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(210, 210, 210);\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(190, 190, 190);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(170, 170, 170);\n"
        "}")
        self.pushButton_3.clicked.connect(self.chamar_sobre)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QRect(12, 14, 60, 16))
        font = QFont()
        font.setPointSize(7)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(210, 210, 210);\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(190, 190, 190);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(170, 170, 170);\n"
        "}")
        self.pushButton_4.clicked.connect(self.chamar_ajuda)
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def ativa_btn(self):
        if self.lineEdit_3.text() and self.lineEdit_4.text():
            self.pushButton_2.setEnabled(True)
        else:
            self.pushButton_2.setEnabled(False)

    def chamar_config(self):
        self.janela = QDialog()
        self.tela = init_email.Config()
        self.tela.laranja(self.janela)
        self.janela.show()

    def chamar_sobre(self):
        self.janela = QDialog()
        self.tela = sobe_MT.Ui_Dialog()
        self.tela.setupUi(self.janela)
        self.janela.show()

    def chamar_ajuda(self):
        self.janela = QDialog()
        self.tela = help_dialog.Ui_Dialog()
        self.tela.setupUi(self.janela)
        self.janela.show()

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WSE"))
        self.label_3.setText(_translate("MainWindow", "E-mail\n"
        "Destinatário"))
        self.label_4.setText(_translate("MainWindow", "Mensagem"))
        self.pushButton_2.setText(_translate("MainWindow", "ENVIAR [Enter]"))
        self.pushButton_2.setShortcut(_translate("MainWindow", "Enter"))
        self.label_5.setText(_translate("MainWindow", "Enviar Email"))
        self.label_6.setText(_translate("MainWindow", "Assunto"))
        self.label_7.setText(_translate("MainWindow", "Anexar Arquivos"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Insira o E-mail do Destinatário"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Insira o Assunto da Conversa"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Insira a Mensagem"))
        self.pushButton.setShortcut(_translate("MainWindow", "F1"))
        self.pushButton_3.setText(_translate("MainWindow", "SOBRE"))
        self.pushButton_3.setShortcut(_translate("MainWindow", "F3"))
        self.pushButton_4.setText(_translate("MainWindow", "AJUDA"))
        self.pushButton_4.setShortcut(_translate("MainWindow", "F4"))
        self.pushButton_5.setShortcut(_translate("MainWindow", "F2"))

    def anexar_arquivo(self):

        try:
            self.file_name = QFileDialog.getOpenFileNames(self, 'OPEN', r"<Default dir>", "Image files (*.jpg *.jpeg *.gif *.pdf *.rar *)")
            self.names = ','.join(self.file_name[0])
            self.textEdit_2.setText(self.names.replace(",", "\n"))
            self.textEdit_2.setReadOnly(False)

            if len(self.textEdit_2.toPlainText()) < 1:
                self.textEdit_2.setReadOnly(True)

        except Exception as ERROR:
            print(ERROR)
            QMessageBox.warning(QMessageBox(), 'ERROR', 'SELECIONE O(S) ARQUIVOS(S)')


    def enviar_email(self):

        try:
            self.arquivo = open('config.txt', encoding='utf8')
            self.lista = []
            for linha in self.arquivo:
                linha = linha.strip()
                self.lista.append(linha)

            self.arquivo.close()
            self.email = self.lista[0]
            self.senha = self.lista[1]
            self.smpt = self.lista[2]
            self.porta = self.lista[3]

            self.server = smtplib.SMTP(self.smpt, int(self.porta))
            self.server.ehlo()
            self.server.starttls()
            self.server.login(self.email, self.senha)

            self.mail = MIMEMultipart()
            self.mail['From'] = self.email
            self.mail['To'] = self.lineEdit_3.text()
            self.mail['Subject'] = self.lineEdit_4.text()
            self.mail.attach(MIMEText(self.textEdit.toPlainText(), 'plain'))

            self.lin = self.file_name[0]
            for b in self.lin:
                self.attchment = open(b, 'rb')

                self.att = MIMEBase('application', 'octet-stream')
                self.att.set_payload(self.attchment.read())
                encoders.encode_base64(self.att)

                self.att.add_header('Content-Disposition', f'attachment; filename={b}')
                self.attchment.close()
                self.mail.attach(self.att)

            self.server.sendmail(self.mail['From'], self.mail['To'], self.mail.as_string())
            self.server.quit()
            QMessageBox.information(QMessageBox(), 'kaiqueafonsoferreira21@gmail.com', 'E-MAIL ENVIADO COM SUCESSO!')
            self.lineEdit_3.setText("")
            self.lineEdit_4.setText("")
            self.textEdit.setText("")
            self.textEdit_2.setText("")

        except Exception as ERROR:
            print(ERROR)
            QMessageBox.warning(QMessageBox(), 'ERROR', 'VERIFIQUE SUAS CREDENCIAIS E TENTE NOVAMENTE!')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Enviar_Email()
    ui.inicio(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
