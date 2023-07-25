from abc import ABC, abstractmethod

import requests

from classes.vacancy import Vacancy


class APIInteraction(ABC):
    @abstractmethod
    def request(self, url):
        """
        Создаем метод для получения страницы со списком вакансий.
        """
        pass

    @abstractmethod
    def parse(self, data) -> list[Vacancy]:
        pass
