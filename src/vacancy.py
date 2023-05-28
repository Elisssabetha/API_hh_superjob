from statistics import mean


class Vacancy:
    """Класс для сохранения инфо о вакансии"""

    def __init__(self, name: str, salary_from: int, salary_to: int, experience: str, description: str, link:str):
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.experience = experience
        self.description = description
        self.__link = link

        if self.salary_from == 0 and self.salary_to != 0:
            self.salary = self.salary_to
        elif self.salary_to == 0 and self.salary_from != 0:
            self.salary = self.salary_from
        else:
            self.salary = mean((self.salary_from, self.salary_to))

    def __str__(self):
        return f"""Вакансия: {self.name}.
Зарплата {self.salary} руб/мес
Требуемый опыт: {self.experience}.
Ссылка на вакансию: {self.link}
"""

    def __gt__(self, other):
        return self.salary > other.salary

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value

    @property
    def salary_from(self):
        return self.__salary_from

    @salary_from.setter
    def salary_from(self, value):
        if isinstance(value, int):
            self.__salary_from = value

    @property
    def salary_to(self):
        return self.__salary_to

    @salary_to.setter
    def salary_to(self, value):
        if isinstance(value, int):
            self.__salary_to = value

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, value):
        if isinstance(value, str):
            self.__experience = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        if isinstance(value, str):
            self.__description = value

    @property
    def link(self):
        return self.__link

    @link.setter
    def link(self, value):
        if isinstance(value, str):
            self.__link = value