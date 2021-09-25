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
    encodings = utils.get_encoding_from_headers(response.headers)
    data = response.content.decode(encoding=encodings)

    return data


def get_curs_date(content):
    """
    Получим дату курса валюты

    :param content:Строка ответа API
    :return: Дата курса валюты как объект date
    """
    date_object = None

    # нашли строку Date=, вырезали ее до имени атрибута name, убрали Date=, пробелы и ковычки
    curs_str = content[content.find('Date='):content.find('name')].replace('Date=', '').replace(' ', '').replace('"',
                                                                                                                 '')

    # разделили дату на составляющие
    curs_values = curs_str.split('.')

    # конверитировали в объект datetime
    date_object = datetime(day=int(curs_values[0]), month=int(curs_values[1]), year=int(curs_values[2]))
    return date_object


def currency_rates(val_name='USD'):
    """
    Получим курс и дату валюты

    :param val_name:Имя валюты для поиска
    :return: Список [курс,дата]
    """
    content = get_url_data()

    # получили начало имени валюты
    elem_end_pos = content.find(val_name.upper())
    if elem_end_pos > -1:

        # вырезали кусок строки с начала имени валюты до элемента /Value найденного с начала имени валюты
        str_content = content[elem_end_pos:content.find('</Value>', elem_end_pos)]

        # из вырезанного куска вырезали еще один с имени Value и до конца строки,
        # убрали Value и заменили запятые на точки
        curs_str = str_content[str_content.rfind('<Value>'):].replace('<Value>', '').replace(',', '.')

        # конвертировали валюту в число
        curs_digit = float(curs_str)

        # получили дату
        date_curs = get_curs_date(content)

        result = curs_digit, date_curs
    else:
        result = None

    return result
