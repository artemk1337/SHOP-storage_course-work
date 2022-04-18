#!/usr/bin/env python3
# coding --utf-8--
from store.widgets.buttons.base import BaseButton, Ui_MainWindow


class DelButton(BaseButton):

    def __init__(self, parent: Ui_MainWindow = None):
        super().__init__(parent)

        parent.button_del.clicked.connect(self._action)

    def _action(self):
        logger.info("TEST DEL BUTTON")
        pass
