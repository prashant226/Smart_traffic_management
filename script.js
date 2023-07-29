// Define a function to load the data
// Define a function to load the data
function loadData() {
    // Make an HTTP request to the server
    fetch('/data')
        .then((response) => {
            // Convert the response to JSON
            return response.json();
        })
        .then((data) => {
            // Update the count display
            const countDisplay = document.getElementById('count-display');
            countDisplay.innerHTML = data;
        })
        .catch((error) => {
            console.error(error);
        });
}

// Call the loadData function when the page loads
window.onload = loadData;