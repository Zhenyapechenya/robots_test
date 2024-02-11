# Тестовое задание для Лиги Роботов

Выполнила Псарева Евгения
<br>
epsareva77@gmail.com

## Задание 1

#### Лежит в папке task_1

### Описание задачи
Предметная область — издательство. Спроектировать структуру реляционной БД, содержащую следующие сущности:
Книги: ID, ISBN, авторы, название, количество страниц, жанры, дата публикации
Авторы:  ID, Имя, Фамилия
Жанры: ID, название
Требования к реализации модели предметной области
книга может быть написана несколькими авторами
книга может относиться к нескольким жанрам.
Требования к выполненному заданию
сделан отдельный SQL-скрипт с тестовым набором данных
сделан отдельный SQL-скрипт который выводит название книги и ее авторов для жанра “Фантастика”
сделан отдельный SQL-скрипт который выводит автора, который написал больше всего книг
код будет запускаться на MySQL версии не ниже 5.6
Плюсом будет наличие визуальной схемы БД


## Задание 2

#### Лежит в папке task_2

### Описание задачи
Необходимо реализовать форму обратной связи, поля формы:
комментарий;
ФИО;
адрес;
email;
мобильный телефон;
Дополнительные требования
поля ФИО и мобильный телефон обязательны к заполнению
Добавить валидацию  полей мобильный телефон и email
на стороне бэкенда (желательно PHP) производить повторную проверку обязательных полей и если указана почта в домене @gmail.com, то возвращать ошибку с сообщением о том, что регистрация пользователей с таким почтовым адресом невозможна
На бэкенде складировать данные успешно заполненных форм в файл или реляционную БД, например SQLite/MySQL
+1 балл от руководителя группы фронтенда (но не обязательно)
для подсказок пользовательского ввода в поля ФИО и адрес использовать бесплатный сервис «Подсказки» от DaData
решить задачу с использованием фреймворка Vue.js на клиентской стороне
