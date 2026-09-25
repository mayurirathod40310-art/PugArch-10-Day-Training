USE pugarch_day8;

INSERT INTO departments (id, name, description) VALUES
(1, 'Information Technology', 'Technology and software systems'),
(2, 'Human Resources', 'People and administration'),
(3, 'Finance', 'Finance and accounts'),
(4, 'Operations', 'Campus operations and services');

INSERT INTO employees
(id, employee_code, name, email, department_id, salary, designation)
VALUES
(1, 'E001', 'Mayuri Rathod', 'mayuri@example.com', 1, 50000.00, 'Software Engineer'),
(2, 'E002', 'Riya Sharma', 'riya@example.com', 2, 55000.00, 'HR Executive'),
(3, 'E003', 'Aarav Patil', 'aarav@example.com', 3, 65000.00, 'Finance Analyst'),
(4, 'E004', 'Sneha Kulkarni', 'sneha@example.com', 1, 60000.00, 'Software Developer'),
(5, 'E005', 'Rahul Deshmukh', 'rahul@example.com', 4, 52000.00, 'Operations Executive');

INSERT INTO facilities
(id, name, location, facility_type, status, description)
VALUES
(1, 'Computer Laboratory 1', 'Block A - First Floor', 'Laboratory', 'Needs Attention', 'Main student computer laboratory'),
(2, 'Central Library', 'Academic Block - Ground Floor', 'Library', 'Good', 'Central academic library'),
(3, 'College Canteen', 'Block B - Ground Floor', 'Food Service', 'Critical', 'Student and staff canteen'),
(4, 'Seminar Hall', 'Main Building - Second Floor', 'Hall', 'Good', 'Large seminar and event hall');

INSERT INTO inspections
(id, facility_id, inspection_date, inspector_name, status, remarks)
VALUES
(1, 1, '2026-09-20', 'Anita Joshi', 'Needs Improvement', 'Several systems need maintenance'),
(2, 2, '2026-09-21', 'Vivek Shah', 'Passed', 'Facility is well maintained'),
(3, 3, '2026-09-22', 'Anita Joshi', 'Failed', 'Cleanliness and maintenance issues found'),
(4, 4, '2026-09-23', 'Vivek Shah', 'Passed', 'Safety checks completed successfully');

INSERT INTO complaints
(id, facility_id, complainant_name, title, description, priority, status)
VALUES
(1, 1, 'Mayuri Rathod', 'System maintenance', 'Multiple systems require maintenance.', 'Medium', 'Open'),
(2, 2, 'Riya Sharma', 'Library lighting', 'A few lights need replacement.', 'Low', 'In Progress'),
(3, 3, 'Aarav Patil', 'Canteen cleanliness', 'Cleaning standards need immediate improvement.', 'High', 'Open'),
(4, 4, 'Sneha Kulkarni', 'Projector issue', 'Projector occasionally loses signal.', 'Medium', 'Resolved');
