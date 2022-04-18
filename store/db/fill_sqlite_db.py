#!/usr/bin/env python3
# coding --utf-8--

from loguru import logger
from store.db import sqlite_wrapper
import sqlite3

if __name__ == '__main__':
    try:
        sqlite_connection, cursor = sqlite_wrapper.SqlitWrapper.create_table()
        sqlite_wrapper.SqlitWrapper.fill_database(sqlite_connection)
    except sqlite3.Error as error:
        logger.info("Ошибка при подключении к sqlite", error)
    finally:
        cursor.close()
        if sqlite_connection:
            sqlite_connection.close()
            logger.info("Соединение с SQLite закрыто")
