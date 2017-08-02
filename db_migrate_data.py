import pymysql
from app import db, models
#test
def ConnectToDB():
    return pymysql.connect(host="localhost",   
        user="root", # your username
        passwd="", # your password
        db="test",
        charset='utf8') 

#setup database
global database
connect = ConnectToDB()
database = connect.cursor(pymysql.cursors.DictCursor)

#get all categories
def GetAllCategories():
    database.execute("SELECT * FROM mig_jokes_categories ORDER BY id ASC")
    return database.fetchall()

def InsertCategories(categories):
    for category in categories:
        current_category = models.Category(id = category['id'], name=category['name'], average_rank = category['average_rank'])
        db.session.add(current_category)
        print(category['id'])

categories = GetAllCategories()
InsertCategories(categories)
db.session.commit()

db_categories = models.Category.query.all()
for db_category in db_categories:
    print(db_category.name, db_category.id)


#get all jokes
def GetAllJokes():
    database.execute("SELECT * FROM mig_jokes ORDER BY id ASC")
    return database.fetchall()

def InsertJokes(jokes):
    for joke in jokes:
        current_joke = models.Joke(id = joke['id'], joke=joke['joke'], joke_length = joke['joke_length'], rank = joke['rank'], category_id = joke['category_id'])
        db.session.add(current_joke)
        print(joke['id'])

jokes = GetAllJokes()
InsertJokes(jokes)
db.session.commit()

db_jokes = models.Joke.query.all()
for db_joke in db_jokes:
    print(db_joke.id)
# for joke in jokes:
#     print(joke['id'])