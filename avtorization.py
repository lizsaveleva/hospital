import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from mysql.connector import Error

from database import create_connection, close_connection, authenticate_user, register_user
from registration import Ui_RegistrationWindow
from main import Ui_MainWindow

class Ui_AvtorizationWindow(object):
    def setupUi(self, AvtorizationWindow):
        AvtorizationWindow.setObjectName("MainWindow")
        AvtorizationWindow.resize(680, 460)
        self.centralwidget = QtWidgets.QWidget(AvtorizationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 230, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QWidget {\n"
" \n"
"    background-color: rgb(180, 232, 255);\n"
"}\n"
"QPushButton {\n"
"border-radius:15px;\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 110, 221, 31))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"border-color: rgb(67, 101, 255);\n"
"border-radius:15px;\n"
"color:rgb(102, 212, 241);\n"
"font: 75 9pt \"Candara\";\n"
"}\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 180, 221, 31))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"border-color: rgb(67, 101, 255);\n"
"border-radius:15px;\n"
"color:rgb(102, 212, 241);\n"
"font: 75 9pt \"Candara\";\n"
"}")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 80, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 150, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(0, 0, 681, 441))
        self.listView.setStyleSheet("background-color: rgb(225, 239, 255);")
        self.listView.setObjectName("listView")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(390, 310, 101, 101))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("hospital-building.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(270, 20, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 110, 21, 21))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("profile (1).png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(200, 190, 21, 21))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("view.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 280, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QWidget {\n"
" \n"
"    background-color: rgb(180, 232, 255);\n"
"}\n"
"QPushButton {\n"
"border-radius:15px;\n"
"\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(300, 330, 91, 91))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("hospital-building.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_3.raise_()
        self.listView.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.pushButton_2.raise_()
        self.label_7.raise_()
        AvtorizationWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AvtorizationWindow)
        self.statusbar.setObjectName("statusbar")
        AvtorizationWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.avtorization)
        self.pushButton_2.clicked.connect(self.open_registration)

        self.retranslateUi(AvtorizationWindow)
        QtCore.QMetaObject.connectSlotsByName(AvtorizationWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Войти"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.label.setText(_translate("MainWindow", "Логин:"))
        self.label_2.setText(_translate("MainWindow", "Пароль"))
        self.label_4.setText(_translate("MainWindow", " Авторизация"))
        self.pushButton_2.setText(_translate("MainWindow", "Регистрация"))

    def avtorization(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if not username or not password:
            QtWidgets.QMessageBox.warning(None, "Ошибка", "Введите логин и пароль!")
            return

        connection = create_connection()

        try:
            user = authenticate_user(connection, username, password)

            if user:
                QtWidgets.QMessageBox.information(None, "Успех", "Авторизация успешна!")

                self.main_window = QtWidgets.QMainWindow()
                self.ui_main = Ui_MainWindow()
                self.ui_main.setupUi(self.main_window)
                self.main_window.show()
            else:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Неверный логин или пароль!")

        except Error as e:
            QtWidgets.QMessageBox.critical(None, "Ошибка", f"Произошла ошибка: {e}")
        finally:
            close_connection(connection)

    def open_registration(self):
        self.registration_window = QtWidgets.QMainWindow()
        self.ui = Ui_RegistrationWindow()
        self.ui.setupUi(self.registration_window)
        self.registration_window.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AvtorizationWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
