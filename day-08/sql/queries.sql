-- PugArch Day 8 - Required SQL Queries

USE pugarch_day8;

-- 1. SELECT
SELECT * FROM employees;

-- 2. WHERE + ORDER BY
SELECT name, salary
FROM employees
WHERE salary >= 55000
ORDER BY salary DESC;

-- 3. JOIN - employees by department
SELECT e.employee_code, e.name,
       d.name AS department, e.salary
FROM employees e
JOIN departments d ON d.id = e.department_id
ORDER BY d.name, e.name;

-- 4. Employees in a department
SELECT e.name, e.designation, e.salary
FROM employees e
JOIN departments d ON d.id = e.department_id
WHERE d.name = 'Information Technology';

-- 5. Average salary
SELECT d.name AS department,
       AVG(e.salary) AS average_salary
FROM departments d
JOIN employees e ON e.department_id = d.id
GROUP BY d.id, d.name;

-- 6. GROUP BY + HAVING
SELECT d.name AS department,
       AVG(e.salary) AS average_salary
FROM departments d
JOIN employees e ON e.department_id = d.id
GROUP BY d.id, d.name
HAVING AVG(e.salary) > 55000;

-- 7. Highest-paid employee using SUBQUERY
SELECT employee_code, name, salary
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);

-- 8. Poor facilities
SELECT name, location, facility_type, status
FROM facilities
WHERE status IN ('Needs Attention', 'Critical')
ORDER BY status, name;

-- 9. Complaint counts
SELECT f.name AS facility,
       COUNT(c.id) AS complaint_count
FROM facilities f
LEFT JOIN complaints c ON c.facility_id = f.id
GROUP BY f.id, f.name
ORDER BY complaint_count DESC;

-- 10. Inspection history
SELECT f.name AS facility,
       i.inspection_date,
       i.inspector_name,
       i.status,
       i.remarks
FROM facilities f
JOIN inspections i ON i.facility_id = f.id
ORDER BY f.name, i.inspection_date DESC;

-- 11. INSERT
INSERT INTO departments (name, description)
VALUES ('Quality Assurance', 'Software quality management');

-- 12. UPDATE
UPDATE departments
SET description = 'Software and process quality management'
WHERE name = 'Quality Assurance';

-- 13. DELETE
DELETE FROM departments
WHERE name = 'Quality Assurance';

-- 14. TRANSACTION
START TRANSACTION;

UPDATE facilities
SET status = 'Needs Attention'
WHERE id = 1;

INSERT INTO complaints
(facility_id, complainant_name, title, description, priority, status)
VALUES
(1, 'Demo User', 'Transaction Test',
 'Temporary transaction record.', 'Low', 'Open');

COMMIT;

-- Use ROLLBACK instead of COMMIT if the transaction fails.

-- 15. INDEXES
SHOW INDEX FROM employees;
SHOW INDEX FROM inspections;
SHOW INDEX FROM complaints;
