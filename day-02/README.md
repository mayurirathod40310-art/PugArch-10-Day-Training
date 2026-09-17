# Day 2 — Python Development

## Objective

Learn Python fundamentals, object-oriented programming, file handling, exception handling, and data processing by building practical applications.

## Problem Statement

The objective of this task is to develop maintainable Python programs and practice working with structured employee data.

The practical work includes an employee management system with JSON storage and a CSV analysis program that calculates useful statistics from employee records.

## Projects

### 1. Employee Management System

A JSON-based employee management system supporting:

* Add Employee
* Update Employee
* Delete Employee
* Search Employee
* Filter Employee
* Sort Employee
* Statistics
* Exception Handling

Employee records are stored in a JSON file.

### 2. CSV Analysis

A Python program that analyzes employee data from a CSV file and reports:

* Total records
* Missing values
* Duplicate records
* Average salary
* Minimum salary
* Maximum salary
* Department-wise statistics

## Python Concepts

* Variables and data types
* Lists, tuples, sets and dictionaries
* Conditions and loops
* Functions
* Lambda functions
* List comprehensions
* Modules
* Exception handling
* File handling
* Classes and objects
* Inheritance
* Encapsulation
* Virtual environments and pip

## Technology Stack

* Python
* JSON
* CSV
* Python Standard Library

## Architecture

### Employee Management System

```text
User
  ↓
Management System
  ↓
Employee Management Functions
  ↓
JSON File
```

### CSV Analysis

```text
CSV File
  ↓
Read Employee Data
  ↓
Data Analysis
  ↓
Statistics and Results
```

## Installation

### Prerequisites

* Python 3.x
* pip
* Git

No external Python libraries are required for the core Day 2 applications.

### Setup

Activate the project's virtual environment before running the programs.

## How to Run

### Employee Management System

Navigate to the management-system directory:

```bash
cd management-system
python management_system.py
```

### CSV Analysis

Navigate to the csv-analysis directory:

```bash
cd csv-analysis
python csv_analysis.py
```

## Challenges Faced

* Handling employee records stored in JSON format.
* Implementing multiple management operations.
* Handling invalid input and exceptions.
* Reading and analyzing structured CSV data.
* Calculating department-wise statistics.

## Solutions

* Used JSON file handling for employee data storage.
* Implemented separate functions for different management operations.
* Added exception handling for invalid operations and input.
* Used Python's CSV handling capabilities to process employee data.
* Applied basic data-processing techniques to calculate required statistics.

## Future Improvements

* Add automated tests.
* Improve input validation.
* Add a graphical or web-based interface.
* Add more advanced employee analytics.
* Improve data persistence and validation.

## Project Structure

```text
day-02/
├── python-exercises/
│   ├── basics.py
│   └── helper.py
├── management-system/
│   ├── management_system.py
│   └── employees.json
├── csv-analysis/
│   ├── csv_analysis.py
│   └── employees.csv
└── README.md
```

## Git & GitHub

The completed Day 2 work was committed and pushed to the GitHub repository as part of the PugArch 10-Day Training.



