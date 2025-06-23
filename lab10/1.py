import psycopg2
import csv

# Connect to PostgreSQL
conn = psycopg2.connect(host="localhost", database="suppliers", user="postgres", password="9874563210" )
cur = conn.cursor()

# Create table
cur.execute("""
    CREATE TABLE IF NOT EXISTS PhoneBook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        phone_number VARCHAR(15)
    )
""")
conn.commit()


# Function to insert data from CSV file into PhoneBook
def insert_from_csv(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            cur.execute("INSERT INTO PhoneBook (first_name, last_name, phone_number) VALUES (%s, %s, %s)", row)
    conn.commit()

# Function to insert data from console
def insert_from_console():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone_number = input("Enter phone number: ")
    cur.execute("INSERT INTO PhoneBook (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
                (first_name, last_name, phone_number))
    conn.commit()

# Function to update data in PhoneBook
def update_data(username, new_first_name=None, new_phone=None):
    if new_first_name:
        cur.execute("UPDATE PhoneBook SET first_name = %s WHERE first_name = %s",
                    (new_first_name, username))
    if new_phone:
        cur.execute("UPDATE PhoneBook SET phone_number = %s WHERE first_name = %s",
                    (new_phone, username))
    conn.commit()

# Function to query data from PhoneBook
def query_data(**kwargs):
    conditions = []
    for key, value in kwargs.items():
        conditions.append(f"{key} = '{value}'")
    query = "SELECT * FROM PhoneBook"
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_data(username=None, phone=None, _id=None):
    if username:
        cur.execute("DELETE FROM PhoneBook WHERE first_name = %s", (username,))
    elif phone:
        cur.execute("DELETE FROM PhoneBook WHERE phone_number = %s", (phone,))
    elif _id is not None:
        cur.execute("DELETE FROM PhoneBook WHERE id = %s", (_id,))
    else:
        print("Invalid parameters. Please provide 'username', 'phone', or 'id'.")
    conn.commit()


# Function to update data from console
def update_from_console():
    username = input("Enter the first name of the user you want to update: ")
    new_first_name = input("Enter the new first name (press Enter to skip): ")
    new_phone_number = input("Enter the new phone number (press Enter to skip): ")

    if not new_first_name and not new_phone_number:
        print("No new data provided. Exiting update process.")
        return

    update_data(username, new_first_name=new_first_name, new_phone=new_phone_number)
    print("Data updated successfully.")

# Function to query data from console
def query_from_console():
    field_name = input("Enter the field name you want to search (first_name, last_name, phone_number): ")
    field_value = input(f"Enter the value for {field_name}: ")
    
    # Формирование SQL-запроса на основе введенных значений
    query = f"SELECT * FROM PhoneBook WHERE {field_name} = %s"
    
    # Выполнение запроса с передачей значения параметра
    cur.execute(query, (field_value,))
    
    # Получение результатов запроса
    rows = cur.fetchall()
    
    # Вывод результатов на экран
    for row in rows:
        print(row)


def delete_from_console():
    field_name = input("Enter the field name you want to delete by (username, phone, id): ")
    
    if field_name == 'id':
        field_value = int(input(f"Enter the value for {field_name}: "))
        delete_data(_id=field_value)
    elif field_name == 'username' or field_name == 'phone':
        field_value = input(f"Enter the value for {field_name}: ")
        delete_data(**{field_name: field_value})
    else:
        print("Invalid field name. Please enter 'username', 'phone', or 'id'.")


# Example usage:

# Insert from CSV file
insert_from_csv('contacts.csv')

# Insert from console
insert_from_console()

# Update data
update_from_console()

# Query data
query_from_console()

# Delete data
delete_from_console()
'''