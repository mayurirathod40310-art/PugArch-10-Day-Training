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

function App() {
  const [formData, setFormData] = useState(initialForm);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [history, setHistory] = useState([]);

  const handleChange = (event) => {
    const { name, value, type } = event.target;

    setFormData({
      ...formData,
      [name]: type === "number" ? Number(value) : value,
    });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error("Prediction request failed.");
      }

      const data = await response.json();

      setResult(data);

      // Add prediction to session history
      const historyItem = {
        id: Date.now(),
        location: formData.location,
        facilityType: formData.facility_type,
        prediction: data.prediction,
        probability: data.probabilities[data.prediction],
      };

      setHistory((previousHistory) => [
        historyItem,
        ...previousHistory,
      ]);
    } catch (err) {
      setError(
        "Unable to connect to the prediction API. Make sure the FastAPI server is running."
      );
    } finally {
      setLoading(false);
    }
  };

  const getRiskClass = () => {
    if (!result) return "";

    return result.prediction.toLowerCase();
  };

  return (
    <div className="app">
      {/* Header */}
      <header className="header">
        <div>
          <p className="eyebrow">AI-POWERED FACILITY MONITORING</p>

          <h1>Smart Hygiene Risk Prediction</h1>

          <p className="subtitle">
            Predict facility hygiene risk using machine learning.
          </p>
        </div>

        <div className="status">
          <span className="status-dot"></span>
          API Ready
        </div>
      </header>

      {/* Main Dashboard */}
      <main className="dashboard">

        {/* Facility Form */}
        <section className="card form-card">
          <div className="card-header">
            <h2>Facility Information</h2>

            <p>
              Enter the latest inspection details.
            </p>
          </div>

          <form onSubmit={handleSubmit}>
            <div className="form-grid">

              {/* Location */}
              <div className="field">
                <label>Location</label>

                <select
                  name="location"
                  value={formData.location}
                  onChange={handleChange}
                >
                  <option value="Dharampeth">Dharampeth</option>
                  <option value="Sadar">Sadar</option>
                  <option value="Wardha Road">Wardha Road</option>
                  <option value="Nagpur Central">
                    Nagpur Central
                  </option>
                </select>
              </div>

              {/* Facility Type */}
              <div className="field">
                <label>Facility Type</label>

                <select
                  name="facility_type"
                  value={formData.facility_type}
                  onChange={handleChange}
                >
                  <option value="Public Washroom">
                    Public Washroom
                  </option>

                  <option value="Office Washroom">
                    Office Washroom
                  </option>

                  <option value="School Washroom">
                    School Washroom
                  </option>

                  <option value="Hospital Washroom">
                    Hospital Washroom
                  </option>

                  <option value="Mall Washroom">
                    Mall Washroom
                  </option>

                  <option value="Transit Washroom">
                    Transit Washroom
                  </option>
                </select>
              </div>

              {/* Cleanliness */}
              <div className="field">
                <label>Cleanliness Score</label>

                <input
                  type="number"
                  name="cleanliness_score"
                  min="1"
                  max="10"
                  step="0.1"
                  value={formData.cleanliness_score}
                  onChange={handleChange}
                  required
                />
              </div>

              {/* Odor */}
              <div className="field">
                <label>Odor Score</label>

                <input
                  type="number"
                  name="odor_score"
                  min="1"
                  max="10"
                  step="0.1"
                  value={formData.odor_score}
                  onChange={handleChange}
                  required
                />
              </div>

              {/* Waste */}
              <div className="field">
                <label>Waste Level</label>

                <input
                  type="number"
                  name="waste_level"
                  min="0"
                  max="100"
                  step="0.1"
                  value={formData.waste_level}
                  onChange={handleChange}
                  required
                />
              </div>

              {/* Water */}
              <div className="field">
                <label>Water Availability</label>

                <select
                  name="water_availability"
                  value={formData.water_availability}
                  onChange={handleChange}
                >
                  <option value="Yes">Yes</option>
                  <option value="No">No</option>
                </select>
              </div>

              {/* Footfall */}
              <div className="field">
                <label>Footfall</label>

                <input
                  type="number"
                  name="footfall"
                  min="0"
                  value={formData.footfall}
                  onChange={handleChange}
                  required
                />
              </div>

              {/* Complaints */}
              <div className="field">
                <label>Complaints</label>

                <input
                  type="number"
                  name="complaints"
                  min="0"
                  value={formData.complaints}
                  onChange={handleChange}
                  required
                />
              </div>

              {/* Cleaning Time */}
              <div className="field">
                <label>Hours Since Cleaning</label>

                <input
                  type="number"
                  name="hours_since_cleaning"
                  min="0"
                  step="0.1"
                  value={formData.hours_since_cleaning}
                  onChange={handleChange}
                  required
                />
              </div>

              {/* Month */}
              <div className="field">
                <label>Inspection Month</label>

                <input
                  type="number"
                  name="inspection_month"
                  min="1"
                  max="12"
                  value={formData.inspection_month}
                  onChange={handleChange}
                  required
                />
              </div>

              {/* Day */}
              <div className="field">
                <label>Day of Week</label>

                <input
                  type="number"
                  name="inspection_day_of_week"
                  min="0"
                  max="6"
                  value={formData.inspection_day_of_week}
                  onChange={handleChange}
                  required
                />
              </div>
            </div>

            <button
              className="predict-button"
              type="submit"
              disabled={loading}
            >
              {loading
                ? "Analyzing..."
                : "Predict Hygiene Risk"}
            </button>
          </form>
        </section>

        {/* Prediction Result */}
        <section className="card result-card">
          <div className="card-header">
            <h2>Prediction Result</h2>

            <p>
              Machine learning assessment.
            </p>
          </div>

          {/* Initial State */}
          {!result && !error && !loading && (
            <div className="empty-state">
              <div className="empty-icon">
                AI
              </div>

              <h3>Ready for Prediction</h3>

              <p>
                Enter facility information and click the
                prediction button.
              </p>
            </div>
          )}

          {/* Loading */}
          {loading && (
            <div className="empty-state">
              <div className="loader"></div>

              <h3>
                Analyzing Facility...
              </h3>

              <p>
                The ML model is processing your input.
              </p>
            </div>
          )}

          {/* Error */}
          {error && (
            <div className="error-box">
              <strong>
                Connection Error
              </strong>

              <p>
                {error}
              </p>
            </div>
          )}

          {/* Result */}
          {result && !loading && (
            <div className="result-content">

              <div
                className={`risk-badge ${getRiskClass()}`}
              >
                {result.prediction}
              </div>

              <h3 className="risk-title">
                {result.prediction} Hygiene Risk
              </h3>

              <p className="result-description">
                Based on the submitted facility conditions,
                the trained Logistic Regression model
                classified this facility as{" "}
                <strong>
                  {result.prediction}
                </strong>{" "}
                risk.
              </p>

              {/* Probabilities */}
              <div className="probabilities">
                <h3>
                  Risk Probabilities
                </h3>

                {Object.entries(
                  result.probabilities
                ).map(
                  ([risk, probability]) => (
                    <div
                      className="probability-row"
                      key={risk}
                    >
                      <div className="probability-label">
                        <span>
                          {risk}
                        </span>

                        <span>
                          {(probability * 100).toFixed(2)}%
                        </span>
                      </div>

                      <div className="progress-bar">
                        <div
                          className={`progress-fill ${risk.toLowerCase()}`}
                          style={{
                            width: `${probability * 100}%`,
                          }}
                        ></div>
                      </div>
                    </div>
                  )
                )}
              </div>
            </div>
          )}
        </section>

        {/* Prediction History */}
        <section className="card history-card">
          <div className="card-header">
            <h2>Prediction History</h2>

            <p>
              Predictions made during this session.
            </p>
          </div>

          {history.length === 0 ? (
            <div className="history-empty">
              No predictions yet.
            </div>
          ) : (
            <div className="history-list">
              {history.map((item) => (
                <div
                  className="history-item"
                  key={item.id}
                >
                  <div className="history-details">
                    <strong>
                      {item.location}
                    </strong>

                    <span>
                      {item.facilityType}
                    </span>
                  </div>

                  <div
                    className={`history-risk ${item.prediction.toLowerCase()}`}
                  >
                    {item.prediction}
                  </div>

                  <div className="history-probability">
                    {(
                      item.probability * 100
                    ).toFixed(2)}
                    %
                  </div>
                </div>
              ))}
            </div>
          )}
        </section>

      </main>

      {/* Footer */}
      <footer>
        Smart Hygiene Risk Prediction System •
        Machine Learning + FastAPI + React
      </footer>
    </div>
  );
}

export default App;

