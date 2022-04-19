#!/usr/bin/env python3
# coding --utf-8--

from PyQt5.QtWidgets import QTableWidgetItem, QSpinBox

from store.db.sqlite_wrapper import SqliteWrapper
from store.ui.main_ui import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from loguru import logger
import threading
import zmq


class WinTableData:
    def __init__(self, win: Ui_MainWindow):
        self._WIN = win

        self._WIN.table_main.itemSelectionChanged.connect(self.__update_image_preview)
        self._WIN.table_main.itemChanged.connect(self.update_selected_element)
        self._WIN.text_search.textChanged.connect(self.__search_db)
        self.sqlite_db = SqliteWrapper()

        self._update_data_from_db(self.sqlite_db.get_all_data_from_db())

        self.context = zmq.Context()

        self.socket = self.context.socket(zmq.SUB)
        self.socket.connect('tcp://127.0.0.1:4000')

        self.socket.subscribe('remove_button')
        self.socket.subscribe('update_button')
        self.socket.subscribe('clear_button')

        self.listener_thread = threading.Thread(target=self.__listener, daemon=True)
        self.listener_thread.start()

    def add_table_row(self, idx: int, name: str, count: int, price: int, description: None or str = None) -> None:
        n_row = self._WIN.table_main.rowCount()
        self._WIN.table_main.insertRow(n_row)

        for n_col, value in zip((0, 1, 3, 4), (str(idx), name, str(price) + " $", description)):
            self._add_cell_item(n_row, n_col, value)

        self._add_cell_widget(n_row, 2, count, QSpinBox)

    def _add_cell_item(self, n_row, n_col, value):
        item = QTableWidgetItem(value)
        item.setToolTip(value)
        self._WIN.table_main.setItem(n_row, n_col, item)

    def _add_cell_widget(self, n_row, n_col, value, widget):
        item = QSpinBox()
        item.setValue(value)
        self._WIN.table_main.setCellWidget(n_row, n_col, item)

    def _update_data_from_db(self, values: list):
        index = 1

        for db_object in values:
            self.add_table_row(index, name=db_object[3], count=50, price=db_object[-1])
            index += 1
        n_row = self._WIN.table_main.rowCount()

        for row_id in range(n_row):
            if row_id > index:
                self._WIN.table_main.removeRow(row_id)

    def _remove_data_from_db(self):
        name = self._WIN.table_main.selectedItems()[1]

        logger.info(f"Trying to delete attribute with name: \"{name.text()}\"")

        find_attributes = self.sqlite_db.DBAttributes(name=name.text())
        find_values = self.sqlite_db.get_db_object(find_attributes)
        try:
            for att in find_values:
                self._WIN.table_main.removeRow(att[0] - 1)
        except Exception as e:
            logger.error(e)
        if len(find_values) > 0:
            self.sqlite_db.remove_db_object("name", name.text())
        else:
            # Remove last object which not in db
            selected_row_id = self._WIN.table_main.rowCount()
            try:
                self._WIN.table_main.removeRow(selected_row_id - 1)
            except Exception as e:
                logger.warning(e)

    def __update_image_preview(self):
        try:
            name = self.sqlite_db.find_image(self._WIN.table_main.selectedItems()[1].text())
            pixmap = QPixmap(name)
            self._WIN.preview_img.setPixmap(pixmap)
        except Exception as e:
            logger.error(e)

    def __search_db(self):
        current_text = self._WIN.text_search.toPlainText() + "%"
        self._WIN.table_main.clear()
        self._WIN.table_main.setRowCount(0)
        if len(current_text):

            find_attributes = self.sqlite_db.DBAttributes(name=current_text)
            found_values = self.sqlite_db.get_db_object(find_attributes)
            self._update_data_from_db(found_values)
        else:
            self._update_data_from_db(self.sqlite_db.get_all_data_from_db())

    def update_selected_element(self, new_values):
        if self._WIN.table_main.currentItem() is not None:
            find_attribute = self.sqlite_db.DBAttributes(id=self._WIN.table_main.currentRow() + 1)
            update_attribute = self.sqlite_db.DBAttributes(name=new_values.text())
            self.sqlite_db.update_db_object(find_attribute, update_attribute)
            logger.info("Value changed in db!")

    def __del__(self):
        if hasattr(self, "listener_thread"):
            self.listener_thread.join()

    def __listener(self):
        while True:
            try:
                topic = self.socket.recv()
                data = self.socket.recv()
                logger.info(f"Got {data=} from {topic=}")

                match topic:
                    case b"update_button":
                        self._update_data_from_db(self.sqlite_db.get_all_data_from_db())
                    case b"remove_button":
                        self._remove_data_from_db()
            except zmq.ZMQError as e:
                if e.errno == zmq.ETERM:
                    break
            except Exception as e:
                logger.error(e)
