/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx,ts,tsx}'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#eefdf4',
          100: '#d4f9e3',
          200: '#a9f3c9',
          300: '#73e8a9',
          400: '#43d988',
          500: '#1fbd6c',
          600: '#149b57',
          700: '#137a46',
          800: '#145f38',
          900: '#124d31',
        },
      },
      boxShadow: {
        soft: '0 14px 34px rgba(3, 14, 10, 0.14)',
      },
    },
  },
  plugins: [],
}
