<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\Facility;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;

class FacilityController extends Controller
{
    public function index(): JsonResponse
    {
        $facilities = Facility::withCount(['inspections', 'complaints'])
            ->orderBy('name')
            ->get();

        return response()->json([
            'success' => true,
            'data' => $facilities,
        ]);
    }

    public function store(Request $request): JsonResponse
    {
        $validated = $request->validate([
            'name' => ['required', 'string', 'max:255'],
            'location' => ['required', 'string', 'max:255'],
            'facility_type' => ['required', 'string', 'max:255'],
            'status' => ['required', 'in:Good,Needs Attention,Critical'],
            'description' => ['nullable', 'string'],
        ]);

        $facility = Facility::create($validated);

        return response()->json([
            'success' => true,
            'message' => 'Facility created successfully.',
            'data' => $facility,
        ], 201);
    }

    public function show(Facility $facility): JsonResponse
    {
        $facility->load(['inspections', 'complaints']);

        return response()->json([
            'success' => true,
            'data' => $facility,
        ]);
    }

    public function update(Request $request, Facility $facility): JsonResponse
    {
        $validated = $request->validate([
            'name' => ['required', 'string', 'max:255'],
            'location' => ['required', 'string', 'max:255'],
            'facility_type' => ['required', 'string', 'max:255'],
            'status' => ['required', 'in:Good,Needs Attention,Critical'],
            'description' => ['nullable', 'string'],
        ]);

        $facility->update($validated);

        return response()->json([
            'success' => true,
            'message' => 'Facility updated successfully.',
            'data' => $facility,
        ]);
    }

    public function destroy(Facility $facility): JsonResponse
    {
        $facility->delete();

        return response()->json([
            'success' => true,
            'message' => 'Facility deleted successfully.',
        ]);
    }
}

