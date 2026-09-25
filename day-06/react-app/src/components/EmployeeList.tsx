import type { Employee } from "../types";

interface EmployeeListProps {
    employees: Employee[];
    onSelectEmployee: (employee: Employee) => void;
    onDeleteEmployee: (id: string) => void;
    onEditEmployee: (employee: Employee) => void;
}

function EmployeeList({
    employees,
    onSelectEmployee,
    onDeleteEmployee,
    onEditEmployee
}: EmployeeListProps) {
    return (
        <div>
            <h2>Employee List</h2>

            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Department</th>
                        <th>Salary</th>
                        <th>Email</th>
                        <th>Action</th>
                    </tr>
                </thead>

                <tbody>
                    {employees.map((employee) => (
                        <tr key={employee.id}>
                            <td>{employee.id}</td>

                            <td
                                onClick={() => onSelectEmployee(employee)}
                                style={{ cursor: "pointer" }}
                            >
                                {employee.name}
                            </td>

                            <td>{employee.department}</td>

                            <td>₹{employee.salary}</td>

                            <td>{employee.email}</td>

                            <td>
                                <button
                                    onClick={() =>
                                        onEditEmployee(employee)
                                    }
                                >
                                    Edit
                                </button>

                                <button
                                    onClick={() =>
                                        onDeleteEmployee(employee.id)
                                    }
                                >
                                    Delete
                                </button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default EmployeeList;
