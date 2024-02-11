"""
Создание подключения к базе данных и выполнение SQL скриптов
"""
import mysql.connector
from mysql.connector import Error


my_db = None

def connect():
    global my_db
    try:
        my_db = mysql.connector.connect(
            user='root',
            password='admin',
            host='localhost',
            database='library'
        )
        if my_db.is_connected():
            print('Successfully connection')

    except Error as e:
        print(e)


connect()


def manipulate_table(my_db, queries):
    cursor = my_db.cursor()
    try:
        for query in queries:
            cursor.execute(query)

        results = cursor.fetchall()
        for row in results:
            print(row)

        my_db.commit()

        print("Query executed")

    except Error as e:
        print(e)

