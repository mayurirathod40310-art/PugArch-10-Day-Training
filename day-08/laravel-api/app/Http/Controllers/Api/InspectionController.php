<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\Inspection;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;

class InspectionController extends Controller
{
    public function index(): JsonResponse
    {
        $inspections = Inspection::with('facility')
            ->orderByDesc('inspection_date')
            ->get();

        return response()->json([
            'success' => true,
            'data' => $inspections,
        ]);
    }

    public function store(Request $request): JsonResponse
    {
        $validated = $request->validate([
            'facility_id' => ['required', 'exists:facilities,id'],
            'inspection_date' => ['required', 'date'],
            'inspector_name' => ['required', 'string', 'max:255'],
            'status' => ['required', 'in:Passed,Failed,Needs Improvement'],
            'remarks' => ['nullable', 'string'],
        ]);

        $inspection = Inspection::create($validated);
        $inspection->load('facility');

        return response()->json([
            'success' => true,
            'message' => 'Inspection created successfully.',
            'data' => $inspection,
        ], 201);
    }

    public function show(Inspection $inspection): JsonResponse
    {
        $inspection->load('facility');

        return response()->json([
            'success' => true,
            'data' => $inspection,
        ]);
    }

    public function update(Request $request, Inspection $inspection): JsonResponse
    {
        $validated = $request->validate([
            'facility_id' => ['required', 'exists:facilities,id'],
            'inspection_date' => ['required', 'date'],
            'inspector_name' => ['required', 'string', 'max:255'],
            'status' => ['required', 'in:Passed,Failed,Needs Improvement'],
            'remarks' => ['nullable', 'string'],
        ]);

        $inspection->update($validated);
        $inspection->load('facility');

        return response()->json([
            'success' => true,
            'message' => 'Inspection updated successfully.',
            'data' => $inspection,
        ]);
    }

    public function destroy(Inspection $inspection): JsonResponse
    {
        $inspection->delete();

        return response()->json([
            'success' => true,
            'message' => 'Inspection deleted successfully.',
        ]);
    }
}

