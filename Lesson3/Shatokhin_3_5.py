# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):

from random import choice

# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(jcount=1, uniq_only=False):
    """
    Генерирует указанное количество шуток, склеенных из слов определенных списков

    :param jcount: Количество шуток к генерации
    :uniq_only: Использовать те слова которые еще не встречались
    :return: Список сгенерированных шуток
    """

    # списки можно сделать глобальными, но вынес в функцию для решения сразу с уникальными значениями
    # копии глобального списка для удаления данных
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    result = []
    for i in range(1, jcount + 1):
        _nouns = choice(nouns)
        _adverbs = choice(adverbs)
        _adjectives = choice(adjectives)

        result.append(f'{_nouns} {_adverbs} {_adjectives}')

        # если используем уникальные значения, то использованные элементы удаляем из списков
        if uniq_only:
            nouns.pop(nouns.index(_nouns))
            adverbs.pop(adverbs.index(_adverbs))
            adjectives.pop(adjectives.index(_adjectives))

            # контроль длины оставшихся списков
            # если список будет пустой, choice даст ошибку
            # поэтому прекращаем генерацию шуток
            if len(nouns) == 0 or len(adverbs) == 0 or len(adjectives) == 0:
                break

    return result


print(get_jokes(40, True))
