from src.hh_api import HeadHunterAPI
from src.vacancy import Vacancy
from src.json_storage import JSONStorage
from src.helpers import sort_vacancies, get_top_vacancies


def user_interaction() -> None:
    """Основная функция взаимодействия с пользователем."""

    hh_api = HeadHunterAPI()

    search_query = input("Введите поисковый запрос: ")

    # Получение вакансий с hh.ru в формате JSON и преобразование в объекты Vacancy.
    vacancies_data = hh_api.get_vacancies(search_query)

    vacancies_list = [
        Vacancy(
            v['name'],
            v['alternate_url'],
            v.get('salary', {}).get('from', 0),
            v['snippet']['requirement']
        ) for v in vacancies_data
    ]

    # Сохранение вакансий в файл.
    json_saver = JSONStorage('data/test_vacancies.json')  # Укажите имя файла для сохранения

    for vacancy in vacancies_list:
        json_saver.add_vacancy(vacancy)

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))

    sorted_vacancies = sort_vacancies(vacancies_list)

    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    print("Топ вакансий:")
    for vacancy in top_vacancies:
        print(vacancy)


if __name__ == "__main__":
    user_interaction()
