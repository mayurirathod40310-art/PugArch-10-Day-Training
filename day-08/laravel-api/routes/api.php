<?php

use App\Http\Controllers\Api\ComplaintController;
use App\Http\Controllers\Api\DepartmentController;
use App\Http\Controllers\Api\EmployeeController;
use App\Http\Controllers\Api\FacilityController;
use App\Http\Controllers\Api\InspectionController;
use Illuminate\Support\Facades\Route;

Route::apiResource('departments', DepartmentController::class);
Route::apiResource('employees', EmployeeController::class);
Route::apiResource('facilities', FacilityController::class);
Route::apiResource('inspections', InspectionController::class);
Route::apiResource('complaints', ComplaintController::class);
