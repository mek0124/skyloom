from PySide6.QtWidgets import QApplication
from pathlib import Path

from app.database.db import get_base, get_db, get_engine

import sys


def run_setup():
    pass


def run_app():
    pass


def main():
    app = QApplication(sys.argv)

    root_dir = Path(__file__).parent
    storage_dir = root_dir / "app" / "storage"
    storage_dir.mkdir(parents=True, exist_ok=True)

    get_base().metadata.create_all(bind=get_engine())

    db = next(get_db())

    any_existing_users = db


if __name__ == "__main__":
    main()
