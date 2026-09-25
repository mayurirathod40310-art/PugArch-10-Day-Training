// Type Alias

type EmployeeID = string | number;

let id1: EmployeeID = "E001";
let id2: EmployeeID = 101;


// Union Type

let employeeStatus: "Active" | "Inactive" = "Active";

console.log("Employee ID:", id1);
console.log("Employee Status:", employeeStatus);


// Enum

enum Department {
    IT = "IT",
    HR = "HR",
    Finance = "Finance",
    Sales = "Sales"
}

let employeeDepartment: Department = Department.IT;

console.log("Department:", employeeDepartment);


// Function

function calculateAnnualSalary(monthlySalary: number): number {
    return monthlySalary * 12;
}

console.log("Annual Salary:", calculateAnnualSalary(50000));


// Function with optional parameter

function greetEmployee(name: string, department?: string): string {
    if (department) {
        return `Hello ${name}, you work in ${department}.`;
    }

    return `Hello ${name}.`;
}

console.log(greetEmployee("Mayuri", "IT"));
console.log(greetEmployee("Riya"));