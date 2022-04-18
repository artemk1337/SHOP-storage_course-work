#!/usr/bin/env python3
# coding --utf-8--

from pathlib import Path
import configparser
import os

from store.utils.update_ui import Md5Ui

BASE_DIR = Path(__file__).resolve().parent.parent


class InitSettings:
    table_conf = configparser.ConfigParser()

    def __init__(self, win):
        self._WIN = win
        self.table_conf.read(os.path.join(BASE_DIR, 'store/configs/table.conf'))

        self._global()
        self._table()

    @staticmethod
    def update_ui():
        Md5Ui.update_ui(os.path.join(BASE_DIR, 'store/ui/md5.txt'), os.path.join(BASE_DIR, 'store/ui/main.ui'))

    def _global(self):
        self._WIN.setWindowTitle("Store")

    def _table(self):
        self.table_conf.read(os.path.join(BASE_DIR, 'store/configs/table.conf'))

        for n_col in range(3):
            self._WIN.table_main.setColumnWidth(n_col, int(self.table_conf[f'col{n_col}']['width']))
