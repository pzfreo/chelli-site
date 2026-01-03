import { defineCollection, z } from 'astro:content';

const instruments = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    subtitle: z.string(),
    type: z.enum(['viol', 'violin', 'fiddle', 'guitar']),
    status: z.enum(['for-sale', 'sold', 'not-for-sale']),
    price: z.number().optional(),
    featuredImage: z.string(),
    images: z.array(z.string()),
    order: z.number().default(0),
  }),
});

export const collections = {
  instruments,
};
