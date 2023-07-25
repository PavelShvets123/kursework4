import json

from classes.vacancy import Vacancy


class JSONSaver:
    filename = "../data.json"

    def read_file(self):
        """
        Функция чтения json файла
        :return: возвращает список словарей с нужными ключами из Json файла
        """
        with open(self.filename, encoding="utf-8") as file:
            data = json.load(file)
        all_vacancies = []
        for vacancy in data:
            name = vacancy['name']
            url = vacancy['url']
            salary_min = vacancy["salary_min"]
            salary_max = vacancy["salary_max"]
            experience = vacancy["experience"]
            all_vacancies.append(Vacancy(name, url, salary_min, salary_max, experience))
        return all_vacancies

    def write_file(self, data):
        """
        Создает json фаил
        :param data: Получение данных
        :return: Обрабатывает данные и собирает их json фаил
        """
        with open(self.filename, 'w', encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def sort_by_salary(self):
        """
        Сортировка данные по минимально зарплате
        :return: возвращает данные по ключу от меньшего к большему
        """
        with open(self.filename, encoding="utf-8") as file:
            data = json.load(file)
            data = [elem for elem in data if elem["salary_min"] != 0 and elem["salary_max"] != 0]
            sort_file = sorted(data, key=lambda x: x['salary_min'], reverse=False)
            return sort_file
