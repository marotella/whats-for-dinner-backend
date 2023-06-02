from peewee import *
import datetime
from flask_login import UserMixin

DATABASE = SqliteDatabase("ingredients.sqlite")

## Ingredients model:

class Ingredient(Model):
    ingredient = CharField(unique=True)## Makes sure we are not making duplicates
    quantity = IntegerField()
    image = CharField(null=True)
    created_at = DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        database = DATABASE


class User(Model, UserMixin):
    username = CharField(unique=True)
    email = CharField(unique = True)
    password = CharField()
    
    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    # DATABASE.drop_tables([Ingredient], safe=True)

    DATABASE.create_tables([User, Ingredient], safe=True)
    print("Connected to the database, tables created.")
    DATABASE.close()
    