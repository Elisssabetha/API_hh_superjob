import requests

from src.abstract_classes import SearchVacancies
from src.vacancy import Vacancy


class HeadHunterAPI(SearchVacancies):

    def __init__(self, vacancy_name: str, page=0):
        self.url = 'https://api.hh.ru/vacancies'
        self.vacancy_name = vacancy_name
        self.page = page

    def pars(self) -> list:

        """Осуществляет поиск по API"""

        list_dict_vacancies = []

        params = {
            'text': self.vacancy_name,  # Текст фильтра. Что должно быть в названии вакансии
            'area': 113,  # Поиск по России
            'page': self.page,
        }
        response = requests.get(self.url, params=params)
        vacancies = response.json()['items']

        for vacancy_data in vacancies:
            name = vacancy_data.get('name')

            salary = vacancy_data.get('salary')
            if salary is None:
                salary_from = 0
                salary_to = 0
            else:
                salary_from = salary.get('from')
                if salary_from is None:
                    salary_from = 0
                salary_to = salary.get('to')
                if salary_to is None:
                    salary_to = 0
            experience = vacancy_data.get('experience')['name']
            description = vacancy_data.get('snippet')['requirement']
            alternative_url = vacancy_data.get('alternate_url')

            vacancy_info = {'name': name,
                            'salary_from': salary_from,
                            'salary_to': salary_to,
                            'experience': experience,
                            'description': description,
                            'alternative_url': alternative_url
                            }

            list_dict_vacancies.append(vacancy_info)
        return list_dict_vacancies

    def get_vacancies(self) -> list:

        """Создает список с экземплярами класса Vacancy"""

        list_vacancies = []
        for item in self.pars():
            vacancy = Vacancy(item['name'], item['salary_from'], item['salary_to'], item['experience'],
                              item['description'], item['alternative_url'])
            list_vacancies.append(vacancy)
        return list_vacancies
