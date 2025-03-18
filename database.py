import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="root",
        database="hospital"
    )

    if conn.is_connected():
        print("1.Соединение с базой данных успешно установлено")

except Error as e:
    print(f"1.Ошибка подключения: {e}")

finally:
    if conn and conn.is_connected():
        conn.close()
        print("3.Соединение с базой данных закрыто")
