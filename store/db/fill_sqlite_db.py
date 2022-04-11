#!/usr/bin/env python3
# coding --utf-8--

import get_db_data
import sqlite3


def create_table(sqlite_db_name: str = 'sqlite_table.db') -> tuple:
    sqlite_connection = sqlite3.connect(sqlite_db_name)
    sqlite_create_table_query = '''CREATE TABLE sqlitedb_developers (
                                        id INTEGER PRIMARY KEY,
                                        image text NOT NULL,
                                        sound REAL NOT NULL,
                                        name TEXT NOT NULL,
                                        year INTEGER NOT NULL,
                                        commute REAL NOT NULL,
                                        sports REAL NOT NULL,
                                        office REAL NOT NULL,
                                        wireless_gaming REAL NOT NULL,
                                        wired_gaming REAL NOT NULL,
                                        phone_cals INTEGER NOT NULL,
                                        color TEXT NOT NULL,
                                        price INTEGER NOT NULL
                                        );'''

    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print("Таблица SQLite создана")

    return sqlite_connection, cursor


def fill_database(sqlite_connection):
    headphones = get_db_data.HeadphonesWeb.parse_page(filename='page.xml')

    sql = '''INSERT INTO sqlitedb_developers(image,name,sound,year,commute,sports,
    office,wireless_gaming,wired_gaming,phone_cals,color,price)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?);'''

    for tasks in headphones:
        tasks = list(tasks)
        sqlite_connection.execute(sql, tasks)
        sqlite_connection.commit()

    print("Filled data into database")


if __name__ == '__main__':
    try:
        sqlite_connection, cursor = create_table()
        fill_database(sqlite_connection)
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        cursor.close()
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
