from PySide6 import QtWidgets, QtGui, QtCore


class NavButton(QtWidgets.QPushButton):
    def __init__(self, text, icon_text="●"):
        super().__init__()

        self.setObjectName("btn")
        self.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.setFixedHeight(44)

        # ===== CONTENT LAYOUT =====
        self.container = QtWidgets.QHBoxLayout(self)
        self.container.setContentsMargins(12, 0, 12, 0)
        self.container.setSpacing(10)

        self.icon = QtWidgets.QLabel(icon_text)
        self.text = QtWidgets.QLabel(text)

        self.container.addWidget(self.icon)
        self.container.addWidget(self.text)
        self.container.addStretch()

        # ===== ACTIVE STATE =====
        self._active = False

        # ===== HOVER ANIMATION =====
        self._base_width = None
        self.animation = QtCore.QPropertyAnimation(self, b"minimumWidth")
        self.animation.setDuration(160)
        self.animation.setEasingCurve(QtCore.QEasingCurve.Type.OutCubic)

    # ---------- ACTIVE ----------
    def setActive(self, state: bool):
        self._active = state
        if state:
            self.setObjectName("btn-primary")
        else:
            self.setObjectName("btn")
        self.style().unpolish(self)
        self.style().polish(self)

    # ---------- HOVER ----------
    def enterEvent(self, event):
        if self._base_width is None:
            self._base_width = self.width()

        self.animation.stop()
        self.animation.setStartValue(self.minimumWidth())
        self.animation.setEndValue(self._base_width + 6)
        self.animation.start()

        super().enterEvent(event)

    def leaveEvent(self, event):
        if self._base_width is None:
            return

        self.animation.stop()
        self.animation.setStartValue(self.minimumWidth())
        self.animation.setEndValue(self._base_width)
        self.animation.start()

        super().leaveEvent(event)
