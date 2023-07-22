import params as params
import requests

from abstract import APIInteraction

from vacancy import Vacancy


class Headhunter(APIInteraction):
    def request(self, name, page=0):

        # params = {
        #     'text': f'NAME:{name}',  # Текст фильтра. В имени должно быть слово "Аналитик"
        #     'area': 1,  # Поиск осуществляется по вакансиям города Москва
        #     'page': page,  # Индекс страницы поиска на HH
        #     'per_page': 100  # Кол-во вакансий на 1 странице
        # }
        get_data = requests.get('https://api.hh.ru/vacancies')  # Посылаем запрос к API # добавить params
        data = get_data.json()  # Декодируем его ответ, чтобы Кириллица отображалась корректно

        return self.parse(data)

    def parse(self, data) -> list[Vacancy]:  # Почему пайчарм мне предложил такую формулеровку?
        vacancy_list = []
        for vacancy in data['items']:
            name = vacancy['name']
            url = vacancy['alternate_url']
            if "salary" in vacancy and vacancy["salary"]:
                salary = f' от {vacancy["salary"]["from"]} до {vacancy["salary"]["to"]}'
            else:
                salary = f'Заработная плата не указана'
            experience = vacancy["snippet"]["requirement"]
            vacancy_list.append(Vacancy(name, url, salary, experience))
            return vacancy_list


client = Headhunter()
print(client.request("python"))
