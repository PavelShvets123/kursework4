from classes.abstract import APIInteraction
from classes.vacancy import Vacancy
import requests
import os


print(os.getenv("superjob_API_KEY"))
class SuperJobAPI(APIInteraction):

    def request(self, name):
        params = {
            'keyword': {name},
            'area': 1,
            'page': 0,
            'count': 1
        }
        url = 'https://api.superjob.ru/2.0/vacancies/'
        headers = {'X-Api-App-Id': os.getenv("superjob_API_KEY")}
        req = requests.get(url, params=params, headers=headers)
        data = req.json()
        return data

    def parse(self, data) -> list[dict]:
        vacancy_list = []
        for vacancy in data['objects']:
            name = vacancy['name']
            url = vacancy['link']
            salary_min = vacancy["payment_from"]
            salary_max = vacancy["payment_to"]
            experience = vacancy["candidat"]
            vacancy_list.append({
                "name": {name},
                "url": {url},
                "salary_min": {salary_min},
                "salary_max": {salary_max},
                "experience": {experience},
            })
            return vacancy_list

sj = SuperJobAPI()
print(sj.request('python'))