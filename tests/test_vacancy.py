import unittest

from src.vacancy import Vacancy


class TestVacancy(unittest.TestCase):
    """Тесты для класса Vacancy."""

    def test_initialization(self) -> None:
        """Тестирование инициализации объекта Vacancy."""
        vacancy = Vacancy(title="Software Engineer", url="http://example.com", salary="100000",
                          description="Develop software.")

        self.assertEqual(vacancy.title, "Software Engineer")
        self.assertEqual(vacancy.url, "http://example.com")
        self.assertEqual(vacancy.salary, "100000")
        self.assertEqual(vacancy.description, "Develop software.")

    def test_validate_salary_with_value(self) -> None:
        """Тестирование проверки зарплаты с указанным значением."""
        vacancy = Vacancy(title="Data Scientist", url="http://example.com", salary="120000",
                          description="Analyze data.")

        self.assertEqual(vacancy.salary, "120000")

    def test_validate_salary_without_value(self) -> None:
        """Тестирование проверки зарплаты без указанного значения."""
        vacancy = Vacancy(title="Product Manager", url="http://example.com", salary="", description="Manage products.")

        self.assertEqual(vacancy.salary, "Зарплата не указана")

    def test_comparison_less_than(self) -> None:
        """Тестирование сравнения вакансий по зарплате (меньше)."""
        vacancy1 = Vacancy(title="Junior Developer", url="http://example.com/junior", salary="80000",
                           description="Entry level developer.")
        vacancy2 = Vacancy(title="Senior Developer", url="http://example.com/senior", salary="120000",
                           description="Experienced developer.")

        self.assertTrue(vacancy1 < vacancy2)
        self.assertFalse(vacancy2 < vacancy1)

    def test_repr(self) -> None:
        """Тестирование строкового представления объекта Vacancy."""
        vacancy = Vacancy(title="Software Engineer", url="http://example.com", salary="100000",
                          description="Develop software.")

        expected_repr = ("Vacancy(title=Software Engineer,"
                         " url=http://example.com,"
                         " salary=100000,"
                         " description=Develop software.)")
        self.assertEqual(repr(vacancy), expected_repr)
