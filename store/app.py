from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPixmap
import sys

from store.settings import SetSettings, Ui_MainWindow, BASE_DIR
from store.widgets.buttons import InitButtons


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setCentralWidget(self.layoutWidget)

        SetSettings(self)
        InitButtons(self)


if __name__ == "__main__":
    APP = QApplication(sys.argv)
    WIN = MainWindow()
    WIN.show()
    sys.exit(APP.exec())
