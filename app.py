__author__ = "jayaimzzz"

from tinydb import TinyDB, Query
from flask import render_template, Flask
from jinja2 import Template, Environment, PackageLoader, select_autoescape
import random

env = Environment(
    loader=PackageLoader('app', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)
template = env.get_template('recipe.html')
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
    return render_template(template, recipe=recipe)



