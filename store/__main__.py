#!/usr/bin/env python3
# coding --utf-8--

import sys
from store import settings
from PyQt5.QtWidgets import QApplication
from store.main_window.main_window import MainWindow
from store.widgets.main_table_widget import WinTableData

if __name__ == "__main__":
    settings.InitSettings.update_ui()
    APP = QApplication(sys.argv)
    WIN = MainWindow()
    WIN.show()

    TA = WinTableData(WIN)

    sys.exit(APP.exec())
