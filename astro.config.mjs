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
    // Keep bundled scripts in external files so the CSP needs no per-build hashes.
    build: { assetsInlineLimit: 0 },
  },
  image: {
    domains: [],
    remotePatterns: [],
  },
  build: {
    assets: 'assets'
  }
});
