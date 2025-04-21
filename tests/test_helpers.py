import unittest

from src.helpers import filter_vacancies, get_top_vacancies, sort_vacancies
from src.vacancy import Vacancy


class TestVacancyFunctions(unittest.TestCase):
    """Тесты для функций фильтрации и сортировки вакансий."""

    def setUp(self) -> None:
        """Настройка тестовых данных."""
        self.vacancies = [
            {'id': '1', 'name': 'Software Engineer', 'description': 'Develop software applications.',
             'salary': '100000'},
            {'id': '2', 'name': 'Data Scientist', 'description': 'Analyze data and build models.', 'salary': '120000'},
            {'id': '3', 'name': 'Product Manager', 'description': 'Manage product development.', 'salary': '110000'},
            {'id': '4', 'name': 'Junior Developer', 'description': '', 'salary': ''},
        ]
        self.vacancy_objects = [
            Vacancy(title='Software Engineer', url='http://example.com/1', salary='100000',
                    description='Develop software applications.'),
            Vacancy(title='Data Scientist', url='http://example.com/2', salary='120000',
                    description='Analyze data and build models.'),
            Vacancy(title='Product Manager', url='http://example.com/3', salary='110000',
                    description='Manage product development.'),
            Vacancy(title='Junior Developer', url='http://example.com/4', salary='', description=''),
        ]

    def test_filter_vacancies(self) -> None:
        """Тестирование фильтрации вакансий по ключевым словам."""
        keywords = ['software', 'data']
        filtered = filter_vacancies(self.vacancies, keywords)

        self.assertEqual(len(filtered), 2)
        self.assertIn(self.vacancies[0], filtered)  # Software Engineer
        self.assertIn(self.vacancies[1], filtered)  # Data Scientist

    def test_sort_vacancies(self) -> None:
        """Тестирование сортировки вакансий по зарплате."""
        sorted_vacancies = sort_vacancies(self.vacancy_objects)

        # Проверяем порядок вакансий после сортировки
        self.assertEqual(sorted_vacancies[0].salary, '100000')
        self.assertEqual(sorted_vacancies[1].salary, '110000')
        self.assertEqual(sorted_vacancies[2].salary, '120000')

    def test_get_top_vacancies(self) -> None:
        """Тестирование получения топ N вакансий."""
        top_vacancies = get_top_vacancies(self.vacancy_objects, 2)

        self.assertEqual(len(top_vacancies), 2)
        self.assertEqual(top_vacancies[0].title, 'Software Engineer')
        self.assertEqual(top_vacancies[1].title, 'Data Scientist')
