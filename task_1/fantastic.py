"""
SQL-скрипт, который выводит название книги и ее авторов для жанра “Фантастика”

"""
from connect import manipulate_table, my_db


fantastica = f"""
    SELECT 
        books.title AS "Название Книги",
        GROUP_CONCAT(CONCAT(authors.name, " ", authors.surname) SEPARATOR ', ') AS "Авторы"
    FROM
        books
    JOIN 
        book_genre ON books.book_id = book_genre.book_id
    JOIN
        genres ON book_genre.genre_id = genres.genre_id
    JOIN
        book_author ON books.book_id = book_author.book_id
    JOIN
        authors ON book_author.author_id = authors.author_id
    WHERE
        genres.name = "Фантастика"
    GROUP BY 
        books.title
    ;
    
"""

manipulate_table(my_db, fantastica)
