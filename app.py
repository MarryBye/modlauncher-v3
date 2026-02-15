import sys
import os

from PySide6.QtWidgets import QApplication

app = QApplication(sys.argv)

print("Loading styles...")

for stylesheet in os.listdir("./styles"):
    print("Loading " + stylesheet)
    with open(os.path.join("./styles", stylesheet)) as f:
        app.setStyleSheet(f.read())
        print("Successfully loaded " + stylesheet)

