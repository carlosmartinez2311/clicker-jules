# Cookie Clicker Web App

A simple, interactive web application featuring a cookie in the center that tracks how many times it has been clicked.

## Structure

- `index.html`: Contains the HTML layout and embedded CSS styling.
- `script.js`: Contains the JavaScript logic for click handling, counter updates, and cookie-based persistence.

## Features

- **Centered Cookie**: A large cookie icon prominently displayed in the middle of the screen.
- **Click Counter**: Real-time counter showing the total number of clicks.
- **Click Animations & Styling**: Smooth hover and click animation feedback.
- **Browser Cookie Persistence**: Uses browser HTTP cookies (`document.cookie`) so your click count persists across page reloads.
- **Reset Functionality**: Includes a reset button to start the click count over.

## How to Run

1. Clone or download this repository.
2. Open `index.html` directly in any standard web browser (e.g., Chrome, Firefox, Safari, Edge) or serve via a web server.
3. Serve the files using a simple local web server:
   ```bash
   npx serve .
   # or
   python3 -m http.server 8000
   ```
4. Click the cookie and watch your count grow!
