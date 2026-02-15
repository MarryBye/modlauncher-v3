from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget

from core.ui_manager import UIManager

from layouts import HomeLayout, SettingsLayout

pages = [
    ("home", HomeLayout()),
    ("settings", SettingsLayout()),
]

class BaseWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(BaseWindow, self).__init__(*args, **kwargs)

        self.widget = QWidget()
        self.ui_manager = UIManager()
        self.setWindowTitle("Home")
        self.widget.setLayout(self.ui_manager)
        self.setCentralWidget(self.widget)

        for page in pages:
            self.ui_manager.add_layout(page[0], page[1])
