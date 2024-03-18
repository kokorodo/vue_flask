/** @type {import('tailwindcss').Config} */
export default {

  darkMode: false, // or 'media' or 'class'
  content: [
          './index.html',
          './src/**/*.{vue,js,ts,jsx,tsx}',
          './node_modules/vue-tailwind-datatable/src/**/*.vue'
        ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}

