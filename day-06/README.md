# Day 6 — TypeScript and React Employee Management Dashboard

## Project Overview

A component-based Employee Management Dashboard built using TypeScript and React. The application allows users to manage employee records, view dashboard statistics, search and filter employees, sort salaries, and fetch API data.

## Problem Statement

Organizations need a simple interface to manage employee information and quickly view important employee statistics such as total employees, average salary, and departments.

This project demonstrates how TypeScript and React can be used to build a structured, reusable, and interactive dashboard.

## Features

- Display total employees
- Calculate average salary
- Display number of departments
- Add new employees
- Edit existing employees
- Delete employees
- Search employees by name
- Filter employees by department
- Sort employees by salary
- View employee details
- Form validation
- Reusable React components
- Custom API hook using `useApi`
- Fetch and display external API data
- Responsive dashboard design

## Technology Stack

- React
- TypeScript
- Vite
- HTML5
- CSS3
- JavaScript
- JSONPlaceholder API
- ESLint

## Architecture

The application follows a component-based React architecture.

```text
react-app/
├── src/
│   ├── components/
│   │   ├── Dashboard.tsx
│   │   ├── EmployeeList.tsx
│   │   ├── EmployeeForm.tsx
│   │   └── ApiDemo.tsx
│   ├── hooks/
│   │   └── useApi.ts
│   ├── types.ts
│   ├── data.ts
│   ├── App.tsx
│   ├── main.tsx
│   └── index.css
├── public/
├── package.json
└── vite.config.ts
```

### Main Components

- **App:** Manages application state and coordinates components.
- **Dashboard:** Displays employee statistics.
- **EmployeeForm:** Handles adding and editing employees.
- **EmployeeList:** Displays employee records and actions.
- **ApiDemo:** Demonstrates API integration.
- **useApi:** Custom generic hook for fetching API data.

## Database Design

No database is used in this project.

Employee records are stored in React state using sample data. Therefore, changes are temporary and reset when the page is refreshed.

## API Documentation

### External API

**Endpoint:**

```text
https://jsonplaceholder.typicode.com/users
```

**Method:** `GET`

**Purpose:** Fetch sample user data for demonstrating API integration.

### Response Fields Used

- `id`
- `name`
- `email`

## Installation

Clone the repository and navigate to the React application folder:

```bash
cd day-06/react-app
```

Install dependencies:

```bash
npm install
```

## Environment Variables

No environment variables are required for this project.

## How to Run

Start the development server:

```bash
npm run dev
```

Open the local URL displayed in the terminal, usually:

```text
http://localhost:5173/
```

## Screenshots

Add screenshots of the following after capturing them:

- Dashboard overview
- Add/Edit employee form
- Employee list
- Search and filter functionality
- API integration section

## Challenges Faced

1. Understanding TypeScript types and interfaces.
2. Passing data and functions between React components.
3. Managing employee records using React state.
4. Implementing a reusable custom API hook.
5. Resolving a default export issue in the `useApi` hook.
6. Applying CSS styling consistently across components.

## Solutions

1. Defined reusable `Employee` interfaces in `types.ts`.
2. Used typed props for communication between components.
3. Used `useState` to manage employee data and UI state.
4. Created a generic `useApi<T>` hook for API requests.
5. Added the correct default export for the custom hook.
6. Added meaningful CSS classes and responsive styling.

## Future Improvements

- Add a backend API
- Store employee data in a database
- Add user authentication
- Persist data using localStorage or a database
- Add pagination
- Add advanced form validation
- Add charts and analytics
- Deploy the application online

## Learning Outcomes

- TypeScript interfaces, type aliases, unions, enums, generics, and type guards
- React components and JSX
- Props and state management
- Event handling and forms
- Conditional rendering
- List rendering
- Custom React hooks
- API integration
- Responsive CSS styling

