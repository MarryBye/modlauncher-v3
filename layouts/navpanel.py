from PySide6 import QtWidgets, QtCore, QtGui
from core.ui_layout import UILayout
from widgets.navbutton import NavButton
from widgets.navlabel import NavSectionLabel


class NavPanelLayout(QtWidgets.QVBoxLayout, UILayout):
    def __init__(self):
        super().__init__()

        self.setSpacing(8)
        self.setContentsMargins(8, 8, 8, 8)

        # ================= PANEL STYLE =================
        self.container = QtWidgets.QFrame()
        self.container.setObjectName("panel-sidebar")

        self.container_layout = QtWidgets.QVBoxLayout()
        self.container_layout.setSpacing(6)
        self.container_layout.setContentsMargins(10, 10, 10, 10)
        self.container.setLayout(self.container_layout)

        # ================= HEADER =================
        self.header = QtWidgets.QLabel("My Application")
        self.header.setObjectName("label-title")
        self.container_layout.addWidget(self.header)

        self.container_layout.addSpacing(6)

        # ================= MAIN SECTION =================
        self.main_label = NavSectionLabel("MAIN")
        self.main_label.setObjectName("label-header")
        self.container_layout.addWidget(self.main_label)

        self.btn_home = NavButton(text="Home", icon_text="🏠")
        self.btn_home.setObjectName("btn")

        self.btn_dashboard = NavButton(text="Dashboard", icon_text="📊")
        self.btn_dashboard.setObjectName("btn")

        self.btn_projects = NavButton(text="Projects", icon_text="📁")
        self.btn_projects.setObjectName("btn")

        self.container_layout.addWidget(self.btn_home)
        self.container_layout.addWidget(self.btn_dashboard)
        self.container_layout.addWidget(self.btn_projects)

        self.container_layout.addSpacing(10)

        # ================= MANAGEMENT =================
        self.manage_label = NavSectionLabel("MANAGEMENT")
        self.manage_label.setObjectName("label-header")
        self.container_layout.addWidget(self.manage_label)

        self.btn_users = NavButton(text="Users", icon_text="👤")
        self.btn_users.setObjectName("btn")

        self.btn_settings = NavButton(text="Settings", icon_text="⚙")
        self.btn_settings.setObjectName("btn")

        self.btn_logs = NavButton(text="Logs", icon_text="📝")
        self.btn_logs.setObjectName("btn")

        self.container_layout.addWidget(self.btn_users)
        self.container_layout.addWidget(self.btn_settings)
        self.container_layout.addWidget(self.btn_logs)

        self.container_layout.addStretch()

        # ================= FOOTER =================
        self.footer = QtWidgets.QFrame()
        self.footer.setObjectName("panel-footer")

        self.footer_layout = QtWidgets.QVBoxLayout()
        self.footer_layout.setContentsMargins(0, 0, 0, 0)
        self.footer_layout.setSpacing(4)
        self.footer.setLayout(self.footer_layout)

        self.user_label = QtWidgets.QLabel("Signed in as User")
        self.user_label.setObjectName("label-muted")

        self.btn_logout = NavButton(text="Logout", icon_text="⏻")
        self.btn_logout.setObjectName("btn-danger")

        self.footer_layout.addWidget(self.user_label)
        self.footer_layout.addWidget(self.btn_logout)

        self.container_layout.addWidget(self.footer)

        # ================= ADD ROOT =================
        self.addWidget(self.container)
