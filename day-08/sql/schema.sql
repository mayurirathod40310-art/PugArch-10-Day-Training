-- PugArch Day 8 - Database Schema
-- MySQL 8+

CREATE DATABASE IF NOT EXISTS pugarch_day8;
USE pugarch_day8;

CREATE TABLE departments (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    description VARCHAR(255) NULL,
    created_at TIMESTAMP NULL,
    updated_at TIMESTAMP NULL
);

CREATE TABLE employees (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    employee_code VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    department_id BIGINT UNSIGNED NOT NULL,
    salary DECIMAL(10,2) NOT NULL,
    designation VARCHAR(255) NULL,
    created_at TIMESTAMP NULL,
    updated_at TIMESTAMP NULL,
    FOREIGN KEY (department_id) REFERENCES departments(id)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE facilities (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    facility_type VARCHAR(255) NOT NULL,
    status ENUM('Good','Needs Attention','Critical') DEFAULT 'Good',
    description TEXT NULL,
    created_at TIMESTAMP NULL,
    updated_at TIMESTAMP NULL
);

CREATE TABLE inspections (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    facility_id BIGINT UNSIGNED NOT NULL,
    inspection_date DATE NOT NULL,
    inspector_name VARCHAR(255) NOT NULL,
    status ENUM('Passed','Failed','Needs Improvement') NOT NULL,
    remarks TEXT NULL,
    created_at TIMESTAMP NULL,
    updated_at TIMESTAMP NULL,
    FOREIGN KEY (facility_id) REFERENCES facilities(id)
        ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE complaints (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    facility_id BIGINT UNSIGNED NOT NULL,
    complainant_name VARCHAR(255) NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    priority ENUM('Low','Medium','High') DEFAULT 'Medium',
    status ENUM('Open','In Progress','Resolved') DEFAULT 'Open',
    created_at TIMESTAMP NULL,
    updated_at TIMESTAMP NULL,
    FOREIGN KEY (facility_id) REFERENCES facilities(id)
        ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE INDEX idx_employees_department_id ON employees(department_id);
CREATE INDEX idx_inspections_facility_date ON inspections(facility_id, inspection_date);
CREATE INDEX idx_complaints_facility_status ON complaints(facility_id, status);
