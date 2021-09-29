import itertools as it

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б'
    # , '10А', '10Б', '9А'
]

gen = ((t, k) for t, k in it.zip_longest(tutors, klasses))

# это генератор
print(type(gen))

# результат задачи
print(list(gen))

# проверка на истощение
print(next(gen))
