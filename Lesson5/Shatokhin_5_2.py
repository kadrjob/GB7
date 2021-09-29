import itertools as it
import time
n_count = 8

# using itertools
n_start = time.perf_counter()
num_gen = it.filterfalse(lambda n: n % 2 == 0, (num for num in (range(1, n_count))))
n_end = time.perf_counter()
print(f'Itertools start: {n_start}, end: {n_end} elapsed: {n_end}')

# using Build'in filter
n1_start = time.perf_counter()
num_gen1 = filter(lambda n: n % 2 != 0, (num for num in (range(1, n_count))))
n1_end = time.perf_counter()
print(f'Buildin filter start: {n1_start}, end: {n1_end} elapsed: {n1_start}')

print(next(num_gen))
print(next(num_gen))
print(next(num_gen))
print(next(num_gen))
print(next(num_gen))
print(next(num_gen))
print(next(num_gen))

print(next(num_gen1))
print(next(num_gen1))
print(next(num_gen1))
print(next(num_gen1))
print(next(num_gen1))
print(next(num_gen1))
print(next(num_gen1))