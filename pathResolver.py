# -*- coding: utf-8 -*-

import sys
import re

from enum import Enum
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

class AllowedOperations(Enum):
    REVERSE_SLASHES=1
    GET_FILENAME=2
    GET_PATH=3
    GET_FSTRING=4

class PathResolverMain(QWidget):
    def __init__(self):
        super(PathResolverMain, self).__init__()
        self._init_ui()

    # Private

    def _on_text_changed(self):
        if self.past_box != '':
            self._reverse_slashes()

    def _reverse_slashes(self):
        box_text=self.past_box.text()
        box_text=box_text.replace('/', '\\')
        self.clipboard.clear()
        self.clipboard.setText(box_text)
        self.copy_box.setText(box_text)

    def _get_filename(self):
        box_text=self.past_box.text()
        if re.search(r'[^\\/]+$', box_text):
            filename=re.search(r'[^\\/]+$', box_text)
            self.clipboard.clear()
            self.clipboard.setText(filename[0])
            self.copy_box.setText(filename[0])
        else:
            self.copy_box.setText('File pattern haven\'t recognized')

    def _get_pathtofile(self):
        box_text=self.past_box.text()
        if re.search(r'(.*[\\|/]).*', box_text):
            pathtofile=re.search(r'(.*[\\|/]).*', box_text)
            self.clipboard.clear()
            self.clipboard.setText(pathtofile.group(1))
            self.copy_box.setText(pathtofile.group(1))
        else:
            self.copy_box.setText('Path pattern haven\'t recognized')
    
    def _get_fstring(self):
        box_text="\"" + self.past_box.text() + "\""
        box_text=box_text.replace('\\', '\\\\')
        self.clipboard.clear()
        self.clipboard.setText(box_text)
        self.copy_box.setText(box_text)

    def _init_ui(self):
        self.setWindowTitle("Path Resolver")
        self.setFixedSize(QSize(600, 130))

        self.clipboard=QApplication.clipboard()

        base_layout=QVBoxLayout()
        top_layout=QFormLayout()
        bottom_layout=QHBoxLayout()

        # Menu bar

        self.menu_bar=QMenuBar()
        file_menu=self.menu_bar.addMenu('File')
        edit_menu=self.menu_bar.addMenu('Edit')
        auto_menu=edit_menu.addMenu('Auto action')
        window_menu=edit_menu.addMenu('Window')

        exit_action=QAction('Exit', self)

        auto_none=QAction('None', self)
        auto_reverse=QAction('Reverse', self)
        auto_path=QAction('Get path', self)
        auto_file=QAction('Get filename', self)
        auto_fstring=QAction('Get fstring', self)

        window_default=QAction('Default', self)
        window_aot=QAction('Always on top', self)

        auto_none.setCheckable(True)
        auto_reverse.setCheckable(True)
        auto_path.setCheckable(True)
        auto_file.setCheckable(True)
        auto_fstring.setCheckable(True)

        window_default.setCheckable(True)
        window_aot.setCheckable(True)

        file_menu.addAction(exit_action)
        auto_menu.addAction(auto_none)
        auto_menu.addAction(auto_reverse)
        auto_menu.addAction(auto_path)
        auto_menu.addAction(auto_file)
        auto_menu.addAction(auto_fstring)
        window_menu.addAction(window_default)
        window_menu.addAction(window_aot)
        base_layout.addWidget(self.menu_bar)


        # Top layout

        self.past_box=QLineEdit()
        self.copy_box=QLineEdit()

        self.past_box=QLineEdit(self)
        self.copy_box=QLineEdit(self)
        self.copy_box.setReadOnly(True)

        self.past_box.textChanged.connect(self._on_text_changed)

        top_layout.addRow('Past', self.past_box)
        top_layout.addRow('Copy', self.copy_box)

        # Bottom layout

        reverse_button=QPushButton('[1] Reverse slahes')
        pathonly_button=QPushButton('[2] Get path only')
        fileonly_button=QPushButton('[3] Get file only')
        fstring_button=QPushButton('[4] Get format string')

        reverse_button.setObjectName('reverse_button')
        pathonly_button.setObjectName('pathonly_button')
        fileonly_button.setObjectName('fileonly_button')
        fstring_button.setObjectName('fstring_button')

        reverse_button.clicked.connect(self._reverse_slashes)
        pathonly_button.clicked.connect(self._get_pathtofile)
        fileonly_button.clicked.connect(self._get_filename)
        fstring_button.clicked.connect(self._get_fstring)

        bottom_layout.addWidget(reverse_button)
        bottom_layout.addWidget(pathonly_button)
        bottom_layout.addWidget(fileonly_button)
        bottom_layout.addWidget(fstring_button)

        base_layout.addLayout(top_layout)
        base_layout.addLayout(bottom_layout)
        self.setLayout(base_layout)


if __name__ == "__main__":
    app=QApplication(sys.argv)

    app_instance=PathResolverMain()
    app_instance.show()

    app.exec_()
