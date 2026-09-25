type Employee = {
    id: string;
    name: string;
    department: string;
    salary: number;
    email: string;
};

async function getEmployees(): Promise<Employee[]> {
    const response = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/employees`
    );

    if (!response.ok) {
        throw new Error("Failed to fetch employees");
    }

    return response.json();
}

export default async function EmployeesPage() {
    const employees = await getEmployees();

    const averageSalary =
        employees.reduce((sum, employee) => sum + employee.salary, 0) /
        employees.length;

    const departments = new Set(
        employees.map((employee) => employee.department)
    ).size;

    return (
        <main className="min-h-screen bg-gray-100 p-8">
            <div className="mx-auto max-w-6xl">

                {/* Header */}
                <div className="mb-8 flex items-center justify-between">
                    <div>
                        <h1 className="text-4xl font-bold text-gray-900">
                            Employee Dashboard
                        </h1>
                        <p className="mt-2 text-gray-600">
                            Manage and view employee information
                        </p>
                    </div>

                    <a
                        href="/employees/create"
                        className="rounded-lg bg-blue-600 px-5 py-3 font-semibold text-white hover:bg-blue-700"
                    >
                        + Add Employee
                    </a>
                </div>

                {/* Summary Cards */}
                <div className="mb-8 grid gap-5 md:grid-cols-3">
                    <div className="rounded-xl bg-white p-6 shadow">
                        <p className="text-sm text-gray-500">
                            Total Employees
                        </p>
                        <h2 className="mt-2 text-3xl font-bold">
                            {employees.length}
                        </h2>
                    </div>

                    <div className="rounded-xl bg-white p-6 shadow">
                        <p className="text-sm text-gray-500">
                            Average Salary
                        </p>
                        <h2 className="mt-2 text-3xl font-bold">
                            ₹{averageSalary.toFixed(2)}
                        </h2>
                    </div>

                    <div className="rounded-xl bg-white p-6 shadow">
                        <p className="text-sm text-gray-500">
                            Departments
                        </p>
                        <h2 className="mt-2 text-3xl font-bold">
                            {departments}
                        </h2>
                    </div>
                </div>

                {/* Employee List */}
                <div className="rounded-xl bg-white p-6 shadow">
                    <h2 className="mb-5 text-2xl font-bold text-gray-900">
                        Employees
                    </h2>

                    <div className="grid gap-4 md:grid-cols-3">
                        {employees.map((employee) => (
                            <div
                                key={employee.id}
                                className="rounded-lg border border-gray-200 p-5 hover:shadow-md"
                            >
                                <div className="flex items-start justify-between">
                                    <div>
                                        <h3 className="text-xl font-bold text-gray-900">
                                            {employee.name}
                                        </h3>

                                        <p className="mt-1 text-gray-500">
                                            {employee.id}
                                        </p>
                                    </div>

                                    <span className="rounded-full bg-blue-100 px-3 py-1 text-sm font-medium text-blue-700">
                                        {employee.department}
                                    </span>
                                </div>

                                <div className="mt-4 space-y-1 text-gray-600">
                                    <p>💰 ₹{employee.salary}</p>
                                    <p>✉️ {employee.email}</p>
                                </div>

                                <a
                                    href={`/employees/${employee.id}`}
                                    className="mt-4 inline-block font-semibold text-blue-600 hover:underline"
                                >
                                    View Details →
                                </a>
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        </main>
    );
}

