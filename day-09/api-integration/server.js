const express = require('express');
const cors = require('cors');

const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());

const facilities = [
  {
    id: 'F001',
    name: 'Central Manufacturing Plant',
    location: 'Nagpur',
    type: 'Manufacturing',
    status: 'Good',
    lastInspection: '2026-09-20',
    score: 92
  },
  {
    id: 'F002',
    name: 'North Warehouse',
    location: 'Amravati',
    type: 'Warehouse',
    status: 'Needs Attention',
    lastInspection: '2026-09-18',
    score: 74
  },
  {
    id: 'F003',
    name: 'Chemical Processing Unit',
    location: 'Pune',
    type: 'Processing',
    status: 'Critical',
    lastInspection: '2026-09-15',
    score: 48
  },
  {
    id: 'F004',
    name: 'East Distribution Center',
    location: 'Aurangabad',
    type: 'Distribution',
    status: 'Good',
    lastInspection: '2026-09-22',
    score: 88
  },
  {
    id: 'F005',
    name: 'Quality Testing Lab',
    location: 'Nashik',
    type: 'Laboratory',
    status: 'Good',
    lastInspection: '2026-09-21',
    score: 95
  }
];

app.get('/api/facilities', (req, res) => {
  res.json(facilities);
});

app.get('/api/facilities/:id', (req, res) => {
  const facility = facilities.find(item => item.id === req.params.id);

  if (!facility) {
    return res.status(404).json({
      message: 'Facility not found'
    });
  }

  res.json(facility);
});

app.get('/api/health', (req, res) => {
  res.json({
    status: 'API is running',
    message: 'Facility Inspection API'
  });
});

app.listen(PORT, () => {
  console.log(`API server running at http://localhost:${PORT}`);
});
