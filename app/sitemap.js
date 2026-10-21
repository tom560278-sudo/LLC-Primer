/**
 * Native Next.js Dynamic Sitemap Generator (App Router)
 * File: app/sitemap.js
 *
 * Programmatically maps core static routes, all 50-state formation guides,
 * comparison reviews, and calculator tools using canonical URLs on https://llcprimer.com.
 */

const BASE_URL = process.env.NEXT_PUBLIC_SITE_URL || 'https://llcprimer.com';

// 50 State Slugs matching the LLC Primer state database
export const stateSlugs = [
  'alabama', 'alaska', 'arizona', 'arkansas', 'california',
  'colorado', 'connecticut', 'delaware', 'florida', 'georgia',
  'hawaii', 'idaho', 'illinois', 'indiana', 'iowa',
  'kansas', 'kentucky', 'louisiana', 'maine', 'maryland',
  'massachusetts', 'michigan', 'minnesota', 'mississippi', 'missouri',
  'montana', 'nebraska', 'nevada', 'new-hampshire', 'new-jersey',
  'new-mexico', 'new-york', 'north-carolina', 'north-dakota', 'ohio',
  'oklahoma', 'oregon', 'pennsylvania', 'rhode-island', 'south-carolina',
  'south-dakota', 'tennessee', 'texas', 'utah', 'vermont',
  'virginia', 'washington', 'west-virginia', 'wisconsin', 'wyoming'
];

export default function sitemap() {
  const currentDate = new Date().toISOString().split('T')[0];

  // 1. Core Static Routes (Homepage, Legal & Transparency) - 8 URLs
  const coreRoutes = [
    {
      url: `${BASE_URL}/`,
      lastModified: currentDate,
      changeFrequency: 'daily',
      priority: 1.0,
    },
    {
      url: `${BASE_URL}/about`,
      lastModified: currentDate,
      changeFrequency: 'monthly',
      priority: 0.5,
    },
    {
      url: `${BASE_URL}/affiliate-disclosure`,
      lastModified: currentDate,
      changeFrequency: 'monthly',
      priority: 0.5,
    },
    {
      url: `${BASE_URL}/contact`,
      lastModified: currentDate,
      changeFrequency: 'monthly',
      priority: 0.5,
    },
    {
      url: `${BASE_URL}/editorial-policy`,
      lastModified: currentDate,
      changeFrequency: 'monthly',
      priority: 0.5,
    },
    {
      url: `${BASE_URL}/how-we-review`,
      lastModified: currentDate,
      changeFrequency: 'monthly',
      priority: 0.6,
    },
    {
      url: `${BASE_URL}/privacy-policy`,
      lastModified: currentDate,
      changeFrequency: 'monthly',
      priority: 0.5,
    },
    {
      url: `${BASE_URL}/terms-of-service`,
      lastModified: currentDate,
      changeFrequency: 'monthly',
      priority: 0.5,
    },
  ];

  // 2. Programmatically Mapped 50-State Guide Slugs - 50 URLs
  const stateRoutes = stateSlugs.map((slug) => ({
    url: `${BASE_URL}/how-to-start-llc-in-${slug}`,
    lastModified: currentDate,
    changeFrequency: 'monthly',
    priority: 0.8,
  }));

  // 3. Calculators, Tools & Compliance Trackers - 7 URLs
  const toolRoutes = [
    'llc-annual-report-tracker',
    'llc-cost-calculator',
    'llc-startup-cost-estimator',
    'quiz',
    'sos-search',
    'start-llc',
    'tools',
  ].map((slug) => ({
    url: `${BASE_URL}/${slug}`,
    lastModified: currentDate,
    changeFrequency: 'weekly',
    priority: 0.8,
  }));

  // 4. Comparison, Formation Service Reviews & Pillar Guides - 44 URLs
  const guideRoutes = [
    'bank-account-for-non-residents',
    'best-business-bank-accounts',
    'best-llc-formation-services',
    'best-llc-services',
    'best-registered-agent-services',
    'best-state-for-non-us-residents',
    'best-state-to-form-an-llc',
    'business-setup',
    'dba-vs-llc',
    'do-llc-get-1099',
    'doola-vs-northwest',
    'ein-guide-for-non-residents',
    'ein-guide',
    'how-are-llcs-taxed',
    'how-much-does-an-llc-cost',
    'how-to-dissolve-an-llc',
    'how-to-pay-yourself-llc',
    'llc-business-insurance',
    'llc-cost-for-non-residents',
    'llc-for-amazon-etsy-sellers',
    'llc-for-real-estate',
    'llc-for-rental-property',
    'llc-guide',
    'llc-tax-benefits',
    'llc-vs-corporation',
    'llc-vs-scorp',
    'llc-vs-sole-proprietorship',
    'multi-member-llc',
    'non-resident-llc-guide',
    'northwest-registered-agent-review',
    'northwest-vs-legalzoom',
    'operating-agreement',
    'pllc-vs-llc',
    'registered-agent-guide',
    'series-llc',
    'single-member-llc',
    'tailor-brands-vs-legalzoom',
    'tailor-brands-vs-northwest',
    'tailor-brands-vs-zenbusiness',
    'virtual-business-address',
    'what-is-an-llc',
    'zenbusiness-vs-bizee',
    'zenbusiness-vs-legalzoom',
    'zenbusiness-vs-northwest',
  ].map((slug) => ({
    url: `${BASE_URL}/${slug}`,
    lastModified: currentDate,
    changeFrequency: 'monthly',
    priority: 0.7,
  }));

  return [...coreRoutes, ...stateRoutes, ...toolRoutes, ...guideRoutes];
}
