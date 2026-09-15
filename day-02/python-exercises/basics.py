# # Exercise 1: Python Collections

# # List
employees = ["Amit", "Sneha", "Rahul", "Priya"]
print("Employees:", employees)

# # Tuple
departments = ("IT", "HR", "Finance", "Marketing")
print("Departments:", departments)

# # Set
skills = {"Python", "SQL", "Python", "Excel"}
print("Skills:", skills)

# # Dictionary
employee = {
    "id": 101,
    "name": "Amit",
    "department": "IT",
    "salary": 35000
}

print("Employee:", employee)
print("Employee Name:", employee["name"])
print("Employee Salary:", employee["salary"])

# # Exercise 2: Conditions and Loops

employees = [
    {"name": "Amit", "salary": 35000},
    {"name": "Sneha", "salary": 45000},
    {"name": "Rahul", "salary": 28000},
    {"name": "Priya", "salary": 55000}
]

# Check salary category
for employee in employees:
    if employee["salary"] >= 50000:
        print(employee["name"], "- High Salary")
    elif employee["salary"] >= 30000:
        print(employee["name"], "- Medium Salary")
    else:
        print(employee["name"], "- Low Salary")

# # Exercise 3: Functions

def calculate_bonus(salary, bonus_percentage):
    bonus = salary * bonus_percentage / 100
    return bonus


salary = 40000
bonus = calculate_bonus(salary, 10)

print("Salary:", salary)
print("Bonus:", bonus)
print("Total Salary:", salary + bonus)

# Exercise 4: Lambda

square = lambda number: number * number

print("Square of 5:", square(5))
print("Square of 10:", square(10))

# Exercise 5: List Comprehension

salaries = [25000, 32000, 45000, 28000, 55000]

high_salaries = [salary for salary in salaries if salary >= 40000]

print("All Salaries:", salaries)
print("High Salaries:", high_salaries)

# Exercise 6: Modules

import helper

message = helper.greet("Mayuri")
total_salary = helper.calculate_total_salary(40000, 5000)

print(message)
print("Total Salary:", total_salary)

import helper

# Exercise 7: Exception Handling

try:
    salary = float(input("Enter employee salary: "))
    print("Salary:", salary)

except ValueError:
    print("Invalid input! Please enter a valid number.")


# Exercise 8: File Handling

employee_data = "Employee ID: 101, Name: Amit, Department: IT"

# Write data to a file
with open("employee.txt", "w") as file:
    file.write(employee_data)

print("Employee data written successfully.")

# Read data from the file
with open("employee.txt", "r") as file:
    data = file.read()

print("Employee Data:", data)

# Exercise 9: Classes and Objects

class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def display_details(self):
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)


employee1 = Employee("Amit", "IT", 40000)

employee1.display_details()

# Exercise 10: Inheritance and Encapsulation

class Manager(Employee):
    def __init__(self, name, department, salary, team_size):
        super().__init__(name, department, salary)
        self.__team_size = team_size

    def display_manager_details(self):
        self.display_details()
        print("Team Size:", self.__team_size)


manager1 = Manager("Sneha", "IT", 60000, 8)

manager1.display_manager_details()

