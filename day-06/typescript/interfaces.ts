// Arrays

let departments: string[] = ["IT", "HR", "Finance"];

let salaries: number[] = [50000, 60000, 70000];

console.log("Departments:", departments);
console.log("Salaries:", salaries);


// Object

let employee = {
    id: "E001",
    name: "Mayuri",
    department: "IT",
    salary: 50000
};

console.log("Employee:", employee);


// Interface

interface Employee {
    id: string;
    name: string;
    department: string;
    salary: number;
    email?: string;
}


// Using the interface

let employee1: Employee = {
    id: "E002",
    name: "Riya",
    department: "HR",
    salary: 55000
};

let employee2: Employee = {
    id: "E003",
    name: "Aarav",
    department: "IT",
    salary: 65000,
    email: "aarav@example.com"
};

console.log("Employee 1:", employee1);
console.log("Employee 2:", employee2);