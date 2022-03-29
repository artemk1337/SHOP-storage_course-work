from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import sys

from store.widgets.buttons import InitButtons
from store.settings import InitSettings, update_ui
from store.ui.main_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setCentralWidget(self.layoutWidget)

        InitSettings(self)
        InitButtons(self)


if __name__ == "__main__":
    update_ui()
    APP = QApplication(sys.argv)
    WIN = MainWindow()
    WIN.show()
    sys.exit(APP.exec())
