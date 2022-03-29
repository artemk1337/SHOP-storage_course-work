from PyQt5.QtWidgets import QWidget

from store.settings import Ui_MainWindow


class BaseButton(QWidget, Ui_MainWindow):
    def __init__(self, parent: Ui_MainWindow = None):
        super().__init__(parent)

    @property
    def _action(self):
        raise NotImplementedError
