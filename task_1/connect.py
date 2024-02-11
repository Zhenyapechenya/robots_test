"""
В данном модуле создаю подключение к базе данных.
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


def manipulate_table(my_db, query):
    cursor = my_db.cursor()
    try:
        cursor.execute(query, multi=True)

        results = cursor.fetchall()
        for row in results:
            print(row)

        my_db.commit()

        print("Query executed")

    except Error as e:
        print(e)
