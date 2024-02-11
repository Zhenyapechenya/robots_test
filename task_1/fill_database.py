"""
SQL-скрипт с тестовым набором данных
"""
from connect import manipulate_table, my_db


create_table = [
    "CREATE TABLE IF NOT EXISTS authors (\
    id INT PRIMARY KEY,\
    name VARCHAR(50),\
    surname VARCHAR(50));",

    "CREATE TABLE IF NOT EXISTS genres (\
    id INT PRIMARY KEY,\
    name VARCHAR(50));",

    "CREATE TABLE IF NOT EXISTS books (\
    id INT PRIMARY KEY,\
    isbn VARCHAR(17),\
    title VARCHAR(200) NOT NULL,\
    pages INT,\
    date_published DATE\
    );",

    "CREATE TABLE IF NOT EXISTS book_author (\
    author_id INT,\
    book_id INT,\
    PRIMARY KEY (author_id, book_id),\
    FOREIGN KEY (author_id) REFERENCES authors (id) ON DELETE CASCADE,\
    FOREIGN KEY (book_id) REFERENCES books (id)\
    );",

    "CREATE TABLE IF NOT EXISTS book_genre (\
    book_id INT,\
    genre_id INT,\
    PRIMARY KEY (book_id, genre_id),\
    FOREIGN KEY (genre_id) REFERENCES genres (id),\
    FOREIGN KEY (book_id) REFERENCES books (id)\
    );"
]

test_data = [
    "INSERT INTO authors (id, name, surname) VALUES (1, 'Александр', 'Пушкин'), (2, 'Сергей', 'Есенин'), (3, 'Джоан', 'Роулинг'), (4, 'Аркадий', 'Стругацкий'), (5, 'Борис', 'Стругацкий');",
    "INSERT INTO genres (id, name) VALUES (1, 'Проза'), (2, 'Фантастика'), (3, 'Поэзия');",
    "INSERT INTO books (id, isbn, title, pages, date_published) VALUES (1, '123-4-56547-789-0', 'Сказка о рыбаке и рыбке', 300, '2023-01-01'), (2, '098-4-76543-214-1', 'Сборник стихов', 400, '2022-02-15'), (3, '111-2-22333-744-8', 'Гарри Поттер и кубок огня', 850, '2015-03-10'), (4, '111-2-22333-744-8', 'Пикник на обочине', 650, '2020-08-18');",
    "INSERT INTO book_author (book_id, author_id) VALUES (1, 1), (2, 2), (3, 3), (4, 4), (4, 5);",
    "INSERT INTO book_genre (book_id, genre_id) VALUES (1, 1), (1, 2), (2, 3), (3, 2), (4, 2);"
]

# delete = [
#     "DROP TABLE book_author;",
#     "DROP TABLE book_genre;",
#     "DROP TABLE genres;",
#     "DROP TABLE books;",
#     "DROP TABLE authors;",

# ]

manipulate_table(my_db, create_table)

manipulate_table(my_db, test_data)

# manipulate_table(my_db, delete)
