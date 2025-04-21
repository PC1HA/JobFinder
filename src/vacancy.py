class Vacancy:
    """Класс для работы с вакансиями"""
    __slots__ = ('title', 'url', 'salary', 'description')

    def __init__(self, title: str, url: str, salary: str, description: str) -> None:
        """Инициализирует объект Vacancy.

        Args:
            title (str): Название вакансии.
            url (str): URL на вакансию.
            salary (str): Зарплата.
            description (str): Описание вакансии.
        """
        self.title = title
        self.url = url
        self.salary = self.validate_salary(salary)
        self.description = description

    def validate_salary(self, salary: str) -> str:
        """Проверяет корректность зарплаты.

        Args:
            salary (str): Зарплата.

        Returns:
            str: Проверенная зарплата или сообщение о том, что она не указана.
        """
        return salary if salary else "Зарплата не указана"

    def __lt__(self, other: 'Vacancy') -> bool:
        """Сравнивает две вакансии по зарплате.

        Args:
            other (Vacancy): Другая вакансия для сравнения.

        Returns:
            bool: True если текущая вакансия имеет меньшую зарплату.
        """
        if self.salary == "Зарплата не указана":
            return False
        if other.salary == "Зарплата не указана":
            return True

        try:
            return int(self.salary.split()[0]) < int(other.salary.split()[0])
        except ValueError:
            return False

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта Vacancy."""
        return f"Vacancy(title={self.title}, url={self.url}, salary={self.salary}, description={self.description})"

    def to_dict(self) -> dict:
        return {
            'title': self.title,
            'salary': self.salary,
            'url': self.url,
            'description': self.description,
        }
