/** @type {import('tailwindcss').Config} */
const defaultTheme = require("tailwindcss/defaultTheme");
const colors = require("tailwindcss/colors");
import animate from "tailwindcss-animate"
const {
    default: flattenColorPalette,
  } = require("tailwindcss/lib/util/flattenColorPalette");

module.exports = {
    content: [
      "./app/**/*.{js,ts,jsx,tsx,mdx}",
      "./pages/**/*.{js,ts,jsx,tsx,mdx}",
      "./components/**/*.{js,ts,jsx,tsx,mdx}",
      "./src/**/*.{js,ts,jsx,tsx,mdx}",
    ],
    theme: {
      extend: {
        animation: {
          'shimmer': 'shimmer 2s linear infinite',
          'shine': 'shine 2s linear infinite',
          'spotlight': 'spotlight 2s ease .75s infinite',
        },
        keyframes: {
          shimmer: {
            from: { backgroundPosition: "0 0" },
            to: { backgroundPosition: "-200% 0" }
          },
          shine: {
            'from': { backgroundPosition: '200% center' },
            'to': { backgroundPosition: '-200% center' }
          },
          spotlight: {
            "0%": {
              opacity: 0,
              transform: "translate(-72%, -62%) scale(0.5)",
            },
            "100%": {
              opacity: 1,
              transform: "translate(-50%,-40%) scale(1)",
            },
          },
        },
        backgroundImage: {
          "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
          "gradient-conic":
            "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
        },
      },
    },
    plugins: [animate, addVariablesForColors],
};

function addVariablesForColors({ addBase, theme }: any) {
    let allColors = flattenColorPalette(theme("colors"));
    let newVars = Object.fromEntries(
      Object.entries(allColors).map(([key, val]) => [`--${key}`, val])
    );
   
    addBase({
      ":root": newVars,
    });
} 