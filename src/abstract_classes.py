from abc import abstractmethod, ABC


class SearchVacancies(ABC):

    """Абстрактный класс, который определяет метод получения вакансий с использованием API"""
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass
