# import time
# import os
# import urllib
# import googletrans
# import json
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup
# from urllib.request import urlretrieve
#
# # после того как сайт будет готов, попытаться через time автоматизировать скрипт
# # при попытке автоматизации обновления указать headers и прочее HEADERS очень нужно!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
#
# # функция для создания новой директории
# def new_directory(name):
#     directory = name
#     if not os.path.exists(directory):
#         os.makedirs(directory)
#
#
# # объект класса Translator
# translator = googletrans.Translator()
# # объект класса webdriver chrome
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#
# for i in range(1, 2): #10
#     # директория для фотографий на i странице
#     new_directory(f'static/images/page_{i}')
#     # директория для json файлов на i странице
#     new_directory(f'static/json/page_{i}')
#
#     # загрузка страницы со списком домов по url
#     driver.get(f'https://www.4zida.rs/prodaja-kuca/novi-sad?skuplje_od=15000eur&jeftinije_od=100000eur&strana={i}')
#     # время, чтобы страница полностью прогрузилась
#     time.sleep(1)
#     # объект класса beautifulsoup, который позволяет работать с html данными, полученными с url, указанного в driver.get
#     # lxml - синтаксический анализатор
#     soup = BeautifulSoup(driver.page_source, 'lxml')
#     # список всех элементов html-страницы с соответствующим классом
#     all_houses = soup.find_all(class_='ed-card-image-wrapper')
#     # пустой словарь для сохранения данных обо всех домах на странице
#     dict = {}
#     # переменная для определения номера дома на странице
#     house_number = 1
#
#     for each_house in all_houses:
#         # проверка на наличие у дома фотографий
#         if each_house.find(class_='photo-count ng-star-inserted'):
#             # загрузка html-страницы дома
#             driver.get(f'https://www.4zida.rs' + each_house.find('a').get('href'))
#             # время, чтобы страница полностью прогрузилась
#             time.sleep(1)
#             # объект класса beautifulsoup, который позволяет работать с html данными, полученными с url, указанного в driver.get
#             # lxml - синтаксический анализатор
#             soup = BeautifulSoup(driver.page_source, 'lxml')
#             # проверка на наличие класса, в котором содержится описание дома
#             if soup.find(class_='ed-description collapsed-description ng-star-inserted'):
#                 # директория для каждого дома с i страницы. здесь буду храниться фотографии дома
#                 new_directory(f'static/images/page_{i}/house_{house_number}_page_{i}')
#
#                 #####################################################
#                 # блок скачивания описания домов
#                 #####################################################
#
#                 # поиск тега с кратким описанием дома и получение текста из html-тега
#                 h1 = soup.find('h1').text
#                 # переведенный текст с кратким описанием дома
#                 h1_translated = translator.translate(h1, dest='ru', src='sr').text
#                 # поиск тега с полным описанием дома и получение текста из html-тега
#                 description = soup.find(class_='ed-description collapsed-description ng-star-inserted').text
#                 # переведенный текст с полным описанием дома
#                 description_translated = translator.translate(description, dest='ru', src='sr').text
#                 # добавляем в словарь пару ключ: значение, где ключ - краткое описание, значение - полное описание
#                 dict[h1_translated] = description_translated
#
#                 #####################################################
#                 # конец блока скачивания описания домов
#                 #####################################################
#
#                 #####################################################
#                 # блок скачивания фотографий
#                 #####################################################
#
#                 # поиск элемента на странице с классом, в котором содержатся фотографии дома
#                 images_carousel = driver.find_element(By.CLASS_NAME, 'carousel')
#                 # нажатие на элемент карусели, чтобы получить фото в хорошем качестве
#                 images_carousel.click()
#
#                 soup = BeautifulSoup(driver.page_source, 'lxml')
#                 # список всех элементов html-страницы с соответствующим классом
#                 images = soup.find_all(class_='gallery-image ng-star-inserted')
#                 # переменная для определения номера фото
#                 image_number = 1
#
#                 for image in images:
#
#                     try:
#                         # получение url каждой фотографии дома и сохранение ее в нужной директории
#                         save_image = urlretrieve(image.get('src'), f'static/images/page_{i}/house_{house_number}_page_{i}/img_{image_number}_house_{house_number}.jpg')
#                         image_number += 1
#                         print(f'image_{image_number}_house_{house_number}.jpg saved')
#
#                         # обработка исключений
#                     except urllib.error.HTTPError as e:
#                         print(f'{e} - img_{image_number}_house_{house_number}')
#
#                 #####################################################
#                 # конец блока скачивания фотографий
#                 #####################################################
#
#         house_number += 1
import json

# закрытие всех окон браузера и безопасное завершение сеанса webdriver
#driver.quit()
data = []
for i in range(1, 171):
    with open(f'C:/Users/drear/PycharmProjects/serbia_site_v/app/templates/static/assets/json/house_{i}.json', 'r', encoding='utf-8') as file:
        data.append(json.load(file))
print(data)
