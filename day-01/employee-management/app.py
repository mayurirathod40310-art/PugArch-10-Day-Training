employees = []


def add_employee():
    print("\n--- Add New Employee ---")

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    department = input("Enter Department: ")

    while True:
        try:
            salary = float(input("Enter Salary: "))

            if salary < 0:
                print("Salary cannot be negative.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    employee = {
        "id": emp_id,
        "name": name,
        "department": department,
        "salary": salary
    }

    employees.append(employee)

    print("Employee added successfully!")


def view_employees():
    print("\n--- Employee List ---")

    if not employees:
        print("No employees found.")
        return

    for employee in employees:
        print(
            f"ID: {employee['id']} | "
            f"Name: {employee['name']} | "
            f"Department: {employee['department']} | "
            f"Salary: {employee['salary']}"
        )


def update_employee():
    print("\n--- Update Employee ---")

    emp_id = input("Enter Employee ID to update: ")

    for employee in employees:
        if employee["id"] == emp_id:
            print("Enter new details (leave blank to keep current):")

            name = input(f"New Name ({employee['name']}): ")
            department = input(
                f"New Department ({employee['department']}): "
            )
            salary = input(f"New Salary ({employee['salary']}): ")

            if name != "":
                employee["name"] = name

            if department != "":
                employee["department"] = department

            if salary != "":
                try:
                    new_salary = float(salary)

                    if new_salary < 0:
                        print("Salary cannot be negative.")
                        return

                    employee["salary"] = new_salary

                except ValueError:
                    print("Please enter a valid salary.")
                    return

            print("Employee updated successfully!")
            return

    print("Employee not found.")


def delete_employee():
    print("\n--- Delete Employee ---")

    emp_id = input("Enter Employee ID to delete: ")

    for employee in employees:
        if employee["id"] == emp_id:
            employees.remove(employee)
            print("Employee deleted successfully!")
            return

    print("Employee not found.")


def search_employee():
    print("\n--- Search Employee ---")

    emp_id = input("Enter Employee ID to search: ")

    for employee in employees:
        if employee["id"] == emp_id:
            print("\nEmployee Found!")
            print(f"ID: {employee['id']}")
            print(f"Name: {employee['name']}")
            print(f"Department: {employee['department']}")
            print(f"Salary: {employee['salary']}")
            return

    print("Employee not found.")


def highest_salary():
    print("\n--- Highest Salary Employee ---")

    if not employees:
        print("No employees found.")
        return

    highest = employees[0]

    for employee in employees:
        if employee["salary"] > highest["salary"]:
            highest = employee

    print(f"ID: {highest['id']}")
    print(f"Name: {highest['name']}")
    print(f"Department: {highest['department']}")
    print(f"Salary: {highest['salary']}")


def average_salary():
    print("\n--- Average Salary ---")

    if not employees:
        print("No employees found.")
        return

    total = 0

    for employee in employees:
        total = total + employee["salary"]

    average = total / len(employees)

    print(f"Average Salary: {average:.2f}")


def department_filter():
    print("\n--- Department Filter ---")

    department = input("Enter Department: ").strip().lower()

    found = False

    for employee in employees:
        if employee["department"].strip().lower() == department:
            print(
                f"ID: {employee['id']} | "
                f"Name: {employee['name']} | "
                f"Salary: {employee['salary']}"
            )
            found = True

    if not found:
        print("No employees found in this department.")


while True:
    print("\n=== Employee Management System ===")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Update Employee")
    print("4. Search Employee")
    print("5. Delete Employee")
    print("6. Highest Salary")
    print("7. Average Salary")
    print("8. Department Filter")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        update_employee()

    elif choice == "4":
        search_employee()

    elif choice == "5":
        delete_employee()

    elif choice == "6":
        highest_salary()

    elif choice == "7":
        average_salary()

    elif choice == "8":
        department_filter()

    elif choice == "9":
        print("Exiting application. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 9.")
        
