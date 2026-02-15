from PySide6 import QtWidgets
from core.ui_layout import UILayout

from layouts.navpanel import NavPanelLayout


class HomeLayout(QtWidgets.QVBoxLayout, UILayout):
    def __init__(self):
        super().__init__()

        # --- MAIN HORIZONTAL CONTAINER ---
        self.main = QtWidgets.QHBoxLayout()

        # --- LEFT NAV PANEL ---
        self.nav_panel = QtWidgets.QWidget()
        self.nav_layout = NavPanelLayout()
        self.nav_panel.setLayout(self.nav_layout)
        self.nav_panel.setFixedWidth(180)

        # --- RIGHT CONTENT ---
        self.content = QtWidgets.QVBoxLayout()

        self.header = QtWidgets.QLabel("Home")
        self.info = QtWidgets.QLabel("Welcome to the home page")

        self.list_widget = QtWidgets.QListWidget()
        self.list_widget.addItems([
            "Item 1",
            "Item 2",
            "Item 3",
            "Item 4",
        ])

        self.hbox = QtWidgets.QHBoxLayout()
        self.input = QtWidgets.QLineEdit()
        self.button = QtWidgets.QPushButton("Submit")

        self.hbox.addWidget(self.input)
        self.hbox.addWidget(self.button)

        self.content.addWidget(self.header)
        self.content.addWidget(self.info)
        self.content.addWidget(self.list_widget)
        self.content.addLayout(self.hbox)
        self.content.addStretch()

        # --- ADD TO MAIN ---
        self.main.addWidget(self.nav_panel)
        self.main.addLayout(self.content)

        # --- ADD TO ROOT ---
        self.addLayout(self.main)