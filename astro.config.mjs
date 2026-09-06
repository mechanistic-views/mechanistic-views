import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import mdx from '@astrojs/mdx';
import { execSync } from 'child_process';
import remarkMath from 'remark-math';
import remarkGfm from 'remark-gfm';
import rehypeKatex from 'rehype-katex';
import starlightImageZoom from 'starlight-image-zoom';

export default defineConfig({
  site: 'https://mechanistic-views.github.io',
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
            { label: 'Using the Framework', link: '/framework/using/' },
            { label: 'Cross-View Promotion', link: '/framework/cross-view-promotion/' },
            { label: 'Methods', link: '/methods/' },
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
            { label: 'Contrastive', link: '/views/contrastive/' },
            { label: 'View Mappings', link: '/views/mappings/' },
            { label: 'View Assessment', link: '/views/assessment/' },
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
        {
          label: 'Decision Points',
          collapsed: false,
          items: [
            { label: 'Overview', link: '/decisions/' },
            { label: 'Object vs. Role', link: '/decisions/object-vs-role/' },
            { label: 'Subspace vs. Structural', link: '/decisions/subspace-vs-structural/' },
            { label: 'Localized vs. Distributed', link: '/decisions/localized-vs-distributed/' },
            { label: 'Single vs. Triangulated', link: '/decisions/single-vs-triangulated/' },
            { label: 'Static vs. Process', link: '/decisions/static-vs-process/' },
            { label: 'Behavioral vs. Mechanistic', link: '/decisions/behavioral-vs-mechanistic/' },
          ],
        },
        {
          label: 'Worked Examples',
          collapsed: false,
          items: [
            { label: 'Overview', link: '/cases/' },
            { label: 'Indirect Object Identification', link: '/cases/ioi/' },
            { label: 'Induction Heads', link: '/cases/induction/' },
            { label: 'Superposition', link: '/cases/superposition/' },
            { label: 'Grokking', link: '/cases/grokking/' },
            { label: 'Hallucination', link: '/cases/hallucination/' },
            { label: 'Self-Knowledge', link: '/cases/self-knowledge/' },
          ],
        },
        {
          label: 'Open Problems',
          collapsed: true,
          items: [
            { label: 'Problem Map', link: '/open-problems/' },
            { label: 'Decomposition Identity', link: '/open-problems/decomposition-identity/' },
            { label: 'SAE "True" Features', link: '/open-problems/sae-true-features/' },
            { label: 'Superposition', link: '/open-problems/superposition/' },
            { label: 'Circuit Disagreements', link: '/open-problems/circuit-disagreements/' },
            { label: 'Unit of Analysis', link: '/open-problems/unit-of-analysis/' },
            { label: 'Intervention Limits', link: '/open-problems/intervention-limits/' },
            { label: 'Linear Assumption', link: '/open-problems/linear-assumption/' },
            { label: 'Probe Features', link: '/open-problems/probe-features/' },
            { label: 'Safety Evidence Gaps', link: '/open-problems/safety-evidence-gaps/' },
            { label: 'Cross-Model Identity', link: '/open-problems/cross-model-identity/' },
            { label: 'CoT Faithfulness', link: '/open-problems/cot-faithfulness/' },
            { label: 'Validation Methodology', link: '/open-problems/validation-methodology/' },
            { label: 'Training Dynamics', link: '/open-problems/training-dynamics/' },
            { label: 'Resolution & Completeness', link: '/open-problems/resolution-completeness/' },
            { label: 'Deceptive Alignment', link: '/open-problems/deceptive-alignment/' },
            { label: 'World Models', link: '/open-problems/world-models/' },
          ],
        },
      ],
    }),
    mdx({
      remarkPlugins: [remarkGfm, remarkMath],
      rehypePlugins: [rehypeKatex],
    }),
  ],
});
