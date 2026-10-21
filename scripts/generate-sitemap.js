/**
 * Automated Dynamic Sitemap Generator for LLC Primer
 * Script: scripts/generate-sitemap.js
 *
 * Scans all site pages and state guides to dynamically generate a valid sitemap.xml
 */

const fs = require('fs');
const path = require('path');

const rootDir = path.resolve(__dirname, '..');
const primaryBaseUrl = process.env.NEXT_PUBLIC_SITE_URL || 'https://llcprimer.com';
const currentDate = new Date().toISOString().split('T')[0];

// Extract 50 states from app.js stateData
function getStateSlugs() {
  try {
    const appJsContent = fs.readFileSync(path.join(rootDir, 'app.js'), 'utf8');
    const match = appJsContent.match(/const stateData = (\[[\s\S]*?\]);/);
    if (match) {
      const parsed = eval(match[1]);
      return parsed.map((s) => s.slug);
    }
  } catch (err) {
    console.warn('Could not parse app.js stateData, using fallback slugs');
  }

  return [
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
}

function buildSitemapXml() {
  const stateSlugs = getStateSlugs();
  const allHtmlFiles = fs.readdirSync(rootDir).filter(f => f.endsWith('.html'));

  const baseUrls = [
    primaryBaseUrl,
    'https://llc-primer-eight.vercel.app'
  ];

  // Remove duplicate if primaryBaseUrl is already the vercel domain
  const uniqueBases = Array.from(new Set(baseUrls));

  const urlEntries = [];

  uniqueBases.forEach(baseUrl => {
    // 1. Homepage
    urlEntries.push({
      loc: `${baseUrl}/`,
      lastmod: currentDate,
      changefreq: 'daily',
      priority: '1.0'
    });

    // 2. Core Legal & Transparency Routes
    const legalMap = [
      { file: 'privacy-policy.html', priority: '0.5', changefreq: 'monthly' },
      { file: 'privacy-policy', priority: '0.5', changefreq: 'monthly' },
      { file: 'terms-of-service.html', priority: '0.5', changefreq: 'monthly' },
      { file: 'terms-of-service', priority: '0.5', changefreq: 'monthly' },
      { file: 'affiliate-disclosure.html', priority: '0.5', changefreq: 'monthly' },
      { file: 'disclosure-transparency', priority: '0.5', changefreq: 'monthly' },
      { file: 'editorial-policy.html', priority: '0.5', changefreq: 'monthly' },
      { file: 'how-we-review.html', priority: '0.6', changefreq: 'monthly' },
      { file: 'about.html', priority: '0.5', changefreq: 'monthly' },
      { file: 'contact.html', priority: '0.5', changefreq: 'monthly' },
    ];

    legalMap.forEach(item => {
      urlEntries.push({
        loc: `${baseUrl}/${item.file}`,
        lastmod: currentDate,
        changefreq: item.changefreq,
        priority: item.priority
      });
    });

    // 3. 50-State Guide Slugs
    stateSlugs.forEach(slug => {
      urlEntries.push({
        loc: `${baseUrl}/how-to-start-llc-in-${slug}.html`,
        lastmod: currentDate,
        changefreq: 'monthly',
        priority: '0.8'
      });
      urlEntries.push({
        loc: `${baseUrl}/how-to-start-llc-in-${slug}`,
        lastmod: currentDate,
        changefreq: 'monthly',
        priority: '0.8'
      });
    });

    // 4. Remaining HTML Pages (Calculators, Reviews, Comparisons, Guides)
    const trackedFiles = new Set([
      'index.html',
      ...legalMap.map(l => l.file),
      ...stateSlugs.map(s => `how-to-start-llc-in-${s}.html`)
    ]);

    allHtmlFiles.forEach(file => {
      if (trackedFiles.has(file)) return;

      let priority = '0.7';
      let changefreq = 'monthly';

      if (file.includes('calculator') || file.includes('estimator') || file.includes('tracker') || file === 'tools.html') {
        priority = '0.8';
        changefreq = 'weekly';
      } else if (file.includes('best-') || file.includes('review') || file.includes('-vs-')) {
        priority = '0.7';
        changefreq = 'monthly';
      }

      urlEntries.push({
        loc: `${baseUrl}/${file}`,
        lastmod: currentDate,
        changefreq,
        priority
      });
    });
  });

  // Generate XML Output
  let xml = '<?xml version="1.0" encoding="UTF-8"?>\n';
  xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n';

  urlEntries.forEach(entry => {
    xml += '  <url>\n';
    xml += `    <loc>${entry.loc}</loc>\n`;
    xml += `    <lastmod>${entry.lastmod}</lastmod>\n`;
    xml += `    <changefreq>${entry.changefreq}</changefreq>\n`;
    xml += `    <priority>${entry.priority}</priority>\n`;
    xml += '  </url>\n';
  });

  xml += '</urlset>\n';

  const outputPath = path.join(rootDir, 'sitemap.xml');
  fs.writeFileSync(outputPath, xml, 'utf8');
  console.log(`Successfully generated dynamic sitemap with ${urlEntries.length} URLs at: ${outputPath}`);
}

buildSitemapXml();
