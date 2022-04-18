#!/usr/bin/env python3
# coding --utf-8--

from store.db import get_db_data
from loguru import logger
import sqlite3


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SqlitWrapper(metaclass=Singleton):
    def __init__(self, db_file_name: str):
        self._init(db_file_name)

    def _init(self, db_file_name: str):
        """
            Open connection with selected database
        :param db_file_name: path to db file name
        :return: nothing

        """
        self.db_file_name = db_file_name
        assert (self.db_file_name.split(".")[-1] != ".db", "You using not database file! Try to open \"sqlite3.db\".")

        self.sqlite_connection = sqlite3.connect(self.db_file_name)
        self.cursor = self.sqlite_connection.cursor()

    def __del__(self):
        self.cursor.close()
        if self.sqlite_connection:
            self.sqlite_connection.close()

    def reset(self, db_file_name: str):
        """
            If you want to open a new database
        :param db_file_name: path to sqlite database file
        :return: nothing
        """
        self._init(db_file_name)

    def create_table(self) -> tuple:
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

        logger.info("База данных подключена к SQLite")

        self.cursor.execute(sqlite_create_table_query)
        self.sqlite_connection.commit()

        logger.info("Таблица SQLite создана")

    def fill_database(self, page_file: str = 'page.xml'):
        """
            Parse xml page to fill up headphones
        :return:
        """
        headphones = get_db_data.HeadphonesWeb.parse_page(filename=page_file)

        sql = '''INSERT INTO sqlitedb_developers(image,name,sound,year,commute,sports,
        office,wireless_gaming,wired_gaming,phone_cals,color,price)
                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?);'''

        for tasks in headphones:
            tasks = list(tasks)
            self.sqlite_connection.execute(sql, tasks)
            self.sqlite_connection.commit()

        logger.info("Filled data into database")

    def get_all_data_from_db(self):
        pass

    def update_db_object(self):
        pass

    def insert_db_object(self):
        pass

    def add_db_object(self):
        pass

    def remove_db_object(self):
        pass
