"use strict";
// Class
class EmployeeRecord {
    constructor(id, name, salary) {
        this.id = id;
        this.name = name;
        this.salary = salary;
    }
    getAnnualSalary() {
        return this.salary * 12;
    }
}
const emp = new EmployeeRecord("E001", "Mayuri", 50000);
console.log("Employee:", emp.name);
console.log("Annual Salary:", emp.getAnnualSalary());
// Generic Function
function getFirstItem(items) {
    return items[0];
}
const firstEmployee = getFirstItem(["Mayuri", "Riya", "Aarav"]);
const firstSalary = getFirstItem([50000, 60000, 70000]);
console.log("First Employee:", firstEmployee);
console.log("First Salary:", firstSalary);
// Union + Type Narrowing
function displayEmployeeValue(value) {
    if (typeof value === "string") {
        console.log("Employee Name:", value.toUpperCase());
    }
    else {
        console.log("Employee Salary:", value.toFixed(2));
    }
}
displayEmployeeValue("Mayuri");
displayEmployeeValue(50000);
// Type Guard
function isEmployee(value) {
    return value instanceof EmployeeRecord;
}
const record = new EmployeeRecord("E002", "Riya", 55000);
if (isEmployee(record)) {
    console.log("Verified Employee:", record.name);
    console.log("Verified Salary:", record.salary);
}
