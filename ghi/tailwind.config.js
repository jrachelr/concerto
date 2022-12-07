/** @type {import('tailwindcss').Config} */
const { blue } = require("tailwindcss/colors");

module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      backgroundImage: {
        hero: "url('/public/background.jpg')",
      },
      colors: {
        primary: blue,
      },
    },
  },
  plugins: [require("@tailwindcss/forms")],
};
