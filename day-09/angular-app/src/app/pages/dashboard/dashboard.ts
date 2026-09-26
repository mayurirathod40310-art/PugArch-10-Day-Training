import { Component, ChangeDetectorRef, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { FacilityService } from '../../services/facility.service';
import { Facility } from '../../models/facility.model';

@Component({
  selector: 'app-dashboard',
  imports: [CommonModule, FormsModule, RouterLink],
  templateUrl: './dashboard.html',
  styleUrl: './dashboard.css',
})
export class Dashboard implements OnInit {

  facilities: Facility[] = [];
  loading = true;
  errorMessage = '';

  searchTerm = '';
  statusFilter = 'All';
  sortBy = 'name';

  constructor(
    private facilityService: FacilityService,
    private changeDetector: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    this.facilityService.getFacilities().subscribe({
      next: (data) => {
        console.log('Facilities received from API:', data);

        this.facilities = [...data];
        this.loading = false;

        this.changeDetector.detectChanges();
      },
      error: (error) => {
        console.error('API Error:', error);
        this.errorMessage = 'Unable to load facilities from API.';
        this.loading = false;

        this.changeDetector.detectChanges();
      }
    });
  }

  get filteredFacilities(): Facility[] {
    let result = this.facilities.filter(facility => {
      const search = this.searchTerm.toLowerCase();

      const matchesSearch =
        facility.name.toLowerCase().includes(search) ||
        facility.location.toLowerCase().includes(search) ||
        facility.type.toLowerCase().includes(search) ||
        facility.status.toLowerCase().includes(search);

      const matchesStatus =
        this.statusFilter === 'All' ||
        facility.status === this.statusFilter;

      return matchesSearch && matchesStatus;
    });

    result = [...result].sort((a, b) => {
      if (this.sortBy === 'score') {
        return b.score - a.score;
      }

      if (this.sortBy === 'location') {
        return a.location.localeCompare(b.location);
      }

      return a.name.localeCompare(b.name);
    });

    return result;
  }

  get totalFacilities(): number {
    return this.facilities.length;
  }

  get goodFacilities(): number {
    return this.facilities.filter(f => f.status === 'Good').length;
  }

  get attentionFacilities(): number {
    return this.facilities.filter(f => f.status === 'Needs Attention').length;
  }

  get criticalFacilities(): number {
    return this.facilities.filter(f => f.status === 'Critical').length;
  }

  get averageScore(): number {
    if (this.facilities.length === 0) return 0;

    const total = this.facilities.reduce((sum, f) => sum + f.score, 0);
    return Math.round(total / this.facilities.length);
  }
}

