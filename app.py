__author__ = "jayaimzzz"

from tinydb import TinyDB, Query
from flask import render_template, Flask
import random

app = Flask(__name__)
db = TinyDB('db.json')
recipes = db.all()


@app.route('/')
def index():
    random_recipe = random.choice(recipes)
    return render_template('recipe.html', recipe=random_recipe)



