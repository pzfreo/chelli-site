import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  site: 'https://chellistrings.co.uk',
  integrations: [tailwind()],
  image: {
    domains: [],
    remotePatterns: [],
  },
  build: {
    assets: 'assets'
  }
});
