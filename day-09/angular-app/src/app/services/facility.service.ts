import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { Facility, Inspection } from '../models/facility.model';

@Injectable({
  providedIn: 'root'
})
export class FacilityService {

  private apiUrl = 'http://localhost:3000/api';

  private inspections: Inspection[] = [
    {
      id: 'I001',
      facilityId: 'F001',
      facilityName: 'Central Manufacturing Plant',
      inspector: 'Rahul Sharma',
      date: '2026-09-20',
      score: 92,
      status: 'Passed',
      remarks: 'All major safety checks completed successfully.'
    },
    {
      id: 'I002',
      facilityId: 'F002',
      facilityName: 'North Warehouse',
      inspector: 'Priya Patil',
      date: '2026-09-18',
      score: 74,
      status: 'Pending',
      remarks: 'Storage area requires corrective action.'
    },
    {
      id: 'I003',
      facilityId: 'F003',
      facilityName: 'Chemical Processing Unit',
      inspector: 'Amit Joshi',
      date: '2026-09-15',
      score: 48,
      status: 'Failed',
      remarks: 'Multiple safety issues require immediate attention.'
    }
  ];

  constructor(private http: HttpClient) {}

  getFacilities(): Observable<Facility[]> {
    return this.http.get<Facility[]>(`${this.apiUrl}/facilities`);
  }

  getFacilityById(id: string): Observable<Facility | undefined> {
    return this.http.get<Facility>(`${this.apiUrl}/facilities/${id}`);
  }

  getInspections(): Observable<Inspection[]> {
    return of(this.inspections);
  }

  addInspection(inspection: Inspection): Observable<Inspection> {
    this.inspections.push(inspection);
    return of(inspection);
  }
}

