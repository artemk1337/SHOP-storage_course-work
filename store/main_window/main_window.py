from PyQt5.QtWidgets import QMainWindow

from store.widgets.buttons import InitButtons
from store.ui.main_ui import Ui_MainWindow
from store.settings import InitSettings


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setCentralWidget(self.layoutWidget)

        InitSettings(self)
        InitButtons(self)




