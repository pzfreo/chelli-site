/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        charcoal: '#1a1a1a',
        offwhite: '#fafafa',
        warmgold: '#b8860b',
        cream: '#f5f5f0',
      },
      fontFamily: {
        serif: ['Playfair Display', 'Georgia', 'serif'],
        sans: ['Inter', 'system-ui', 'sans-serif'],
        script: ['Mrs Saint Delafield', 'cursive'],
      },
      fontSize: {
        '7xl': '5rem',
        '8xl': '6rem',
      },
      spacing: {
        '128': '32rem',
        '144': '36rem',
      },
      aspectRatio: {
        '4/3': '4 / 3',
        '3/4': '3 / 4',
      },
    },
  },
  plugins: [],
};
