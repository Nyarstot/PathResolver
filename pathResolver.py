# -*- coding: utf-8 -*-

import sys
import re

from PyQt5.QtCore import QSize

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QMenu

class PathResolverMain(QWidget):
    def __init__(self):
        super(PathResolverMain, self).__init__()
        self._init_ui()

    # Private

    def _init_ui(self):
        self.setWindowTitle("Path Resolver")
        self.setFixedSize(QSize(600, 100))

        base_layout=QVBoxLayout()
        top_layout=QFormLayout()
        bottom_layout=QHBoxLayout()

        # Menu bar

        # menu_bar=QMenuBar()

        # file_menu=menu_bar.addMenu('File')
        # exit_action=QAction('Exit')
        # file_menu.addAction(exit_action)

        # edit_menu=menu_bar.addMenu('Edit')

        # base_layout.addWidget(menu_bar)

        # Top layout

        past_box=QLineEdit(self)
        copy_box=QLineEdit(self)
        copy_box.setReadOnly(True)

        top_layout.addRow('Past', past_box)
        top_layout.addRow('Copy', copy_box)

        # Bottom layout

        reverse_button=QPushButton('Reverse slahes')
        pathonly_button=QPushButton('Get path only')
        fileonly_button=QPushButton('Get file only')
        fstring_button=QPushButton('Get format string')

        bottom_layout.addWidget(reverse_button)
        bottom_layout.addWidget(pathonly_button)
        bottom_layout.addWidget(fileonly_button)
        bottom_layout.addWidget(fstring_button)

        base_layout.addLayout(top_layout)
        base_layout.addLayout(bottom_layout)
        self.setLayout(base_layout)

    # Public

if __name__ == "__main__":
    app=QApplication(sys.argv)

    app_instance=PathResolverMain()
    app_instance.show()

    app.exec_()