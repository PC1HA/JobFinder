import requests
from typing import List, Dict, Any
from src.base_api import BaseAPI


class HeadHunterAPI(BaseAPI):
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
            'per_page': 20,
        }
        response = requests.get(self.BASE_URL, params=params)
        return response.json().get('items', [])
