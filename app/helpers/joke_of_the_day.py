"""helper for selecting the joke of the day"""
import time

from app.models import Joke
from app.constants import languages

def current_joke(date):
    """method select one specific joke which is selected by current date"""
    valid_jokes_count = Joke.query.count()
    date_num = time.mktime(time.strptime(date, "%Y-%m-%d"))
    days_in_date = int(date_num / 86400)
    current_joke_id = int(days_in_date % valid_jokes_count)
    if current_joke_id == 0:
        current_joke_id = valid_jokes_count
    selected_joke = Joke.query.filter_by(id=current_joke_id).first()
    return selected_joke

class UiDate:
    """generate slovak date name"""
    def get_day_name(self):
        """method returns name of the day in Slovak language"""
        return languages.SLOVAK_DAYS_IN_WEEK[self.day_name]
    def get_month_name(self):
        """method returns name of month in Slovak language"""
        return languages.SLOVAK_MONTHS[self.month]
    def get_day_number(self):
        """method returns number of day in month"""
        return self.day_num
    def __init__(self, day_name, day_num, month):
        """set year, name of day and day number"""
        self.day_name = int(day_name)
        self.day_num = day_num
        self.month = int(month)
