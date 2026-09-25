const express = require("express");

const app = express();

const cors = require("cors");

app.use(express.json());

app.use(cors());

const employeeRoutes = require("./routes/employeeRoutes");

app.use("/employees", employeeRoutes);

const PORT = 5000;

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});

