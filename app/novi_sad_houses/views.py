import json
import os

from django.shortcuts import render
from random import randint


path = os.path.abspath(os.curdir)

number_of_houses = len(os.listdir(f'{path}/templates/static/assets/json'))


def main_page(request):
    data, roll = [], []
    for i in range(1, 10):
        x = randint(1, number_of_houses)
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
            print(f'house_{i}.json no house with number {i}')
    # добавляем словарь с ключами(номера страниц) и значениями(url этих страниц)
    pages_list = [n for n in range(1, number_of_houses + 1, 15)]
    pages = {k: f'/ns_houses/{pages_list[k-1]}/{pages_list[k-1]+15}' for k in range(1, len(pages_list)+1)}
    #
    return render(request=request, template_name='novi_sad_houses/page_with_houses.html', context={'data': data, 'pages': pages})


def each_house(request, qwerty):
    if 0 < qwerty <= number_of_houses:
        with open(f'{path}/templates/static/assets/json/house_{qwerty}.json', 'r', encoding='utf-8') as file:
            data = (json.load(file))
        return render(request=request, template_name=f'novi_sad_houses/each_house.html', context={'data': data})

