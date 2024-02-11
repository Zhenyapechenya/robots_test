"""
SQL-скрипт с тестовым набором данных
"""
from connect import manipulate_table, my_db


create_table = """
    CREATE TABLE IF NOT EXISTS authors (
    author_id INT PRIMARY KEY,
    name VARCHAR(50),
    surname VARCHAR(50)
    );

    CREATE TABLE IF NOT EXISTS genres (
    genre_id INT PRIMARY KEY,
    name VARCHAR(50)
    );

    CREATE TABLE IF NOT EXISTS books (
    book_id INT PRIMARY KEY,
    isbn VARCHAR(17),
    title VARCHAR(200) NOT NULL,
    pages INT,
    date_published DATE
    );

    CREATE TABLE IF NOT EXISTS book_author (
    author_id INT,
    book_id INT,
    PRIMARY KEY (author_id, book_id),
    FOREIGN KEY (author_id) REFERENCES authors (author_id) ON DELETE CASCADE,
    FOREIGN KEY (book_id) REFERENCES books (book_id)
    );

    CREATE TABLE IF NOT EXISTS book_genre (
    book_id INT,
    genre_id INT,
    PRIMARY KEY (book_id, genre_id),
    FOREIGN KEY (genre_id) REFERENCES genres (genre_id),
    FOREIGN KEY (book_id) REFERENCES books (book_id)
    );
"""

test_data = """
    INSERT INTO authors (author_id, name, surname) VALUES
    (1, 'Александр', 'Пушкин'),
    (2, 'Сергей', 'Есенин'),
    (3, 'Джоан', 'Роулинг');

    INSERT INTO genres (genre_id, name) VALUES
    (1, 'Роман'),
    (2, 'Фантастика'),
    (3, 'Детектив');

    INSERT INTO books (book_id, isbn, title, pages, date_published) VALUES
    (1, '123-4-56547-789-0', 'Сказка о рыбаке и рыбке', 300, '2023-01-01'),
    (2, '098-4-76543-214-1', 'Сборник стихов', 400, '2022-02-15'),
    (3, '111-2-22333-744-8', 'Гарри Поттер и кубок огня', 850, '2015-03-10');

    INSERT INTO book_author (book_id, author_id) VALUES
    (1, 1),
    (1, 2),
    (2, 2),
    (3, 3);

    INSERT INTO book_genre (book_id, genre_id) VALUES
    (1, 1),
    (1, 2),
    (2, 2),
    (3, 3);
"""

# delete = """
#     DROP TABLE books;
#     DROP TABLE authors;
#     DROP TABLE genres;
#     DROP TABLE book_author;
#     DROP TABLE book_genre;
# """

# manipulate_table(my_db, create_table)

manipulate_table(my_db, test_data)
