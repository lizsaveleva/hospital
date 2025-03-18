import sys
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector
from mysql.connector import Error

from database import create_connection, close_connection


class Ui_RegistrationWindow(object):
    def setupUi(self, RegistrationWindow):
        RegistrationWindow.setObjectName("RegistrationWindow")
        RegistrationWindow.resize(680, 462)
        self.centralwidget = QtWidgets.QWidget(RegistrationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(0, -10, 681, 441))
        self.listView.setStyleSheet("background-color: rgb(225, 239, 255);")
        self.listView.setObjectName("listView")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(270, 50, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 130, 221, 31))
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
        self.lineEdit_2.setGeometry(QtCore.QRect(350, 130, 221, 31))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
                                      "border-color: rgb(67, 101, 255);\n"
                                      "border-radius:15px;\n"
                                      "color:rgb(102, 212, 241);\n"
                                      "font: 75 9pt \"Candara\";\n"
                                      "}")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)  # Changed to Password mode
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 340, 231, 51))
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 100, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 100, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 200, 221, 31))
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
                                      "border-color: rgb(67, 101, 255);\n"
                                      "border-radius:15px;\n"
                                      "color:rgb(102, 212, 241);\n"
                                      "font: 75 9pt \"Candara\";\n"
                                      "}\n"
                                      "")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 170, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(430, 170, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(350, 200, 221, 31))
        self.lineEdit_4.setStyleSheet("QLineEdit {\n"
                                      "border-color: rgb(67, 101, 255);\n"
                                      "border-radius:15px;\n"
                                      "color:rgb(102, 212, 241);\n"
                                      "font: 75 9pt \"Candara\";\n"
                                      "}\n"
                                      "")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(160, 240, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 270, 221, 31))
        self.lineEdit_5.setStyleSheet("QLineEdit {\n"
                                      "border-color: rgb(67, 101, 255);\n"
                                      "border-radius:15px;\n"
                                      "color:rgb(102, 212, 241);\n"
                                      "font: 75 9pt \"Candara\";\n"
                                      "}\n"
                                      "")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(400, 240, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(350, 270, 221, 31))
        self.lineEdit_6.setStyleSheet("QLineEdit {\n"
                                      "border-color: rgb(67, 101, 255);\n"
                                      "border-radius:15px;\n"
                                      "color:rgb(102, 212, 241);\n"
                                      "font: 75 9pt \"Candara\";\n"
                                      "}\n"
                                      "")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(540, 30, 91, 81))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("medical-checkup_10476244.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        RegistrationWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RegistrationWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 680, 21))
        self.menubar.setObjectName("menubar")
        RegistrationWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RegistrationWindow)
        self.statusbar.setObjectName("statusbar")
        RegistrationWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.registration)

        self.retranslateUi(RegistrationWindow)
        QtCore.QMetaObject.connectSlotsByName(RegistrationWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Регистрация"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Зарегестрироваться"))
        self.label.setText(_translate("MainWindow", "Логин:"))
        self.label_2.setText(_translate("MainWindow", "Пароль"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "Имя"))
        self.label_5.setText(_translate("MainWindow", "Фамилия"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Surname"))
        self.label_6.setText(_translate("MainWindow", "Отчество"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Patronymic"))
        self.label_7.setText(_translate("MainWindow", "Дата рождения"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "Date"))

    def show_error_message(self, message):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setText(message)
        error_dialog.setWindowTitle("Ошибка")
        error_dialog.exec_()

    def show_success_message(self, message):
        success_dialog = QMessageBox()
        success_dialog.setIcon(QMessageBox.Information)
        success_dialog.setText(message)
        success_dialog.setWindowTitle("Успех")
        success_dialog.exec_()

    def validate_input(self):
        username = self.lineEdit.text().strip()
        password = self.lineEdit_2.text().strip()
        name = self.lineEdit_3.text().strip()
        surname = self.lineEdit_4.text().strip()
        patronymic = self.lineEdit_5.text().strip()
        birth_year = self.lineEdit_6.text().strip()

        if not (username and password and name and surname and birth_year):
            self.show_error_message("Заполните обязательные поля")
            return False

        if not birth_year.isdigit() or len(birth_year) != 4:
            self.show_error_message("Год рождения должен быть в формате YYYY")
            return False

        current_year = datetime.datetime.now().year
        birth_year_int = int(birth_year)

        if birth_year_int > current_year:
            self.show_error_message("Год рождения не может быть в будущем")
            return False

        if birth_year_int < 1900:
            self.show_error_message("Указан слишком ранний год рождения")
            return False

        age = current_year - birth_year_int

        if age < 14:
            self.show_error_message("Регистрация доступна только для лиц старше 14 лет")
            return False

        if age > 120:
            self.show_error_message("Указан недопустимый возраст")
            return False

        if len(password) < 6:
            self.show_error_message("Пароль должен содержать минимум 6 символов")
            return False

        return True

    def registration(self):
        if not self.validate_input():
            return

        username = self.lineEdit.text().strip()
        password = self.lineEdit_2.text().strip()
        name = self.lineEdit_3.text().strip()
        surname = self.lineEdit_4.text().strip()
        patronymic = self.lineEdit_5.text().strip()
        birth_year = self.lineEdit_6.text().strip()

        try:
            connection = create_connection()
            cursor = connection.cursor()

            cursor.execute("SELECT username FROM Users WHERE username = %s", (username,))
            if cursor.fetchone():
                self.show_error_message("Пользователь с таким логином уже существует")
                return

            cursor.execute(
                "INSERT INTO Patients (name, surname, patronymic, birth_year) VALUES (%s, %s, %s, %s)",
                (name, surname, patronymic, birth_year)
            )

            patient_id = cursor.lastrowid

            try:
                password_int = int(password)
            except ValueError:
                password_int = hash(password) % (2 ** 31 - 1)

            # Insert user data
            cursor.execute(
                "INSERT INTO Users (username, password, patient_id) VALUES (%s, %s, %s)",
                (username, password_int, patient_id)
            )

            connection.commit()
            self.show_success_message("Регистрация успешно завершена!")

            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()

        except mysql.connector.Error as error:
            self.show_error_message(f"Ошибка базы данных: {error}")
        finally:
            if connection and connection.is_connected():
                cursor.close()
                close_connection(connection)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    RegistrationWindow = QtWidgets.QMainWindow()
    ui = Ui_RegistrationWindow()
    ui.setupUi(RegistrationWindow)
    RegistrationWindow.show()
    sys.exit(app.exec_())
