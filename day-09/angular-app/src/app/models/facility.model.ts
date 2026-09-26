export interface Facility {
  id: string;
  name: string;
  location: string;
  type: string;
  status: 'Good' | 'Needs Attention' | 'Critical';
  lastInspection: string;
  score: number;
}

export interface Inspection {
  id: string;
  facilityId: string;
  facilityName: string;
  inspector: string;
  date: string;
  score: number;
  status: 'Passed' | 'Failed' | 'Pending';
  remarks: string;
}
