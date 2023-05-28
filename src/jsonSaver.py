import json
import os

from src.abstract_classes import VacancySaver
from src.vacancy import Vacancy


class FileManagerMixin:
    @staticmethod
    def connect(filename) -> None:
        if not os.path.exists(os.path.dirname(filename)):
            os.mkdir(os.path.dirname(filename))

        if not os.path.exists(filename):
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(json.dumps([]))

    @staticmethod
    def _open_file(filename) -> list:

        """Метод возвращет список со словарями, хранящимися в файле"""

        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)


class JSONSaver(FileManagerMixin, VacancySaver):

    """Класс, методы которого реализуют добавление вакансий в файл JSON и работу с записанными данными"""

    def __init__(self, file_path):
        self.data_file = file_path

    def add_vacancy(self, data:dict) -> None:

        """Метод добавления вакансии"""

        file_data = self._open_file(self.data_file)
        file_data.append(data)

        with open(self.data_file, 'w', encoding='utf=8') as file:
            json.dump(file_data, file, indent=4, ensure_ascii=False)

    def select(self, query: str = None) -> list:

        """Метод выбора информации по доп критерию"""

        file_data = self._open_file(self.data_file)

        if not query:
            return file_data

        result = []

        for item in file_data:
            if query in item.values():
                result.append(item)

        filtered_list =[]
        for item in result:
            name = item['_Vacancy__name']
            salary_from = item['_Vacancy__salary_from']
            salary_to = item['_Vacancy__salary_to']
            experience = item['_Vacancy__experience']
            description = item['_Vacancy__description']
            link = item['_Vacancy__link']
            vacancy = Vacancy(name, salary_from, salary_to, experience, description, link)
            filtered_list.append(vacancy)
        return filtered_list

    def delete(self) -> None:

        """Метод удаления вакансий из файла"""
        file_data = self._open_file(self.data_file)

        result = []
        for item in file_data:
            if item['salary'] != 0:
                result.append(item)

        # for item in file_data:
        #     if not all(item.get(key) == value for key, value in query.items()):
        #         result.append(item)
        with open(self.data_file, 'w', encoding='utf-8') as file:
            json.dump(result, file, indent=4, ensure_ascii=False)

    def clear_data(self) -> None:
        """Очистка всего файла"""
        with open(self.data_file, 'w', encoding='utf-8') as file:
            file.write(json.dumps([]))