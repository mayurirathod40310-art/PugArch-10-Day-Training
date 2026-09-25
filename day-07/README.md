# Employee Management System

A full-stack Employee Management System built using **Next.js, TypeScript, Node.js, and Express.js**. The application provides a modern dashboard for viewing employee information and communicates with a REST API for employee data operations.

---

## 1. Project Overview

The Employee Management System is a full-stack web application designed to manage and display employee information.

The frontend is developed using **Next.js and TypeScript**, while the backend is built using **Node.js and Express.js**. The frontend communicates with the backend through REST APIs.

The application allows users to view employees, view individual employee details, and create new employees.

---

## 2. Problem Statement

Develop a full-stack employee management application with a separate frontend and backend.

The system should provide a user-friendly interface for displaying employee information and should communicate with a backend REST API for employee data operations.

---

## 3. Features

### Frontend Features

- Employee dashboard
- Display total number of employees
- Calculate average salary
- Display number of departments
- View all employees
- View individual employee details
- Create new employee
- Dynamic employee routes
- Responsive user interface
- API integration
- Environment variable based API configuration

### Backend Features

- REST API using Express.js
- Get all employees
- Get employee by ID
- Create employee
- Update employee
- Delete employee
- CORS support
- JSON request handling
- Route and controller separation

---

## 4. Technology Stack

### Frontend

- Next.js
- React
- TypeScript
- Tailwind CSS

### Backend

- Node.js
- Express.js
- JavaScript
- REST API

### Development Tools

- Visual Studio Code
- npm
- Git
- GitHub

---

## 5. Architecture

The application follows a **client-server architecture**.

```text
                 Employee Management System
                           |
             +-------------+-------------+
             |                           |
             v                           v
      Next.js Frontend             Express Backend
             |                           |
             |       HTTP Requests       |
             +------------->-------------+
                                         |
                                         v
                                Employee Model
                                (In-Memory Data)

# Frontend Structure
nextjs-app/
│
├── app/
│   ├── employees/
│   │   ├── [id]/
│   │   │   └── page.tsx
│   │   │
│   │   ├── create/
│   │   │   └── page.tsx
│   │   │
│   │   └── page.tsx
│   │
│   ├── data.ts
│   └── types.ts
│
├── .env.local
├── package.json
└── tsconfig.json

##Backend Structure 
node-api/
│
├── controllers/
│   └── employeeController.js
│
├── models/
│   └── employeeModel.js
│
├── routes/
│   └── employeeRoutes.js
│
├── index.js
└── package.json

 ## Backend Request Flow
 Client Request
      ↓
Express Route
      ↓
Controller
      ↓
Employee Model
      ↓
JSON Response

6. Application Pages
Employee Dashboard

Route: /employees

The dashboard displays:

Total employees
Average salary
Number of departments
Employee cards
Employee department
Salary
Email
View Details option
Add Employee option
Employee Details

Route: /employees/[id]

Displays detailed information about a selected employee.

Example:

/employees/E001

Create Employee

Route: /employees/create

Provides a form for creating a new employee.

The form sends employee data to the backend using the POST API.

7. API Documentation

Base URL
http://localhost:5000


Method	Endpoint	Description
GET	/employees	Get all employees
GET	/employees/:id	Get employee by ID
POST	/employees	Create a new employee
PUT	/employees/:id	Update an employee
DELETE	/employees/:id	Delete an employee

GET All Employees

GET /employees

Returns the list of all employees.

GET Employee by ID
GET /employees/E001

Returns the employee with the specified ID.

POST Create Employee


POST /employees

Example request body:

{
  "name": "Karan",
  "department": "IT",
  "salary": 60000,
  "email": "karan@example.com"
}


PUT Update Employee
PUT /employees/E001

Example request body:

{
  "name": "Mayuri",
  "department": "IT",
  "salary": 55000,
  "email": "mayuri@example.com"
}


DELETE Employee

DELETE /employees/E005

Deletes the employee with the specified ID.

8. Environment Variables

The frontend uses an environment variable to configure the backend API URL.

Create:

.env.local

inside the nextjs-app folder.

Add:

NEXT_PUBLIC_API_URL=http://localhost:5000

This allows the backend URL to be configured without directly hardcoding it into the application.

9. Installation

Clone the Repository
git clone <https://github.com/mayurirathod40310-art/PugArch-10-Day-Training>

Navigate to the project:

cd PugArch-10-Day-Training
Install Backend Dependencies

cd day-07/node-api
npm install

Install Frontend Dependencies

Open another terminal:

cd day-07/nextjs-app
npm install


10. How to Run
Start the Backend
cd day-07/node-api
node index.js

The backend will run at:

http://localhost:5000
Start the Frontend

Open another terminal:

cd day-07/nextjs-app
npm run dev

The frontend will run at:

http://localhost:3000

Open:

http://localhost:3000/employees


https://github.com/mayurirathod40310-art/PugArch-10-Day-Training

12. Testing

The following operations were tested:

GET all employees
GET employee by ID
POST new employee
PUT employee details
DELETE employee
Frontend-to-backend API communication
Dynamic employee routing
Create employee form
Environment variable based API connection

The following frontend pages were also tested:

http://localhost:3000/employees
http://localhost:3000/employees/E001
http://localhost:3000/employees/create


13. Challenges Faced
1. PowerShell Execution Policy

PowerShell initially prevented npm commands from running.

2. CORS Configuration

The frontend and backend were running on different ports, requiring CORS configuration.

3. Backend Connection

The frontend displayed a connection error when the Express backend was not running.

4. Dynamic Routing

The employee details page required the correct Next.js [id] dynamic route structure.

5. API Configuration

The backend URL was configured using an environment variable instead of hardcoding it.

6. UI Readability

Text colors and layouts were adjusted to improve readability and presentation.

14. Solutions
Used a process-level PowerShell execution policy to allow npm commands.
Installed and configured the cors package.
Kept the Express backend running while testing the frontend.
Implemented dynamic routing using [id].
Added .env.local for API configuration.
Used Tailwind CSS for styling and responsive layouts.
Tested backend endpoints separately before frontend integration.


15. Limitations
Employee data is stored in memory.
Data is reset when the backend server restarts.
Authentication is not implemented.
Frontend update and delete controls are not implemented.
Backend validation is basic.

16. Future Improvements
Integrate MongoDB or PostgreSQL.
Add complete frontend CRUD operations.
Implement authentication and authorization.
Add stronger backend validation.
Add loading and error states.
Add search, filtering, and sorting.
Add pagination for large datasets.
Deploy the application to production.


17. Learning Outcomes

The project demonstrates practical implementation of:

Next.js App Router
Dynamic routes
React components
TypeScript
Server-side data fetching
Node.js
Express.js
REST API development
Routing and controllers
CORS
Environment variables
Frontend-backend integration
Git and GitHub


18. Conclusion

The Employee Management System demonstrates a basic full-stack web application using Next.js and Express.js.

The Next.js frontend communicates with the Express REST API to retrieve and manage employee data. The backend follows a structured route-controller-model architecture, providing a foundation for future database integration, authentication, and complete CRUD functionality.

