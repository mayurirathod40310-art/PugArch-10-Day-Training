<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('inspections', function (Blueprint $table) {
            $table->id();

            $table->foreignId('facility_id')
                ->constrained('facilities')
                ->cascadeOnUpdate()
                ->cascadeOnDelete();

            $table->date('inspection_date');
            $table->string('inspector_name');
            $table->enum('status', ['Passed', 'Failed', 'Needs Improvement']);
            $table->text('remarks')->nullable();

            $table->timestamps();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('inspections');
    }
};

