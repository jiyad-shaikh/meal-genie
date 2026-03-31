# Meal Genie Frontend (Phase 2 Progress)

This folder contains the React + Tailwind + PWA frontend for the migration track.
It currently runs separately from Flask templates, but now uses Flask APIs for dynamic data.

## Run locally

```bash
cd ..
python app.py

# in another terminal
cd frontend
npm install
npm run dev
```

## Build

```bash
npm run build
npm run preview
```

React app URL in dev: `http://localhost:5173`

## Included now

- React routes: `/`, `/menu`, `/plan`, `/faq`, `/about`, `/contact`
- Multi-step plan flow connected to Flask `POST /api/meal-plan`
- Plan options from Flask `GET /api/plan-options`
- Menu data from Flask `GET /api/menu-items`
- Tailwind styling with light/dark themes
- PWA plugin setup (`vite-plugin-pwa`)

## Migration plan

1. Finish parity for remaining pages (blog/pricing/privacy/terms).
2. Add payment flow (Razorpay) in React plan/order journey.
3. Decide deployment model: separate frontend or Flask-served React build.
