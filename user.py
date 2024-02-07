import database
class User():
    def __init__(self, username, name, lastname, password, role):
        # Constructor to initialize user attributes
        self.username = username
        self.name = name
        self.lastname = lastname
        self.password = password
        self.role = role

    @classmethod
    def login(self, username, password, role):
        # Class method to authenticate user login
        customer_data = database.get_all("person")
        for customer in customer_data:
            if username == customer['username'] and password == customer['password'] and role == customer['role']:
                return True  # Return True if login credentials match
        else:
            return False  # Return False if login credentials do not match

    @classmethod
    def get_all_customers(self):
        # Class method to retrieve all customers from the database
        customer_data = database.get_all("person")
        return customer_data

    @classmethod
    def get_username(self, username):
        # Class method to retrieve customer information by username
        user_data = database.get_by_username(username)
        return user_data

    def insert_custamer(self):
        # Method to insert customer data into the database
        database.add_customer(self.username, self.name, self.lastname, self.password, self.role)

    def get_customer_info(self, id_customer):
        # Method to retrieve customer information by customer ID
        customer = database.get_by_id("customer", id_customer)
        return customer

    @classmethod
    def edit_customer_info(self, username, id, name, lastname, password, role):
        # Class method to edit customer information
        database.edit_customer(username, id, name, lastname, password, role)

    @classmethod
    def delete_customer(self, id_customer):
        # Class method to delete a customer from the database
        database.delete("person", id_customer)

    def add_customer(self):
        # Method to add a new customer to the database
        database.add_customer(self.username, self.name, self.lastname, self.password, self.role)



