function getCookie(name) {
  const nameEQ = name + "=";
  const ca = document.cookie.split(';');
  for (let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) === ' ') c = c.substring(1, c.length);
    if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
  }
  return null;
}

function setCookie(name, value, days = 365) {
  const date = new Date();
  date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
  const expires = "; expires=" + date.toUTCString();
  document.cookie = name + "=" + (value || "0") + expires + "; path=/; SameSite=Lax";
}

// Disable right-click context menu
document.addEventListener('contextmenu', (e) => {
  e.preventDefault();
});

// Disable developer tools shortcuts
document.addEventListener('keydown', (e) => {
  const isCmdOrCtrl = e.ctrlKey || e.metaKey;
  const key = e.key.toLowerCase();

  // F12 key
  if (e.key === 'F12' || e.keyCode === 123) {
    e.preventDefault();
    return false;
  }

  // Ctrl+Shift+I / Cmd+Option+I (Inspect element)
  // Ctrl+Shift+J / Cmd+Option+J (Console)
  // Ctrl+Shift+C / Cmd+Option+C (Inspect element selection)
  if ((isCmdOrCtrl && e.shiftKey && (key === 'i' || key === 'j' || key === 'c')) ||
      (e.metaKey && e.altKey && (key === 'i' || key === 'j' || key === 'c'))) {
    e.preventDefault();
    return false;
  }

  // Ctrl+U / Cmd+Option+U (View source)
  if ((isCmdOrCtrl && key === 'u') || (e.metaKey && e.altKey && key === 'u')) {
    e.preventDefault();
    return false;
  }
});

document.addEventListener('DOMContentLoaded', () => {
  const countEl = document.getElementById('count');
  const cookieBtn = document.getElementById('cookie-btn');
  const resetBtn = document.getElementById('reset-btn');

  let count = parseInt(getCookie('cookieCount')) || 0;
  countEl.textContent = count;

  cookieBtn.addEventListener('click', () => {
    count++;
    countEl.textContent = count;
    setCookie('cookieCount', count, 365);
  });

  resetBtn.addEventListener('click', () => {
    count = 0;
    countEl.textContent = count;
    setCookie('cookieCount', count, 365);
  });
});
