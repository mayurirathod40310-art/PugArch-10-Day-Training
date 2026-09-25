<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\Employee;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Validation\Rule;

class EmployeeController extends Controller
{
    public function index(): JsonResponse
    {
        $employees = Employee::with('department')
            ->orderBy('name')
            ->get();

        return response()->json([
            'success' => true,
            'data' => $employees,
        ]);
    }

    public function store(Request $request): JsonResponse
    {
        $validated = $request->validate([
            'employee_code' => ['required', 'string', 'max:50', 'unique:employees,employee_code'],
            'name' => ['required', 'string', 'max:255'],
            'email' => ['required', 'email', 'max:255', 'unique:employees,email'],
            'department_id' => ['required', 'exists:departments,id'],
            'salary' => ['required', 'numeric', 'min:0'],
            'designation' => ['nullable', 'string', 'max:255'],
        ]);

        $employee = Employee::create($validated);
        $employee->load('department');

        return response()->json([
            'success' => true,
            'message' => 'Employee created successfully.',
            'data' => $employee,
        ], 201);
    }

    public function show(Employee $employee): JsonResponse
    {
        $employee->load('department');

        return response()->json([
            'success' => true,
            'data' => $employee,
        ]);
    }

    public function update(Request $request, Employee $employee): JsonResponse
    {
        $validated = $request->validate([
            'employee_code' => [
                'required',
                'string',
                'max:50',
                Rule::unique('employees', 'employee_code')->ignore($employee->id),
            ],
            'name' => ['required', 'string', 'max:255'],
            'email' => [
                'required',
                'email',
                'max:255',
                Rule::unique('employees', 'email')->ignore($employee->id),
            ],
            'department_id' => ['required', 'exists:departments,id'],
            'salary' => ['required', 'numeric', 'min:0'],
            'designation' => ['nullable', 'string', 'max:255'],
        ]);

        $employee->update($validated);
        $employee->load('department');

        return response()->json([
            'success' => true,
            'message' => 'Employee updated successfully.',
            'data' => $employee,
        ]);
    }

    public function destroy(Employee $employee): JsonResponse
    {
        $employee->delete();

        return response()->json([
            'success' => true,
            'message' => 'Employee deleted successfully.',
        ]);
    }
}
