
from datetime import date, datetime

today = date.today()

class Northcoder:
    def __init__(self, name, location, course, graduation_date):
        self.name = name
        self.location = location
        self.course = course
        self.graduation_date = graduation_date

    def greet(self, teacher):
        print(f'Hello {teacher}, my name is {self.name}')
        return f'Hello {teacher}, my name is {self.name}'
    
    def alumni(self):
        month_split = self.graduation_date.split()
        month_to_num = datetime.strptime(month_split[0], '%B').month
        today_convert_str = str(today)
        today_total_val = int(today_convert_str[0:4]) * 100 + int(today_convert_str[5:7])
        month_total_val = int(month_split[1]) * 100 + month_to_num

        if month_total_val < today_total_val:
            return True
        




        




