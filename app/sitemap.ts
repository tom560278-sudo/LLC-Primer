import { MetadataRoute } from 'next';

/**
 * Native Next.js Dynamic Sitemap Generator (App Router)
 * File: app/sitemap.ts
 *
 * Programmatically maps core static routes, all 50-state formation guides,
 * comparison reviews, and calculator tools.
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

export default function sitemap(): MetadataRoute.Sitemap {
  const currentDate = new Date().toISOString().split('T')[0];

  // 1. Core Static Routes (Homepage, Legal & Transparency)
  const coreRoutes: MetadataRoute.Sitemap = [
    {
      url: `${BASE_URL}/`,
      lastModified: currentDate,
      changeFrequency: 'daily',
      priority: 1.0,
    },
    {
      url: `${BASE_URL}/privacy-policy`,
      lastModified: currentDate,
      changeFrequency: 'monthly',
      priority: 0.5,
    },
    {
      url: `${BASE_URL}/privacy-policy.html`,
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
    {
      url: `${BASE_URL}/terms-of-service.html`,
      lastModified: currentDate,
      changeFrequency: 'monthly',
      priority: 0.5,
    },
    {
      url: `${BASE_URL}/disclosure-transparency`,
      lastModified: currentDate,
      changeFrequency: 'monthly',
      priority: 0.5,
    },
    {
      url: `${BASE_URL}/affiliate-disclosure.html`,
      lastModified: currentDate,
      changeFrequency: 'monthly',
      priority: 0.5,
    },
    {
      url: `${BASE_URL}/editorial-policy.html`,
      lastModified: currentDate,
      changeFrequency: 'monthly',
      priority: 0.5,
    },
    {
      url: `${BASE_URL}/how-we-review.html`,
      lastModified: currentDate,
      changeFrequency: 'monthly',
      priority: 0.6,
    },
    {
      url: `${BASE_URL}/about.html`,
      lastModified: currentDate,
      changeFrequency: 'monthly',
      priority: 0.5,
    },
    {
      url: `${BASE_URL}/contact.html`,
      lastModified: currentDate,
      changeFrequency: 'monthly',
      priority: 0.5,
    },
  ];

  // 2. Programmatically Mapped 50-State Guide Slugs
  const stateRoutes: MetadataRoute.Sitemap = stateSlugs.flatMap((slug) => [
    {
      url: `${BASE_URL}/how-to-start-llc-in-${slug}.html`,
      lastModified: currentDate,
      changeFrequency: 'monthly',
      priority: 0.8,
    },
    {
      url: `${BASE_URL}/how-to-start-llc-in-${slug}`,
      lastModified: currentDate,
      changeFrequency: 'monthly',
      priority: 0.8,
    },
  ]);

  // 3. Calculators, Tools & Compliance Trackers
  const toolRoutes: MetadataRoute.Sitemap = [
    'llc-cost-calculator.html',
    'llc-startup-cost-estimator.html',
    'llc-annual-report-tracker.html',
    'sos-search.html',
    'tools.html',
    'quiz.html',
    'start-llc.html',
  ].map((slug) => ({
    url: `${BASE_URL}/${slug}`,
    lastModified: currentDate,
    changeFrequency: 'weekly' as const,
    priority: 0.8,
  }));

  // 4. Comparison, Formation Service Reviews & Pillar Guides
  const guideRoutes: MetadataRoute.Sitemap = [
    'best-llc-services.html',
    'best-llc-formation-services.html',
    'best-registered-agent-services.html',
    'best-state-to-form-an-llc.html',
    'northwest-registered-agent-review.html',
    'doola-vs-northwest.html',
    'northwest-vs-legalzoom.html',
    'tailor-brands-vs-legalzoom.html',
    'tailor-brands-vs-northwest.html',
    'tailor-brands-vs-zenbusiness.html',
    'zenbusiness-vs-bizee.html',
    'zenbusiness-vs-legalzoom.html',
    'zenbusiness-vs-northwest.html',
    'what-is-an-llc.html',
    'how-are-llcs-taxed.html',
    'how-much-does-an-llc-cost.html',
    'how-to-dissolve-an-llc.html',
    'how-to-pay-yourself-llc.html',
    'llc-guide.html',
    'llc-tax-benefits.html',
    'llc-vs-corporation.html',
    'llc-vs-scorp.html',
    'llc-vs-sole-proprietorship.html',
    'single-member-llc.html',
    'multi-member-llc.html',
    'series-llc.html',
    'registered-agent-guide.html',
    'operating-agreement.html',
    'ein-guide.html',
    'business-setup.html',
    'dba-vs-llc.html',
    'do-llc-get-1099.html',
    'pllc-vs-llc.html',
    'virtual-business-address.html',
    'best-business-bank-accounts.html',
    'llc-business-insurance.html',
    'llc-for-amazon-etsy-sellers.html',
    'llc-for-real-estate.html',
    'llc-for-rental-property.html',
    'non-resident-llc-guide.html',
    'best-state-for-non-us-residents.html',
    'bank-account-for-non-residents.html',
    'ein-guide-for-non-residents.html',
    'llc-cost-for-non-residents.html',
  ].map((slug) => ({
    url: `${BASE_URL}/${slug}`,
    lastModified: currentDate,
    changeFrequency: 'monthly' as const,
    priority: 0.7,
  }));

  return [...coreRoutes, ...stateRoutes, ...toolRoutes, ...guideRoutes];
}
