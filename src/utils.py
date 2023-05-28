def sorting(vacancies: list) -> list:

    """Сортирует вакансии по зп от меньшего к большему"""

    return sorted(vacancies)


def get_top(vacancies: list, top_n: int) -> list:

    """Выводит заданное число вакансий с максимальной зп"""

    return sorted(vacancies, reverse=True)[:top_n]
