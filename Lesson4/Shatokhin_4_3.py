# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp
from datetime import datetime

import requests
from requests import utils


def get_url_data(url='http://www.cbr.ru/scripts/XML_daily.asp'):
    """
    Получим ответ API в виде строки

    :param url: url API
    :return: Строка ответ API
    """
    response = requests.api.get(url)
    # или как вариант без декодирования
    data = response.text

    encodings = utils.get_encoding_from_headers(response.headers)
    data = response.content.decode(encoding=encodings)

    return data


def get_kurs_date(content):
    """
    Получим дату курса валюты

    :param content:Строка ответа API
    :return: Дата курса валюты как объект date
    """
    date_object = None

    # нашли строку Date=, вырезали ее до имени атрибута name, убрали Date=, пробелы и ковычки
    kurs_str = content[content.find('Date='):content.find('name')].replace('Date=', "").replace(' ', '').replace('"','')

    # разделили дату на составляющие
    kurs_values = kurs_str.split('.')

    # конверитировали в объект datetime
    date_object = datetime(day=int(kurs_values[0]), month=int(kurs_values[1]), year=int(kurs_values[2]))
    return date_object


def currency_rates(val_name='USD'):
    """
    Получим курс и дату валюты

    :param val_name:Имя валюты для поиска
    :return: Список [курс,дата]
    """
    content = get_url_data()
    date_kurs = get_kurs_date(content)

    # получили начало имени валюты
    elem_end_pos = content.find(val_name.upper())
    if elem_end_pos > -1:

        # вырезали кусок строки с начала имени валюты до элемента /Value найденного с начала имени валюты
        str_content = content[elem_end_pos:content.find('</Value>', elem_end_pos)]

        # из вырезанного куска вырезали еще один с имени Value и до конца строки,
        # убрали Value и заменили запятые на точки
        kurs_str = str_content[str_content.rfind('<Value>'):].replace('<Value>', '').replace(',', '.')

        # конвертировали валюту в число
        kurs_digit = float(kurs_str)

        result = kurs_digit, date_kurs
    else:
        result = None

    return result


print(currency_rates('GBP'))
