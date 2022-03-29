from store.widgets.buttons.button_add import AddButton
from store.widgets.buttons.button_del import DelButton
from store.widgets.buttons.button_update import UpdateButton
from store.widgets.buttons.button_clear import ClearButton
from store.settings import Ui_MainWindow


class InitButtons:

    def __init__(self, parent: Ui_MainWindow = None):
        AddButton(parent)
        DelButton(parent)
        UpdateButton(parent)
        ClearButton(parent)
