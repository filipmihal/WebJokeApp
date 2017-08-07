"""helper for selecting the joke of the day"""
import time
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
