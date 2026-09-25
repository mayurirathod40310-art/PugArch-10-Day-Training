<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Employee extends Model
{
    protected $fillable = [
        'employee_code',
        'name',
        'email',
        'department_id',
        'salary',
        'designation',
    ];

    protected $casts = [
        'salary' => 'decimal:2',
    ];

    public function department(): BelongsTo
    {
        return $this->belongsTo(Department::class);
    }
}
