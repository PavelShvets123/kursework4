from classes.hhru import HeadHunterAPI
from classes.jsonsaver import JSONSaver
from classes.superjob import SuperJobAPI


def main():
    hh_api = HeadHunterAPI()
    sj_api = SuperJobAPI()

    #    Получение вакансий с разных платформ
    # keyword = input("Введите поисковый запрос")
    keyword = "Python"
    vacancies = hh_api.request(keyword)
    sj_vacancies = sj_api.request(keyword)

    vacancies.extend(sj_vacancies)

    js = JSONSaver()
    js.write_file(vacancies)
    vacancies = js.read_file()

    while True:

        command = input(
            "1 - Вывести список вакансий;\n"
            "2 - Отсортировать по минимальной зарплате;\n"
            "3 = Фильтрация по ключевому слову;\n"
            "exit - для выхода.\n"
        )
        if command.lower() == "exit":
            break
        elif command == "1":
            for vacancy in vacancies:
                print(vacancy)
                print("-" * 100) # Для более удобного вывода по профессиям
        elif command == "2":
            vacancies = js.sort_by_salary()
            for vacancy in vacancies:
                print(vacancy)
                print("-" * 100)  # Для более удобного вывода по профессиям
        elif command == "3":
            user_input = input('Введите ключевое слово - ')
            for vacancy in vacancies:
                if user_input in vacancy["name"]:
                    print(vacancy)


if __name__ == "__main__":
    main()
