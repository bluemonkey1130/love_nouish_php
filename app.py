from flask import Flask, render_template, request, redirect, url_for
from add_recipe import create_recipe_with_ingredients
from add_recipe import get_available_ingredients
from add_recipe import get_available_recipes

from add_ingredient import add_ingredient
from add_ingredient import get_available_measurement_units

app = Flask(__name__)

# Define your Flask routes

@app.route('/')
def index():
    # You can render a homepage or index page here
    return render_template('index.html')

@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        # Handling a POST request
        recipe_name = request.form['recipe_name']
        ingredients = request.form.getlist('ingredient')
        quantities = request.form.getlist('quantity')

        # Call the create_recipe_with_ingredients function
        create_recipe_with_ingredients(recipe_name, ingredients, quantities)

        # Redirect to a success page or home page
        return redirect(url_for('index'))

    # Handling a GET request (fetch available ingredients and render the form)
    ingredients = get_available_ingredients()
    recipes = get_available_recipes()
    return render_template('add_recipe.html', ingredients=ingredients, recipes=recipes)


@app.route('/add_ingredient', methods=['GET', 'POST'])
def add_ingredient_route():
    if request.method == 'POST':
        ingredient_name = request.form['ingredient_name']
        unit_id = request.form['unit_id']

        # Call the add_ingredient function from add_ingredient.py
        add_ingredient(ingredient_name, unit_id)

        # Redirect to a success page or home page
        return redirect(url_for('index'))

    # Fetch available Measurement Units from the database
    measurement_units = get_available_measurement_units()
    # You can render the add ingredient form here
    return render_template('add_ingredient.html', measurement_units=measurement_units)

if __name__ == '__main__':
    app.run(debug=True)
