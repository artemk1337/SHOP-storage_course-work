from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap
import sys

from store.main_window import MainWindow
from store.widgets.main_table_widget import WinTableData


if __name__ == "__main__":
    APP = QApplication(sys.argv)
    WIN = MainWindow()
    WIN.show()

    TA = WinTableData(WIN)
    TA.add_table_row(12355, "Example", 21, 9999, "Example description")
    TA.add_table_row(12398, "Best ITEM", 42, 999, None)

    pixmap = QPixmap("../banan.jpeg")
    WIN.preview_img.setPixmap(pixmap)

    sys.exit(APP.exec())
