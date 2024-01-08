import mysql.connector

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="love_nourish"
    )

def get_available_measurement_units():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT UnitID, UnitName, UnitShortName FROM MeasurementUnits")
    units = cursor.fetchall()
    cursor.close()
    conn.close()
    return units

def add_ingredient(ingredient_name, unit_id):
    # Create a database connection
    conn = create_connection()

    try:
        # Create a cursor object
        cursor = conn.cursor()

        # Insert the ingredient into the Ingredients table
        add_ingredient_query = "INSERT INTO Ingredients (Name, MeasurementUnitID) VALUES (%s, %s)"
        print(add_ingredient_query)

        cursor.execute(add_ingredient_query, (ingredient_name, unit_id))
        conn.commit()

        # Close the cursor and database connection
        cursor.close()
        conn.close()

        # Ingredient added successfully
        return True

    except Exception as e:
        print("Error:", e)
        conn.rollback()
        conn.close()
        return False

if __name__ == "__main__":
    # You can add testing or command-line functionality here if needed
    pass
