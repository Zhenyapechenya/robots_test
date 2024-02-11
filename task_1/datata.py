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



test_data = [
    "INSERT INTO authors (author_id, name, surname) VALUES (1, 'Александр', 'Пушкин'), (2, 'Сергей', 'Есенин'), (3, 'Джоан', 'Роулинг');",
    "INSERT INTO genres (genre_id, name) VALUES (1, 'Роман'), (2, 'Фантастика'), (3, 'Детектив');",
    "INSERT INTO books (book_id, isbn, title, pages, date_published) VALUES (1, '123-4-56547-789-0', 'Сказка о рыбаке и рыбке', 300, '2023-01-01'), (2, '098-4-76543-214-1', 'Сборник стихов', 400, '2022-02-15'), (3, '111-2-22333-744-8', 'Гарри Поттер и кубок огня', 850, '2015-03-10');",
    "INSERT INTO book_author (book_id, author_id) VALUES (1, 1), (1, 2), (2, 2), (3, 3);",
    "INSERT INTO book_genre (book_id, genre_id) VALUES (1, 1), (1, 2), (2, 2), (3, 3);"
]


manipulate_table(my_db, test_data)