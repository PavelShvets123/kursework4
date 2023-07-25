import requests

from classes.abstract import APIInteraction

from classes.vacancy import Vacancy


class HeadHunterAPI(APIInteraction):
    def request(self, name):

        params = {
            'text': f'NAME:{name}',
            'area': 1,
            'page': 0,
            'per_page': 100
        }
        get_data = requests.get('https://api.hh.ru/vacancies', params)
        data = get_data.json()

        return self.parse(data)

    def parse(self, data) -> list[dict]:
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
                "name": {name},
                "url": {url},
                "salary_min": {salary_min},
                "salary_max": {salary_max},
                "experience": {experience},
            })
            return vacancy_list
