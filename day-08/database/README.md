# Database Notes

The Laravel runtime is verified with SQLite for portability.

The SQL scripts in `../sql` provide a MySQL-compatible schema, sample data and practice queries covering CRUD, joins, grouping, subqueries, indexes and transactions.

## Relationships

- Department has many Employees.
- Employee belongs to Department.
- Facility has many Inspections.
- Facility has many Complaints.
- Inspection belongs to Facility.
- Complaint belongs to Facility.
