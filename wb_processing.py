#импортируем библиотеки
import requests as rq
from bs4 import BeautifulSoup as bs


"""Извлечение из раздела MORE FROM CGTN CHINA"""

#url страницы
url_MFCH = 'https://www.cgtn.com/china'

#User-Agents
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) '
           'Gecko/20100101 Firefox/88.0'}

# Получаем страницу
response = rq.get(url=url_MFCH, headers=headers)
response.raise_for_status()  # Убедимся, что запрос был успешным

# Создаем объект BeautifulSoup
soup_mfch = bs(response.text, 'html.parser')

inf_1_mfch = soup_mfch.find('div', {'class':'first-module-8-1 common-module'})
inf_list_mfch = inf_1_mfch.findAll('div', {'class':'cg-content-description'})
for element in inf_list_mfch:
    print (str.strip(element.find('div', {'class':'cg-title'}).find('a').text))


"""Извлечение ifeng"""

#url страницы
url_ifeng = 'https://news.ifeng.com/'

#User-Agents
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) '
           'Gecko/20100101 Firefox/88.0'}

# Получаем страницу
response = rq.get(url=url_ifeng, headers=headers)
response.raise_for_status()  # Убедимся, что запрос был успешным
response.encoding = 'utf-8' #корректное отображение китайского

# Создаем объект BeautifulSoup
soup_ifeng = bs(response.text, 'html.parser')

inf_ifeng = soup_ifeng.find('div', {'class':'index_content_RQk8t'})
inf_list_ifeng = inf_ifeng.findAll('div', {'class':'news-stream-newsStream-news-item-infor'})

news_ifeng = {}
for element in inf_list_ifeng:
    news_ifeng[f'{str.strip(element.find('a').text)}'] = f'{str.strip(element.find('div', {'class':'clearfix'}).text)}'


"""Извлечение baidu"""

#url страницы
url_baidu = 'https://news.baidu.com/'

#User-Agents
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) '
           'Gecko/20100101 Firefox/88.0'}

# Получаем страницу
response = rq.get(url=url_baidu, headers=headers)
response.raise_for_status()  # Убедимся, что запрос был успешным
response.encoding = 'utf-8'

# Создаем объект BeautifulSoup
soup_baidu = bs(response.text, 'html.parser')

inf_1_baidu = soup_baidu.find('div', {'class':'mod-tab-content'})
inf_list_baidu = inf_1_baidu.findAll('a')
for i, element in enumerate(inf_list_baidu):
    print(f'Новость № {i+1} - {element.text}')


"""most read"""

#url страницы
url_sky = 'https://news.sky.com/uk'

#User-Agents
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) '
           'Gecko/20100101 Firefox/88.0'}

# Получаем страницу
response = rq.get(url=url_sky, headers=headers)
response.raise_for_status()  # Убедимся, что запрос был успешным

# Создаем объект BeautifulSoup
soup_sky = bs(response.text, 'html.parser')

inf_1_sky = soup_sky.find('div', {'class':'site-wrap site-wrap-padding'})
inf_list_sky = inf_1_sky.findAll('li', {'class':'ui-trending-item'})
for num, element in enumerate(inf_list_sky):
    print(f'Новость № {num + 1}: {str.strip(element.find('a').text)}')