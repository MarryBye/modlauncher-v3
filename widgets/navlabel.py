from PySide6 import QtWidgets

class NavSectionLabel(QtWidgets.QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.setObjectName("label-header")
        self.setContentsMargins(6, 8, 0, 2)
