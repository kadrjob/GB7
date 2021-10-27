class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


a = int(input('Enter 1 number: '))
b = int(input('Enter 2 number: '))

try:
    if b == 0:
        raise MyException('Zero devision error')
except (ZeroDivisionError, MyException) as e:
    print(e)
else:
    print(a / b)
