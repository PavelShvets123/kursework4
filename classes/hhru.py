import requests

from classes.abstract import APIInteraction


class HeadHunterAPI(APIInteraction):
    def request(self, name):
        """
        Получение данных с сайта hh.ru
        :param name: Название данных для парсинга
        :return:  возвращает готовые данные для обработки
        """

        params = {
            'text': name,
            'archive': False,
            'page': 0,
            'per_page': 10
        }
        get_data = requests.get('https://api.hh.ru/vacancies', params)
        data = get_data.json()

        return self.parse(data)

    def parse(self, data) -> list[dict]:
        """
        Парсинг сайта
        :param data: Название данных для парсинга
        :return: возвращает нужные данные по ключам
        """
        vacancy_list = []
        for vacancy in data['items']:
            name = vacancy['name']
            url = vacancy['alternate_url']
            salary_min = 0
            salary_max = 0
            if "salary" in vacancy and vacancy["salary"]:
                salary_min = vacancy["salary"]["from"] if vacancy["salary"]["from"] else 0
                salary_max = vacancy["salary"]["to"] if vacancy["salary"]["to"] else 0
            experience = vacancy["snippet"]["requirement"]
            vacancy_list.append({
                "name": name,
                "url": url,
                "salary_min": salary_min,
                "salary_max": salary_max,
                "experience": experience,
            })
        return vacancy_list
