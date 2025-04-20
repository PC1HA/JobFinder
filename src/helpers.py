from typing import List, Dict

from src.vacancy import Vacancy


def filter_vacancies(vacancies: List[Dict], keywords: List[str]) -> List[Dict]:
    """Фильтрует вакансии по ключевым словам в описании.

    Args:
       vacancies (List[Dict]): Список вакансий.
       keywords (List[str]): Список ключевых слов для фильтрации.

    Returns:
       List[Dict]: Отфильтрованный список вакансий.
    """
    return [v for v in vacancies if any(keyword.lower() in v['description'].lower() for keyword in keywords)]

def sort_vacancies(vacancies: List['Vacancy']) -> List['Vacancy']:
    """Сортирует список вакансий по зарплате.

    Args:
       vacancies (List[Vacancy]): Список вакансий.

    Returns:
       List[Vacancy]: Отсортированный список вакансий.
    """
    return sorted(vacancies)

def get_top_vacancies(vacancies: List['Vacancy'], n: int) -> List['Vacancy']:
    """Получает топ N вакансий из списка.

    Args:
       vacancies (List[Vacancy]): Список вакансий.
       n (int): Количество топовых вакансий для получения.

    Returns:
       List[Vacancy]: Топ N вакансий.
   """
    return vacancies[:n]