<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Inspection extends Model
{
    protected $fillable = [
        'facility_id',
        'inspection_date',
        'inspector_name',
        'status',
        'remarks',
    ];

    protected $casts = [
        'inspection_date' => 'date',
    ];

    public function facility(): BelongsTo
    {
        return $this->belongsTo(Facility::class);
    }
}

