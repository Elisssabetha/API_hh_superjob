from abc import abstractmethod, ABC


class SearchVacancies(ABC):
    """Абстрактный класс, который определяет метод получения вакансий с использованием API"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass


class VacancySaver(ABC):
    """Абстрактный класс, который определяет методы добавления вакансий в файл,
     получения данных из файла по указанным критериям и удаления информации о вакансиях."""

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def select(self, **kwargs):
        pass

    @abstractmethod
    def delete(self):
        pass
