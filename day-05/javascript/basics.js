// DAY 5 - JavaScript Fundamentals & Practice

// 1. let and const
let employeeName = "Mayuri";
const department = "AI/ML";

console.log("Employee:", employeeName);
console.log("Department:", department);


// 2. Data Types
let age = 20;
let isEmployee = true;
let skills = ["Python", "JavaScript", "Machine Learning"];
let employee = {
    id: "E001",
    name: "Mayuri",
    department: "AI/ML"
};

console.log(age);
console.log(isEmployee);
console.log(skills);
console.log(employee);


// 3. Functions
function greet(name) {
    return `Hello, ${name}!`;
}

console.log(greet("Mayuri"));


// 4. Arrow Function
const add = (a, b) => a + b;

console.log("Sum:", add(10, 20));


// 5. Arrays
const employees = [
    { id: "E001", name: "Mayuri", salary: 50000, department: "AI/ML" },
    { id: "E002", name: "Rahul", salary: 45000, department: "IT" },
    { id: "E003", name: "Priya", salary: 60000, department: "HR" },
    { id: "E004", name: "Aman", salary: 55000, department: "IT" }
];


// 6. map()
const employeeNames = employees.map(employee => employee.name);

console.log("Names:", employeeNames);


// 7. filter()
const itEmployees = employees.filter(
    employee => employee.department === "IT"
);

console.log("IT Employees:", itEmployees);


// 8. reduce()
const totalSalary = employees.reduce(
    (total, employee) => total + employee.salary,
    0
);

console.log("Total Salary:", totalSalary);


// 9. find()
const employeeFound = employees.find(
    employee => employee.id === "E003"
);

console.log("Found Employee:", employeeFound);


// 10. some()
const highSalaryExists = employees.some(
    employee => employee.salary > 55000
);

console.log("Salary above 55000:", highSalaryExists);


// 11. every()
const allHaveSalary = employees.every(
    employee => employee.salary > 0
);

console.log("All employees have salary:", allHaveSalary);


// 12. sort()
const sortedEmployees = [...employees].sort(
    (a, b) => b.salary - a.salary
);

console.log("Sorted by salary:", sortedEmployees);


// 13. Destructuring
const { name, department: dept } = employees[0];

console.log("Destructured Name:", name);
console.log("Destructured Department:", dept);


// 14. Spread Operator
const newEmployee = {
    ...employees[0],
    name: "New Employee"
};

console.log("Spread:", newEmployee);


// 15. Rest Operator
function calculateTotal(...numbers) {
    return numbers.reduce((total, number) => total + number, 0);
}

console.log("Rest:", calculateTotal(10, 20, 30));


// 16. Template Literal
const message = `${employeeName} works in the ${department} department.`;

console.log(message);


// 17. Error Handling
try {
    throw new Error("Example error");
} catch (error) {
    console.log("Error:", error.message);
}

