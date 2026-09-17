

// DAY 5 - Employee Dashboard

let employees = [];

const employeeList = document.getElementById("employeeList");
const searchInput = document.getElementById("searchInput");
const departmentFilter = document.getElementById("departmentFilter");
const sortSelect = document.getElementById("sortSelect");
const addEmployeeBtn = document.getElementById("addEmployeeBtn");

const API_URL = "https://jsonplaceholder.typicode.com/users";


// Fetch employees using GET
async function loadEmployees() {
    try {
        const response = await fetch(API_URL);

        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }

        const data = await response.json();

        employees = data.map(employee => ({
            id: employee.id,
            name: employee.name,
            email: employee.email,
            department: employee.company.name,
            phone: employee.phone,
            salary: 30000 + employee.id * 2500
        }));

        populateDepartments();
        displayEmployees(employees);

    } catch (error) {
        employeeList.innerHTML = "<p>Failed to load employees.</p>";
        console.error("Error:", error.message);
    }
}


// Display employees
function displayEmployees(employeeData) {
    employeeList.innerHTML = "";

    if (employeeData.length === 0) {
        employeeList.innerHTML = "<p>No employees found.</p>";
        return;
    }

    employeeData.forEach(employee => {
        const card = document.createElement("div");

        card.className = "employee-card";

        card.innerHTML = `
            <h3>${employee.name}</h3>

            <p><strong>ID:</strong> ${employee.id}</p>
            <p><strong>Email:</strong> ${employee.email}</p>
            <p><strong>Department:</strong> ${employee.department}</p>
            <p><strong>Phone:</strong> ${employee.phone}</p>
            <p><strong>Salary:</strong> ₹${employee.salary.toLocaleString()}</p>

            <div class="card-buttons">

                <button onclick="viewEmployee(${employee.id})">
                    Details
                </button>

                <button onclick="editEmployee(${employee.id})">
                    Edit
                </button>

                <button onclick="deleteEmployee(${employee.id})">
                    Delete
                </button>

            </div>
        `;

        employeeList.appendChild(card);
    });
}


// Add departments to filter
function populateDepartments() {
    const departments = [
        ...new Set(employees.map(employee => employee.department))
    ];

    departments.forEach(department => {

        const alreadyExists = Array.from(
            departmentFilter.options
        ).some(option => option.value === department);

        if (!alreadyExists) {
            const option = document.createElement("option");

            option.value = department;
            option.textContent = department;

            departmentFilter.appendChild(option);
        }
    });
}


// Search, filter and sort
function applyFilters() {
    const searchText = searchInput.value.toLowerCase();
    const selectedDepartment = departmentFilter.value;
    const selectedSort = sortSelect.value;

    let filteredEmployees = employees.filter(employee => {

        const matchesSearch =
            employee.name.toLowerCase().includes(searchText) ||
            employee.email.toLowerCase().includes(searchText);

        const matchesDepartment =
            selectedDepartment === "all" ||
            employee.department === selectedDepartment;

        return matchesSearch && matchesDepartment;
    });


    // Sort by name
    if (selectedSort === "name") {
        filteredEmployees.sort((a, b) =>
            a.name.localeCompare(b.name)
        );
    }


    // Sort by salary - high to low
    if (selectedSort === "salary-high") {
        filteredEmployees.sort(
            (a, b) => b.salary - a.salary
        );
    }


    // Sort by salary - low to high
    if (selectedSort === "salary-low") {
        filteredEmployees.sort(
            (a, b) => a.salary - b.salary
        );
    }

    displayEmployees(filteredEmployees);
}


// View employee details
function viewEmployee(id) {
    const employee = employees.find(
        employee => employee.id === id
    );

    if (!employee) {
        return;
    }

    alert(
        `Employee Details\n\n` +
        `ID: ${employee.id}\n` +
        `Name: ${employee.name}\n` +
        `Email: ${employee.email}\n` +
        `Department: ${employee.department}\n` +
        `Phone: ${employee.phone}\n` +
        `Salary: ₹${employee.salary.toLocaleString()}`
    );
}


