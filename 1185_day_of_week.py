from datetime import date
import calendar
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        my_date = date(year,month,day)
        return calendar.day_name[my_date.weekday()]