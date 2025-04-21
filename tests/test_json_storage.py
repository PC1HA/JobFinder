import os
import unittest

from src.json_storage import JSONStorage
from src.vacancy import Vacancy


class TestJSONStorage(unittest.TestCase):
    """Тесты для класса JSONStorage."""

    storage: JSONStorage  # Явная аннотация типа

    @classmethod
    def setUpClass(cls) -> None:
        """Создает экземпляр JSONStorage."""
        cls.storage = JSONStorage('data/test_vacancies.json')

    @classmethod
    def tearDownClass(cls) -> None:
        """Удаляет тестовый файл после завершения тестов."""
        try:
            os.remove('data/test_vacancies.json')
        except FileNotFoundError:
            pass

    def setUp(self) -> None:
        """Очищает файл перед каждым тестом."""
        open('data/test_vacancies.json', 'w').close()  # Открываем файл в режиме записи и сразу закрываем его

    def test_add_vacancy(self) -> None:
        """Тестирование добавления вакансии."""
        vacancy = Vacancy(title="Software Engineer", salary='100000', url="http://example.com",
                          description="Develop software.")

        self.storage.add_vacancy(vacancy)

        vacancies = self.storage.get_vacancies()

        self.assertEqual(len(vacancies), 1)
        self.assertEqual(vacancies[0]['title'], "Software Engineer")

    def test_delete_vacancy(self) -> None:
        """Тестирование удаления вакансии."""

        vacancy1 = Vacancy(title="Software Engineer", salary='100000', url="http://example.com",
                           description="Develop software.")
        vacancy2 = Vacancy(title="Data Scientist", salary='120000',
                           url="http://example.com",
                           description="Analyze data.")

        self.storage.add_vacancy(vacancy1)
        self.storage.add_vacancy(vacancy2)

        self.storage.delete_vacancy("Software Engineer")

        vacancies = self.storage.get_vacancies()

        self.assertEqual(len(vacancies), 1)
        self.assertEqual(vacancies[0]['title'], "Data Scientist")

    def test_get_vacancies_empty(self) -> None:
        """Тестирование получения вакансий из пустого файла."""

        vacancies = self.storage.get_vacancies()

        self.assertEqual(vacancies, [])
