import json
import requests

from googletrans import Translator


# сохраняем json файл в формате словаря
def get_json(url):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }

    r = requests.get(url, headers=headers)
    src = r.json()
    return src


translator = Translator()

check_list = ['title', 'price', 'm2', 'roomCount', 'desc', 'structureName', 'images', 'pricePerM2']

house_number = 1

for i in range(1, 10):

    page = get_json(
        f'https://api.4zida.rs/v6/search/houses?for=sale&priceFrom=15000&priceTo=100000&page={i}&placeIds%5B%5D=600')

    for house in page['ads']:

        if 'image' in house:

            h = get_json('https://api.4zida.rs/v6/eds/' + house['id'])

            house_dic = {'href': f'ns_houses/house_with_num_{house_number}'}
            for k, v in h.items():
                if k in check_list:
                    if k in check_list[4] or k in check_list[5]:
                        house_dic[k] = translator.translate(v, dest='ru', src='sr').text
                    else:
                        house_dic[k] = v
            print(house_dic)

            with open(f'templates/static/assets/json/house_{house_number}.json', 'w', encoding='utf-8') as fp:
                json.dump(house_dic, fp)
                print(f'house_{house_number}.json saved')

            house_number += 1
