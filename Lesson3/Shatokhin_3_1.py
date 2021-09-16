# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.

translate_list = {'один': 'one',
                  'два': 'two',
                  'три': 'three',
                  'четыре': 'four',
                  'пять': 'five',
                  'шесть': 'six',
                  'семь': 'seven',
                  'восемь': 'eight',
                  'девять': 'nine',
                  'десять': 'ten',
                  'ноль': 'zero'
                  }


def num_translate(num):
    """
    Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
    # >>> num_translate("one")
    # "один"
    # >>> num_translate("eight")
    # "восемь

    функция переводит как рус-анг так и анг-рус
    если входящее значение начинается с Заглавной буквы, выходное значение также будет начинаться с заглавной
    """
    result = None
    num_lower = num.lower()  # переведем в нижный регистр тк ключи у нас в нижних

    # ищем сначала как русское значение - в ключах
    if num_lower in translate_list.keys():
        result = translate_list[num_lower]

    # если не нашли - ищем как анг - в значениях
    elif num_lower in translate_list.values():
        result = tuple(*filter(lambda el: num_lower in el, translate_list.items()))[0]

    # переводим в нужный регистр при необходимости
    if result:
        if num[0].isupper():
            result = result.capitalize()

    return result


print(num_translate('nine'))
