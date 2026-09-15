import json
import os

FILE_NAME = os.path.join(os.path.dirname(__file__), "employees.json")


def load_employees():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        print("Error reading employee data.")
        return []


def save_employees(employees):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(employees, file, indent=4)

    except OSError:
        print("Error saving employee data.")


employees = load_employees()

print("Employee Management System Started")
print("Total Employees:", len(employees))


def add_employee():
    print("\n--- Add Employee ---")

    emp_id = input("Enter Employee ID: ").strip()

    if not emp_id:
        print("Employee ID cannot be empty.")
        return

    # Check for duplicate ID
    for employee in employees:
        if employee["id"] == emp_id:
            print("Employee ID already exists.")
            return

    name = input("Enter Name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    department = input("Enter Department: ").strip()

    if not department:
        print("Department cannot be empty.")
        return

    while True:
        try:
            salary = float(input("Enter Salary: "))

            if salary < 0:
                print("Salary cannot be negative.")
                continue

            break

        except ValueError:
            print("Invalid salary. Please enter a number.")

    employee = {
        "id": emp_id,
        "name": name,
        "department": department,
        "salary": salary
    }

    employees.append(employee)
    save_employees(employees)

    print("Employee added successfully.")

def update_employee():
    print("\n--- Update Employee ---")

    emp_id = input("Enter Employee ID to update: ").strip()

    for employee in employees:
        if employee["id"] == emp_id:

            print("Employee found.")
            print("Press Enter to keep the existing value.")

            name = input(f"Enter Name [{employee['name']}]: ").strip()
            department = input(
                f"Enter Department [{employee['department']}]: "
            ).strip()

            while True:
                salary_input = input(
                    f"Enter Salary [{employee['salary']}]: "
                ).strip()

                if salary_input == "":
                    break

                try:
                    salary = float(salary_input)

                    if salary < 0:
                        print("Salary cannot be negative.")
                        continue

                    employee["salary"] = salary
                    break

                except ValueError:
                    print("Invalid salary. Please enter a number.")

            if name:
                employee["name"] = name

            if department:
                employee["department"] = department

            save_employees(employees)

            print("Employee updated successfully.")
            return

    print("Employee not found.")

def delete_employee():
    print("\n--- Delete Employee ---")

    emp_id = input("Enter Employee ID to delete: ").strip()

    for employee in employees:
        if employee["id"] == emp_id:

            print("\nEmployee Found")
            print("Name:", employee["name"])
            print("Department:", employee["department"])
            print("Salary:", employee["salary"])

            confirm = input("Are you sure you want to delete? (y/n): ").strip().lower()

            if confirm == "y":
                employees.remove(employee)
                save_employees(employees)
                print("Employee deleted successfully.")
            else:
                print("Deletion cancelled.")

            return

    print("Employee not found.")


def search_employee():
    print("\n--- Search Employee ---")

    keyword = input("Enter Employee ID or Name: ").strip().lower()

    if not keyword:
        print("Search value cannot be empty.")
        return

    found = False

    for employee in employees:
        if (
            keyword in employee["id"].lower()
            or keyword in employee["name"].lower()
        ):
            print("\nEmployee Found")
            print("ID:", employee["id"])
            print("Name:", employee["name"])
            print("Department:", employee["department"])
            print("Salary:", employee["salary"])

            found = True

    if not found:
        print("No matching employee found.")

def filter_employees():
    print("\n--- Filter Employees ---")
    print("1. Filter by Department")
    print("2. Filter by Minimum Salary")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        department = input("Enter Department: ").strip().lower()

        if not department:
            print("Department cannot be empty.")
            return

        filtered = [
            employee
            for employee in employees
            if employee["department"].lower() == department
        ]

    elif choice == "2":
        while True:
            try:
                minimum_salary = float(
                    input("Enter Minimum Salary: ")
                )

                if minimum_salary < 0:
                    print("Salary cannot be negative.")
                    continue

                break

            except ValueError:
                print("Invalid salary. Please enter a number.")

        filtered = [
            employee
            for employee in employees
            if employee["salary"] >= minimum_salary
        ]

    else:
        print("Invalid choice.")
        return

    if not filtered:
        print("No employees match the filter.")
        return

    print("\n--- Filter Results ---")

    for employee in filtered:
        print(
            f"ID: {employee['id']} | "
            f"Name: {employee['name']} | "
            f"Department: {employee['department']} | "
            f"Salary: {employee['salary']}"
        )

def sort_employees():
    print("\n--- Sort Employees ---")
    print("1. Sort by Name")
    print("2. Sort by Salary")

    choice = input("Enter your choice: ").strip()

    if choice not in ["1", "2"]:
        print("Invalid choice.")
        return

    print("\n1. Ascending")
    print("2. Descending")

    order = input("Enter order: ").strip()

    if order not in ["1", "2"]:
        print("Invalid order.")
        return

    reverse = order == "2"

    if choice == "1":
        sorted_employees = sorted(
            employees,
            key=lambda employee: employee["name"].lower(),
            reverse=reverse
        )
    else:
        sorted_employees = sorted(
            employees,
            key=lambda employee: employee["salary"],
            reverse=reverse
        )

    print("\n--- Sorted Employees ---")

    for employee in sorted_employees:
        print(
            f"ID: {employee['id']} | "
            f"Name: {employee['name']} | "
            f"Department: {employee['department']} | "
            f"Salary: {employee['salary']}"
        )

def show_statistics():
    print("\n--- Employee Statistics ---")

    if not employees:
        print("No employee data available.")
        return

    salaries = [employee["salary"] for employee in employees]

    total_employees = len(employees)
    average_salary = sum(salaries) / total_employees
    minimum_salary = min(salaries)
    maximum_salary = max(salaries)

    print("Total Employees:", total_employees)
    print("Average Salary:", round(average_salary, 2))
    print("Minimum Salary:", minimum_salary)
    print("Maximum Salary:", maximum_salary)

    department_stats = {}

    for employee in employees:
        department = employee["department"]

        if department not in department_stats:
            department_stats[department] = {
                "count": 0,
                "total_salary": 0
            }

        department_stats[department]["count"] += 1
        department_stats[department]["total_salary"] += employee["salary"]

    print("\n--- Department Statistics ---")

    for department, stats in department_stats.items():
        average = stats["total_salary"] / stats["count"]

        print(
            f"{department}: "
            f"{stats['count']} employees, "
            f"Average Salary: {round(average, 2)}"
        )



def display_employees():
    print("\n--- All Employees ---")

    if not employees:
        print("No employees available.")
        return

    for employee in employees:
        print(
            f"ID: {employee['id']} | "
            f"Name: {employee['name']} | "
            f"Department: {employee['department']} | "
            f"Salary: {employee['salary']}"
        )





def main():
    while True:
        print("\n=================================")
        print("     Employee Management System")
        print("=================================")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. Search Employee")
        print("5. Filter Employees")
        print("6. Sort Employees")
        print("7. Statistics")
        print("8. Display All Employees")
        print("9. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_employee()

        elif choice == "2":
            update_employee()

        elif choice == "3":
            delete_employee()

        elif choice == "4":
            search_employee()

        elif choice == "5":
            filter_employees()

        elif choice == "6":
            sort_employees()

        elif choice == "7":
            show_statistics()

        elif choice == "8":
            display_employees()

        elif choice == "9":
            print("Exiting Employee Management System.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 9.")


if __name__ == "__main__":
    main()


