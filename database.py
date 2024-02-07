import mysql.connector
import pandas as pd



database = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="admin",
    database="careport"
)

cursor = database.cursor(dictionary=True)


def save_infor_db():
    car_data = pd.read_csv('data/car_data.csv')
    car_data.fillna(0, inplace=True)
    database.commit()
    insert_query = """INSERT INTO car_sales (car_id, date, customer_Name, gender, annual_Income, dealer_Name, company,  model, engine,  transmission, color,  price, dealer_No, body_Style, phone, dealer_Region) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    for index, row in car_data.iterrows():
        cursor.execute(insert_query, (
            row['Car_id'],
            row['Date'],
            row['Customer Name'],
            row['Gender'],
            row['Annual Income'],
            row['Dealer_Name'],
            row['Company'],
            row['Model'],
            row['Engine'],
            row['Transmission'],
            row['Color'],
            row['Price'],
            row['Dealer_No '],
            row['Body Style'],
            row['Phone'],
            row['Dealer_Region']
        ))
    database.commit()
    database.close()


def login_query(username, password):
    """
    Function to perform a login query.
    Returns:
        list: The result of the query.
    """
    cursor.execute(f"SELECT * FROM person where username = '{username}' and password = '{password}' LIMIT 1")
    result = cursor.fetchall()
    return result


def check_if_user_exist(username):
    """
    Function to check if a user exists.
    Returns:
        list: The result of the query.
    """
    cursor.execute(f"SELECT * FROM person where username = '{username}'")
    result = cursor.fetchall()
    return result


def create_user(username, password):
    """
    Function to create a new user.
    """
    cursor.execute("INSERT INTO users (username, password, role) "
                   f"VALUES ('{username}', '{password}', 'USER')")
    database.commit()


def get_all(table_name):
    """
    Function to retrieve all records from a table.
    Returns:
        list: The result of the query.
    """
    cursor.execute(f"SELECT * FROM {table_name}")
    return cursor.fetchall()


def get_by_id(table_name, id):
    """
    Function to retrieve a record by ID from a table.
    Returns:
        list: The result of the query.
    """
    consulta = "SELECT * FROM {} WHERE id=%s".format(table_name)
    cursor.execute(consulta, (id,))
    return cursor.fetchall()


def get_by_username(username):
    """
    Function to retrieve a record by username.
    Returns:
        list: The result of the query.
    """
    consulta = "SELECT * FROM person WHERE username =%s"
    cursor.execute(consulta, (username,))
    return cursor.fetchall()


def delete(table_name, id):
    """
    Function to delete a record from a table.
    """
    consulta = "DELETE FROM {} WHERE id=%s".format(table_name)
    cursor.execute(consulta, (id,))
    database.commit()


def add_customer(username, name, lastname, password, role):
    """
    Function to add a new customer.

    """
    cursor.execute(
        f"INSERT INTO person (username, name, lastname, password, role) VALUES ('{username}','{name}', '{lastname}', '{password}', '{role}')")
    database.commit()


def edit_customer(username, id, name, lastname, password, role):
    """
    Function to edit customer details.

    """
    consulta = "UPDATE person SET username = %s, name = %s, lastname = %s, password= %s, role = %s WHERE id = %s"
    cursor.execute(consulta, (username, name, lastname, password, role, id))
    database.commit()



