import time
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

t1_start = time.perf_counter()
result = [num for num in src if src.count(num) == 1]
t1_end = time.perf_counter()
print(f'1. Время старта: {t1_start} время окончания: {t1_end} длительность: {t1_end - t1_start}')
print (result)

# оптимизация - создадим список имеющихся значений
t2_start = time.perf_counter()
uniq_dict = {num: 0 for num in src}

for num in src:
    uniq_dict[num] += 1

result = [num for num in uniq_dict if uniq_dict[num] == 1]
t2_end = time.perf_counter()
print(f'2. Время старта: {t2_start} время окончания: {t2_end} длительность: {t2_end - t2_start}')

print(result)

