#!/usr/bin/env python3
# coding --utf-8--
import time

from store.widgets.buttons.base import BaseButton, Ui_MainWindow
from store.db.sqlite_wrapper import SqliteWrapper
from loguru import logger


class AddButton(BaseButton):
    def __init__(self, parent: Ui_MainWindow = None):
        super().__init__(parent)

        parent.button_add.clicked.connect(self._action)
        self.sqlite_db = SqliteWrapper()

    def _action(self):
        logger.info("Add new default value...")
        self.sqlite_db.add_db_object("None", "Default", 10, 2015, 9, 6.7, 7.0, 9.0, 8.0, 5, "Default", 100)

        # define topic
        self._update_request()
