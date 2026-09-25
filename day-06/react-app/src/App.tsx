import { useState } from "react";
import Dashboard from "./components/Dashboard";
import EmployeeList from "./components/EmployeeList";
import EmployeeForm from "./components/EmployeeForm";
import ApiDemo from "./components/ApiDemo";
import { employees as initialEmployees } from "./data";
import type { Employee } from "./types";

function App() {
    const [employeeList, setEmployeeList] =
        useState<Employee[]>(initialEmployees);

    const [search, setSearch] = useState("");
    const [department, setDepartment] = useState("All");
    const [sortOrder, setSortOrder] = useState("none");
    const [selectedEmployee, setSelectedEmployee] =
        useState<Employee | null>(null);
    const [editingEmployee, setEditingEmployee] =
        useState<Employee | null>(null);

    const handleAddEmployee = (newEmployee: Employee) => {
        setEmployeeList((currentEmployees) => [
            ...currentEmployees,
            newEmployee
        ]);
    };

    const handleDeleteEmployee = (id: string) => {
        setEmployeeList((currentEmployees) =>
            currentEmployees.filter((employee) => employee.id !== id)
        );
        setSelectedEmployee(null);
    };

    const handleEditEmployee = (employee: Employee) => {
        setEditingEmployee(employee);
        setSelectedEmployee(null);
    };

    const handleUpdateEmployee = (updatedEmployee: Employee) => {
        setEmployeeList((currentEmployees) =>
            currentEmployees.map((employee) =>
                employee.id === updatedEmployee.id
                    ? updatedEmployee
                    : employee
            )
        );

        setEditingEmployee(null);
    };

    const handleCancelEdit = () => {
        setEditingEmployee(null);
    };

    const filteredEmployees = employeeList
        .filter((employee) => {
            const matchesSearch = employee.name
                .toLowerCase()
                .includes(search.toLowerCase());

            const matchesDepartment =
                department === "All" ||
                employee.department === department;

            return matchesSearch && matchesDepartment;
        })
        .sort((a, b) => {
            if (sortOrder === "low") return a.salary - b.salary;
            if (sortOrder === "high") return b.salary - a.salary;
            return 0;
        });

    return (
        <div className="app-container">
            <header className="app-header">
                <h1>Employee Management Dashboard</h1>
                <p>Manage employees, salaries, and departments efficiently.</p>
            </header>

            <section className="dashboard-section">
                <Dashboard employees={employeeList} />
            </section>

            <section className="form-section">
                <EmployeeForm
                    onAddEmployee={handleAddEmployee}
                    editingEmployee={editingEmployee}
                    onUpdateEmployee={handleUpdateEmployee}
                    onCancelEdit={handleCancelEdit}
                />
            </section>

            <section className="filter-section">
                <h2>Search and Filter Employees</h2>

                <div className="filters">
                    <input
                        type="text"
                        placeholder="Search employee by name"
                        value={search}
                        onChange={(event) => setSearch(event.target.value)}
                    />

                    <select
                        value={department}
                        onChange={(event) =>
                            setDepartment(event.target.value)
                        }
                    >
                        <option value="All">All Departments</option>
                        <option value="IT">IT</option>
                        <option value="HR">HR</option>
                        <option value="Finance">Finance</option>
                        <option value="Sales">Sales</option>
                    </select>

                    <select
                        value={sortOrder}
                        onChange={(event) =>
                            setSortOrder(event.target.value)
                        }
                    >
                        <option value="none">Sort by Salary</option>
                        <option value="low">Low to High</option>
                        <option value="high">High to Low</option>
                    </select>
                </div>
            </section>

            <section className="table-section">
                <EmployeeList
                    employees={filteredEmployees}
                    onSelectEmployee={setSelectedEmployee}
                    onDeleteEmployee={handleDeleteEmployee}
                    onEditEmployee={handleEditEmployee}
                />
            </section>

            {selectedEmployee && (
                <section className="details-section">
                    <h2>Employee Details</h2>

                    <p>
                        <strong>ID:</strong> {selectedEmployee.id}
                    </p>
                    <p>
                        <strong>Name:</strong> {selectedEmployee.name}
                    </p>
                    <p>
                        <strong>Department:</strong>{" "}
                        {selectedEmployee.department}
                    </p>
                    <p>
                        <strong>Salary:</strong> ₹{selectedEmployee.salary}
                    </p>
                    <p>
                        <strong>Email:</strong> {selectedEmployee.email}
                    </p>

                    <button onClick={() => setSelectedEmployee(null)}>
                        Close Details
                    </button>
                </section>
            )}

            <section className="api-section">
                <ApiDemo />
            </section>
        </div>
    );
}

export default App;
