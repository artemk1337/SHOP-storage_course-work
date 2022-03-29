from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import sys
import os

from store.settings import InitSettings, get_update_ui
from store.widgets.buttons import InitButtons


Ui_MainWindow = get_update_ui()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setCentralWidget(self.layoutWidget)

        InitSettings(self)
        InitButtons(self)


if __name__ == "__main__":
    APP = QApplication(sys.argv)
    WIN = MainWindow()
    WIN.show()
    sys.exit(APP.exec())
