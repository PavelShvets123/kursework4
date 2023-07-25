import json

from classes.vacancy import Vacancy


class JSONSaver():
    filename = "../data.json"

    def read_file(self):
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
        with open(self.filename, 'w', encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy):
        data = self.read_file()
        data.append(vacancy.to_dict())
        self.write_file(data)

    def get_vacancies_by_salary(self, salary):
        vacancies_by_salary = []
        for vacancy in self.read_file():
            if vacancy["salary"] == salary:
                vacancies_by_salary.append(vacancy)
        return vacancies_by_salary

    def delete_vacancy(self, vacancy_):
        vacancies = []
        for vacancy in self.read_file():
            if vacancy["url"] != vacancy_.url:
                vacancies.append(vacancy)
        self.write_file(vacancies)
