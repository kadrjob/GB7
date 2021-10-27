class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    s = input('Enter digit: ')
    if s.lower() == 'stop':
        break

    try:
        if not s.isdigit():
            raise MyException('Enter only digit!')
        else:
            my_list.append(int(s))
    except (ValueError, MyException) as e:
        print(e)

print(my_list)
