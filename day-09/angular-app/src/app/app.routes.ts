import { Routes } from '@angular/router';
import { Dashboard } from './pages/dashboard/dashboard';
import { FacilityDetails } from './pages/facility-details/facility-details';
import { InspectionForm } from './pages/inspection-form/inspection-form';
import { InspectionHistory } from './pages/inspection-history/inspection-history';

export const routes: Routes = [
  {
    path: '',
    redirectTo: 'dashboard',
    pathMatch: 'full'
  },
  {
    path: 'dashboard',
    component: Dashboard
  },
  {
    path: 'facilities/:id',
    component: FacilityDetails
  },
  {
    path: 'inspection',
    component: InspectionForm
  },
  {
    path: 'inspection-history',
    component: InspectionHistory
  }
];

