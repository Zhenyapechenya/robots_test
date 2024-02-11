"""
SQL-скрипт, который выводит автора, который написал больше всего книг
"""
from connect import manipulate_table, my_db


productive_author = [
    'SELECT\
        authors.name,\
        authors.surname,\
        COUNT(book_author.book_id) AS num_books\
    FROM\
        authors\
    JOIN\
        book_author ON book_author.author_id = authors.id\
    GROUP BY authors.id\
    HAVING num_books = (\
        SELECT MAX(book_count)\
        FROM (\
            SELECT book_author.author_id, COUNT(book_author.author_id) AS book_count\
            FROM book_author\
            GROUP BY author_id\
        ) AS book_count\
    );'
]

manipulate_table(my_db, productive_author)