// Add employee using POST
async function addEmployee() {

    const name = prompt("Enter employee name:");
    const email = prompt("Enter employee email:");
    const department = prompt("Enter employee department:");
    const phone = prompt("Enter employee phone:");
    const salaryInput = prompt("Enter employee salary:");

    if (
        !name ||
        !email ||
        !department ||
        !phone ||
        !salaryInput
    ) {
        alert("All fields are required.");
        return;
    }

    const salary = Number(salaryInput);

    if (isNaN(salary) || salary <= 0) {
        alert("Please enter a valid salary.");
        return;
    }


    const newEmployee = {
        name: name,
        email: email,
        department: department,
        phone: phone,
        salary: salary
    };


    try {

        const response = await fetch(API_URL, {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(newEmployee)
        });


        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }


        const createdEmployee = await response.json();


        const employee = {
            id: createdEmployee.id,
            name: newEmployee.name,
            email: newEmployee.email,
            department: newEmployee.department,
            phone: newEmployee.phone,
            salary: newEmployee.salary
        };


        employees.push(employee);

        populateDepartments();
        applyFilters();

        alert("Employee added successfully!");

    } catch (error) {

        console.error("POST Error:", error.message);

        alert("Failed to add employee.");
    }
}


// Edit employee using PUT
async function editEmployee(id) {

    const employee = employees.find(
        employee => employee.id === id
    );

    if (!employee) {
        return;
    }


    const name = prompt(
        "Enter new name:",
        employee.name
    );

    const email = prompt(
        "Enter new email:",
        employee.email
    );

    const department = prompt(
        "Enter new department:",
        employee.department
    );

    const phone = prompt(
        "Enter new phone:",
        employee.phone
    );

    const salaryInput = prompt(
        "Enter new salary:",
        employee.salary
    );


    if (
        !name ||
        !email ||
        !department ||
        !phone ||
        !salaryInput
    ) {
        alert("All fields are required.");
        return;
    }


    const salary = Number(salaryInput);

    if (isNaN(salary) || salary <= 0) {
        alert("Please enter a valid salary.");
        return;
    }


    const updatedEmployee = {
        id: id,
        name: name,
        email: email,
        department: department,
        phone: phone,
        salary: salary
    };


    try {

        const response = await fetch(
            `${API_URL}/${id}`,
            {
                method: "PUT",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(updatedEmployee)
            }
        );


        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }


        await response.json();


        employee.name = name;
        employee.email = email;
        employee.department = department;
        employee.phone = phone;
        employee.salary = salary;


        populateDepartments();
        applyFilters();

        alert("Employee updated successfully!");

    } catch (error) {

        console.error("PUT Error:", error.message);

        alert("Failed to update employee.");
    }
}


// Delete employee using DELETE
async function deleteEmployee(id) {

    const employee = employees.find(
        employee => employee.id === id
    );

    if (!employee) {
        return;
    }


    const confirmed = confirm(
        `Are you sure you want to delete ${employee.name}?`
    );


    if (!confirmed) {
        return;
    }


    try {

        const response = await fetch(
            `${API_URL}/${id}`,
            {
                method: "DELETE"
            }
        );


        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }


        employees = employees.filter(
            employee => employee.id !== id
        );


        applyFilters();

        alert("Employee deleted successfully!");

    } catch (error) {

        console.error("DELETE Error:", error.message);

        alert("Failed to delete employee.");
    }
}


// Event listeners
searchInput.addEventListener(
    "input",
    applyFilters
);

departmentFilter.addEventListener(
    "change",
    applyFilters
);

sortSelect.addEventListener(
    "change",
    applyFilters
);

addEmployeeBtn.addEventListener(
    "click",
    addEmployee
);


// Start application
loadEmployees();

