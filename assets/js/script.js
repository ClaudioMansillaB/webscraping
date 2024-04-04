// Function to fetch CSV file
function fetchCSV(url) {
    return fetch(url)
        .then(response => response.text())
        .then(text => {
            // Convert CSV text to array of objects
            const data = text.split('\n').map(row => row.split(','));
            const headers = data.shift(); // Extract headers

            return data.map(row => {
                const entry = {};
                headers.forEach((header, index) => {
                    entry[header.trim()] = row[index].trim();
                });
                return entry;
            });
        });
}

// Function to display data on webpage
function displayData(data) {
    const container = document.getElementById('data-container');

    // Clear existing content
    container.innerHTML = '';

    // Loop through each entry and create HTML elements
    data.forEach(entry => {
        const div = document.createElement('div');
        div.classList.add('entry');

        // Create title element
        const title = document.createElement('h2');
        title.textContent = entry.title;
        div.appendChild(title);

        // Create author element
        const author = document.createElement('p');
        author.textContent = 'Author: ' + entry.author;
        div.appendChild(author);

        // Create link element
        const link = document.createElement('a');
        link.textContent = 'Link';
        link.href = entry.link;
        link.target = '_blank'; // Open link in new tab
        div.appendChild(link);

        container.appendChild(div);
    });
}

// Fetch CSV data and display it
const path = 'lessons-ph_es.csv'

fetchCSV('path')
    .then(data => displayData(data))
    .catch(error => console.error('Error fetching CSV:', error));
