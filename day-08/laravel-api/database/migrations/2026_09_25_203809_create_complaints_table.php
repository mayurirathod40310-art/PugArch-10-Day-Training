<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('complaints', function (Blueprint $table) {
            $table->id();

            $table->foreignId('facility_id')
                ->constrained('facilities')
                ->cascadeOnUpdate()
                ->cascadeOnDelete();

            $table->string('complainant_name');
            $table->string('title');
            $table->text('description');
            $table->enum('priority', ['Low', 'Medium', 'High'])
                ->default('Medium');
            $table->enum('status', ['Open', 'In Progress', 'Resolved'])
                ->default('Open');

            $table->timestamps();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('complaints');
    }
};

