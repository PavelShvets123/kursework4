from abc import ABC, abstractmethod

from classes.vacancy import Vacancy


class APIInteraction(ABC):
    @abstractmethod
    def request(self, url):
        pass

    @abstractmethod
    def parse(self, data) -> list[Vacancy]:
        pass
