from datetime import datetime
from uuid import uuid4

import json


class JsonEngine:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.config_path = self.root_dir / "app" / "storage" / "config.json"

    def create_default_json(self):
        try:
            with open(self.config_path, 'w+', encoding="utf-8-sig") as new_file:
                json.dump(
                    {
                        "read_write": False,
                    },
                    new_file,
                    indent = 2
                )

        except Exception as e:
            print(f"Unknown Exception Creating Config File: {e}")
        
    def create_user_profile(self, new_user: dict) -> dict:
        if not new_user:
            return False
        
        try:
            with open(self.config_path, 'w', encoding="utf-8-sig") as new:
                json.dump(new_user, new, indent=2)

            return new_user

        except FileNotFoundError:
            self.create_default_json()
            self.create_user_profile()

        except Exception as e:
            print(f"Unknown Exception Creating User Profile: {e}")
            return None
        
    def get_user_profile(self) -> dict:
        try:
            with open(self.config_path, 'r', encoding="utf-8-sig") as f:
                data = json.load(f)

            return data
        
        except FileNotFoundError:
            self.create_default_json()
            self.get_user_profile()

        except Exception as e:
            print(f"Unknown Exception Getting User Profile: {e}")
            return None