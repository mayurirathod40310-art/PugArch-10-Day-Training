import { useState } from "react";
import "./App.css";

const initialForm = {
  location: "Dharampeth",
  facility_type: "Public Washroom",
  cleanliness_score: 5.5,
  odor_score: 6,
  waste_level: 60,
  water_availability: "Yes",
  footfall: 500,
  complaints: 6,
  hours_since_cleaning: 10,
  inspection_month: 9,
  inspection_day_of_week: 5,
};

const numericFields = [
  "cleanliness_score",
  "odor_score",
  "waste_level",
  "footfall",
  "complaints",
  "hours_since_cleaning",
  "inspection_month",
  "inspection_day_of_week",
];

function App() {
  const [formData, setFormData] = useState(initialForm);
  const [result, setResult] = useState(null);
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleChange = (event) => {
    const { name, value } = event.target;

    setFormData((previous) => ({
      ...previous,
      [name]: value,
    }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const payload = { ...formData };

      numericFields.forEach((field) => {
        payload[field] = Number(formData[field]);
      });

      for (const field of numericFields) {
        if (!Number.isFinite(payload[field])) {
          throw new Error(`Please enter a valid value for ${field}.`);
        }
      }

      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });

      if (!response.ok) {
        throw new Error("Prediction request failed.");
      }

      const data = await response.json();

      setResult(data);

      setHistory((previous) => [
        {
          ...data,
          time: new Date().toLocaleTimeString(),
        },
        ...previous,
      ]);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const getRiskClass = (risk) => {
    if (risk === "High") return "risk-high";
    if (risk === "Medium") return "risk-medium";
    return "risk-low";
  };

  return (
    <div className="app">
      <header className="hero">
        <div className="hero-content">
          <p className="hero-tag">AI • MACHINE LEARNING • FASTAPI</p>

          <h1>Smart Hygiene Risk Prediction System</h1>

          <p>
            Predict facility hygiene risk using machine learning and real-time
            facility information.
          </p>
        </div>
      </header>

      <main className="container">
        {/* FACILITY INFORMATION */}
        <section className="card">
          <div className="section-heading">
            <h2>Facility Information</h2>
            <p>Enter the current facility inspection details.</p>
          </div>

          <form onSubmit={handleSubmit}>
            <div className="form-grid">
              <div className="form-group">
                <label>Location</label>
                <select
                  name="location"
                  value={formData.location}
                  onChange={handleChange}
                >
                  <option>Dharampeth</option>
                  <option>Sadar</option>
                  <option>Nagpur Central</option>
                  <option>Wardha Road</option>
                </select>
              </div>

              <div className="form-group">
                <label>Facility Type</label>
                <select
                  name="facility_type"
                  value={formData.facility_type}
                  onChange={handleChange}
                >
                  <option>Public Washroom</option>
                  <option>Office Washroom</option>
                  <option>School Washroom</option>
                  <option>Hospital Washroom</option>
                  <option>Mall Washroom</option>
                  <option>Transit Washroom</option>
                </select>
              </div>

              <div className="form-group">
                <label>Cleanliness Score</label>
                <input
                  type="text"
                  inputMode="decimal"
                  name="cleanliness_score"
                  value={formData.cleanliness_score}
                  onChange={handleChange}
                  placeholder="1 - 10"
                  required
                />
              </div>

              <div className="form-group">
                <label>Odor Score</label>
                <input
                  type="text"
                  inputMode="decimal"
                  name="odor_score"
                  value={formData.odor_score}
                  onChange={handleChange}
                  placeholder="1 - 10"
                  required
                />
              </div>

              <div className="form-group">
                <label>Waste Level</label>
                <input
                  type="text"
                  inputMode="decimal"
                  name="waste_level"
                  value={formData.waste_level}
                  onChange={handleChange}
                  placeholder="0 - 100"
                  required
                />
              </div>

              <div className="form-group">
                <label>Water Availability</label>
                <select
                  name="water_availability"
                  value={formData.water_availability}
                  onChange={handleChange}
                >
                  <option>Yes</option>
                  <option>No</option>
                </select>
              </div>

              <div className="form-group">
                <label>Footfall</label>
                <input
                  type="text"
                  inputMode="numeric"
                  name="footfall"
                  value={formData.footfall}
                  onChange={handleChange}
                  placeholder="Number of visitors"
                  required
                />
              </div>

              <div className="form-group">
                <label>Complaints</label>
                <input
                  type="text"
                  inputMode="numeric"
                  name="complaints"
                  value={formData.complaints}
                  onChange={handleChange}
                  placeholder="Number of complaints"
                  required
                />
              </div>

              <div className="form-group">
                <label>Hours Since Cleaning</label>
                <input
                  type="text"
                  inputMode="decimal"
                  name="hours_since_cleaning"
                  value={formData.hours_since_cleaning}
                  onChange={handleChange}
                  placeholder="Hours"
                  required
                />
              </div>

              <div className="form-group">
                <label>Inspection Month</label>
                <input
                  type="text"
                  inputMode="numeric"
                  name="inspection_month"
                  value={formData.inspection_month}
                  onChange={handleChange}
                  placeholder="1 - 12"
                  required
                />
              </div>

              <div className="form-group">
                <label>Inspection Day of Week</label>
                <input
                  type="text"
                  inputMode="numeric"
                  name="inspection_day_of_week"
                  value={formData.inspection_day_of_week}
                  onChange={handleChange}
                  placeholder="0 - 6"
                  required
                />
              </div>
            </div>

            <button type="submit" className="predict-button" disabled={loading}>
              {loading ? "Predicting..." : "Predict Hygiene Risk"}
            </button>
          </form>

          {error && <div className="error-box">{error}</div>}
        </section>

        {/* PREDICTION RESULT */}
        {result && (
          <section className="card result-card">
            <div className="section-heading">
              <h2>Prediction Result</h2>
              <p>Machine learning prediction for the submitted facility.</p>
            </div>

            <div className={`risk-result ${getRiskClass(result.prediction)}`}>
              <span>Predicted Hygiene Risk</span>
              <strong>{result.prediction}</strong>
            </div>

            <div className="probability-grid">
              {Object.entries(result.probabilities).map(([risk, value]) => (
                <div className="probability-card" key={risk}>
                  <span>{risk}</span>
                  <strong>{(value * 100).toFixed(2)}%</strong>
                </div>
              ))}
            </div>
          </section>
        )}

        {/* HISTORY */}
        <section className="card">
          <div className="section-heading">
            <h2>Prediction History</h2>
            <p>Recent predictions from this browser session.</p>
          </div>

          {history.length === 0 ? (
            <div className="empty-history">
              No predictions yet. Submit the form to create prediction
              history.
            </div>
          ) : (
            <div className="history-list">
              {history.map((item, index) => (
                <div className="history-item" key={index}>
                  <div>
                    <strong>{item.prediction} Risk</strong>
                    <span>{item.time}</span>
                  </div>

                  <div className={`history-badge ${getRiskClass(item.prediction)}`}>
                    {item.prediction}
                  </div>
                </div>
              ))}
            </div>
          )}
        </section>
      </main>

      <footer>
        Smart Hygiene Risk Prediction System • PugArch Day 10 Final Project
      </footer>
    </div>
  );
}

export default App;

