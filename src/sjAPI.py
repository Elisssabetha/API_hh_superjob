import os

import requests

from src.abstract_classes import SearchVacancies
from src.vacancy import Vacancy

api_key: str = os.getenv('SUPERJOB_API_KEY')


class SuperJobAPI(SearchVacancies):
    def __init__(self, vacancy_name: str, page=0):
        self.url = 'https://api.superjob.ru/2.0/vacancies/'
        self.vacancy_name = vacancy_name
        self.page = page

    def pars(self) -> list:

        """Осуществляет поиск по API"""

        list_dict_vacancies = []

        headers = {'X-Api-App-Id': api_key}
        params = {'keywords': self.vacancy_name, 'count': self.page}
        response = requests.get(self.url, headers=headers, params=params)
        vacancies = response.json()['objects']

        # убираем лишнюю информацию, оставляя только необходимое для Vacancy

        for vacancy_data in vacancies:
            name = vacancy_data.get('profession')
            salary_from = vacancy_data.get('payment_from')
            salary_to = vacancy_data.get('payment_to')
            experience = vacancy_data.get('experience')['title']
            description = vacancy_data.get('candidat')
            link = vacancy_data.get('link')
            vacancy_info = {'name': name,
                            'salary_from': salary_from,
                            'salary_to': salary_to,
                            'experience': experience,
                            'description': description,
                            'link': link
                            }
            list_dict_vacancies.append(vacancy_info)
        return list_dict_vacancies

    def get_vacancies(self) -> list:

        """Создает список с экземплярами класса Vacancy"""

        list_vacancies = []
        for item in self.pars():
            vacancy = Vacancy(item['name'], item['salary_from'], item['salary_to'], item['experience'],
                              item['description'], item['link'])
            list_vacancies.append(vacancy)
        return list_vacancies
