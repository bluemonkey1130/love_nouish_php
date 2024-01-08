import mysql.connector

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="love_nourish"
    )

def get_available_ingredients():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT IngredientID, Name, MeasurementUnitID FROM Ingredients")
    ingredients = cursor.fetchall()
    cursor.close()
    conn.close()
    return ingredients

def get_available_recipes():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT RecipeID, Title FROM Recipes")
    recipes = cursor.fetchall()
    cursor.close()
    conn.close()
    return recipes

def create_recipe_with_ingredients(recipe_name, ingredients, quantities):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        # Insert the recipe into the Recipes table
        add_recipe_query = "INSERT INTO Recipes (Title) VALUES (%s)"
        cursor.execute(add_recipe_query, (recipe_name,))
        conn.commit()

        # Get the ID of the newly inserted recipe
        recipe_id = cursor.lastrowid

        # Insert ingredients and quantities into RecipeIngredients table
        for ingredient, quantity in zip(ingredients, quantities):
            add_ingredient_query = "INSERT INTO RecipeIngredients (RecipeID, Ingredient, Quantity) VALUES (%s, %s, %s)"
            cursor.execute(add_ingredient_query, (recipe_id, ingredient, quantity))
            conn.commit()

        # Close the cursor and database connection
        cursor.close()
        conn.close()

        # Recipe created successfully
        return True

    except Exception as e:
        print("Error:", e)
        conn.rollback()
        conn.close()
        return False

if __name__ == "__main__":
    # You can add testing or command-line functionality here if needed
    pass
