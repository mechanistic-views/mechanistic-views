import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import mdx from '@astrojs/mdx';
import { execSync } from 'child_process';
import remarkMath from 'remark-math';
import remarkGfm from 'remark-gfm';
import rehypeKatex from 'rehype-katex';
import starlightImageZoom from 'starlight-image-zoom';

export default defineConfig({
  site: 'https://mechanistic-validity.github.io',
  base: '/mechanistic-views',
  markdown: {
    remarkPlugins: [remarkMath],
    rehypePlugins: [rehypeKatex],
  },
  integrations: [
    {
      name: 'build-backlinks',
      hooks: {
        'astro:build:start': () => execSync('node scripts/build-backlinks.mjs'),
        'astro:server:start': () => execSync('node scripts/build-backlinks.mjs'),
      },
    },
    starlight({
      plugins: [starlightImageZoom()],
      title: 'Mechanistic Views',
      lastUpdated: false,
      description: 'A five-axis ontology for mechanistic interpretability: what mechanisms are, how we know them, when two are the same, and what follows from each stance',
      customCss: ['./src/styles/custom.css'],
      expressiveCode: {
        themes: ['github-dark', 'github-light'],
        styleOverrides: {
          borderRadius: '0.375rem',
        },
      },
      components: {
        Pagination: './src/components/PageFooter.astro',
        PageTitle: './src/components/PageTitle.astro',
        ThemeSelect: './src/components/ThemeSelect.astro',
      },
      sidebar: [
        { label: 'Home', link: '/' },
        {
          label: 'Framework',
          collapsed: false,
          items: [
            { label: 'Overview', link: '/framework/' },
            { label: 'Methods', link: '/methods/' },
            { label: 'Mechanistic Validity Interface', link: '/mechval-interface/' },
            { label: 'Glossary', link: '/glossary/' },
            { label: 'About & Citation', link: '/about_cite/' },
          ],
        },
        {
          label: 'Views',
          collapsed: false,
          items: [
            { label: 'Overview', link: '/views/' },
            { label: 'Instrumental', link: '/views/instrumental/' },
            { label: 'Perspectival', link: '/views/perspectival/' },
            { label: 'Object', link: '/views/object/' },
            { label: 'Role', link: '/views/role/' },
            { label: 'Subspace', link: '/views/subspace/' },
            { label: 'Structural', link: '/views/structural/' },
            { label: 'Process', link: '/views/process/' },
            { label: 'Stratified', link: '/views/stratified/' },
            { label: 'View Mappings', link: '/views/mappings/' },
          ],
        },
        {
          label: 'Formalisms',
          collapsed: true,
          items: [
            { label: 'Overview', link: '/formalism/' },
            { label: 'Model Theory', link: '/formalism/model-theory/' },
            { label: 'Measurement Algebra', link: '/formalism/measurement-algebra/' },
            { label: 'Directed Graph', link: '/formalism/directed-graph/' },
            { label: 'Role Graph', link: '/formalism/role-graph/' },
            { label: 'Grassmannian', link: '/formalism/grassmannian/' },
            { label: 'Fiber Bundle Quotient', link: '/formalism/fiber-bundle-quotient/' },
            { label: 'Dynamical System', link: '/formalism/dynamical-system/' },
            { label: 'Whitney Stratification', link: '/formalism/stratification/' },
            { label: 'Causal Graph', link: '/formalism/causal-graph/' },
            { label: 'Linear Classifier', link: '/formalism/linear-classifier/' },
            { label: 'Dictionary', link: '/formalism/dictionary/' },
            { label: 'Linear Projection', link: '/formalism/linear-projection/' },
            { label: 'Information Theory', link: '/formalism/information-theory/' },
            { label: 'Category Theory', link: '/formalism/category-theory/' },
            { label: 'Representation Theory', link: '/formalism/representation-theory/' },
            {
              label: 'Deep Dives',
              collapsed: true,
              items: [
                { label: 'Overview', link: '/formalism/deep-dives/' },
                { label: 'Grassmannian Geometry', link: '/formalism/deep-dives/grassmannian/' },
                { label: 'Gauge Quotients & Holonomy', link: '/formalism/deep-dives/gauge-holonomy/' },
                { label: 'Sheaf Cohomology', link: '/formalism/deep-dives/sheaves/' },
                { label: 'Stratification', link: '/formalism/deep-dives/stratification/' },
              ],
            },
          ],
        },
        // Decisions, Case Studies, and Open Problem Map hidden — content is half-baked
        // Pages still exist at their URLs but are not linked from the sidebar
      ],
    }),
    mdx({
      remarkPlugins: [remarkGfm, remarkMath],
      rehypePlugins: [rehypeKatex],
    }),
  ],
});
