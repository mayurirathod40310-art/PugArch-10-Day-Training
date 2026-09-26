import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { FacilityService } from '../../services/facility.service';
import { Inspection } from '../../models/facility.model';

@Component({
  selector: 'app-inspection-history',
  imports: [CommonModule, RouterLink],
  templateUrl: './inspection-history.html',
  styleUrl: './inspection-history.css',
})
export class InspectionHistory implements OnInit {

  inspections: Inspection[] = [];

  constructor(private facilityService: FacilityService) {}

  ngOnInit(): void {
    this.facilityService.getInspections().subscribe({
      next: (data) => {
        this.inspections = data;
      },
      error: (error) => {
        console.error('Error loading inspection history:', error);
      }
    });
  }
}

