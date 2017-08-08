"""this is the script which migrates all data from my old DATABASE to new sqlite db"""
import pymysql
from app import DB, models
def connect_to_db():
    """connect to my localhost DB"""
    return pymysql.connect(host="localhost",
                           user="root",
                           passwd="",
                           db="test",
                           charset='utf8')
CONNECT = connect_to_db()
DATABASE = CONNECT.cursor(pymysql.cursors.DictCursor)
def get_all_categories():
    """get all categories from old DB"""
    DATABASE.execute("SELECT * FROM mig_jokes_categories ORDER BY id ASC")
    return DATABASE.fetchall()
def insert_categories(categories):
    """insert all categories to sqlite"""
    for category in categories:
        current_category = models.Category(id=category['id'],
                                           name=category['name'],
                                           average_rank=category['average_rank']
                                          )
        DB.session.add(current_category)
CATEGORIES = get_all_categories()
insert_categories(CATEGORIES)
DB.session.commit()
DB_CATEGORIES = models.Category.query.all()
for db_category in DB_CATEGORIES:
    print(db_category.name, db_category.id)
def get_all_jokes():
    """get all jokes from old DB"""
    DATABASE.execute("SELECT * FROM mig_jokes ORDER BY id ASC")
    return DATABASE.fetchall()
def insert_jokes(jokes):
    """insert all jokes to new sqlite"""
    for joke in jokes:
        current_joke = models.Joke(joke=joke['joke'],
                                   joke_length=joke['joke_length'],
                                   rank=joke['rank'],
                                   category_id=joke['category_id']
                                  )
        DB.session.add(current_joke)
JOKES = get_all_jokes()
insert_jokes(JOKES)
DB.session.commit()
DB_JOKES = models.Joke.query.all()
for db_joke in DB_JOKES:
    print(db_joke.id)
print(models.Joke.query.count())
