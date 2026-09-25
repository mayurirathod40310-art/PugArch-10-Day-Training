<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\Complaint;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;

class ComplaintController extends Controller
{
    public function index(): JsonResponse
    {
        $complaints = Complaint::with('facility')
            ->orderByDesc('created_at')
            ->get();

        return response()->json([
            'success' => true,
            'data' => $complaints,
        ]);
    }

    public function store(Request $request): JsonResponse
    {
        $validated = $request->validate([
            'facility_id' => ['required', 'exists:facilities,id'],
            'complainant_name' => ['required', 'string', 'max:255'],
            'title' => ['required', 'string', 'max:255'],
            'description' => ['required', 'string'],
            'priority' => ['required', 'in:Low,Medium,High'],
            'status' => ['required', 'in:Open,In Progress,Resolved'],
        ]);

        $complaint = Complaint::create($validated);
        $complaint->load('facility');

        return response()->json([
            'success' => true,
            'message' => 'Complaint created successfully.',
            'data' => $complaint,
        ], 201);
    }

    public function show(Complaint $complaint): JsonResponse
    {
        $complaint->load('facility');

        return response()->json([
            'success' => true,
            'data' => $complaint,
        ]);
    }

    public function update(Request $request, Complaint $complaint): JsonResponse
    {
        $validated = $request->validate([
            'facility_id' => ['required', 'exists:facilities,id'],
            'complainant_name' => ['required', 'string', 'max:255'],
            'title' => ['required', 'string', 'max:255'],
            'description' => ['required', 'string'],
            'priority' => ['required', 'in:Low,Medium,High'],
            'status' => ['required', 'in:Open,In Progress,Resolved'],
        ]);

        $complaint->update($validated);
        $complaint->load('facility');

        return response()->json([
            'success' => true,
            'message' => 'Complaint updated successfully.',
            'data' => $complaint,
        ]);
    }

    public function destroy(Complaint $complaint): JsonResponse
    {
        $complaint->delete();

        return response()->json([
            'success' => true,
            'message' => 'Complaint deleted successfully.',
        ]);
    }
}

