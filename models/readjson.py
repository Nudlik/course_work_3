import os
import json


class ReadJson:
    """
    Класс для работы с json
    """

    @staticmethod
    def load_json(path):
        """
        Загрузка json
        :param path: путь до файла
        :return: json.load()
        """
        if not os.path.exists(path):
            return None
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
