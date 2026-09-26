import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { FacilityService } from '../../services/facility.service';
import { Facility } from '../../models/facility.model';

@Component({
  selector: 'app-facility-details',
  imports: [CommonModule, RouterLink],
  templateUrl: './facility-details.html',
  styleUrl: './facility-details.css',
})
export class FacilityDetails implements OnInit {

  facility?: Facility;
  loading = true;
  errorMessage = '';

  constructor(
    private route: ActivatedRoute,
    private facilityService: FacilityService,
    private changeDetector: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    const id = this.route.snapshot.paramMap.get('id');

    console.log('Facility ID from route:', id);

    if (!id) {
      this.loading = false;
      this.errorMessage = 'Facility ID is missing.';
      return;
    }

    this.facilityService.getFacilityById(id).subscribe({
      next: (data) => {
        console.log('Facility data received:', data);
        console.log('Facility name:', data?.name);

        this.facility = data;
        this.loading = false;

        if (!data) {
          this.errorMessage = 'Facility not found.';
        }

        this.changeDetector.detectChanges();
      },
      error: (error) => {
        console.error('Error loading facility:', error);
        this.loading = false;
        this.errorMessage = 'Unable to load facility details.';

        this.changeDetector.detectChanges();
      }
    });
  }
}
