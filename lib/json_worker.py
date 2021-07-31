import json
from os import path


class Json_worker:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self._validate_filename()

    def update_json(self, key: str, data: dict) -> None:
        try:
            with open(path.join('orders', self.filename), 'r', encoding='utf-8') as json_file:
                py_dict = json.load(json_file)
        except FileNotFoundError:
            self.create_json_file()
            py_dict = {}

        py_dict[key] = data

        with open(path.join('orders', self.filename), 'w', encoding='utf-8') as updated_json_file:
            json.dump(py_dict, updated_json_file, indent=4, ensure_ascii=False)

    def create_json_file(self) -> None:
        with open(path.join('orders', self.filename), 'w', encoding='utf-8') as new_json_file:
            json.dump({}, new_json_file, ensure_ascii=False)

    def _validate_filename(self) -> None:
        if not self.filename.endswith('.json'):
            self.filename += '.json'
