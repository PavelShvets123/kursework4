from classes.hhru import HeadHunterAPI
from classes.jsonsaver import JSONSaver
from classes.superjob import SuperJobAPI

hh_api = HeadHunterAPI()
sj_api = SuperJobAPI()

# Получение вакансий с разных платформ
#keyword = input("Введите поисковый запрос")
vacancies = hh_api.request("Python")
sj_vacancies = sj_api.request("Python")
vacancies.extend(sj_vacancies)

js = JSONSaver()
js.write_file(vacancies)
all_vacancies = js.read_file()
for vacancies in all_vacancies:
    print(vacancies)
    print("-" * 100)




