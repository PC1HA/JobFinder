import unittest
import os

from src.vacancy import Vacancy
from src.json_storage import JSONStorage


class TestJSONStorage(unittest.TestCase):
    """Тесты для класса JSONStorage."""

    @classmethod
    def setUpClass(cls):
        """Создает экземпляр JSONStorage и очищает файл перед тестами."""
        cls.storage = JSONStorage('data/test_vacancies.json')

    @classmethod
    def tearDownClass(cls):
        """Удаляет тестовый файл после завершения тестов."""
        try:
            os.remove('data/test_vacancies.json')
        except FileNotFoundError:
            pass

    def test_add_vacancy(self):
        """Тестирование добавления вакансии."""
        vacancy = Vacancy(title="Software Engineer", salary=100000)

        self.storage.add_vacancy(vacancy)

        vacancies = self.storage.get_vacancies()

        self.assertEqual(len(vacancies), 1)
        self.assertEqual(vacancies[0]['title'], "Software Engineer")

    def test_get_vacancies_empty(self):
        """Тестирование получения вакансий из пустого файла."""

        vacancies = self.storage.get_vacancies()

        self.assertEqual(vacancies, [])

    def test_delete_vacancy(self):
        """Тестирование удаления вакансии."""

        vacancy1 = Vacancy(title="Software Engineer", salary=100000)
        vacancy2 = Vacancy(title="Data Scientist", salary=120000)

        self.storage.add_vacancy(vacancy1)
        self.storage.add_vacancy(vacancy2)

        self.storage.delete_vacancy("Software Engineer")

        vacancies = self.storage.get_vacancies()

        self.assertEqual(len(vacancies), 1)
        self.assertEqual(vacancies[0]['title'], "Data Scientist")
