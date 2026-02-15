import sys

from app import app

from core.base import BaseWindow

window = BaseWindow()
window.ui_manager.show_layout("home")

window.show()
sys.exit(app.exec_())

