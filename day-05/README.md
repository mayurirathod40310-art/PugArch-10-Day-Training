# Day 5 — JavaScript

## Project Overview

This assignment focuses on modern JavaScript, asynchronous programming, APIs, and building an interactive Employee Dashboard using JavaScript.

## Problem Statement

Build an Employee Dashboard that consumes employee data from a REST API and provides listing, searching, filtering, sorting, viewing details, adding, editing, and deleting employees.

## Features

### JavaScript Practice

* Variables using `let` and `const`
* Functions and arrow functions
* Arrays and objects
* Destructuring
* Spread and rest operators
* Template literals
* Array methods: `map`, `filter`, `reduce`, `find`, `some`, `every`, `sort`
* Scope, closures, and error handling
* Callbacks, Promises, and `async/await`

### Employee Dashboard

* Fetch employee data
* Display employee cards
* Search employees
* Filter by department
* Sort by name
* Sort by salary
* View employee details
* Add employee
* Edit employee
* Delete employee

## Technology Stack

* HTML5
* CSS3
* JavaScript (ES6+)
* Fetch API
* JSON
* REST API
* Node.js

## Architecture

```text
Employee Dashboard
│
├── index.html
│   └── Dashboard UI
│
├── style.css
│   └── Dashboard styling
│
└── script.js
    ├── GET employee data
    ├── POST new employee
    ├── PUT employee updates
    ├── DELETE employee
    ├── Search
    ├── Filter
    └── Sort
```

JavaScript practice files are maintained separately in the `javascript` folder.

## Database Design

Not applicable.

The project uses JSON data through a REST API and does not use a database.

## API Documentation

Base API:

`https://jsonplaceholder.typicode.com/users`

| Method | Purpose            |
| ------ | ------------------ |
| GET    | Fetch employees    |
| POST   | Add an employee    |
| PUT    | Update an employee |
| DELETE | Delete an employee |

JSONPlaceholder is used as a testing REST API. POST, PUT, and DELETE requests are simulated and are not permanently stored on the server.

## Installation

1. Open the project in VS Code.
2. Make sure Node.js is installed.
3. The JavaScript practice files can be executed using Node.js.
4. Open the Employee Dashboard using VS Code Live Server.

## Environment Variables

No environment variables are required.

## How to Run

### JavaScript Practice

From the project root:

```bash
node day-05/javascript/basics.js
```

```bash
node day-05/javascript/async-api.js
```

### Employee Dashboard

Open:

```text
day-05/employee-dashboard/index.html
```

using VS Code Live Server.

## Screenshots

Screenshots of the Employee Dashboard can be added here after completing the final UI verification.

## Challenges Faced

* Understanding asynchronous JavaScript.
* Working with API responses using `fetch()`.
* Implementing CRUD operations using HTTP methods.
* Combining search, filtering, and sorting.

## Solutions

* Used Promises and `async/await` for asynchronous operations.
* Used `response.json()` to process API data.
* Used GET, POST, PUT, and DELETE requests with the Fetch API.
* Used reusable JavaScript functions for dashboard operations.

## Future Improvements

* Add persistent database storage.
* Replace prompt-based forms with proper HTML forms or modals.
* Add user authentication.
* Add pagination.
* Improve dashboard UI and responsiveness.
* Connect the application to a real backend API.

