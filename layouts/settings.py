from PySide6 import QtWidgets
from core.ui_layout import UILayout

class SettingsLayout(QtWidgets.QHBoxLayout, UILayout):
    def __init__(self):
        super().__init__()

        # ================= LEFT LIST =================

        self.categories = QtWidgets.QListWidget()
        self.categories.setFixedWidth(180)

        self.categories.addItems([
            "General",
            "Appearance",
            "Account",
            "Advanced"
        ])

        # ================= RIGHT SIDE =================

        self.right = QtWidgets.QVBoxLayout()

        # ---- HEADER ----
        self.header = QtWidgets.QLabel("Settings")
        self.header.setObjectName("title")

        # ---- GENERAL ----
        self.general_group = QtWidgets.QGroupBox("General")
        self.general_layout = QtWidgets.QFormLayout()

        self.auto_start = QtWidgets.QCheckBox("Start with system")
        self.notifications = QtWidgets.QCheckBox("Enable notifications")

        self.general_layout.addRow(self.auto_start)
        self.general_layout.addRow(self.notifications)
        self.general_group.setLayout(self.general_layout)

        # ---- APPEARANCE ----
        self.appearance_group = QtWidgets.QGroupBox("Appearance")
        self.appearance_layout = QtWidgets.QFormLayout()

        self.theme = QtWidgets.QComboBox()
        self.theme.addItems(["Dark", "Light", "System"])

        self.font_size = QtWidgets.QSpinBox()
        self.font_size.setRange(10, 24)
        self.font_size.setValue(14)

        self.appearance_layout.addRow("Theme", self.theme)
        self.appearance_layout.addRow("Font size", self.font_size)
        self.appearance_group.setLayout(self.appearance_layout)

        # ---- ACCOUNT ----
        self.account_group = QtWidgets.QGroupBox("Account")
        self.account_layout = QtWidgets.QFormLayout()

        self.username = QtWidgets.QLineEdit()
        self.email = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

        self.account_layout.addRow("Username", self.username)
        self.account_layout.addRow("Email", self.email)
        self.account_layout.addRow("Password", self.password)
        self.account_group.setLayout(self.account_layout)

        # ---- ADVANCED ----
        self.advanced_group = QtWidgets.QGroupBox("Advanced")
        self.advanced_layout = QtWidgets.QVBoxLayout()

        self.debug_mode = QtWidgets.QCheckBox("Enable debug mode")
        self.save_logs = QtWidgets.QCheckBox("Save logs to file")

        self.advanced_layout.addWidget(self.debug_mode)
        self.advanced_layout.addWidget(self.save_logs)
        self.advanced_group.setLayout(self.advanced_layout)

        # ---- BOTTOM BUTTONS ----
        self.buttons = QtWidgets.QHBoxLayout()
        self.buttons.addStretch()

        self.reset_btn = QtWidgets.QPushButton("Reset")
        self.apply_btn = QtWidgets.QPushButton("Apply")
        self.apply_btn.setObjectName("primary")

        self.buttons.addWidget(self.reset_btn)
        self.buttons.addWidget(self.apply_btn)

        # ================= ADD RIGHT =================

        self.right.addWidget(self.header)
        self.right.addWidget(self.general_group)
        self.right.addWidget(self.appearance_group)
        self.right.addWidget(self.account_group)
        self.right.addWidget(self.advanced_group)
        self.right.addStretch()
        self.right.addLayout(self.buttons)

        # ================= MAIN =================

        self.addWidget(self.categories)
        self.addLayout(self.right)
