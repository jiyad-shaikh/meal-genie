document.addEventListener("DOMContentLoaded", () => {
  if (localStorage.getItem("theme") === "light") {
    document.body.classList.add("light-mode");
  }

  const toggleBtn = document.getElementById("theme-toggle");
  if (toggleBtn) {
    toggleBtn.addEventListener("click", () => {
      document.body.classList.toggle("light-mode");
      localStorage.setItem(
        "theme",
        document.body.classList.contains("light-mode") ? "light" : "dark"
      );
    });
  }

  const hamburgerMenu = document.getElementById("hamburger-menu");
  const navbarMenu = document.querySelector(".navbar-menu");
  if (hamburgerMenu && navbarMenu) {
    hamburgerMenu.addEventListener("click", () => {
      navbarMenu.classList.toggle("active");
    });
  }
});
