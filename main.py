from PySide6.QtWidgets import QApplication
from pathlib import Path

from app.app import Skyloom

import sys


def run():
    app = QApplication(sys.argv)

    root_dir = Path(__file__).parent

    window = Skyloom(root_dir)
    window.setWindowTitle("Skyloom")
    window.setMinimumWidth(800)
    window.setMinimumHeight(600)
    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    run()