import calendar

class Data:
    def __init__(self, day, month, year, date_str):
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)
        self.date_str = date_str
        
    @classmethod
    def get_date_list(cls, date_str):
        day, month, year = date_str.split('-')
        return cls(day, month, year, date_str)

    @staticmethod
    def date_is_valid(obj):
        day = obj.day
        month = obj.month
        year = obj.year

        if month < 1 or month > 12:
            return f'Month {month} is not valid. Must be from 1 to 12'

        if day < 1 or day > 31:
            return f'Day {day} is not valid. Must be from 1 to 31'

        if month == 2:
            if calendar.isleap(year):
                if day > 29:
                    return f'Day {day} is not valid. In leap year Must be from 1 to 29'
            elif day > 28:
                return f'Day {day} is not valid. In non leap year Must be from 1 to 28'

        if 0 > year or len(str(year)) > 4:
            return f'Year {year} is not valid. Must be from 0 to 9999'

        return f'Date {obj.date_str} is valid'


my_data = Data.get_date_list('33-01-2000')
print(my_data.date_is_valid(my_data))