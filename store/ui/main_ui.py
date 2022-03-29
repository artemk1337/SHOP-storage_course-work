# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/artem/misis/store/store/ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(913, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(8, 10, 901, 588))
        self.layoutWidget.setObjectName("layoutWidget")
        self.main_Layout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.main_Layout.setContentsMargins(5, 5, 5, 5)
        self.main_Layout.setSpacing(3)
        self.main_Layout.setObjectName("main_Layout")
        self.buttons_left_Layout = QtWidgets.QVBoxLayout()
        self.buttons_left_Layout.setSpacing(3)
        self.buttons_left_Layout.setObjectName("buttons_left_Layout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.buttons_left_Layout.addItem(spacerItem)
        self.preview_img = QtWidgets.QLabel(self.layoutWidget)
        self.preview_img.setMinimumSize(QtCore.QSize(147, 147))
        self.preview_img.setMaximumSize(QtCore.QSize(147, 147))
        self.preview_img.setText("")
        self.preview_img.setAlignment(QtCore.Qt.AlignCenter)
        self.preview_img.setObjectName("preview_img")
        self.buttons_left_Layout.addWidget(self.preview_img)
        self.button_add = QtWidgets.QPushButton(self.layoutWidget)
        self.button_add.setMinimumSize(QtCore.QSize(147, 34))
        self.button_add.setMaximumSize(QtCore.QSize(147, 34))
        self.button_add.setObjectName("button_add")
        self.buttons_left_Layout.addWidget(self.button_add)
        self.button_update = QtWidgets.QPushButton(self.layoutWidget)
        self.button_update.setMinimumSize(QtCore.QSize(147, 34))
        self.button_update.setMaximumSize(QtCore.QSize(147, 34))
        self.button_update.setObjectName("button_update")
        self.buttons_left_Layout.addWidget(self.button_update)
        self.button_del = QtWidgets.QPushButton(self.layoutWidget)
        self.button_del.setMinimumSize(QtCore.QSize(147, 34))
        self.button_del.setMaximumSize(QtCore.QSize(147, 34))
        self.button_del.setObjectName("button_del")
        self.buttons_left_Layout.addWidget(self.button_del)
        self.main_Layout.addLayout(self.buttons_left_Layout)
        self.table_search_Layout = QtWidgets.QVBoxLayout()
        self.table_search_Layout.setSpacing(2)
        self.table_search_Layout.setObjectName("table_search_Layout")
        self.search_Layout = QtWidgets.QHBoxLayout()
        self.search_Layout.setSpacing(2)
        self.search_Layout.setObjectName("search_Layout")
        self.text_search = QtWidgets.QTextEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_search.sizePolicy().hasHeightForWidth())
        self.text_search.setSizePolicy(sizePolicy)
        self.text_search.setMinimumSize(QtCore.QSize(0, 31))
        self.text_search.setMaximumSize(QtCore.QSize(16777215, 31))
        self.text_search.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text_search.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text_search.setMarkdown("")
        self.text_search.setObjectName("text_search")
        self.search_Layout.addWidget(self.text_search)
        self.button_clear = QtWidgets.QPushButton(self.layoutWidget)
        self.button_clear.setMinimumSize(QtCore.QSize(31, 31))
        self.button_clear.setMaximumSize(QtCore.QSize(31, 31))
        self.button_clear.setObjectName("button_clear")
        self.search_Layout.addWidget(self.button_clear)
        self.table_search_Layout.addLayout(self.search_Layout)
        self.table_main = QtWidgets.QTableWidget(self.layoutWidget)
        self.table_main.setMinimumSize(QtCore.QSize(621, 541))
        self.table_main.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.table_main.setToolTip("")
        self.table_main.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table_main.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.table_main.setDragEnabled(False)
        self.table_main.setAlternatingRowColors(True)
        self.table_main.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_main.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.table_main.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.table_main.setObjectName("table_main")
        self.table_main.setColumnCount(5)
        self.table_main.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_main.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_main.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_main.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_main.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_main.setHorizontalHeaderItem(4, item)
        self.table_main.horizontalHeader().setVisible(True)
        self.table_main.horizontalHeader().setCascadingSectionResizes(False)
        self.table_main.horizontalHeader().setDefaultSectionSize(75)
        self.table_main.horizontalHeader().setMinimumSectionSize(49)
        self.table_main.horizontalHeader().setSortIndicatorShown(False)
        self.table_main.horizontalHeader().setStretchLastSection(True)
        self.table_main.verticalHeader().setVisible(False)
        self.table_main.verticalHeader().setCascadingSectionResizes(False)
        self.table_main.verticalHeader().setHighlightSections(True)
        self.table_main.verticalHeader().setSortIndicatorShown(False)
        self.table_search_Layout.addWidget(self.table_main)
        self.main_Layout.addLayout(self.table_search_Layout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_add.setText(_translate("MainWindow", "Добавить"))
        self.button_update.setText(_translate("MainWindow", "Обновить"))
        self.button_del.setText(_translate("MainWindow", "Удалить"))
        self.text_search.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.text_search.setPlaceholderText(_translate("MainWindow", "field for search...  "))
        self.button_clear.setText(_translate("MainWindow", "X"))
        self.table_main.setSortingEnabled(False)
        item = self.table_main.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Артикул"))
        item = self.table_main.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Название"))
        item = self.table_main.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Кол."))
        item = self.table_main.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Цена"))
        item = self.table_main.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Описание"))
