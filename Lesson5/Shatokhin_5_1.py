def odd_nums(num=1):
    for n in range(1,num+1,2):
        yield n+1

num = odd_nums(5)
print(next(num))
print(next(num))
print(next(num))
print(next(num))