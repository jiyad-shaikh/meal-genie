
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

// WhatsApp Sharing
document.getElementById('send-whatsapp').addEventListener('click', (e) => {
  e.preventDefault();
  const planText = `Meal Genie Plan\n\nProfile: {{ gender|capitalize }}, {{ age }}, {{ activity|capitalize }} activity\n\n` +
    `{% for meal_time, meals in meal_plans.items() %}` +
    `{{ meal_time|capitalize }}:\n` +
    `{% if meals is iterable and meals is not string %}` +
    `{% for meal in meals %}` +
    `- {{ meal.item }} ({{ meal.quantity }})\n` +
    `  Calories: {{ meal.calories }}kcal\n` +
    `  Protein: {{ meal.protein }}g\n` +
    `  Carbs: {{ meal.carbs }}g\n` +
    `  Fats: {{ meal.fats }}g\n\n` +
    `{% endfor %}` +
    `{% else %}` +
    `- {{ meals.item }} ({{ meals.quantity }})\n` +
    `  Calories: {{ meals.calories }}kcal\n` +
    `  Protein: {{ meals.protein }}g\n` +
    `  Carbs: {{ meals.carbs }}g\n` +
    `  Fats: {{ meals.fats }}g\n\n` +
    `{% endif %}` +
    `{% endfor %}` +
    `Tip: {{ healthy_tip if healthy_tip else 'Stay hydrated!' }}`;

  window.open(`https://wa.me/?text=${encodeURIComponent(planText)}`, '_blank');
});

// Email Sharing
document.getElementById('send-email').addEventListener('click', () => {
  const planText = `Meal Genie Plan\n\nProfile: {{ gender|capitalize }}, {{ age }}, {{ activity|capitalize }} activity\n\n` +
    `{% for meal_time, meals in meal_plans.items() %}` +
    `{{ meal_time|capitalize }}:\n` +
    `{% if meals is iterable and meals is not string %}` +
    `{% for meal in meals %}` +
    `- {{ meal.item }} ({{ meal.quantity }})\n` +
    `  Calories: {{ meal.calories }}kcal\n` +
    `  Protein: {{ meal.protein }}g\n` +
    `  Carbs: {{ meal.carbs }}g\n` +
    `  Fats: {{ meal.fats }}g\n\n` +
    `{% endfor %}` +
    `{% else %}` +
    `- {{ meals.item }} ({{ meals.quantity }})\n` +
    `  Calories: {{ meals.calories }}kcal\n` +
    `  Protein: {{ meals.protein }}g\n` +
    `  Carbs: {{ meals.carbs }}g\n` +
    `  Fats: {{ meals.fats }}g\n\n` +
    `{% endif %}` +
    `{% endfor %}` +
    `Tip: {{ healthy_tip if healthy_tip else 'Stay hydrated!' }}`;

  window.location.href = `mailto:?subject=Meal%20Genie%20Plan&body=${encodeURIComponent(planText)}`;
});


// Load theme
if (localStorage.getItem('theme') === 'light') {
  document.body.classList.add('light-mode');
}

