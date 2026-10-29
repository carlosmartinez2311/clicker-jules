# Cookie Clicker Web Application

A simple, interactive web application featuring a cookie in the center that tracks how many times it has been clicked.

## Structure

- `index.html`: Contains the HTML layout and embedded CSS styling.
- `script.js`: Contains the JavaScript logic for click handling, counter updates, cookie persistence, and client-side security measures.

## Features

- **Centered Cookie**: A large cookie icon prominently displayed in the middle of the screen.
- **Click Counter**: Real-time counter showing the total number of clicks.
- **Click Animations & Styling**: Smooth hover and click animation feedback.
- **Browser Cookie Persistence**: Uses browser HTTP cookies (`document.cookie`) so your click count persists across page reloads.
- **Reset Functionality**: Includes a reset button to start the click count over.
- **Client-Side Security Protections**:
  - **Context Menu Prevention**: Right-clicking is disabled to reduce direct inspection.
  - **DevTools Shortcut Blocking**: Disables keyboard shortcuts used to open Developer Tools (such as F12, Ctrl+Shift+I/J/C, and Ctrl+U) to discourage casual tampering with cookie values.
  - *Note*: Client-side protections provide basic deterrence against casual manipulation; robust application security requires server-side validation.

## How to Run

1. Open `index.html` in any modern web browser (e.g. Chrome, Firefox, Safari, Edge).
2. Click the cookie in the middle to start baking cookies!
