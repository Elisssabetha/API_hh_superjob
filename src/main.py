from src.hhAPI import HeadHunterAPI
from src.jsonSaver import JSONSaver
from src.sjAPI import SuperJobAPI
from src.utils import sorting, get_top


def main():
    # проверяем наличие файла для записи (создаем)
    vacancy_connector = JSONSaver('parsed_data/vacancies.json')
    vacancy_connector.connect('parsed_data/vacancies.json')
    vacancy_connector.clear_data()  # очищаем

    # платформы для выбора, где искать инфу
    platforms = ["HeadHunter", "SuperJob"]
    platforms_lower = [item.lower() for item in platforms]

    platform_choice = input('Выберите платформу для поиска: HeadHunter или SuperJob\n').lower()

    if platform_choice not in platforms_lower:
        print('Некорректный ввод')
    else:
        name_vacancy = input('Введите название вакансии для поиска\n')

        if platform_choice == 'headhunter':
            api = HeadHunterAPI(name_vacancy)
        else:
            api = SuperJobAPI(name_vacancy)

        # список экземпляров класса Vacancy
        vacancies = api.get_vacancies()

        # запись полученных вакансий в файл
        for vacancy in vacancies:
            vacancy_connector.add_vacancy(vacancy.__dict__)

        while True:
            is_for_delete = input('Исключить ли вакансии без зарплаты - y/n:\n').lower()
            if is_for_delete not in ('n', 'y'):
                print('Некорректный ввод')
                continue
            elif is_for_delete == 'y':
                vacancy_connector.delete()

            is_query = input('Нужно ли фильтровать по опыту - y/n: \n').lower()
            if is_query not in ('n', 'y'):
                print('Некорректный ввод')
                continue

            elif is_query == 'y':
                if platform_choice == 'headhunter':
                    print("""Возможные варианты фильтрации:
                 - Нет опыта,
                 - От 1 года до 3 лет,
                 - От 3 до 6 лет,
                 - Более 6 лет""")
                else:
                    print("""Возможные варианты фильтрации:
                 - Без опыта,
                 - От 1 года,
                 - От 3 лет,
                 - От 6 лет""")
                query = input('Введите фильтр: \n')
                selected_vacancies = vacancy_connector.select(query)
                vacancies = selected_vacancies

            command = input('Введите команду sort или top:\n').lower()

            if command == 'sort':
                sorted_vacations = sorting(vacancies)
                for vacancy in sorted_vacations:
                    print(vacancy)

            elif command == 'top':
                try:
                    top_n = int(input('Сколько вакансий необходимо вывести: \n'))
                except ValueError:
                    print('Некорректный ввод')
                else:
                    top_vacancies = get_top(vacancies, top_n)
                    for vacancy in top_vacancies:
                        print(vacancy)
            else:
                print('Некорректный ввод')

            continue_running = input('Хотите продолжить работу - y/n: \n').lower()
            if continue_running == 'n':
                break


if __name__ == '__main__':
    main()
