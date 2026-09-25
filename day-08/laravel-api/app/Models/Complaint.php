<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Complaint extends Model
{
    protected $fillable = [
        'facility_id',
        'complainant_name',
        'title',
        'description',
        'priority',
        'status',
    ];

    public function facility(): BelongsTo
    {
        return $this->belongsTo(Facility::class);
    }
}
