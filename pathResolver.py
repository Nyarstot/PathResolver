import glob
import sys
import re

from PyQt5 import QtGui
from PyQt5 import QtCore

from PyQt5.QtCore import QSize

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget

class PathResolverMain(QWidget):
    def __init__(self):
        super().__init__()
        self._init_ui()

    # Private

    def _init_ui(self):
        self.setWindowTitle("Path Resolver")
        self.setFixedSize(QSize(600, 300))

        base_layout=QVBoxLayout()
        textbox_layout=QFormLayout()

        past_box=QLineEdit(self)
        copy_box=QLineEdit(self)
        copy_box.setReadOnly(True)

        textbox_layout.addRow('Past', past_box)
        textbox_layout.addRow('Copy', copy_box)

        base_layout.addLayout(textbox_layout)

        self.setLayout(base_layout)

    # Public

if __name__ == "__main__":
    app=QApplication(sys.argv)

    app_instance=PathResolverMain()
    app_instance.show()

    app.exec_()