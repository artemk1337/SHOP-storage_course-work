from PyQt5.QtWidgets import QTableWidgetItem, QSpinBox

from store.settings import Ui_MainWindow


class WinTableData:
    def __init__(self, win: Ui_MainWindow):
        self._WIN = win

    def add_table_row(self, idx: int, name: str, count: int, price: int, description: None or str = None) -> None:
        n_row = self._WIN.table_main.rowCount()
        self._WIN.table_main.insertRow(n_row)

        for n_col, value in zip((0, 1, 3, 4), (str(idx), name, str(price), description)):
            self._add_cell_item(n_row, n_col, value)

        self._add_cell_widget(n_row, 2, count, QSpinBox)

    def _add_cell_item(self, n_row, n_col, value):
        item = QTableWidgetItem(value)
        item.setToolTip(value)
        self._WIN.table_main.setItem(n_row, n_col, item)

    def _add_cell_widget(self, n_row, n_col, value, widget):
        item = QSpinBox()
        item.setValue(value)
        self._WIN.table_main.setCellWidget(n_row, n_col, item)
