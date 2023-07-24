import requests


import json


def getPage(page=0):

    params = {
        'text': 'NAME:python',
        'area': 1,
        'page': page,
        'per_page': 1
    }

    req = requests.get('https://api.hh.ru/vacancies', params)
    data = req.content.decode()
    req.close()
    return data

print(getPage())