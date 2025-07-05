
const toggleBtn = document.getElementById("theme-toggle");
toggleBtn.addEventListener("click", () => {
  document.body.classList.toggle("light-mode");
  localStorage.setItem('theme', document.body.classList.contains('light-mode') ? 'light' : 'dark');
});

// Load theme on page load
window.addEventListener('DOMContentLoaded', () => {
  if (localStorage.getItem('theme') === 'light') {
    document.body.classList.add('light-mode');
  }
});

const hamburgerMenu = document.getElementById("hamburger-menu");
const navbarMenu = document.querySelector(".navbar-menu");
hamburgerMenu.addEventListener("click", () => {
  navbarMenu.classList.toggle("active");
});

// Load theme
if (localStorage.getItem('theme') === 'light') {
  document.body.classList.add('light-mode');
}