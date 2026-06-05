import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import { execSync } from 'child_process';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

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
      title: 'Mechanistic Views',
      description: 'An atlas of what mechanisms are, how we know them, when two are the same, and what follows from each stance',
      customCss: ['./src/styles/custom.css'],
      expressiveCode: {
        themes: ['github-dark', 'github-light'],
        styleOverrides: {
          borderRadius: '0.375rem',
        },
      },
      components: {
        Pagination: './src/components/PageFooter.astro',
      },
      sidebar: [
        { label: 'Home', link: '/' },
        {
          label: 'Framework',
          collapsed: false,
          items: [
            { label: 'Overview', link: '/framework/' },
            { label: 'Methods', link: '/methods/' },
            { label: 'MechVal Interface', link: '/mechval-interface/' },
            { label: 'Glossary', link: '/glossary/' },
          ],
        },
        {
          label: 'Views',
          collapsed: false,
          items: [
            { label: 'Overview', link: '/views/' },
            { label: 'Object', link: '/views/object/' },
            { label: 'Role', link: '/views/role/' },
            { label: 'Subspace', link: '/views/subspace/' },
            { label: 'Structural', link: '/views/structural/' },
            { label: 'Process', link: '/views/process/' },
            { label: 'Stratified', link: '/views/stratified/' },
            { label: 'Perspectival', link: '/views/perspectival/' },
            { label: 'Instrumental', link: '/views/instrumental/' },
          ],
        },
        {
          label: 'Formalisms',
          collapsed: true,
          items: [
            { label: 'Overview', link: '/formalism/' },
            { label: 'Grassmannian Geometry', link: '/formalism/grassmannian/' },
            { label: 'Gauge Quotients & Holonomy', link: '/formalism/gauge-holonomy/' },
            { label: 'Sheaf Cohomology', link: '/formalism/sheaves/' },
            { label: 'Stratification', link: '/formalism/stratification/' },
          ],
        },
        {
          label: 'Decisions',
          collapsed: true,
          items: [
            { label: 'Overview', link: '/decisions/' },
            { label: 'Object vs. Role', link: '/decisions/object-vs-role/' },
            { label: 'Subspace vs. Structural', link: '/decisions/subspace-vs-structural/' },
            { label: 'Localized vs. Distributed', link: '/decisions/localized-vs-distributed/' },
            { label: 'Single vs. Triangulated', link: '/decisions/single-vs-triangulated/' },
            { label: 'Static vs. Process', link: '/decisions/static-vs-process/' },
          ],
        },
        {
          label: 'Case Studies',
          collapsed: true,
          items: [
            { label: 'Overview', link: '/cases/' },
            { label: 'IOI Circuit', link: '/cases/ioi/' },
            { label: 'Induction Heads', link: '/cases/induction/' },
            { label: 'Grokking', link: '/cases/grokking/' },
            { label: 'Hallucination', link: '/cases/hallucination/' },
            { label: 'Self-Knowledge', link: '/cases/self-knowledge/' },
          ],
        },
      ],
    }),
  ],
});
