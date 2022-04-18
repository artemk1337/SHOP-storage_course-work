#!/usr/bin/env python3
# coding --utf-8--

from store.widgets.buttons.base import BaseButton, Ui_MainWindow


class AddButton(BaseButton):

    def __init__(self, parent: Ui_MainWindow = None):
        super().__init__(parent)

        parent.button_add.clicked.connect(self._action)

    def _action(self):
        logger.info("TEST ADD BUTTON")
        pass