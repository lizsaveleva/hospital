import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="root",
            database="hospital"
        )
        if connection.is_connected():
            print("1.Соединение с базой данных успешно установлено")
        return connection
    except Error as e:
        print(f"1.Ошибка подключения: {e}")
        return None

def close_connection(connection):
    if connection and connection.is_connected():
        connection.close()
        print("3.Соединение с базой данных закрыто")

def authenticate_user(connection, username, password):
    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Users WHERE username = %s AND password = %s", (username, password))
        return cursor.fetchone()
    except Error as e:
        print(f"Ошибка при аутентификации пользователя: {e}")
        return None
    finally:
        if cursor:
            cursor.close()

def register_user(connection, username, password):
    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Users (username, password) VALUES (%s, %s)", (username, password))
        connection.commit()
        print("Пользователь успешно зарегистрирован")
        return True
    except Error as e:
        print(f"Ошибка при регистрации пользователя: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
