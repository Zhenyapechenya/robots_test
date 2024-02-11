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


def manipulate_table(my_db, queries):
    cursor = my_db.cursor()
    try:
        for query in queries:
            cursor.execute(query)

        # results = cursor.fetchall()
        # for row in results:
        #     print(row)

        my_db.commit()

        print("Query executed")

    except Error as e:
        print(e)



create_table = [
    "CREATE TABLE IF NOT EXISTS authors (\
    author_id INT PRIMARY KEY,\
    name VARCHAR(50),\
    surname VARCHAR(50));",

    "CREATE TABLE IF NOT EXISTS genres (\
    genre_id INT PRIMARY KEY,\
    name VARCHAR(50));",

    "CREATE TABLE IF NOT EXISTS books (\
    book_id INT PRIMARY KEY,\
    isbn VARCHAR(17),\
    title VARCHAR(200) NOT NULL,\
    pages INT, date_published DATE);",

    "CREATE TABLE IF NOT EXISTS book_author (\
    author_id INT,\
    book_id INT,\
    PRIMARY KEY (author_id, book_id),\
    FOREIGN KEY (author_id) REFERENCES authors (author_id) ON DELETE CASCADE,\
    FOREIGN KEY (book_id) REFERENCES books (book_id)\
    );",

    "CREATE TABLE IF NOT EXISTS book_genre (\
    book_id INT,\
    genre_id INT,\
    PRIMARY KEY (book_id, genre_id),\
    FOREIGN KEY (genre_id) REFERENCES genres (genre_id),\
    FOREIGN KEY (book_id) REFERENCES books (book_id)\
    );"
]


manipulate_table(my_db, create_table)