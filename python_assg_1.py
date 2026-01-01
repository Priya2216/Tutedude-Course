# Employee Management System (EMS)

# Objective - Create a simplified Employee Management System (EMS). This project will cover control structures,
#  functions, and object-oriented programming concepts to manage employee data.
# Steps to Implement

# ===============================================================================
# Step 1 - Plan the Data Storage
# Use a dictionary to store employee data where the keys is the emp_id (Employee ID) and 
# the value is another dictionary containing:


# name: Employee's name.
# age: Employee's age.
# department: Employee's department.
# salary: Employee's monthly salary.
# Initialize the dictionary with some sample employee data for testing 
# (e.g., {101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}}).

employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}
}

print(employees)
# ===============================================================================
# Step 2 - Define the Menu System
# Create a menu that displays the following options:


# Add Employee
# View All Employees
# Search for Employee
# Exit
# Implement a loop to continuously display the menu until the user chooses to Exit.

def main_menu():
    while True:
        print("\n===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("Thank you for using the Employee Management System ")
            break
        else:
            print("Invalid choice! Please select a valid option.")
# ===============================================================================
# Step 3 - Add Employee Functionality
# Prompt the User to enter the following details for a new employee:


# emp_id (Employee ID)
# name (Employee Name)
# age (Employee Age)
# department (Employee Department)
# salary (Employee Salary)
# Validate Input: Make sure the Employee ID is unique. If it already exists in the dictionary, ask the user to enter a new ID.


# Store the Employee data in the dictionary using the entered emp_id as the key and the other details as values.


# Display a message indicating the employee was successfully added.
def add_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))

        if emp_id in employees:
            print("Employee ID already exists! Please use a unique ID.")
            return

        name = input("Enter Employee Name: ")
        age = int(input("Enter Employee Age: "))
        department = input("Enter Employee Department: ")
        salary = float(input("Enter Employee Salary: "))

        employees[emp_id] = {
            'name': name,
            'age': age,
            'department': department,
            'salary': salary
        }

        print("Employee added successfully ")

    except ValueError:
        print("Invalid input! Please enter correct data types.")



# ===============================================================================
# Step 4 - View All Employees
# Display all employees stored in the dictionary.
# Format the display in a table-like structure, showing employee details (ID, name, age, department, salary).
# If there are no employees in the system, display a message like:
# "No employees available."

def view_employees():
    if not employees:
        print("No employees available.")
        return

    print("\n--- Employee List ---")
    print(f"{'ID':<6}{'Name':<15}{'Age':<6}{'Department':<15}{'Salary'}")
    print("-" * 50)

    for emp_id, details in employees.items():
        print(f"{emp_id:<6}{details['name']:<15}{details['age']:<6}"
              f"{details['department']:<15}{details['salary']}")
        
# ===============================================================================
# Step 5 - Search for an Employee by ID
# Prompt the User to enter the emp_id they want to search for.
# Search the Dictionary:
# If the employee exists, display their details (name, age, department, salary).
# If the employee does not exist, display a message like:
# "Employee not found."

def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))

        if emp_id in employees:
            emp = employees[emp_id]
            print("\nEmployee Found ")
            print(f"Name       : {emp['name']}")
            print(f"Age        : {emp['age']}")
            print(f"Department : {emp['department']}")
            print(f"Salary     : {emp['salary']}")
        else:
            print("Employee not found ")

    except ValueError:
        print("Please enter a valid Employee ID.")


# ===============================================================================
# Step 6 - Exit the Program
# Add an Exit option in the menu.
# If the user chooses Exit, display a thank-you message and exit the program.
main_menu()

# ===============================================================================
# Project Code Structure
# To keep the project organized, break it into functions:
# main_menu(): Displays the main menu and calls the appropriate function based on user input.
# add_employee(): Adds a new employee to the dictionary.
# view_employees(): Displays all employee details.
# search_employee(): Searches for an employee by ID.
