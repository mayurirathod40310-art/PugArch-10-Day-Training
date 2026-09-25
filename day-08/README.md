# PugArch Day 8 - Database + Laravel API

## Project Overview
A relational database and REST API project for employee and smart facility management using Laravel and Eloquent ORM.

## Problem Statement
The project provides structured management of departments, employees, facilities, inspections, and complaints while maintaining database relationships, validation, and reusable REST APIs.

## Features
- Relational database design
- Primary and foreign keys
- One-to-many Eloquent relationships
- CRUD APIs for departments, employees, facilities, inspections and complaints
- Request validation with HTTP 422 responses
- JSON REST API responses
- Database seeding
- SQL JOIN, GROUP BY, HAVING and subquery examples
- Database indexes
- Transaction example

## Technology Stack
- PHP 8.4
- Laravel 13
- Eloquent ORM
- SQLite for verified local runtime
- MySQL-compatible SQL scripts
- REST API
- PowerShell

## Architecture
Client → API Route → Controller → Eloquent Model → Database → JSON Response

## Database Design
- Department 1 → N Employee
- Facility 1 → N Inspection
- Facility 1 → N Complaint

## API Documentation
Base URL:
`http://127.0.0.1:8000/api`

CRUD resources:
- `/departments`
- `/employees`
- `/facilities`
- `/inspections`
- `/complaints`

Each supports:
- GET collection
- POST
- GET by ID
- PUT/PATCH
- DELETE

## Installation

```powershell
cd laravel-api
composer install
php artisan migrate:fresh --seed
Environment Variables

The verified local project uses SQLite:

DB_CONNECTION=sqlite

Do not commit a personal .env file or real credentials.

How to Run
cd laravel-api
php artisan serve

Test the API:

Invoke-RestMethod http://127.0.0.1:8000/api/employees | ConvertTo-Json -Depth 5
Testing Completed
GET employees — PASS
GET departments — PASS
GET facilities — PASS
POST employee — PASS
Invalid POST validation HTTP 422 — PASS
PUT employee — PASS
DELETE employee — PASS
Department relationship — PASS
Inspection relationship — PASS
Complaint relationship — PASS
Screenshots

Screenshots can be added here if required.

Challenges Faced
Laravel API setup
Migration ordering
Foreign-key relationships
PowerShell API testing
OneDrive project-file issues
Solutions

The Laravel project was rebuilt in a clean Desktop directory, migrations were recreated in dependency order, the database was seeded, relationships were tested, and the major CRUD and validation API flows were verified before packaging.

Future Improvements
API authentication
Role-based authorization
Pagination and filtering
Automated tests
React/Next.js frontend
Angular frontend integration
MySQL/PostgreSQL production database
Production deployment
Project Structure
day-08/
├── sql/
│   ├── schema.sql
│   ├── sample_data.sql
│   └── queries.sql
├── database/
│   └── README.md
├── laravel-api/
└── README.md

