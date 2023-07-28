import yaml

class Localization:
    def __init__(self, path):
        with open(path, "r", encoding="utf-8") as file:
            self.strings = yaml.safe_load(file)

    def get(self, key):
        return self.strings.get(key, key)