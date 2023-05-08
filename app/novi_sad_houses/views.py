import json
import os

from django.shortcuts import render
from random import randint


path = os.path.abspath(os.curdir)


def main_page(request):
    data, roll = [], []
    for i in range(1, 10):
        x = randint(1, 177)
        if x not in roll:
            roll.append(x)
            with open(f'{path}/templates/static/assets/json/house_{x}.json', 'r', encoding='utf-8') as file:
                data.append(json.load(file))
    print(roll)
    return render(request=request, template_name='main.html', context={'data': data})


def page_numb(request, page_n_s, page_n_e):
    data = []
    for i in range(page_n_s, page_n_e):
        try:
            with open(f'{path}/templates/static/assets/json/house_{i}.json', 'r', encoding='utf-8') as file:
                data.append(json.load(file))
        except FileNotFoundError:
            print(f'house_{i}.json no house with number i')
    return render(request=request, template_name='novi_sad_houses/page_with_houses.html', context={'data': data})


def each_house(request, qwerty):
    if 0 < qwerty < 178:
        with open(f'{path}/templates/static/assets/json/house_{qwerty}.json', 'r', encoding='utf-8') as file:
            data = (json.load(file))
        return render(request=request, template_name=f'novi_sad_houses/each_house.html', context={'data': data})

