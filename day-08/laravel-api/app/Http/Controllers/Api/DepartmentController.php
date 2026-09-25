<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\Department;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;

class DepartmentController extends Controller
{
    public function index(): JsonResponse
    {
        $departments = Department::withCount('employees')
            ->orderBy('name')
            ->get();

        return response()->json([
            'success' => true,
            'data' => $departments,
        ]);
    }

    public function store(Request $request): JsonResponse
    {
        $validated = $request->validate([
            'name' => ['required', 'string', 'max:255', 'unique:departments,name'],
            'description' => ['nullable', 'string'],
        ]);

        $department = Department::create($validated);

        return response()->json([
            'success' => true,
            'message' => 'Department created successfully.',
            'data' => $department,
        ], 201);
    }

    public function show(Department $department): JsonResponse
    {
        $department->load('employees');

        return response()->json([
            'success' => true,
            'data' => $department,
        ]);
    }

    public function update(Request $request, Department $department): JsonResponse
    {
        $validated = $request->validate([
            'name' => [
                'required',
                'string',
                'max:255',
                'unique:departments,name,' . $department->id,
            ],
            'description' => ['nullable', 'string'],
        ]);

        $department->update($validated);

        return response()->json([
            'success' => true,
            'message' => 'Department updated successfully.',
            'data' => $department,
        ]);
    }

    public function destroy(Department $department): JsonResponse
    {
        if ($department->employees()->exists()) {
            return response()->json([
                'success' => false,
                'message' => 'Cannot delete a department that has employees.',
            ], 409);
        }

        $department->delete();

        return response()->json([
            'success' => true,
            'message' => 'Department deleted successfully.',
        ]);
    }
}
