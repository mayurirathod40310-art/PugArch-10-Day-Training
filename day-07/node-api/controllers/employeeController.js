const employees = require("../models/employeeModel");

// Get all employees
const getEmployees = (req, res) => {
    res.json(employees);
};

// Get employee by ID
const getEmployeeById = (req, res) => {
    const employee = employees.find(
        (employee) => employee.id === req.params.id
    );

    if (!employee) {
        return res.status(404).json({
            message: "Employee not found"
        });
    }

    res.json(employee);
};

// Create employee
const createEmployee = (req, res) => {
    const newEmployee = {
        id: `E00${employees.length + 1}`,
        name: req.body.name,
        department: req.body.department,
        salary: Number(req.body.salary),
        email: req.body.email
    };

    employees.push(newEmployee);

    res.status(201).json(newEmployee);
};

// Update employee
const updateEmployee = (req, res) => {
    const employee = employees.find(
        (employee) => employee.id === req.params.id
    );

    if (!employee) {
        return res.status(404).json({
            message: "Employee not found"
        });
    }

    employee.name = req.body.name ?? employee.name;
    employee.department = req.body.department ?? employee.department;
    employee.salary = req.body.salary
        ? Number(req.body.salary)
        : employee.salary;
    employee.email = req.body.email ?? employee.email;

    res.json(employee);
};

// Delete employee
const deleteEmployee = (req, res) => {
    const index = employees.findIndex(
        (employee) => employee.id === req.params.id
    );

    if (index === -1) {
        return res.status(404).json({
            message: "Employee not found"
        });
    }

    const deletedEmployee = employees.splice(index, 1);

    res.json({
        message: "Employee deleted successfully",
        employee: deletedEmployee[0]
    });
};

module.exports = {
    getEmployees,
    getEmployeeById,
    createEmployee,
    updateEmployee,
    deleteEmployee
};

