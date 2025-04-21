import unittest
from unittest.mock import Mock, patch
from typing import Dict, Any, List

from src.hh_api import HeadHunterAPI


class TestHeadHunterAPI(unittest.TestCase):
    """Тесты для класса HeadHunterAPI."""

    @patch('src.hh_api.requests.get')
    def test_connect_success(self, mock_get: Mock) -> None:
        """Тестирование успешного подключения к API."""
        mock_get.return_value.status_code = 200

        api = HeadHunterAPI()
        try:
            api.connect()  # Проверяем, что метод не вызывает исключений
        except Exception:
            self.fail("connect() raised Exception unexpectedly!")

    @patch('src.hh_api.requests.get')
    def test_connect_failure(self, mock_get: Mock) -> None:
        """Тестирование неудачного подключения к API."""
        mock_get.return_value.status_code = 404

        api = HeadHunterAPI()
        with self.assertRaises(Exception) as context:
            api.connect()

        self.assertEqual(str(context.exception), "Failed to connect to API")

    @patch('src.hh_api.requests.get')
    def test_get_vacancies_success(self, mock_get: Mock) -> None:
        """Тестирование успешного получения вакансий."""
        mock_response: Dict[str, Any] = {  # Явная аннотация типа
            'items': [
                {'id': '1', 'name': 'Software Engineer'},
                {'id': '2', 'name': 'Data Scientist'}
            ]
        }
        mock_get.return_value.json.return_value = mock_response
        mock_get.return_value.status_code = 200

        api = HeadHunterAPI()
        vacancies = api.get_vacancies("developer")

        self.assertEqual(len(vacancies), 2)
        self.assertEqual(vacancies[0]['name'], 'Software Engineer')

    @patch('src.hh_api.requests.get')
    def test_get_vacancies_no_results(self, mock_get: Mock) -> None:
        """Тестирование получения вакансий при отсутствии результатов."""
        mock_response: Dict[str, Any] = {  # Явная аннотация типа
            'items': []
        }
        mock_get.return_value.json.return_value = mock_response
        mock_get.return_value.status_code = 200

        api = HeadHunterAPI()
        vacancies = api.get_vacancies("nonexistent_job")

        self.assertEqual(len(vacancies), 0)
