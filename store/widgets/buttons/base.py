#!/usr/bin/env python3
# coding --utf-8--
from PyQt5.QtWidgets import QWidget

from store.ui.main_ui import Ui_MainWindow
from loguru import logger
import zmq


class BaseButton(QWidget, Ui_MainWindow):
    # Connection for db updating...
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:4000")

    def __init__(self, parent: Ui_MainWindow = None):
        super().__init__(parent)

    @property
    def _action(self):
        raise NotImplementedError

    def _update_request(self):
        self.socket.send_multipart([b'update_button', b'update'])
