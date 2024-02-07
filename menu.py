import database as data
from data import Data
from user import User
class Menu:

    def __init__(self):
        # Initialize the Menu class
        pass  # No initialization required in the constructor

    def start_menu(self):
        # Method to display the start menu for logging in
        run = True
        while run:
            print("   LOGIN     ")
            username = input("Write your username: ").strip()
            password = input("Write your password: ").strip()
            answer = data.login_query(username, password)
            if answer:
                run = False  # Stop the loop if login is successful
                self.user_menu()  # Proceed to the user menu
            else:
                print("Los datos ingresados no son válidos")  # Print message for invalid login data

    def user_menu(self):
        # Method to display the user menu after successful login
        a = Data()  # Create a Data object
        answer = input("     USER MENU      \n"
                       "1. Sales by days \n"
                       "2. Top 5 stores that sold the most cars \n"
                       "3. Top 10 company with the most revenue \n"
                       "4. Number of cars sold per month\n"
                       "5. Top 10 best selling cars\n"
                       "6. Fastest growing companies\n"
                       "7. \n"
                       "Enter your choice: ")  # Prompt user for menu choice
        if answer.isdigit():
            answer = int(answer)
            # Check user input and execute corresponding action
            match answer:
                case 1:
                    a.sales_x_day()  # Show sales by days
                case 2:
                    a.store_top5()  # Show top 5 stores that sold the most cars
                case 3:
                    a.top_10_company()  # Show top 10 companies with the most revenue
                case 4:
                    a.cars_sold_per_month() # Show top 10 companies with the most revenue
                case 5:
                    a.top_10_car()# Show top 10 companies with the most revenue
                case 6:
                    a.growing_companies()  # Show top 10 companies with the most revenue
        else:
            print(f" { answer } is not a number ")  # Print message for invalid menu choice

    def show_customers(self):
        # Method to display all customers
        customers = User.get_all_customers()  # Get all customers from database
        # Display customer information
        for index, customer in enumerate(customers, start=1):
            print(
                f"{index} . username: {customer['username']} ,name: {customer['name']}, last name: {customer['lastname']}, role: {customer['role']}")

    def edit_customer(self):
        # Method to edit customer information
        customers = User.get_all_customers()  # Get all customers from database
        self.show_customers()  # Show list of customers
        try:
            # Prompt user to select the customer to edit
            customer_number = int(input("write the number of the user you want to edit: "))
            if customer_number:
                customer_data = customers[customer_number - 1]  # Get customer data based on selection
                id = int(customer_data['id'])  # Extract customer ID
                # Prompt user for updated information
                username = input(f"username: {customer_data['username']}")
                name = input(f"name: {customer_data['name']}: ")
                last_name = input(f"last name: {customer_data['lastname']}: ")
                password = input(f"password: {customer_data['password']}: ")
                role = ""
                run = True
                # Validate and prompt user for role until valid input is provided
                while run == True:
                    role = input(f"role(custumer/admin) : {customer_data['role']}: ")
                    if role != "admin" and role != "customer":
                        print("The role is not defined")
                    else:
                        run = False
                # Update customer information in the database
                User.edit_customer_info(id, name, last_name, password, role)
        except:
            print("Invalid input")  # Print message for invalid input

    def delete_customer(self):
        # Method to delete a customer from the database
        customers = User.get_all_customers()  # Get all customers from the database
        self.show_customers()  # Show list of customers
        try:
            # Prompt user to select the customer to delete
            customer_number = int(input("write the number of the user you want to delete: "))
            if customer_number:
                customer_data = customers[customer_number - 1]  # Get customer data based on selection
                id_customer = customer_data['id']  # Extract customer ID
                # Display customer information for confirmation
                print(f"username-> {customer_data['username']}\n"
                      f"name-> {customer_data['name']}\n"
                      f"lastname-> {customer_data['lastname']}\n"
                      f"password-> {customer_data['password']}\n"
                      f"role-> {customer_data['role']}\n")
                # Prompt user for confirmation
                confirmation = input("Select (Y/N) and Q to exit: ").strip().lower()
                if confirmation == "y":
                    User.delete_customer(id_customer)  # Delete customer from the database
                elif confirmation == "n":
                    print("hola")  # Print message if user chooses not to delete
        except:
            print("Invalid input")  # Print message for invalid input

    def admin_menu_customer(self):
        # Method to display admin menu options for managing users
        answer = input("1. Show all user\n"
                       "2. Edit user\n"
                       "3. Delete user\n"
                       ).strip()  # Prompt user for menu choice
        match answer.lower():
            case "1":
                self.show_customers()  # Show all users
            case "2":
                self.edit_customer()  # Edit user information
            case "3":
                self.delete_customer()  # Delete user

    def init_admin(self, name):
        # Method to initialize admin session and display admin menu
        run = True
        while run:
            print(f"Welcome admin {name}")  # Print welcome message with admin name
            # Prompt user for admin menu choice
            answer = input("       MENU \n"
                           "1. Manage user\n"
                           "2. Main menu\n"
                           "q. Exit\n"
                           "-->"
                           ).strip()
            match answer.lower():
                case "1":
                    self.admin_menu_customer()  # Display admin menu for managing users
                case "2":
                    self.menu()  # Go back to the main menu
                case "q":
                    print("Exit")  # Print exit message
                    run = False  # Stop the loop and exit the program

    def login_customer(self, role, menu):
        # Method to log in a customer with the specified role and menu
        x = False
        name = input("write your username: ").strip()  # Prompt user for username
        password = input("write your password: ").strip()  # Prompt user for password
        answer = User.login(name, password, role)  # Check login credentials
        if answer:
            if menu == "1":
                self.user_menu()  # Proceed to user menu if role is user
                x = True
            elif menu == "2":
                self.init_admin(name)  # Initialize admin session if role is admin
        else:
            print("No login")  # Print message for failed login attempt
        return x  # Return login status

    def startMenu(self):
        # Method to start the main menu of the program
        print("Welcome to the Johan programming task!")  # Display welcome message
        run = True
        while run:
            # Prompt user to select user type
            answer = input("option\n"
                           "1. User\n"
                           "2. Admin\n"
                           )
            if answer.isdigit():
                answer = int(answer)
                if answer == 1:
                    role = "customer"
                    # Call login_customer method for user login
                    answer = self.login_customer(role, "1")
                    if answer:
                        run = False
                elif answer == 2:
                    role = "admin"
                    # Call login_customer method for admin login
                    login = self.login_customer(role, "2")
                    if login:
                        run = False
                else:
                    print("Enter the correct number")  # Print message for incorrect input
            else:
                print("Enter a valid number")  # Print message for invalid input

    def login(self):
        # Method to handle login process
        print("login")  # Display login message
        run = True
        while run:
            # Prompt user to select user type or return to menu
            answer = input("Select the user type\n"
                           "1. User\n"
                           "2. Administrator\n"
                           "3. return to menu\n"
                           ).strip()
            match answer.lower():
                case "1":
                    role = "customer"
                    # Call login_customer method for user login
                    answer = self.login_customer(role, "1")
                    if answer:
                        run = False
                case "2":
                    role = "admin"
                    # Call login_customer method for admin login
                    answer = self.login_customer(role, "2")
                    if answer:
                        run = False
                case "3":
                    self.menu()  # Return to main menu
                case _:
                    print("The selection is not correct Choose one of the options")

    def create_account(self):
        # Method to handle account creation
        run = True
        while run:
            # Prompt user to enter account details
            username = input("username: ")
            name = input("name: ")
            last_name = input("last name: ")
            password = input("password: ")
            role = "customer"  # Default role is customer for account creation
            if username and name and last_name and password:
                # Create new user object and add to database
                login = User(username, name, last_name, password, role)
                login.add_customer()
                customers = login.get_all_customers()
                last_customer = customers[-1]
                if last_customer['username'] == username:
                    print(f"The customer {username} was added")  # Print success message
                    run = False
                    self.menu()  # Return to main menu after account creation
            else:
                print("You must fill out all fields")  # Print message for incomplete fields

    def menu(self):
        # Method to display the main menu of the program
        print("Welcome")  # Display welcome message
        run = True
        while run:
            # Prompt user to select an option from the menu
            answer = input("\nMENU OPTIONS\n"
                           "1. Log In\n"
                           "2. Create Account\n"
                           "Q. Exit the program \n"
                           "-->\n"
                           ).strip()
            match answer.lower():
                case "1":
                    self.startMenu()  # Start the login menu
                case "2":
                    self.create_account()  # Create a new user account
                case "q":
                    run = False  # Exit the program
                case _:
                    print("The selection is not correct Choose one of the options")  # Print message for invalid input