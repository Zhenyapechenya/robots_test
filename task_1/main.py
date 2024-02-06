import pymysql
from config import host, user, password, db_name

connection = pymysql.connect(
    host=host,
    port=3306,
    user=user,
    password=password,
    database=db_name,
    cursorsclass=pymysql.cursors.DicrCursor
)