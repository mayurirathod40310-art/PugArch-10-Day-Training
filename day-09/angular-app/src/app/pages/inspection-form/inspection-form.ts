import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { FacilityService } from '../../services/facility.service';
import { Inspection } from '../../models/facility.model';

@Component({
  selector: 'app-inspection-form',
  imports: [CommonModule, FormsModule, RouterLink],
  templateUrl: './inspection-form.html',
  styleUrl: './inspection-form.css',
})
export class InspectionForm {

  inspection: Inspection = {
    id: '',
    facilityId: '',
    facilityName: '',
    inspector: '',
    date: '',
    score: 0,
    status: 'Pending',
    remarks: ''
  };

  submitted = false;

  constructor(private facilityService: FacilityService) {}

  submitInspection(): void {
    this.inspection.id = 'I' + Date.now();

    this.facilityService.addInspection(this.inspection).subscribe({
      next: () => {
        this.submitted = true;
      },
      error: (error) => {
        console.error('Error submitting inspection:', error);
      }
    });
  }
}