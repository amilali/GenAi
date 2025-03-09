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
  
      // Or if using `src` directory:
      "./src/**/*.{js,ts,jsx,tsx,mdx}",
    ],
    theme: {
      extend: {
        animation: {
          shimmer: "shimmer 2s linear infinite"
        },
        keyframes: {
          shimmer: {
            from: {
              backgroundPosition: "0 0"
            },
            to: {
              backgroundPosition: "-200% 0"
            }
          }
        }
      },
    },
    plugins: [animate,addVariablesForColors],
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
  