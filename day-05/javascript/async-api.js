// DAY 5 - Asynchronous JavaScript & APIs

// 1. Callback
function fetchEmployeeData(callback) {
    setTimeout(() => {
        const employee = {
            id: "E001",
            name: "Mayuri",
            department: "AI/ML"
        };

        callback(employee);
    }, 1000);
}

fetchEmployeeData((employee) => {
    console.log("Callback Employee:", employee);
});


// 2. Promise
function getEmployee() {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve({
                id: "E002",
                name: "Rahul",
                department: "IT"
            });
        }, 1000);
    });
}

getEmployee()
    .then(employee => {
        console.log("Promise Employee:", employee);
    })
    .catch(error => {
        console.error("Promise Error:", error);
    });


// 3. async/await
async function displayEmployee() {
    try {
        const employee = await getEmployee();
        console.log("Async/Await Employee:", employee);
    } catch (error) {
        console.error("Async/Await Error:", error);
    }
}

displayEmployee();


// 4. Fetch API - GET request
async function fetchUsers() {
    try {
        const response = await fetch(
            "https://jsonplaceholder.typicode.com/users"
        );

        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }

        const users = await response.json();

        console.log("API Users:", users);
    } catch (error) {
        console.error("Fetch Error:", error.message);
    }
}

fetchUsers();

