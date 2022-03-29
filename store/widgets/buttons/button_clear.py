from store.widgets.buttons.base import BaseButton, Ui_MainWindow


class ClearButton(BaseButton):

    def __init__(self, parent: Ui_MainWindow = None):
        super().__init__(parent)

        parent.button_clear.clicked.connect(self._action)

    def _action(self):
        print("TEST CLEAR BUTTON")
        pass
