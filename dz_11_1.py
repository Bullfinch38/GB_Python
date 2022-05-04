class Date:
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    def string_to_db(self):
        return f'{self.year} {self.month} {self.day}'


date1 = Date.from_string('30-12-2020')
date1.string_to_db()