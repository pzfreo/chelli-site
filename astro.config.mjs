import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://chellistrings.co.uk',
  integrations: [
    sitemap({
      filter: (page) => !page.includes('/thanks'),
    }),
  ],
  vite: {
    plugins: [tailwindcss()],
  },
  image: {
    domains: [],
    remotePatterns: [],
  },
  build: {
    assets: 'assets'
  }
});
