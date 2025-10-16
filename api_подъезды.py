#импортируем библиотеки
import pandas_datareader as pdr
import requests as rq
import wbpy
import wbdata
import pandas as pd

#API fred (Сент-Луис, США)
# загрузить данные по ВВП США (GDP) и уровень инфляции (CPIAUCSL)
# Указываем период времени для загрузки данных
start = '2000-01-01'
end = '2023-01-01'

# Загружаем данные ВВП (GDP) и CPI (CPIAUCSL) из FRED
gdp = pdr.get_data_fred('GDP', start=start, end=end)
cpi = pdr.get_data_fred('CPIAUCSL', start=start, end=end)

# Посмотрим на данные GDP
print(gdp.head())
# Посмотрим и данные по CPI
print(cpi.head())

# Загрузка нескольких рядов одновременно
start = '2000-01-01'
end = '2023-01-01'

# Использование списка для загрузки нескольких данных одновременно
series = ['UNRATE', 'FEDFUNDS']  # UNRATE is the unemployment rate, FEDFUNDS is the effective federal funds rate
data = pdr.get_data_fred(series, start=start, end=end)
print(data.head())

#Alpha Vantage 
my_api_key = ''

# Эндпоинт для временного ряда
url = 'https://www.alphavantage.co/query'

#ежедневные цены акций
# Параметры запроса для ежедневного временного ряда
params = {'function': 'TIME_SERIES_DAILY',
          'symbol': 'AAPL',
          'apikey': my_api_key,
          'outputsize': 'compact'}  #'full' для большего количества данных

response = rq.get(url, params=params)

# Проверяем успешный ли запрос (код ответа 200)
if response.status_code == 200:
    # Конвертируем результат из JSON и обрабатываем данные
    daily_data = response.json()
    print(daily_data)
else:
    print(f"Ошибка запроса, код ответа {response.status_code}")

# 2. Валютные курсы (Forex)
# Пример запроса реального обменного курса:

# Параметры для обменного курса валюты
params = {'function': 'CURRENCY_EXCHANGE_RATE',
          'from_currency': 'USD',
          'to_currency': 'EUR',
          'apikey': my_api_key}

response = rq.get(url, params=params)

if response.status_code == 200:
    forex_data = response.json()
    print(forex_data)
else:
    print(f"Ошибка запроса, код ответа {response.status_code}")

# 3. Криптовалюты
# Пример запроса информации о криптовалюте:

# Параметры для данных криптовалюты
params = {'function': 'DIGITAL_CURRENCY_DAILY',
          'symbol': 'BTC',
          'market': 'USD',
          'apikey': my_api_key}

response = rq.get(url, params=params)

if response.status_code == 200:
    crypto_data = response.json()
    print(crypto_data)
else:
    print(f"Ошибка запроса, код ответа {response.status_code}")

# 4. Технические индикаторы
# Пример запроса простой скользящей средней (SMA):

# Параметры для расчета простой скользящей средней
params = {'function': 'SMA',
          'symbol': 'AAPL',
          'interval': 'daily',
          'time_period': 50,
          'series_type': 'close',
          'apikey': my_api_key}

response = rq.get(url, params=params)

if response.status_code == 200:
    sma_data = response.json()
    print(sma_data)
else:
    print(f"Ошибка запроса, код ответа {response.status_code}")

# Создаем экземпляр API клиента
api = wbpy.IndicatorAPI()

# Например, выберем индикатор доступа к электроэнергии для всех стран за определенный год
indicator_id = "AG.PRD.CROP.XD" # Код индикатора
country_codes = ['USA', 'AF', 'BI']  # 3 выбранные страны
date = "2018:2018"  # Данные за 2018 год

# Запрашиваем данные
dataset = api.get_dataset(indicator_id, country_codes, date=date)
data = dataset.as_dict()

# Выводим данные
for country, values in data.items():
    print(f"{country}: {values}")

indicators = wbdata.get_indicators()

# Преобразование в DataFrame для удобного поиска
df_indicators = pd.DataFrame(indicators)
#параметр поиска
serch_param = 'SE.ADT.LITR'

# Поиск по названию
gdp_results = df_indicators[df_indicators['name'].str.contains(serch_param, case=False, na=False)]
print(gdp_results[['id', 'name']].head(10))

#грамотность взрослого населения латинской америки
id_educ = 'SE.ADT.LITR.ZS'
countr_educ = ['LCN']
date = "2018:2018"  # Данные за 2018 год

dataset_educ = api.get_dataset(id_educ, countr_educ, date=date)
data_educ = dataset_educ.as_dict()

#вывод данных
for country, values in data_educ.items():
    print(f"{country}: {values}")
