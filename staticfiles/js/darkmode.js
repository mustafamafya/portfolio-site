// static/js/theme.js
document.addEventListener('DOMContentLoaded', function() {
  const toggleBtn = document.getElementById('theme-toggle');
  const body = document.body;

  // Exit if button is missing
  if (!toggleBtn) {
    console.error('Theme toggle button not found');
    return;
  }

  // 1) Initialize from localStorage
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme === 'dark') {
    body.classList.add('dark-theme');
    toggleBtn.textContent = '☀️';
  }

  // 2) Listen for clicks to toggle
  toggleBtn.addEventListener('click', function() {
    const isDark = body.classList.toggle('dark-theme');
    toggleBtn.textContent = isDark ? '☀️' : '🌙';
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
  });
});