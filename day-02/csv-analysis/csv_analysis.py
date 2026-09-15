import csv
import os

FILE_NAME = os.path.join(os.path.dirname(__file__), "employees.csv")


def read_csv_file():
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)
            records = list(reader)

        return records

    except FileNotFoundError:
        print("CSV file not found.")
        return []

    except OSError:
        print("Error reading CSV file.")
        return []


records = read_csv_file()

print("Total Records:", len(records))

def find_missing_values(records):
    print("\n--- Missing Values ---")

    missing_found = False

    for column in ["id", "name", "department", "salary"]:
        count = 0

        for record in records:
            if not record[column].strip():
                count += 1

        if count > 0:
            print(f"{column}: {count} missing")
            missing_found = True

    if not missing_found:
        print("No missing values found.")


def find_duplicates(records):
    print("\n--- Duplicate Records ---")

    seen = set()
    duplicates = []

    for record in records:
        record_id = record["id"].strip()

        if record_id in seen:
            duplicates.append(record_id)
        else:
            seen.add(record_id)

    if duplicates:
        print("Duplicate IDs:", ", ".join(duplicates))
        print("Number of duplicate records:", len(duplicates))
    else:
        print("No duplicate records found.")

def calculate_salary_statistics(records):
    print("\n--- Salary Statistics ---")

    salaries = []

    for record in records:
        salary = record["salary"].strip()

        if salary:
            try:
                salaries.append(float(salary))
            except ValueError:
                print(f"Invalid salary value: {salary}")

    if not salaries:
        print("No valid salary data available.")
        return

    average_salary = sum(salaries) / len(salaries)
    minimum_salary = min(salaries)
    maximum_salary = max(salaries)

    print("Average Salary:", round(average_salary, 2))
    print("Minimum Salary:", minimum_salary)
    print("Maximum Salary:", maximum_salary)


records = read_csv_file()

print("Total Records:", len(records))

def department_statistics(records):
    print("\n--- Department-wise Statistics ---")

    departments = {}

    for record in records:
        department = record["department"].strip()

        if not department:
            continue

        if department not in departments:
            departments[department] = {
                "count": 0,
                "total_salary": 0
            }

        departments[department]["count"] += 1

        try:
            departments[department]["total_salary"] += float(
                record["salary"]
            )
        except ValueError:
            pass

    for department, data in departments.items():
        average_salary = data["total_salary"] / data["count"]

        print(
            f"{department}: "
            f"{data['count']} employees, "
            f"Average Salary: {round(average_salary, 2)}"
        )

department_statistics(records)







