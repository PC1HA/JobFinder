import json
import os
from typing import List, Dict

from src.vacancy import Vacancy


class JSONStorage:
    """Класс для работы с JSON-файлом"""

    def __init__(self, filename: str = 'data/vacancies.json') -> None:
        """Инициализирует хранилище JSON.

        Args:
            filename (str): Имя файла для хранения вакансий.
        """
        self._filename = filename
        # Создаем папку data, если она не существует
        os.makedirs(os.path.dirname(self._filename), exist_ok=True)

    def add_vacancy(self, vacancy: 'Vacancy') -> None:
        """Добавляет вакансию в файл.

        Args:
            vacancy (Vacancy): Вакансия для добавления.
        """
        with open(self._filename, 'a') as f:
            json.dump(vacancy.__dict__, f)
            f.write('\n')

    def get_vacancies(self) -> List[Dict]:
        """Получает все вакансии из файла.

        Returns:
            List[Dict]: Список вакансий в формате словарей.
        """
        if not os.path.exists(self._filename):
            return []

        with open(self._filename) as f:
            return [json.loads(line) for line in f]

    def delete_vacancy(self, vacancy_title: str) -> None:
        """Удаляет вакансию по названию из файла.

        Args:
            vacancy_title (str): Название вакансии для удаления.
        """
        vacancies = self.get_vacancies()
        vacancies = [v for v in vacancies if v['title'] != vacancy_title]

        with open(self._filename, 'w') as f:
            for v in vacancies:
                json.dump(v, f)
                f.write('\n')
