from pathlib import Path
import configparser
import os

from store.utils.update_ui import Md5Ui

BASE_DIR = Path(__file__).resolve().parent.parent

table_conf = configparser.ConfigParser()
table_conf.read(os.path.join(BASE_DIR, 'store/configs/table.conf'))


def get_update_ui():
    Md5Ui.update_ui(os.path.join(BASE_DIR, 'store/ui/md5.txt'), os.path.join(BASE_DIR, 'store/ui/main.ui'))
    from store.ui.main_ui import Ui_MainWindow
    return Ui_MainWindow


class InitSettings:

    def __init__(self, win):
        self._WIN = win

        self._global()
        self._table()

    def _global(self):
        self._WIN.setWindowTitle("Store")

    def _table(self):
        for n_col in range(3):
            self._WIN.table_main.setColumnWidth(n_col, int(table_conf[f'col{n_col}']['width']))

