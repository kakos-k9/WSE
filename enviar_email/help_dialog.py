from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setWindowIcon(QIcon('icon.png'))
        Dialog.setMaximumSize(QSize(400, 300))
        Dialog.setMinimumSize(QSize(400, 300))
        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(180, 10, 51, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QLabel(Dialog)
        self.label_2.setGeometry(QRect(20, 60, 371, 211))
        font = QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ajuda"))
        self.label.setText(_translate("Dialog", "Ajuda"))
        self.label_2.setText(_translate("Dialog", "Se o E-mail que você for utilizar for Gmail deve-se seguir\n"
        "as seguintes orientações:\n"
        "\n"
        "1. Clique em gerir sua conta Google\n"
        "\n"
        "2. No canto superior esquedo da tela clique em \"Segurança\"\n"
        "\n"
        "3. Diriga-se até em \"Acesso a app menos seguro\" e ative-o\n"
        "\n"
        "\n"
        "\n"
        "\n"
        "Não se preucupe, o WX-KL324 segue os protocólos do TLS e de\n"
        "maneira alguma fará uma ação fora de suas coordenadas."))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
