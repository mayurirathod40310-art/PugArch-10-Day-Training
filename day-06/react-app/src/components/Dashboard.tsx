import type { Employee } from "../types";


interface DashboardProps {
    employees: Employee[];
}

function Dashboard({ employees }: DashboardProps) {
    const totalEmployees = employees.length;

    const averageSalary =
        totalEmployees > 0
            ? employees.reduce((total, employee) => total + employee.salary, 0) /
              totalEmployees
            : 0;

    const departments = new Set(
        employees.map((employee) => employee.department)
    ).size;

    return (
        <div>
            <h1>Employee Management Dashboard</h1>

            <div>
                <div>
                    <h3>Total Employees</h3>
                    <p>{totalEmployees}</p>
                </div>

                <div>
                    <h3>Average Salary</h3>
                    <p>₹{averageSalary.toFixed(2)}</p>
                </div>

                <div>
                    <h3>Departments</h3>
                    <p>{departments}</p>
                </div>
            </div>
        </div>
    );
}

export default Dashboard;


