<?php

namespace Database\Seeders;

use App\Models\Complaint;
use App\Models\Department;
use App\Models\Employee;
use App\Models\Facility;
use App\Models\Inspection;
use Illuminate\Database\Seeder;

class DayEightSeeder extends Seeder
{
    public function run(): void
    {
        // Departments
        $it = Department::create([
            'name' => 'Information Technology',
            'description' => 'Technology and software development department',
        ]);

        $hr = Department::create([
            'name' => 'Human Resources',
            'description' => 'Employee management and administration',
        ]);

        $finance = Department::create([
            'name' => 'Finance',
            'description' => 'Financial planning and accounting',
        ]);

        $operations = Department::create([
            'name' => 'Operations',
            'description' => 'Facility and operational management',
        ]);

        // Employees
        Employee::create([
            'employee_code' => 'E001',
            'name' => 'Mayuri Rathod',
            'email' => 'mayuri@example.com',
            'department_id' => $it->id,
            'salary' => 50000,
            'designation' => 'Software Developer',
        ]);

        Employee::create([
            'employee_code' => 'E002',
            'name' => 'Riya Sharma',
            'email' => 'riya@example.com',
            'department_id' => $hr->id,
            'salary' => 55000,
            'designation' => 'HR Executive',
        ]);

        Employee::create([
            'employee_code' => 'E003',
            'name' => 'Aarav Patil',
            'email' => 'aarav@example.com',
            'department_id' => $finance->id,
            'salary' => 65000,
            'designation' => 'Financial Analyst',
        ]);

        Employee::create([
            'employee_code' => 'E004',
            'name' => 'Sneha Kulkarni',
            'email' => 'sneha@example.com',
            'department_id' => $it->id,
            'salary' => 60000,
            'designation' => 'System Engineer',
        ]);

        Employee::create([
            'employee_code' => 'E005',
            'name' => 'Rahul Deshmukh',
            'email' => 'rahul@example.com',
            'department_id' => $operations->id,
            'salary' => 52000,
            'designation' => 'Operations Executive',
        ]);

        // Facilities
        $computerLab = Facility::create([
            'name' => 'Computer Laboratory 1',
            'location' => 'Block A - First Floor',
            'facility_type' => 'Laboratory',
            'status' => 'Good',
            'description' => 'Main computer laboratory with desktop systems.',
        ]);

        $library = Facility::create([
            'name' => 'Central Library',
            'location' => 'Block B - Ground Floor',
            'facility_type' => 'Library',
            'status' => 'Needs Attention',
            'description' => 'Central academic library.',
        ]);

        $canteen = Facility::create([
            'name' => 'College Canteen',
            'location' => 'Block C - Ground Floor',
            'facility_type' => 'Canteen',
            'status' => 'Critical',
            'description' => 'Student food and refreshment facility.',
        ]);

        $seminarHall = Facility::create([
            'name' => 'Seminar Hall',
            'location' => 'Block A - Second Floor',
            'facility_type' => 'Seminar Hall',
            'status' => 'Good',
            'description' => 'Hall used for seminars and technical events.',
        ]);

        // Inspections
        Inspection::create([
            'facility_id' => $computerLab->id,
            'inspection_date' => '2026-09-20',
            'inspector_name' => 'Admin Team',
            'status' => 'Passed',
            'remarks' => 'Computers and electrical systems are working properly.',
        ]);

        Inspection::create([
            'facility_id' => $library->id,
            'inspection_date' => '2026-09-21',
            'inspector_name' => 'Maintenance Team',
            'status' => 'Needs Improvement',
            'remarks' => 'Lighting and ventilation require improvement.',
        ]);

        Inspection::create([
            'facility_id' => $canteen->id,
            'inspection_date' => '2026-09-22',
            'inspector_name' => 'Health & Safety Team',
            'status' => 'Failed',
            'remarks' => 'Cleanliness and waste management require immediate attention.',
        ]);

        Inspection::create([
            'facility_id' => $seminarHall->id,
            'inspection_date' => '2026-09-23',
            'inspector_name' => 'Admin Team',
            'status' => 'Passed',
            'remarks' => 'Facility is maintained properly.',
        ]);

        // Complaints
        Complaint::create([
            'facility_id' => $computerLab->id,
            'complainant_name' => 'Amit',
            'title' => 'Computer not working',
            'description' => 'One desktop system is not starting.',
            'priority' => 'Medium',
            'status' => 'In Progress',
        ]);

        Complaint::create([
            'facility_id' => $library->id,
            'complainant_name' => 'Priya',
            'title' => 'Poor ventilation',
            'description' => 'The library needs better ventilation.',
            'priority' => 'High',
            'status' => 'Open',
        ]);

        Complaint::create([
            'facility_id' => $canteen->id,
            'complainant_name' => 'Karan',
            'title' => 'Cleanliness issue',
            'description' => 'Canteen area requires immediate cleaning.',
            'priority' => 'High',
            'status' => 'Open',
        ]);

        Complaint::create([
            'facility_id' => $seminarHall->id,
            'complainant_name' => 'Neha',
            'title' => 'Projector issue',
            'description' => 'Projector display is not working correctly.',
            'priority' => 'Low',
            'status' => 'Resolved',
        ]);
    }
}

