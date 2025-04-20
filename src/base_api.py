from abc import ABC, abstractmethod
from typing import List, Dict, Any


class BaseAPI(ABC):
    @abstractmethod
    def connect(self) -> None:
        """Подключается к API."""
        pass

    @abstractmethod
    def get_vacancies(self, search_query: str) -> List[Dict[str, Any]]:
        """Получает список вакансий по заданному запросу.

        Args:
            search_query (str): Запрос для поиска вакансий.

        Returns:
            List[Dict[str, Any]]: Список вакансий в формате словарей.
        """
        pass
