from classes.abstract import APIInteraction

import requests

import os


class SuperJobAPI(APIInteraction):

    def request(self, name):
        """
        Получение данных с сайта sj.ru с помощью API ключа
        :param name: Название данных для парсинга
        :return:  возвращает готовые данные для обработки
        """
        params = {
            'keyword': name,
            'archive': False,
            'page': 0,
            'count': 10
        }
        url = 'https://api.superjob.ru/2.0/vacancies/'
        headers = {'X-Api-App-Id': os.getenv("superjob_API_KEY")}
        req = requests.get(url, params=params, headers=headers)
        data = req.json()
        return self.parse(data)

    def parse(self, data) -> list[dict]:
        """
        Парсинг сайта
        :param data: Название данных для парсинга
        :return: возвращает нужные данные по ключам
        """
        vacancy_list = []
        for vacancy in data['objects']:
            name = vacancy['profession']
            url = vacancy['link']
            salary_min = vacancy["payment_from"]
            salary_max = vacancy["payment_to"]
            experience = vacancy["candidat"]
            vacancy_list.append({
                "name": name,
                "url": url,
                "salary_min": salary_min,
                "salary_max": salary_max,
                "experience": experience,
            })
        return vacancy_list
