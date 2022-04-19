#!/usr/bin/env python3
# coding --utf-8--
import requests

from store.db.singleton import Singleton
from collections import namedtuple
from store.db import get_db_data
from loguru import logger
import sqlite3
import pathlib
import typing

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent.__str__() + "/data"


class SqliteWrapper(metaclass=Singleton):
    fields = "image,name,sound,year,commute,sports,office,wireless_gaming,wired_gaming,phone_cals,color,price,id" \
        .split(",")
    DBAttributes = namedtuple("DBAttributes", fields, defaults=(None,) * len(fields))
    cursor: sqlite3.Cursor

    def __init__(self, db_file_name: str = BASE_DIR + "/sqlite_table.db", table_name: str = "sqlitedb_developers"):
        self._init(db_file_name)
        self.table_name = table_name

    def _init(self, db_file_name: str):
        """
            Open connection with selected database
        :param db_file_name: path to db file name
        :return: nothing

        """
        self.db_file_name = db_file_name
        assert (self.db_file_name.split(".")[-1] != ".db", "You using not database file! Try to open \"sqlite3.db\".")

        self.sqlite_connection = sqlite3.connect(self.db_file_name, check_same_thread=False)
        self.cursor = self.sqlite_connection.cursor()

    def _stop_db(self):
        self.cursor.close()
        if self.sqlite_connection:
            self.sqlite_connection.close()

    def __del__(self):
        self._stop_db()

    def reset(self, db_file_name: str = BASE_DIR + "/sqlite_table.db"):
        """
            If you want to open a new database
        :param db_file_name: path to sqlite database file
        :return: nothing
        """
        self._stop_db()
        self._init(db_file_name)

    def create_table(self):
        if not self.is_empty_db():
            logger.warning(f"Table \"{self.table_name}\" already exists!")
            return

        sqlite_create_table_query = f'''CREATE TABLE {self.table_name} (
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

        self.cursor = self.sqlite_connection.cursor()
        logger.info("Таблица SQLite создана")

    def fill_database(self, page_file: str = BASE_DIR + '/page.xml'):
        """
            Parse xml page to fill up headphones
        :return:
        """
        headphones = get_db_data.HeadphonesWeb.parse_page(filename=page_file)

        for tasks in headphones:
            tasks = list(tasks)
            self.add_db_object(*tasks)

        logger.info("Filled data into database")

    def get_all_data_from_db(self) -> list:
        self.cursor = self.sqlite_connection.cursor()

        cursor_updated = self.cursor.execute(f"SELECT * FROM {self.table_name};")
        output_data = cursor_updated.fetchall()

        return output_data

    def is_empty_db(self) -> bool:
        sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""
        self.cursor.execute(sql_query)

        names = self.cursor.fetchall()

        return not (len(names) != 0 and names[0][0] == self.table_name)

    def __where_query_request(self, find_attributes: DBAttributes) -> tuple[str, str]:
        if find_attributes._field_defaults == find_attributes:
            logger.warning("You set all values default! Try to set any of parameters...")
            return "", ""

        sql_query_select = f"SELECT * FROM {self.table_name} "

        where_fields = "WHERE "
        for name, value in zip(find_attributes._fields, find_attributes):
            if value is not None:
                if not isinstance(value, str) or "%" not in value:
                    where_fields += f"{name}='{value}'"
                else:
                    where_fields += f"{name} like '{value}'"
        sql_query_select += where_fields + ";"
        return sql_query_select, where_fields

    def get_db_object(self, find_attributes: DBAttributes):
        sql_query_select, where_fields = self.__where_query_request(find_attributes)

        cursor_updated = self.cursor.execute(sql_query_select)
        output_data = cursor_updated.fetchall()

        return output_data

    def update_db_object(self, find_attributes: DBAttributes, update_attributes: DBAttributes) -> bool:
        _, where_fields = self.__where_query_request(find_attributes)

        try:
            for name, value in zip(update_attributes._fields, update_attributes):
                if value is not None:
                    sql_query_update = f"UPDATE {self.table_name} set {name}='{value}' " + where_fields

                    logger.info(sql_query_update)

                    self.sqlite_connection.execute(sql_query_update)
                    self.sqlite_connection.commit()

                    return True
        except Exception as e:
            logger.error(f"Catch error while update from db: {e}")
            return False

    def add_db_object(self, image: str, name: str, sound: float, year: int, commute: int, sports: float,
                      office: float, wireless_gaming: float, wired_gaming: float, phone_cals: int, color: str,
                      price: float):
        sql = f'''INSERT INTO {self.table_name}(image,name,sound,year,commute,sports,
        office,wireless_gaming,wired_gaming,phone_cals,color,price)
                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?);'''

        tasks = (image, name, sound, year, commute, sports,
                 office, wireless_gaming, wired_gaming, phone_cals, color, price)

        try:
            self.sqlite_connection.execute(sql, tasks)
            self.sqlite_connection.commit()

            self.cursor = self.sqlite_connection.cursor()
        except Exception as e:
            logger.error(f"Catch error while add new value in db: {e}")

    def remove_db_object(self, attribute_name: str, attribute_value: typing.Union[int, float, str]):
        try:
            sql_query = f"DELETE from {self.table_name} where {attribute_name}='{attribute_value}'"
            self.sqlite_connection.execute(sql_query)
            self.sqlite_connection.commit()

            self.cursor = self.sqlite_connection.cursor()
            logger.info(f"Successfully removed object with attributes: {attribute_name}='{attribute_value}'")
        except Exception as e:
            logger.error(f"Catch error while removing from db: {e}")

    @staticmethod
    def download_image(url: str, file_name: str):
        r = requests.get(url)
        # retrieving data from the URL using get method

        with open(file_name, 'wb') as f:
            # giving a name and saving it in any required format
            # opening the file in write mode
            f.write(r.content)

    def __prepare_image_name(self, name: str, temp_directory: str = BASE_DIR + "/images") -> str:
        return temp_directory + "/" + name \
                .replace(" ", "_") \
                .replace("/", "-") \
                .lower() + ".jpg"

    def download_images(self, temp_directory: str = BASE_DIR + "/images"):
        for db_object in self.get_all_data_from_db():
            name = self.__prepare_image_name(db_object[3], temp_directory)
            url = db_object[1]
            try:
                self.download_image(url, name)
                logger.info(f"Downloading {name} :{url}")
            except Exception as e:
                logger.warning(f"file_name: \t {db_object[3]} \n {e} ")

    def find_image(self, name: str):
        return self.__prepare_image_name(name)
