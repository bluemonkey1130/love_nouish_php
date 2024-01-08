import mysql.connector

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="love_nourish"
    )

def create_common_units(connection):
    # List of common units: full name followed by abbreviation
    common_units = [
        ("Grams", "g"),
        ("Kilograms", "kg"),
        ("Pieces", "pcs"),
        ("Pinch", "pinch"),
        ("Tablespoon", "tbsp"),
        ("Teaspoon", "tsp"),
        ("Liters", "l"),
        ("Milliliters", "ml"),
        ("Cups", "cup"),
        ("Ounces", "oz"),
        ("Pounds", "lb"),
        # Add more units as needed
    ]

    cursor = connection.cursor()

    for unit_name, unit_short_name in common_units:
        # Check if the unit already exists
        cursor.execute("SELECT * FROM measurementunits WHERE UnitName = %s OR UnitShortName = %s", (unit_name, unit_short_name))
        result = cursor.fetchone()
        if result:
            print(f"Unit {unit_name} ({unit_short_name}) already exists.")
            continue

        # Insert the unit if it doesn't exist
        add_unit_query = ("INSERT INTO measurementunits (UnitName, UnitShortName) "
                          "VALUES (%s, %s)")
        cursor.execute(add_unit_query, (unit_name, unit_short_name))
        print(f"Added unit {unit_name} ({unit_short_name}) to the database.")

    connection.commit()
    cursor.close()

def main():
    conn = create_connection()
    create_common_units(conn)
    conn.close()

if __name__ == "__main__":
    main()
