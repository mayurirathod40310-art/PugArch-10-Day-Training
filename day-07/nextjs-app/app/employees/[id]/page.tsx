type Employee = {
    id: string;
    name: string;
    department: string;
    salary: number;
    email: string;
};

async function getEmployee(id: string): Promise<Employee> {
    const response = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/employees/${id}`
    );

    if (!response.ok) {
        throw new Error("Employee not found");
    }

    return response.json();
}

export default async function EmployeeDetails({
    params,
}: {
    params: Promise<{ id: string }>;
}) {
    const { id } = await params;
    const employee = await getEmployee(id);

    return (
        <main className="min-h-screen bg-gray-100 p-8">
            <div className="mx-auto max-w-2xl">

                <a
                    href="/employees"
                    className="mb-6 inline-block font-semibold text-blue-600 hover:underline"
                >
                    ← Back to Employees
                </a>

                <div className="rounded-xl bg-white p-8 shadow">

                    <div className="mb-6 flex items-center justify-between">
                        <div>
                            <h1 className="text-3xl font-bold text-gray-900">
                                {employee.name}
                            </h1>

                            <p className="mt-1 text-base text-gray-700">
                                Employee ID: {employee.id}
                            </p>
                        </div>

                        <span className="rounded-full bg-blue-100 px-4 py-2 font-medium text-blue-700">
                            {employee.department}
                        </span>
                    </div>

                    <div className="space-y-5 border-t border-gray-200 pt-6">

                        <div>
                            <p className="text-sm font-semibold text-gray-700">
                                Email
                            </p>

                            <p className="mt-1 text-base font-medium text-gray-900">
                                {employee.email}
                            </p>
                        </div>

                        <div>
                            <p className="text-sm font-semibold text-gray-700">
                                Salary
                            </p>

                            <p className="mt-1 text-xl font-bold text-gray-900">
                                ₹{employee.salary}
                            </p>
                        </div>

                        <div>
                            <p className="text-sm font-semibold text-gray-700">
                                Department
                            </p>

                            <p className="mt-1 text-base font-medium text-gray-900">
                                {employee.department}
                            </p>
                        </div>

                    </div>
                </div>
            </div>
        </main>
    );
}

