"use client";

import { FormEvent } from "react";

export default function CreateEmployeePage() {
    async function handleSubmit(event: FormEvent<HTMLFormElement>) {
        event.preventDefault();

        const formData = new FormData(event.currentTarget);

        const employee = {
            name: formData.get("name"),
            department: formData.get("department"),
            salary: Number(formData.get("salary")),
            email: formData.get("email"),
        };

        const response = await fetch(
            `${process.env.NEXT_PUBLIC_API_URL}/employees`,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(employee),
            }
        );

        if (!response.ok) {
            alert("Failed to create employee");
            return;
        }

        const newEmployee = await response.json();

        alert(`Employee ${newEmployee.name} created successfully!`);
        event.currentTarget.reset();
    }

    return (
        <main className="min-h-screen bg-gray-100 p-8">
            <div className="mx-auto max-w-xl">

                <a
                    href="/employees"
                    className="mb-6 inline-block font-semibold text-blue-600 hover:underline"
                >
                    ← Back to Employees
                </a>

                <div className="rounded-xl bg-white p-8 shadow">
                    <h1 className="text-3xl font-bold text-gray-900">
                        Add Employee
                    </h1>

                    <p className="mt-2 mb-6 text-gray-500">
                        Enter the employee information below.
                    </p>

                    <form onSubmit={handleSubmit} className="space-y-5">

                        <div>
                            <label className="mb-1 block font-medium text-gray-900">
                                Name
                            </label>
                            <input
                                type="text"
                                name="name"
                                required
                                className="w-full rounded-lg border border-gray-300 p-3 text-gray-900 outline-none focus:ring-2 focus:ring-blue-500"
                                placeholder="Enter employee name"
                            />
                        </div>

                        <div>
                            <label className="mb-1 block font-medium text-gray-900">
                                Department
                            </label>
                            <input
                                type="text"
                                name="department"
                                required
                                className="w-full rounded-lg border border-gray-300 p-3 text-gray-900 outline-none focus:ring-2 focus:ring-blue-500"
                                placeholder="e.g. IT"
                            />
                        </div>

                        <div>
                            <label className="mb-1 block font-medium text-gray-900">
                                Salary
                            </label>
                            <input
                                type="number"
                                name="salary"
                                required
                                className="w-full rounded-lg border border-gray-300 p-3 text-gray-900 outline-none focus:ring-2 focus:ring-blue-500"
                                placeholder="Enter salary"
                            />
                        </div>

                        <div>
                            <label className="mb-1 block font-medium text-gray-900">
                                Email
                            </label>
                            <input
                                type="email"
                                name="email"
                                required
                                className="w-full rounded-lg border border-gray-300 p-3 text-gray-900 outline-none focus:ring-2 focus:ring-blue-500"
                                placeholder="employee@example.com"
                            />
                        </div>

                        <button
                            type="submit"
                            className="w-full rounded-lg bg-blue-600 py-3 font-semibold text-white hover:bg-blue-700"
                        >
                            Add Employee
                        </button>
                    </form>
                </div>
            </div>
        </main>
    );
}



