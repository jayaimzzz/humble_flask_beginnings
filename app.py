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
    instructions = random_recipe.get("instructions").split("\n")
    ingredients = random_recipe.get("ingredients").split("\n")
    instructions = [step for step in instructions if step]
    ingredients = [item for item in ingredients if item]
    name = random_recipe.get("name")
    url = random_recipe.get("url")
    recipe = {
        "name":name,
        "instructions":instructions,
        "ingredients":ingredients,
        "url":url
    }
    return render_template("recipe.html", recipe=recipe)

