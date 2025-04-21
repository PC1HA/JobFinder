from typing import Any, Dict, List

import requests

from src.base_api import BaseAPI


class HeadHunterAPI(BaseAPI):
    """Реализация API для hh.ru"""
    BASE_URL = "https://api.hh.ru/vacancies"

    def connect(self) -> None:
        """Подключается к API и проверяет доступность."""
        response = requests.get(self.BASE_URL)
        if response.status_code != 200:
            raise Exception("Failed to connect to API")

    def get_vacancies(self, search_query: str) -> List[Dict[str, Any]]:
        """Получает вакансии с hh.ru по заданному запросу.

        Args:
            search_query (str): Запрос для поиска вакансий.

        Returns:
            List[Dict[str, Any]]: Список вакансий в формате словарей.
        """
        self.connect()
        params = {
            'text': search_query,
            'per_page': str(20),
        }

        response = requests.get(self.BASE_URL, params=params)

        items = response.json().get('items', [])

        return [item for item in items if isinstance(item, dict)]
