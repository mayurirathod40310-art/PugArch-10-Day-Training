import { useEffect, useState } from "react";
import type { Employee } from "../types";

interface EmployeeFormProps {
    onAddEmployee: (employee: Employee) => void;
    editingEmployee: Employee | null;
    onUpdateEmployee: (employee: Employee) => void;
    onCancelEdit: () => void;
}

function EmployeeForm({
    onAddEmployee,
    editingEmployee,
    onUpdateEmployee,
    onCancelEdit
}: EmployeeFormProps) {
    const [name, setName] = useState("");
    const [department, setDepartment] = useState("IT");
    const [salary, setSalary] = useState("");
    const [email, setEmail] = useState("");

    // Load employee data when editing
    useEffect(() => {
        if (editingEmployee) {
            setName(editingEmployee.name);
            setDepartment(editingEmployee.department);
            setSalary(String(editingEmployee.salary));
            setEmail(editingEmployee.email);
        } else {
            setName("");
            setDepartment("IT");
            setSalary("");
            setEmail("");
        }
    }, [editingEmployee]);

    const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();

        if (!name || !salary || !email) {
            alert("Please fill all fields.");
            return;
        }

        if (Number(salary) <= 0) {
            alert("Salary must be greater than 0.");
            return;
        }

        if (editingEmployee) {
            const updatedEmployee: Employee = {
                id: editingEmployee.id,
                name,
                department,
                salary: Number(salary),
                email
            };

            onUpdateEmployee(updatedEmployee);
        } else {
            const newEmployee: Employee = {
                id: `E${Date.now()}`,
                name,
                department,
                salary: Number(salary),
                email
            };

            onAddEmployee(newEmployee);
        }

        setName("");
        setDepartment("IT");
        setSalary("");
        setEmail("");
    };

    return (
        <div>
            <h2>
                {editingEmployee ? "Edit Employee" : "Add Employee"}
            </h2>

            <form onSubmit={handleSubmit}>
                <div>
                    <label>Name:</label>
                    <input
                        type="text"
                        value={name}
                        onChange={(event) =>
                            setName(event.target.value)
                        }
                    />
                </div>

                <div>
                    <label>Department:</label>
                    <select
                        value={department}
                        onChange={(event) =>
                            setDepartment(event.target.value)
                        }
                    >
                        <option value="IT">IT</option>
                        <option value="HR">HR</option>
                        <option value="Finance">Finance</option>
                        <option value="Sales">Sales</option>
                    </select>
                </div>

                <div>
                    <label>Salary:</label>
                    <input
                        type="number"
                        value={salary}
                        onChange={(event) =>
                            setSalary(event.target.value)
                        }
                    />
                </div>

                <div>
                    <label>Email:</label>
                    <input
                        type="email"
                        value={email}
                        onChange={(event) =>
                            setEmail(event.target.value)
                        }
                    />
                </div>

                <button type="submit">
                    {editingEmployee ? "Save Changes" : "Add Employee"}
                </button>

                {editingEmployee && (
                    <button
                        type="button"
                        onClick={onCancelEdit}
                    >
                        Cancel
                    </button>
                )}
            </form>
        </div>
    );
}

export default EmployeeForm;
