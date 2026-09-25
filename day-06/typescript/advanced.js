"use strict";
// Type Alias
let id1 = "E001";
let id2 = 101;
// Union Type
let employeeStatus = "Active";
console.log("Employee ID:", id1);
console.log("Employee Status:", employeeStatus);
// Enum
var Department;
(function (Department) {
    Department["IT"] = "IT";
    Department["HR"] = "HR";
    Department["Finance"] = "Finance";
    Department["Sales"] = "Sales";
})(Department || (Department = {}));
let employeeDepartment = Department.IT;
console.log("Department:", employeeDepartment);
// Function
function calculateAnnualSalary(monthlySalary) {
    return monthlySalary * 12;
}
console.log("Annual Salary:", calculateAnnualSalary(50000));
// Function with optional parameter
function greetEmployee(name, department) {
    if (department) {
        return `Hello ${name}, you work in ${department}.`;
    }
    return `Hello ${name}.`;
}
console.log(greetEmployee("Mayuri", "IT"));
console.log(greetEmployee("Riya"));
