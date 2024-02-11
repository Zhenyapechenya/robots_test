"""
SQL-скрипт, который выводит название книги и ее авторов для жанра “Фантастика”

"""
from concurrent.futures.process import BrokenProcessPool
from lzma import FORMAT_ALONE
from connect import manipulate_table, my_db


fantastica = [
    'SELECT\
        books.title AS "Название Книги",\
        GROUP_CONCAT(CONCAT(authors.name, " ", authors.surname) SEPARATOR ", ") AS "Авторы"\
    FROM\
        books\
    JOIN\
        book_genre ON books.id = book_genre.book_id\
    JOIN\
        genres ON book_genre.genre_id = genres.id\
    JOIN\
        book_author ON books.id = book_author.book_id\
    JOIN\
        authors ON book_author.author_id = authors.id\
    WHERE\
        genres.name = "Фантастика"\
    GROUP BY\
        books.title;'
]

manipulate_table(my_db, fantastica)

