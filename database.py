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

