# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp
import requests
from requests import utils


def get_url_data(url='http://www.cbr.ru/scripts/XML_daily.asp'):
    """
    Получим ответ API в виде строки

    :param url: url API
    :return: Строка ответ API
    """
    response = requests.api.get(url)
    encodings = utils.get_encoding_from_headers(response.headers)
    data = response.content.decode(encoding=encodings)

    return data


def currency_rates(val_name='USD'):
    """
    Получим курс валюты

    :param val_name:Имя валюты для поиска
    :return: Список [курс,дата]
    """
    content = get_url_data()

    elem_end_pos = content.find(val_name.upper())
    if elem_end_pos > -1:
        str_content = content[elem_end_pos:content.find('</Value>', elem_end_pos)]
        kurs_str = str_content[str_content.rfind('<Value>'):].replace('<Value>', '').replace(',', '.')
        kurs_digit = float(kurs_str)

        result = kurs_digit
    else:
        result = f'Валюта {val_name} не найдена'

    return result


print(currency_rates('GBP'))
