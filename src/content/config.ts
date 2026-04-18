import { defineCollection, z } from 'astro:content';

const instruments = defineCollection({
  type: 'content',
  schema: ({ image }) => z.object({
    title: z.string(),
    subtitle: z.string(),
    type: z.enum(['viol', 'violin', 'fiddle', 'guitar', 'salter', 'mandolin']),
    status: z.enum(['for-sale', 'sold', 'not-for-sale']),
    price: z.number().optional(),
    featuredImage: image(),
    images: z.array(image()),
    order: z.number().default(0),
  }),
});

export const collections = {
  instruments,
};
