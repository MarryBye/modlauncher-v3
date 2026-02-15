from PySide6.QtWidgets import QWidget, QLayout, QStackedLayout


class UIManager(QStackedLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout_map = {}

    def add_layout(self, name: str, layout: QLayout):
        page = QWidget()
        page.setLayout(layout)

        self.addWidget(page)
        self.layout_map[name] = self.count() - 1
        layout.ui_manager = self

    def show_layout(self, name: str):
        self.setCurrentIndex(self.layout_map[name])
