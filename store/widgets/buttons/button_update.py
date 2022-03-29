from store.widgets.buttons.base import BaseButton, Ui_MainWindow


class UpdateButton(BaseButton):

    def __init__(self, parent: Ui_MainWindow = None):
        super().__init__(parent)

        parent.button_update.clicked.connect(self._action)

    def _action(self):
        print("TEST UPDATE BUTTON")
        pass
