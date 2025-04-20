import unittest
from src.base_api import BaseAPI
from typing import List, Dict, Any


class MockAPI(BaseAPI):
    """Мок-класс для тестирования BaseAPI."""

    def connect(self) -> None:
        """Имитация подключения к API."""
        self.connected = True

    def get_vacancies(self, search_query: str) -> List[Dict[str, Any]]:
        """Имитация получения вакансий по запросу."""
        return [
            {'id': '1', 'title': 'Software Engineer', 'description': 'Develop software applications.'},
            {'id': '2', 'title': 'Data Scientist', 'description': 'Analyze data and build models.'}
        ] if search_query else []


class TestBaseAPI(unittest.TestCase):
    """Тесты для абстрактного класса BaseAPI и его реализации MockAPI."""

    def setUp(self) -> None:
        """Настройка тестовых данных."""
        self.api = MockAPI()
        self.api.connect()

    def test_connect(self) -> None:
        """Тестирование метода подключения к API."""
        self.assertTrue(hasattr(self.api, 'connected'))
        self.assertTrue(self.api.connected)

    def test_get_vacancies_with_query(self) -> None:
        """Тестирование получения вакансий с запросом."""
        vacancies = self.api.get_vacancies('developer')

        self.assertEqual(len(vacancies), 2)
        self.assertEqual(vacancies[0]['title'], 'Software Engineer')
        self.assertEqual(vacancies[1]['title'], 'Data Scientist')

    def test_get_vacancies_without_query(self) -> None:
        """Тестирование получения вакансий без запроса."""
        vacancies = self.api.get_vacancies('')

        self.assertEqual(len(vacancies), 0)
