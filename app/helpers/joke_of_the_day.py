"""helper for selecting the joke of the day"""
import time
import datetime
from app.models import Joke
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
    def __init__(self,day_name, day_num, month):
        days_in_week = ["", "Pondelok", "Utorok", "Streda", "štvrtok", "Piatok", "Sobota", "Nedeľa"]
        months = ["", "Január", "Február", "Marec", "Apríl", "Máj", "Jún", "Júl", "August", "September", "Október", "November", "December"]
        """set year, name of day and day number"""
        self.day_name = days_in_week[int(day_name)]
        self.day_num = day_num
        self.month = months[int(month)]
