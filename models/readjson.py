import json
import os


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
            raise FileNotFoundError(f'Файл по пути {path} не найден')
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
