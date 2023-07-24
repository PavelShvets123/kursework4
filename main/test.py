import requests

params = {
            'text': f'NAME:программист',
            'area': 1,
            'page': 0,
            'per_page': 10
        }
get_data = requests.get('https://api.hh.ru/vacancies', params)
print(get_data.json())