# -*- coding: utf-8 -*-

import sys
import re
import argparse
import pyperclip

from PyQt5.QtCore import Qt
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


class PathResolverApp:

    def __init__(self):
        super(PathResolverApp, self).__init__()

    # Public

    def reverse_slashes(self, path:str):
        reversed_path = path.replace('/', '\\')
        pyperclip.copy(reversed_path)
        return reversed_path

    def get_filename(self, path:str):
        if re.search(r'[^\\/]+$', path):
            filename = re.search(r'[^\\/]+$', path)
            pyperclip.copy(filename[0])
            return filename[0]
        else:
            print("ERROR: File pattern haven\'t recognized")

    def get_path_only(self, path:str):
        if re.search(r'(.*[\\|/]).*', path):
            path_to_file = re.search(r'(.*[\\|/]).*', path)
            pyperclip.copy(path_to_file.group(1))
            return path_to_file.group(1)
        else:
            print("ERROR: Path pattern haven\'t recognized")
    
    def get_formatted_string(self, path:str):
        fpath = path.replace('/', '\\')
        fpath = fpath.replace('\\', '\\\\')
        fpath = "\"" + fpath + "\""
        pyperclip.copy(fpath)
        return fpath


class PathResolverGUI(QWidget):

    def __init__(self):
        super(PathResolverGUI, self).__init__()

        self.base_app = PathResolverApp()
        self.setWindowTitle("Path Resolver")
        self.setFixedSize(QSize(600, 130))

        self.base_layout = QVBoxLayout()
        self.top_layout = QFormLayout()
        self.bottom_layout = QHBoxLayout()

        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        # Menu Bar

        self.menu_bar = QMenuBar()
        self.file_menu = self.menu_bar.addMenu("File")
        self.edit_menu = self.menu_bar.addMenu("Edit")
        self.auto_menu = self.edit_menu.addMenu("Auto Action")
        self.window_menu = self.edit_menu.addMenu("Window")
        
        self.exit_action=QAction('Exit', self)
        self.auto_none=QAction('None', self)
        self.auto_reverse=QAction('Reverse', self)
        self.auto_path=QAction('Get path', self)
        self.auto_file=QAction('Get filename', self)
        self.auto_fstring=QAction('Get fstring', self)

        self.window_default=QAction('Default', self)
        self.window_aot=QAction('Always on top', self)
        self.window_aot.triggered.connect(self._set_window_flag_aot)
        self.window_default.triggered.connect(self._set_window_flag_default)

        self.auto_none.setCheckable(True)
        self.auto_reverse.setCheckable(True)
        self.auto_path.setCheckable(True)
        self.auto_file.setCheckable(True)
        self.auto_fstring.setCheckable(True)

        self.window_default.setCheckable(True)
        self.window_aot.setCheckable(True)

        self.file_menu.addAction(self.exit_action)
        self.auto_menu.addAction(self.auto_none)
        self.auto_menu.addAction(self.auto_reverse)
        self.auto_menu.addAction(self.auto_path)
        self.auto_menu.addAction(self.auto_file)
        self.auto_menu.addAction(self.auto_fstring)
        self.window_menu.addAction(self.window_default)
        self.window_menu.addAction(self.window_aot)
        self.base_layout.addWidget(self.menu_bar)

        # Top Layout

        self.past_box=QLineEdit()
        self.copy_box=QLineEdit()

        self.past_box=QLineEdit(self)
        self.copy_box=QLineEdit(self)
        self.copy_box.setReadOnly(True)
        self.past_box.textChanged.connect(self._on_text_changed)

        self.top_layout.addRow('Past', self.past_box)
        self.top_layout.addRow('Copy', self.copy_box)

        # Bottom Layout

        self.reverse_button=QPushButton('[1] Reverse slahes')
        self.pathonly_button=QPushButton('[2] Get path only')
        self.fileonly_button=QPushButton('[3] Get file only')
        self.fstring_button=QPushButton('[4] Get format string')

        self.reverse_button.setObjectName('reverse_button')
        self.pathonly_button.setObjectName('pathonly_button')
        self.fileonly_button.setObjectName('fileonly_button')
        self.fstring_button.setObjectName('fstring_button')

        self.reverse_button.clicked.connect(self._reverse_action)
        self.pathonly_button.clicked.connect(self._path_only_action)
        self.fileonly_button.clicked.connect(self._filename_action)
        self.fstring_button.clicked.connect(self._fstring_action)

        self.bottom_layout.addWidget(self.reverse_button)
        self.bottom_layout.addWidget(self.pathonly_button)
        self.bottom_layout.addWidget(self.fileonly_button)
        self.bottom_layout.addWidget(self.fstring_button)

        self.base_layout.addLayout(self.top_layout)
        self.base_layout.addLayout(self.bottom_layout)
        self.setLayout(self.base_layout)

    # Private

    def _reverse_action(self):
        box_text = str(self.past_box.text())
        box_text = self.base_app.reverse_slashes(box_text)
        self.copy_box.setText(box_text)

    def _filename_action(self):
        box_text = self.past_box.text()
        box_text = self.base_app.get_filename(box_text)
        self.copy_box.setText(box_text)

    def _path_only_action(self):
        box_text = self.past_box.text()
        box_text = self.base_app.get_path_only(box_text)
        self.copy_box.setText(box_text)

    def _fstring_action(self):
        box_text = self.past_box.text()
        box_text = self.base_app.get_formatted_string(box_text)
        self.copy_box.setText(box_text)

    def _on_text_changed(self):
        if self.past_box != '':
            self._reverse_action()

    def _set_window_flag_default(self):
        if self.window_aot.isChecked():
            self.window_aot.setChecked(False)

    def _set_window_flag_aot(self):
        if self.window_default.isChecked():
            self.window_default.setChecked(False)
            

if __name__ == "__main__":

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-p")
    arg_parser.add_argument("-f")

    args = arg_parser.parse_args()
    path = args.p
    func = args.f

    if path != None:
        no_gui = PathResolverApp()
        if func == "reverse" or func == None:
            result = no_gui.reverse_slashes(path)
            print ("DONE: " + result)
        if func == "filename":
            result = no_gui.get_filename(path)
            print("DONE: " + result)
        if func == "pathonly":
            result = no_gui.get_path_only(path)
            print("DONE: " + result)
        if func == "fstring":
            result = no_gui.get_formatted_string(path)
            print("DONE: " + result)
    else:
        app=QApplication(sys.argv)
        app_instance=PathResolverGUI()
        app_instance.show()
        app.exec_()
