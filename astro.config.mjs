import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://chellistrings.co.uk',
  integrations: [
    tailwind(),
    sitemap({
      filter: (page) => !page.includes('/thanks'),
    }),
  ],
  image: {
    domains: [],
    remotePatterns: [],
  },
  build: {
    assets: 'assets'
  }
});
