// Class

class EmployeeRecord {
    constructor(
        public id: string,
        public name: string,
        public salary: number
    ) {}

    getAnnualSalary(): number {
        return this.salary * 12;
    }
}

const emp = new EmployeeRecord("E001", "Mayuri", 50000);

console.log("Employee:", emp.name);
console.log("Annual Salary:", emp.getAnnualSalary());


// Generic Function

function getFirstItem<T>(items: T[]): T {
    return items[0];
}

const firstEmployee = getFirstItem(["Mayuri", "Riya", "Aarav"]);
const firstSalary = getFirstItem([50000, 60000, 70000]);

console.log("First Employee:", firstEmployee);
console.log("First Salary:", firstSalary);


// Union + Type Narrowing

function displayEmployeeValue(value: string | number): void {
    if (typeof value === "string") {
        console.log("Employee Name:", value.toUpperCase());
    } else {
        console.log("Employee Salary:", value.toFixed(2));
    }
}

displayEmployeeValue("Mayuri");
displayEmployeeValue(50000);


// Type Guard

function isEmployee(value: unknown): value is EmployeeRecord {
    return value instanceof EmployeeRecord;
}

const record: unknown = new EmployeeRecord("E002", "Riya", 55000);

if (isEmployee(record)) {
    console.log("Verified Employee:", record.name);
    console.log("Verified Salary:", record.salary);
}

