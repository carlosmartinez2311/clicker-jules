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
