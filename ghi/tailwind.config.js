/** @type {import('tailwindcss').Config} */
const { blue } = require("tailwindcss/colors");

module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: blue,
      },
    },
  },
  plugins: [require("@tailwindcss/forms")],
};
