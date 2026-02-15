from PySide6 import QtWidgets
from core.ui_layout import UILayout


class HomeLayout(QtWidgets.QVBoxLayout, UILayout):
    def __init__(self):
        super().__init__()

        # ================= HEADER =================

        self.header = QtWidgets.QLabel("Welcome back!")
        self.header.setObjectName("title")

        self.subtitle = QtWidgets.QLabel("Quick overview and actions")
        self.subtitle.setObjectName("muted")

        # ================= STATS / INFO =================

        self.stats_group = QtWidgets.QGroupBox("Overview")
        self.stats_layout = QtWidgets.QHBoxLayout()

        self.users_card = QtWidgets.QLabel("Users\n124")
        self.projects_card = QtWidgets.QLabel("Projects\n8")
        self.tasks_card = QtWidgets.QLabel("Tasks\n23")

        self.users_card.setObjectName("card")
        self.projects_card.setObjectName("card")
        self.tasks_card.setObjectName("card")

        self.stats_layout.addWidget(self.users_card)
        self.stats_layout.addWidget(self.projects_card)
        self.stats_layout.addWidget(self.tasks_card)

        self.stats_group.setLayout(self.stats_layout)

        # ================= QUICK ACTIONS =================

        self.actions_group = QtWidgets.QGroupBox("Quick Actions")
        self.actions_layout = QtWidgets.QHBoxLayout()

        self.new_btn = QtWidgets.QPushButton("New Project")
        self.open_btn = QtWidgets.QPushButton("Open")
        self.settings_btn = QtWidgets.QPushButton("Settings")
        self.settings_btn.clicked.connect(
            lambda: self.ui_manager.show_layout("settings")
        )

        self.new_btn.setObjectName("primary")

        self.actions_layout.addWidget(self.new_btn)
        self.actions_layout.addWidget(self.open_btn)
        self.actions_layout.addWidget(self.settings_btn)

        self.actions_group.setLayout(self.actions_layout)

        # ================= LIST =================

        self.list_group = QtWidgets.QGroupBox("Recent Activity")
        self.list_layout = QtWidgets.QVBoxLayout()

        self.list_widget = QtWidgets.QListWidget()
        self.list_widget.addItems([
            "Opened project Alpha",
            "Updated settings",
            "Created new task",
            "Exported data",
            "Closed application"
        ])

        self.list_layout.addWidget(self.list_widget)
        self.list_group.setLayout(self.list_layout)

        # ================= INPUT =================

        self.input_group = QtWidgets.QGroupBox("Quick Command")
        self.input_layout = QtWidgets.QHBoxLayout()

        self.input = QtWidgets.QLineEdit()
        self.input.setPlaceholderText("Type command...")

        self.button = QtWidgets.QPushButton("Execute")
        self.button.setObjectName("primary")

        self.input_layout.addWidget(self.input)
        self.input_layout.addWidget(self.button)

        self.input_group.setLayout(self.input_layout)

        # ================= ADD =================

        self.addWidget(self.header)
        self.addWidget(self.subtitle)
        self.addWidget(self.stats_group)
        self.addWidget(self.actions_group)
        self.addWidget(self.list_group)
        self.addWidget(self.input_group)
        self.addStretch()
