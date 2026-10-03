import re

header_nav_footer = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{meta}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
  <style>
    .guide-content-container{max-width:1080px;margin:0 auto;padding:0 1.5rem 3.5rem 1.5rem;width:100%;box-sizing:border-box}
    .guide-article h2{font-size:clamp(1.75rem,3.2vw,2.3rem);font-weight:800;color:#12304A;margin:2.75rem 0 1.25rem 0;font-family:var(--font-heading);line-height:1.25}
    .guide-article h3{font-size:clamp(1.15rem,2.2vw,1.45rem);font-weight:700;color:#12304A;margin:2rem 0 1rem 0;font-family:var(--font-heading);line-height:1.3}
    .guide-article h4{font-size:1.05rem;font-weight:700;color:#12304A;margin:1.5rem 0 0.65rem 0}
    .guide-article p{font-size:1rem;line-height:1.75;color:#334155;margin-bottom:1.25rem}
    .guide-article a{color:#159A9C;font-weight:600;text-decoration:underline}
    .guide-article a:hover{color:#0E7490}
    .guide-article ul,.guide-article ol{padding-left:1.65rem!important;margin-bottom:1.5rem!important}
    .guide-article ul li,.guide-article ol li{margin-bottom:0.65rem!important;line-height:1.7!important;color:#334155!important}
    .source-banner-box{background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:0.85rem 1.15rem;font-size:0.875rem;color:#475569;margin-bottom:1.5rem}
    .toc-card-box{background:#F8FAFC;border:1.5px solid #CBD5E1;border-radius:16px;padding:1.5rem 1.75rem;margin-bottom:3rem;box-shadow:0 4px 16px rgba(18,48,74,0.04)}
    .toc-card-box h3{font-size:0.95rem;font-weight:800;color:#12304A;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:1rem;margin-top:0}
    .toc-links-ol{margin:0;padding-left:1.35rem;display:flex;flex-direction:column;gap:0.5rem}
    .toc-links-ol li a{color:#159A9C;font-weight:600;font-size:0.925rem;text-decoration:none}
    .toc-links-ol li a:hover{text-decoration:underline}
    .callout-red{background:#FEE2E2;border:1.5px solid #FCA5A5;border-left:5px solid #EF4444;border-radius:14px;padding:1.25rem 1.5rem;color:#7F1D1D;margin:2rem 0;line-height:1.65;font-size:0.95rem}
    .callout-yellow{background:#FEF3C7;border:1.5px solid #FDE68A;border-left:5px solid #F59E0B;border-radius:14px;padding:1.25rem 1.5rem;color:#78350F;margin:2rem 0;line-height:1.65;font-size:0.95rem}
    .callout-green{background:#ECFDF5;border:1.5px solid #A7F3D0;border-left:5px solid #10B981;border-radius:14px;padding:1.25rem 1.5rem;color:#065F46;margin:2rem 0;line-height:1.65;font-size:0.95rem}
    .callout-blue{background:#F0F9FF;border:1.5px solid #BAE6FD;border-left:5px solid #0284C7;border-radius:14px;padding:1.25rem 1.5rem;color:#0369A1;margin:2rem 0;line-height:1.65;font-size:0.95rem}
    .styled-table-wrap{overflow-x:auto;margin:1.5rem 0;border-radius:14px;border:1px solid #E2E8F0}
    .styled-table{width:100%;border-collapse:collapse;text-align:left;font-size:0.875rem}
    .styled-table th{background:#12304A;color:#FFF;padding:0.9rem 1.1rem;font-size:0.78rem;font-weight:800;text-transform:uppercase;letter-spacing:0.05em}
    .styled-table td{padding:0.9rem 1.1rem;border-bottom:1px solid #E2E8F0;color:#334155;vertical-align:top;line-height:1.5}
    .styled-table tr:last-child td{border-bottom:none}
    .styled-table tr:nth-child(even){background:#F8FAFC}
    .key-numbers-card{background:linear-gradient(135deg,#12304A 0%,#1a4a6e 100%);border-radius:20px;padding:1.75rem 2rem;margin:2rem 0;color:#fff}
    .card-eyebrow{font-size:0.75rem;font-weight:800;text-transform:uppercase;letter-spacing:0.08em;color:rgba(255,255,255,0.55);margin-bottom:1.25rem}
    .key-numbers-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}
    @media(max-width:640px){.key-numbers-grid{grid-template-columns:1fr 1fr}}
    .key-number-cell{background:rgba(255,255,255,0.08);border-radius:12px;padding:1rem 1.25rem}
    .key-number-label{font-size:0.7rem;color:rgba(255,255,255,0.6);text-transform:uppercase;letter-spacing:0.05em;margin-bottom:0.35rem;font-weight:700}
    .key-number-value{font-size:1.45rem;font-weight:900;color:#fff;line-height:1.1}
    .key-number-sub{font-size:0.75rem;color:rgba(255,255,255,0.55);margin-top:0.25rem}
    .req-checklist{background:#F8FAFC;border:1.5px solid #E2E8F0;border-radius:16px;padding:1.5rem 1.75rem;margin:1.5rem 0}
    .req-checklist-title{font-size:0.85rem;font-weight:800;text-transform:uppercase;letter-spacing:0.05em;color:#64748B;margin-bottom:1.1rem}
    .req-item{display:flex;align-items:flex-start;gap:0.85rem;padding:0.75rem 0;border-bottom:1px solid #F1F5F9}
    .req-item:last-child{border-bottom:none}
    .req-icon{width:22px;height:22px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:0.1rem;font-size:0.8rem;font-weight:900}
    .req-icon.ok{background:#10B981;color:#fff}
    .req-icon.no{background:#EF4444;color:#fff}
    .req-icon.maybe{background:#F59E0B;color:#fff}
    .req-item-title{font-weight:700;color:#12304A;font-size:0.925rem}
    .req-item-desc{font-size:0.83rem;color:#64748B;margin-top:0.2rem;line-height:1.55}
    .top-pick-card{background:#FFF;border:2px solid #159a9c;border-radius:18px;padding:1.5rem 1.75rem;margin:1.5rem 0;box-shadow:0 8px 24px rgba(238,170,54,0.12);display:flex;align-items:center;justify-content:space-between;gap:1.5rem;flex-wrap:wrap}
    .step-block{background:#FFF;border:1.5px solid #E2E8F0;border-radius:16px;padding:1.5rem 1.75rem;margin:1.25rem 0;box-shadow:0 4px 16px rgba(18,48,74,0.04)}
    .step-header{display:flex;align-items:center;gap:1rem;margin-bottom:1rem}
    .step-num{min-width:38px;height:38px;background:linear-gradient(135deg,#12304A,#1a4a6e);color:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:1rem;flex-shrink:0}
    .step-title{font-weight:800;color:#12304A;font-size:1.1rem;font-family:var(--font-heading)}
    .dissolution-step{display:flex;align-items:flex-start;gap:1rem;padding:1rem 0;border-bottom:1px solid #F1F5F9}
    .dissolution-step:last-child{border-bottom:none}
    .dissolution-num{min-width:32px;height:32px;background:#159a9c;color:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:0.875rem;flex-shrink:0}
    .dissolution-title{font-weight:700;color:#12304A;font-size:0.95rem;margin-bottom:0.3rem}
    .dissolution-desc{font-size:0.875rem;color:#475569;line-height:1.6}
    .faq-accordion-wrapper{display:flex;flex-direction:column;gap:0.85rem;margin-bottom:2rem;width:100%!important}
    .faq-accordion-item{background:#FFF;border:1px solid #E2E8F0;border-radius:16px;overflow:hidden;box-shadow:0 4px 16px rgba(18,48,74,0.04);transition:border-color 0.25s ease}
    .faq-accordion-item:hover,.faq-accordion-item[open]{border-color:#159A9C;box-shadow:0 6px 22px rgba(21,154,156,0.12)}
    .faq-accordion-question{padding:1.25rem 1.65rem;font-weight:700;font-size:1rem;color:#12304A;cursor:pointer;display:flex;align-items:center;justify-content:space-between;user-select:none;list-style:none;font-family:var(--font-heading)}
    .faq-accordion-question::-webkit-details-marker{display:none}
    .faq-q-badge-title{display:flex;align-items:center;gap:0.85rem}
    .faq-q-badge{background:#F0FDFA;border:1px solid #CCFBF1;color:#159A9C;font-size:0.8rem;font-weight:800;padding:0.25rem 0.65rem;border-radius:8px;flex-shrink:0}
    .faq-chevron{width:20px;height:20px;stroke:#159A9C;transition:transform 0.25s ease;flex-shrink:0}
    .faq-accordion-item[open] .faq-accordion-question .faq-chevron{transform:rotate(180deg)}
    .faq-accordion-answer{padding:0 1.65rem 1.35rem 1.65rem;font-size:0.95rem;color:#475569;line-height:1.7;border-top:1px dashed #F1F5F9;padding-top:1rem}
    .neighboring-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:0.85rem;margin-bottom:1.5rem}
    @media(max-width:700px){.neighboring-grid{grid-template-columns:1fr 1fr}}
    @media(max-width:400px){.neighboring-grid{grid-template-columns:1fr}}
    .state-card{background:#F8FAFC;border:1.5px solid #E2E8F0;border-radius:14px;padding:1.1rem 1.25rem;text-align:center}
    .state-card-name{font-weight:800;color:#12304A;font-size:1rem;margin-bottom:0.3rem}
    .state-card-fee{color:#159A9C;font-size:0.875rem;font-weight:700;margin-bottom:0.35rem}
    .state-card-note{font-size:0.8rem;color:#64748B}
    .bottom-line-card{background:linear-gradient(135deg,#0d2336 0%,#1a4a6e 100%);border-radius:18px;padding:1.75rem 2rem;margin:2.5rem 0}
    .warning-banner{background:#FEF3C7;border:2px solid #F59E0B;border-radius:14px;padding:1.25rem 1.5rem;margin:1.5rem 0;display:flex;gap:1rem;align-items:flex-start}
    .warning-icon{font-size:1.5rem;flex-shrink:0;margin-top:0.1rem}
    @media(max-width:640px){
  
    .primary-sources-box{background:#F8FAFC;border:1.5px solid #CBD5E1;border-radius:18px;padding:1.5rem 1.75rem;margin:2rem 0}
    .primary-src-eyebrow{font-size:0.8rem;font-weight:800;text-transform:uppercase;letter-spacing:0.07em;color:#475569;margin-bottom:1rem}
    .primary-src-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:0.75rem}}
    @media(max-width:640px){.primary-src-grid{grid-template-columns:1fr}}
    .primary-src-item{background:#fff;border:1px solid #E2E8F0;border-radius:12px;padding:0.9rem 1rem}
    .primary-src-link{font-weight:700;color:#12304A;font-size:0.875rem;text-decoration:none;display:block;margin-bottom:0.3rem}
    .primary-src-link:hover{color:#159A9C;text-decoration:underline}
    .primary-src-desc{font-size:0.78rem;color:#64748B;margin:0;line-height:1.5}
  </style>
</head>
<body>
  <header class="site-header">
    <div class="container header-container">
      <a href="index.html" class="site-logo" aria-label="LLC Primer Homepage" style="display:flex;align-items:center;">
        <img src="logo.png" alt="LLC Primer Logo" style="height:56px;width:auto;object-fit:contain;">
      </a>
      <nav class="nav-menu" id="primaryNavMenu" aria-label="Main Navigation">
        <div class="nav-item"><a href="start-llc.html" class="nav-link active" style="color:var(--color-primary);font-weight:800;">Start an LLC</a></div>
        <div class="nav-item"><a href="best-llc-services.html" class="nav-link">LLC Services<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg></a><div class="dropdown-menu"><a href="northwest-registered-agent-review.html" class="dropdown-link">Northwest Registered Agent</a><a href="best-registered-agent-services.html" class="dropdown-link">Best Registered Agent</a><a href="best-llc-formation-services.html" class="dropdown-link">Best LLC Formation Services</a></div></div>
        <div class="nav-item"><a href="llc-guide.html" class="nav-link">LLC Guides<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg></a><div class="dropdown-menu"><a href="what-is-an-llc.html" class="dropdown-link">What is an LLC</a><a href="best-state-to-form-an-llc.html" class="dropdown-link">Best State for LLC</a><a href="how-much-does-an-llc-cost.html" class="dropdown-link">How Much Does An LLC Cost</a><a href="how-are-llcs-taxed.html" class="dropdown-link">How Are LLCs Taxed</a><a href="operating-agreement.html" class="dropdown-link">LLC Operating Agreement</a><a href="registered-agent-guide.html" class="dropdown-link">Registered Agent Guide</a></div></div>
        <div class="nav-item"><a href="business-setup.html" class="nav-link">Business Setup<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg></a><div class="dropdown-menu"><a href="ein-guide.html" class="dropdown-link">Federal EIN (SS-4 Tax ID)</a><a href="best-business-bank-accounts.html" class="dropdown-link">Best Bank Accounts</a><a href="virtual-business-address.html" class="dropdown-link">Virtual Business Address</a></div></div>
        <div class="nav-item"><a href="tools.html" class="nav-link">Tools<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg></a><div class="dropdown-menu"><a href="llc-cost-calculator.html" class="dropdown-link">LLC Cost Calculator</a><a href="sos-search.html" class="dropdown-link">Secretary of State Search</a><a href="quiz.html" class="dropdown-link">Business Structure Quiz</a><a href="llc-annual-report-tracker.html" class="dropdown-link">Annual Report Tracker</a></div></div>
        <div class="nav-item"><a href="non-resident-llc-guide.html" class="nav-link">Non-Residents</a></div>
      </nav>
      <div class="header-actions">
        <a href="quiz.html" class="ls-btn ls-btn--emerald" style="padding:0.6rem 1.35rem;font-size:0.875rem;background:var(--color-primary-gradient);">Build LLC Plan &rarr;</a>
        <button class="mobile-toggle" id="mobileNavToggle" aria-label="Toggle Menu"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg></button>
      </div>
    </div>
  </header>
  <main class="guide-content-container">
    <div style="font-size:0.85rem;color:#64748B;margin-top:1.5rem;margin-bottom:1rem;">
      <a href="index.html" style="color:#64748B;text-decoration:none;">LLC Primer</a> &nbsp;/&nbsp;
      <a href="start-llc.html" style="color:#64748B;text-decoration:none;">Start an LLC</a> &nbsp;/&nbsp;
      <strong style="color:#12304A;">{state}</strong>
    </div>
    <article class="guide-article">
'''

footer = '''
    </article>
  </main>
  <footer class="site-footer">
    <div class="container footer-container">
      <div class="footer-grid">
        <div class="footer-col brand-col"><a href="index.html" class="footer-logo"><img src="logo.png" alt="LLC Primer Logo" style="height:48px;width:auto;object-fit:contain;"></a><p class="footer-tagline">LLC Primer provides 2026 state guides, filing fee calculators, and step-by-step resources to help founders form, manage, and maintain an LLC in any U.S. state.</p></div>
        <div class="footer-col"><h4 class="footer-heading">State LLC Guides</h4><ul class="footer-links"><li><a href="start-llc.html">How to Start an LLC</a></li><li><a href="best-state-to-form-an-llc.html">Best State for LLC</a></li><li><a href="llc-guide.html">LLC Guides</a></li></ul></div>
        <div class="footer-col"><h4 class="footer-heading">Free Tools</h4><ul class="footer-links"><li><a href="llc-annual-report-tracker.html">Annual Report Tracker</a></li><li><a href="quiz.html">Business Structure Quiz</a></li><li><a href="llc-cost-calculator.html">State Fee Calculator</a></li></ul></div>
        <div class="footer-col"><h4 class="footer-heading">Business Setup</h4><ul class="footer-links"><li><a href="ein-guide.html">EIN Guide</a></li><li><a href="best-business-bank-accounts.html">Business Bank Accounts</a></li><li><a href="registered-agent-guide.html">Registered Agent Guide</a></li></ul></div>
      </div>
      <div class="footer-bottom-bar">
        <p class="footer-disclaimer"><b>Disclaimer:</b> LLC Primer is an independent informational website, not a law firm or government agency. Nothing on this site constitutes legal or tax advice. Always verify current fees and requirements with official sources or a qualified professional. Some links may be affiliate links.</p>
        <div class="footer-copyright">&copy; 2026 LLC Primer. All rights reserved.</div>
      </div>
    </div>
  </footer>
  <script src="app.js"></script>
</body>
</html>
'''

def write_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# File 1: Missouri
mo_title = 'How to Start an LLC in Missouri (2026) | LLC Primer'
mo_meta = 'Complete guide to forming a Missouri LLC in 2026. $50 online Articles of Organization, $105 paper, no annual report required, operating agreement required under Missouri law.'
mo_state = 'Missouri'
mo_body = f'''
      <h1 style="font-size:clamp(2rem,4.5vw,3rem);font-weight:800;color:#12304A;line-height:1.2;margin-bottom:0.75rem;font-family:var(--font-heading);">How to Start an LLC in Missouri in 2026</h1>
      <div class="source-banner-box"><strong>Last reviewed:</strong> October 2026 &nbsp;&middot;&nbsp; <strong>Primary sources:</strong> <a href="https://www.sos.mo.gov/" target="_blank" rel="noopener" style="color:#159A9C;font-weight:600;">Missouri Secretary of State</a>, <a href="https://dor.mo.gov/" target="_blank" rel="noopener" style="color:#159A9C;font-weight:600;">Missouri Department of Revenue</a></div>

      <div class="key-numbers-card">
        <div class="card-eyebrow">Missouri LLC at a Glance &mdash; 2026</div>
        <div class="key-numbers-grid">
          <div class="key-number-cell"><div class="key-number-label">Filing Fee</div><div class="key-number-value">$50</div><div class="key-number-sub">online</div></div>
          <div class="key-number-cell"><div class="key-number-label">Paper Filing</div><div class="key-number-value">$105</div><div class="key-number-sub"></div></div>
          <div class="key-number-cell"><div class="key-number-label">Annual Report</div><div class="key-number-value">None</div><div class="key-number-sub">Not required</div></div>
          <div class="key-number-cell"><div class="key-number-label">Registered Agent</div><div class="key-number-value">Required</div><div class="key-number-sub"></div></div>
          <div class="key-number-cell"><div class="key-number-label">Operating Agreement</div><div class="key-number-value">Required</div><div class="key-number-sub">by §347.081</div></div>
          <div class="key-number-cell"><div class="key-number-label">Income Tax</div><div class="key-number-value">Up to 4.70%</div><div class="key-number-sub">Graduated</div></div>
        </div>
      </div>

      <p>Starting an LLC in Missouri begins with choosing an available business name, appointing a registered agent, and filing Articles of Organization with the Missouri Secretary of State. Missouri charges $50 for online Articles of Organization, while paper filing costs $105. Missouri LLCs do not file annual reports with the Secretary of State.</p>
      <p>One Missouri requirement deserves special attention: state law provides for LLC members to adopt an operating agreement under Missouri Revised Statutes §347.081. The operating agreement is an internal document and is not filed with the Secretary of State.</p>

      <div class="toc-card-box">
        <h3>Missouri LLC Guide &mdash; Everything Covered</h3>
        <ol class="toc-links-ol">
          <li><a href="#name">1. Choose a Name</a></li>
          <li><a href="#agent">2. Appoint a Registered Agent</a></li>
          <li><a href="#articles">3. File Articles of Organization</a></li>
          <li><a href="#agreement">4. Adopt an Operating Agreement</a></li>
          <li><a href="#ein">5. Get an EIN</a></li>
          <li><a href="#bank">6. Open a Business Bank Account</a></li>
          <li><a href="#taxes">7. Missouri LLC Taxes</a></li>
          <li><a href="#costs">8. Missouri LLC Cost Breakdown</a></li>
          <li><a href="#compliance">9. Ongoing Compliance</a></li>
          <li><a href="#licenses">10. Business Licenses and Local Requirements</a></li>
          <li><a href="#mistakes">11. Common Mistakes</a></li>
          <li><a href="#faq">12. Frequently Asked Questions</a></li>
        </ol>
      </div>

      <h2 id="what">What You Need to Form a Missouri LLC:</h2>
      <ol>
        <li>Choose a distinguishable LLC name</li>
        <li>Appoint a Missouri registered agent</li>
        <li>Prepare and file Articles of Organization</li>
        <li>Adopt an operating agreement</li>
        <li>Obtain an EIN when required or useful</li>
        <li>Open a dedicated business bank account</li>
        <li>Register for applicable Missouri taxes, licenses, and permits</li>
      </ol>

      <h2 id="name">Step 1: Choose a Name</h2>
      <p>Your Missouri LLC name must be distinguishable from other entities registered with the Missouri Secretary of State and must contain an accepted LLC designator. Missouri's official Articles of Organization form lists Limited Liability Company, Limited Company, LC, L.C., L.L.C., or LLC as acceptable designators.</p>
      
      <div class="req-checklist">
        <div class="req-checklist-title">Missouri LLC Naming Requirements</div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">Use an approved LLC designator</div><div class="req-item-desc"></div></div>
        </div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">Make the name distinguishable</div><div class="req-item-desc">Search the Missouri Secretary of State business database before filing.</div></div>
        </div>
        <div class="req-item">
          <div class="req-icon maybe">!</div>
          <div><div class="req-item-title">Check restricted terminology</div><div class="req-item-desc">Certain words can require additional approval or documentation.</div></div>
        </div>
      </div>
      
      <p><strong>Check Availability Before Filing:</strong> Use the official Missouri business entity search before submitting Articles of Organization. Do not rely only on a Google search or domain-name availability.</p>
      <p><strong>Name Reservation:</strong> Missouri allows an applicant to reserve a business name before formation. A reservation is optional and is useful when you are not ready to file immediately. If you are ready to create the LLC, you can generally proceed directly to the Articles of Organization.</p>

      <h2 id="agent">Step 2: Appoint a Missouri Registered Agent</h2>
      <p>Every Missouri LLC needs a <a href="registered-agent-guide.html">registered agent</a> and registered office in Missouri. The registered agent receives service of process and other official documents on behalf of the LLC.</p>
      
      <div class="req-checklist">
        <div class="req-checklist-title">Missouri Registered Agent Requirements</div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">Missouri physical address</div><div class="req-item-desc">The registered office must have a physical Missouri address. A P.O. Box alone is not sufficient.</div></div>
        </div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">Available to receive documents</div><div class="req-item-desc"></div></div>
        </div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">You can serve as your own agent</div><div class="req-item-desc"></div></div>
        </div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">Professional registered agent</div><div class="req-item-desc">A commercial registered-agent service can receive official documents and help keep your personal address separate.</div></div>
        </div>
      </div>
      
      <p><strong>Registered Agent Privacy:</strong> Using your own home address can place that address in public business records. A professional registered agent may be useful for owners who work from home.</p>

      <h2 id="articles">Step 3: File Missouri Articles of Organization</h2>
      <p>The Articles of Organization officially create your Missouri LLC. Missouri's statute specifies information that must be included, including the LLC name, business purpose, registered-agent information, management structure, duration or dissolution provisions, and the name and physical address of each organizer.</p>
      
      <div class="req-checklist">
        <div class="req-checklist-title">What Missouri Requires</div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">LLC name</div><div class="req-item-desc"></div></div>
        </div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">Business purpose</div><div class="req-item-desc">The purpose for which the LLC is organized. Missouri law allows the purpose to include any lawful business.</div></div>
        </div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">Registered agent and registered office</div><div class="req-item-desc"></div></div>
        </div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">Management structure</div><div class="req-item-desc">The Articles identify whether management is vested in members or managers.</div></div>
        </div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">Duration</div><div class="req-item-desc">The LLC may have a specified duration or continue perpetually.</div></div>
        </div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">Organizer information</div><div class="req-item-desc">Name and physical business or residence address of each organizer.</div></div>
        </div>
      </div>

      <div class="styled-table-wrap">
        <table class="styled-table">
          <thead><tr><th>Filing Method</th><th>Fee</th><th>Note</th></tr></thead>
          <tbody>
            <tr><td>Online</td><td><strong>$50</strong></td><td>Lowest state filing fee</td></tr>
            <tr><td>Paper</td><td><strong>$105</strong></td><td>Available through the Secretary of State</td></tr>
            <tr><td>Military program</td><td><strong>Fee may be waived</strong></td><td>Eligibility requirements apply</td></tr>
          </tbody>
        </table>
      </div>
      
      <div class="callout-blue"><strong>Startups for Soldiers:</strong> Missouri operates a Startup for Soldiers program that can waive the filing fee for qualifying active-duty military members. Missouri says qualifying applicants filing electronically can contact the Secretary of State for a same-day refund, while other qualifying filing methods have separate procedures. Verify current eligibility and filing instructions before submitting.</div>

      <h2 id="agreement">Step 4: Adopt an Operating Agreement</h2>
      <p>Missouri gives <a href="operating-agreement.html">operating agreements</a> significant legal recognition. Under Missouri Revised Statutes §347.081, the member or members of an LLC shall adopt an operating agreement containing provisions governing the company's affairs and the rights, powers, and duties of its members, managers, agents, or employees.</p>
      <p>The operating agreement is not filed with the Secretary of State. Missouri's Secretary of State specifically states that the Articles of Organization are the creation document filed with the state and that the office does not accept operating agreements for filing.</p>
      
      <ul>
        <li>Ownership percentages</li>
        <li>Capital contributions</li>
        <li>Profit and loss allocations</li>
        <li>Voting rights</li>
        <li>Member and manager authority</li>
        <li>Admission of new members</li>
        <li>Transfers of membership interests</li>
        <li>Buyout procedures</li>
        <li>Member death or withdrawal</li>
        <li>Dispute procedures</li>
        <li>Dissolution and winding up</li>
        <li>Tax elections</li>
      </ul>
      
      <div class="styled-table-wrap">
        <table class="styled-table">
          <thead><tr><th>Management Structure</th><th>Description</th></tr></thead>
          <tbody>
            <tr><td>Member-managed</td><td>Members manage the LLC directly</td></tr>
            <tr><td>Manager-managed</td><td>One or more designated managers manage the company</td></tr>
          </tbody>
        </table>
      </div>
      <p>Missouri law allows managers to be designated through the operating agreement, and a manager does not necessarily have to be a member of the LLC.</p>

      <h2 id="ein">Step 5: Get an EIN</h2>
      <p>An <a href="ein-guide.html">Employer Identification Number (EIN)</a> is the federal tax identification number issued by the IRS. The IRS issues EINs at no charge through its official application process.</p>
      <p>An EIN is commonly needed when an LLC: Has employees | Is taxed as a corporation | Has certain federal filing obligations | Needs an EIN for banking</p>
      <p>A single-member LLC may not always be required to have an EIN for federal income-tax purposes, but obtaining one can be useful for banking and business administration.</p>

      <h2 id="bank">Step 6: Open a Business Bank Account</h2>
      <p>Keep LLC finances separate from personal finances. A <a href="best-business-bank-accounts.html">dedicated business bank account</a> makes it easier to track revenue and expenses.</p>
      
      <div class="req-checklist">
        <div class="req-checklist-title">Documents a Bank May Request</div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">Approved Articles of Organization</div><div class="req-item-desc"></div></div>
        </div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">EIN confirmation</div><div class="req-item-desc"></div></div>
        </div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">Operating agreement</div><div class="req-item-desc">Particularly important for multi-member LLCs</div></div>
        </div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">Government-issued identification</div><div class="req-item-desc"></div></div>
        </div>
      </div>

      <h2 id="taxes">Step 7: Missouri LLC Taxes</h2>
      <p>Missouri LLC tax treatment depends on <a href="how-are-llcs-taxed.html">how LLCs are taxed</a> for federal tax purposes. A standard single-member LLC is generally treated as a disregarded entity, while a multi-member LLC is generally treated as a partnership unless another election is made.</p>
      
      <div class="styled-table-wrap">
        <table class="styled-table">
          <thead><tr><th>Missouri Tax Category</th><th>Detail</th></tr></thead>
          <tbody>
            <tr><td>LLC annual report</td><td>Not required</td></tr>
            <tr><td>Missouri franchise tax on LLCs</td><td>None</td></tr>
            <tr><td>Individual income tax</td><td>Graduated rates</td></tr>
            <tr><td>Sales/use tax</td><td>Applies to taxable transactions</td></tr>
            <tr><td>Local taxes</td><td>May apply</td></tr>
          </tbody>
        </table>
      </div>
      
      <p><strong>Missouri Individual Income Tax:</strong> Missouri uses a graduated individual income-tax structure. The Missouri Department of Revenue currently lists rates ranging from 0% on the lowest taxable-income bracket to 4.70% at the top of the published table. Because Missouri tax rules can change, do not assume that a rate from an older LLC guide applies to the current tax year.</p>
      <p><strong>Missouri Sales Tax:</strong> Missouri has a statewide sales/use-tax system, with local jurisdictions potentially adding additional taxes. Businesses selling taxable goods or services may need to register with the Missouri Department of Revenue and collect and remit applicable sales tax.</p>

      <h2 id="costs">Missouri LLC Cost Breakdown</h2>
      <ul>
        <li><strong>Articles of Organization:</strong> $50 online / $105 paper</li>
        <li><strong>Registered Agent:</strong> $0 if you serve yourself; professional service fees vary</li>
        <li><strong>Name Reservation:</strong> Optional</li>
        <li><strong>Operating Agreement:</strong> No state filing fee</li>
        <li><strong>EIN:</strong> Free from IRS</li>
        <li><strong>Annual Report:</strong> Not required</li>
      </ul>
      
      <div class="callout-green"><strong>Minimum State Formation Cost:</strong> For a standard domestic Missouri LLC filing online, the state filing fee is $50. If you serve as your own registered agent and prepare your operating agreement yourself, you can form the LLC without paying a commercial formation or registered-agent service fee.</div>

      <h2 id="compliance">Ongoing Compliance</h2>
      <p>One of Missouri's important administrative features is that LLCs do not file annual reports with the Secretary of State. That does not mean an LLC has no ongoing responsibilities.</p>
      
      <div class="styled-table-wrap">
        <table class="styled-table">
          <thead><tr><th>Requirement</th><th>Frequency</th><th>Cost</th></tr></thead>
          <tbody>
            <tr><td>Registered agent</td><td>Ongoing</td><td>$0 if self</td></tr>
            <tr><td>Annual LLC report</td><td>Not required</td><td>$0</td></tr>
            <tr><td>Federal tax filings</td><td>As applicable</td><td>Varies</td></tr>
            <tr><td>Missouri income-tax filings</td><td>As applicable</td><td>Varies</td></tr>
            <tr><td>Sales-tax filings</td><td>If registered</td><td>Varies</td></tr>
            <tr><td>Local licenses/permits</td><td>As required</td><td>Varies</td></tr>
          </tbody>
        </table>
      </div>
      
      <p>Missouri law also requires LLCs to maintain certain company records, including effective written operating agreements and specified financial and ownership records.</p>

      <h2 id="licenses">Business Licenses and Local Requirements</h2>
      <p>Missouri does not issue one universal statewide business license covering every type of business. Your LLC may still need: City business licenses | County licenses | Sales-tax registration | Professional or occupational licenses | Industry-specific permits | Health or food-service permits | Building or zoning approvals. Requirements depend on your business activity and location.</p>
      <p><strong>Missouri Series LLC:</strong> Missouri law permits designated series within an LLC under Missouri Revised Statutes §347.186. A Series LLC can be useful for certain structures, but it adds legal and administrative complexity. Consider professional legal and tax advice before choosing this structure.</p>

      <h2 id="timeline">Formation Timeline</h2>
      <div class="dissolution-step"><div class="dissolution-num">1</div><div><div class="dissolution-title">Day 1 &mdash; Choose Your Name</div><div class="dissolution-desc">Search the Missouri Secretary of State database.</div></div></div>
      <div class="dissolution-step"><div class="dissolution-num">2</div><div><div class="dissolution-title">Day 1 &mdash; Select Your Registered Agent</div><div class="dissolution-desc"></div></div></div>
      <div class="dissolution-step"><div class="dissolution-num">3</div><div><div class="dissolution-title">Day 1 &mdash; File Articles of Organization</div><div class="dissolution-desc">Submit online ($50) or paper ($105).</div></div></div>
      <div class="dissolution-step"><div class="dissolution-num">4</div><div><div class="dissolution-title">After Formation &mdash; Adopt Your Operating Agreement</div><div class="dissolution-desc">Missouri law gives operating agreements an important role.</div></div></div>
      <div class="dissolution-step"><div class="dissolution-num">5</div><div><div class="dissolution-title">After Formation &mdash; Obtain Your EIN</div><div class="dissolution-desc"></div></div></div>
      <div class="dissolution-step"><div class="dissolution-num">6</div><div><div class="dissolution-title">After Formation &mdash; Open Your Business Bank Account</div><div class="dissolution-desc"></div></div></div>
      <div class="dissolution-step"><div class="dissolution-num">7</div><div><div class="dissolution-title">Before Operating &mdash; Check Licenses and Taxes</div><div class="dissolution-desc"></div></div></div>

      <h2 id="mistakes">Common Missouri LLC Mistakes</h2>
      <ol>
        <li><strong>Assuming No Annual Report Means No Compliance:</strong> Missouri LLCs don't file annual reports but still have tax, licensing, registered-agent, and recordkeeping obligations.</li>
        <li><strong>Treating the Operating Agreement as Optional:</strong> Missouri law specifically provides that LLC members SHALL adopt an operating agreement.</li>
        <li><strong>Filing Without Checking the Business Name:</strong> Search official Missouri database before submitting.</li>
        <li><strong>Mixing Personal and Business Money:</strong></li>
        <li><strong>Ignoring Local Licenses:</strong> State formation does not automatically authorize every type of business activity.</li>
        <li><strong>Assuming Sales Tax Is the Same Everywhere:</strong> Missouri's sales-tax system can include state and local components.</li>
      </ol>

      <div class="primary-sources-box">
        <div class="primary-src-eyebrow">Primary Sources</div>
        <div class="primary-src-grid">
          <div class="primary-src-item"><a href="https://www.sos.mo.gov/" class="primary-src-link" target="_blank" rel="noopener">Missouri Secretary of State</a></div>
          <div class="primary-src-item"><a href="https://bsd.sos.mo.gov/" class="primary-src-link" target="_blank" rel="noopener">Missouri Business Filing</a></div>
          <div class="primary-src-item"><a href="https://dor.mo.gov/" class="primary-src-link" target="_blank" rel="noopener">Missouri Department of Revenue</a></div>
          <div class="primary-src-item"><a href="https://revisor.mo.gov/main/OneSection.aspx?section=347.081" class="primary-src-link" target="_blank" rel="noopener">Missouri Revised Statutes §347.081</a></div>
        </div>
      </div>

      <div class="bottom-line-card">
        <div style="font-size:0.72rem;font-weight:800;text-transform:uppercase;letter-spacing:0.08em;color:rgba(255,255,255,0.5);margin-bottom:0.75rem;">THE BOTTOM LINE</div>
        <p style="color:#fff;margin:0;line-height:1.7;">Starting a Missouri LLC costs $50 online or $105 by paper. Missouri LLCs do not file annual reports with the Secretary of State, but Missouri Revised Statutes §347.081 specifically provides that LLC members shall adopt an operating agreement. The operating agreement is not filed with the Secretary of State but should be maintained with the company's records. Missouri also does not impose a general franchise tax on LLCs, but individual income tax, sales tax, and local taxes may apply.</p>
      </div>

      <h2 id="faq">Frequently Asked Questions</h2>
      <div class="faq-accordion-wrapper">
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">1</span><span>How much does it cost to start an LLC in Missouri?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">$50 online, $105 paper. Total can be higher with professional registered agent, formation service, legal assistance.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">2</span><span>Does Missouri require an annual report for LLCs?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">No. Missouri Secretary of State guidance states that LLCs do not have to file annual reports.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">3</span><span>Is an operating agreement required in Missouri?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">Missouri Revised Statutes §347.081 provides that LLC members shall adopt an operating agreement. Not filed with the Secretary of State.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">4</span><span>Can I be my own registered agent in Missouri?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">Yes, provided you meet Missouri's requirements and maintain an eligible Missouri registered office.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">5</span><span>Does Missouri have a franchise tax for LLCs?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">Missouri does not impose a general franchise tax on LLCs. Your LLC may have other state or local tax obligations.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">6</span><span>Can active-duty military members form a Missouri LLC for free?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">Qualifying active-duty military members may use Missouri's Startup for Soldiers program. Specific eligibility and proof-of-service requirements apply.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">7</span><span>Can I form a Missouri LLC if I live in another state?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">Yes. The LLC must maintain the required Missouri registered-agent and registered-office arrangement.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">8</span><span>Can Missouri LLCs have a Series LLC?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">Yes. Missouri law permits designated series within an LLC subject to statutory requirements.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">9</span><span>Do I need an EIN for a Missouri LLC?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">Depends on federal tax classification. Commonly required for LLCs with employees. Obtain directly from the IRS at no charge.</div>
        </details>
      </div>
'''
html1 = header_nav_footer.replace('{title}', mo_title).replace('{meta}', mo_meta).replace('{state}', mo_state) + mo_body + footer
write_file(r'd:\rename\how-to-start-llc-in-missouri.html', html1)


# File 2: Montana
mt_title = 'How to Start an LLC in Montana (2026) | LLC Primer'
mt_meta = 'Complete guide to forming a Montana LLC in 2026. $35 Articles of Organization, $0 annual report if filed Jan 1–Apr 15, no general state sales tax, vehicle registration LLC considerations explained.'
mt_state = 'Montana'
mt_body = f'''
      <h1 style="font-size:clamp(2rem,4.5vw,3rem);font-weight:800;color:#12304A;line-height:1.2;margin-bottom:0.75rem;font-family:var(--font-heading);">How to Start an LLC in Montana in 2026</h1>
      <div class="source-banner-box"><strong>Last reviewed:</strong> October 2026 &nbsp;&middot;&nbsp; <strong>Primary sources:</strong> <a href="https://sosmt.gov/" target="_blank" rel="noopener" style="color:#159A9C;font-weight:600;">Montana Secretary of State</a>, <a href="https://mtrevenue.gov/" target="_blank" rel="noopener" style="color:#159A9C;font-weight:600;">Montana Department of Revenue</a></div>

      <div class="key-numbers-card">
        <div class="card-eyebrow">Montana LLC at a Glance &mdash; 2026</div>
        <div class="key-numbers-grid">
          <div class="key-number-cell"><div class="key-number-label">Articles of Organization</div><div class="key-number-value">$35</div><div class="key-number-sub"></div></div>
          <div class="key-number-cell"><div class="key-number-label">Name Reservation</div><div class="key-number-value">$10</div><div class="key-number-sub"></div></div>
          <div class="key-number-cell"><div class="key-number-label">Annual Report</div><div class="key-number-value">$0</div><div class="key-number-sub">filed Jan 1–Apr 15</div></div>
          <div class="key-number-cell"><div class="key-number-label">Late Annual Report</div><div class="key-number-value">$35</div><div class="key-number-sub"></div></div>
          <div class="key-number-cell"><div class="key-number-label">Registered Agent</div><div class="key-number-value">Required</div><div class="key-number-sub"></div></div>
          <div class="key-number-cell"><div class="key-number-label">Sales Tax</div><div class="key-number-value">No</div><div class="key-number-sub">general state sales tax</div></div>
        </div>
      </div>

      <p>Montana can be an attractive state for business owners because it does not impose a general state sales tax and has a relatively low $35 filing fee for a domestic LLC. Montana also requires an annual report, but the Secretary of State has waived the annual report filing fee for reports submitted between January 1 and April 15 in 2026. If you're researching how to start an LLC in Montana, this guide explains the formation process, naming requirements, registered-agent rules, filing costs, EIN, operating agreements, taxes, annual compliance, dissolution and special considerations for vehicle-registration LLCs.</p>

      <div class="styled-table-wrap">
        <table class="styled-table">
          <thead><tr><th>Requirement</th><th>Detail</th></tr></thead>
          <tbody>
            <tr><td>Articles of Organization</td><td>$35</td></tr>
            <tr><td>Name reservation</td><td>$10</td></tr>
            <tr><td>Annual report</td><td>$0 if filed Jan 1–Apr 15, 2026</td></tr>
            <tr><td>Late annual report</td><td>$35</td></tr>
            <tr><td>Registered agent</td><td>Required</td></tr>
            <tr><td>Sales tax</td><td>No general state sales tax</td></tr>
            <tr><td>Formation filing</td><td>Online</td></tr>
          </tbody>
        </table>
      </div>

      <div class="toc-card-box">
        <h3>Montana LLC Guide &mdash; Everything Covered</h3>
        <ol class="toc-links-ol">
          <li><a href="#why">1. Why Form an LLC in Montana</a></li>
          <li><a href="#name">2. Naming Your Montana LLC</a></li>
          <li><a href="#agent">3. Your Montana Registered Agent</a></li>
          <li><a href="#articles">4. Filing the Articles of Organization</a></li>
          <li><a href="#agreement">5. The Operating Agreement</a></li>
          <li><a href="#ein">6. Getting Your EIN</a></li>
          <li><a href="#bank">7. Opening a Business Bank Account</a></li>
          <li><a href="#taxes">8. Montana LLC Taxes</a></li>
          <li><a href="#costs">9. Complete Montana LLC Cost Breakdown</a></li>
          <li><a href="#compliance">10. Montana Annual Report and Ongoing Compliance</a></li>
          <li><a href="#dissolve">11. Dissolving a Montana LLC</a></li>
          <li><a href="#foreign">12. Montana Foreign LLC Registration</a></li>
          <li><a href="#series">13. Montana Series LLC</a></li>
          <li><a href="#vehicle">14. Montana LLC Vehicle Registration</a></li>
          <li><a href="#timeline">15. Montana LLC Formation Timeline</a></li>
          <li><a href="#mistakes">16. Common Mistakes to Avoid</a></li>
          <li><a href="#faq">17. Frequently Asked Questions</a></li>
        </ol>
      </div>

      <h2 id="why">1. Why Form an LLC in Montana</h2>
      <p>Montana LLCs provide a formal business structure with limited-liability features and flexible management. The Secretary of State describes an LLC as a structure that combines liability protection with partnership-style tax treatment and flexibility in contributions and distributions.</p>
      <p>Montana also has no general state sales tax. However, that does not mean a Montana LLC is free from all taxes. An LLC may still have federal tax obligations, Montana income-tax obligations depending on its tax classification and activities, employment-tax obligations, and tax obligations in other states where it conducts business.</p>
      <p>The $35 domestic LLC filing fee is another relatively straightforward formation cost. Montana also allows an optional $10 name reservation.</p>
      <p>For founders outside Montana, the state can also be useful because the registered-agent requirement can be satisfied by an individual or qualified commercial registered agent with a physical Montana address.</p>

      <h2 id="name">2. Naming Your Montana LLC</h2>
      <p>Your Montana LLC needs a distinguishable business name before you file. Search the Montana Secretary of State's business records before submitting your Articles of Organization.</p>
      <p>A name reservation is optional. The Secretary of State currently charges $10 for a name reservation. The state's business-structure information says a reserved name is held for 120 days and cannot be renewed.</p>
      
      <div class="req-checklist">
        <div class="req-checklist-title">Montana LLC Naming Checklist</div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">Check name availability</div><div class="req-item-desc">Search the Montana Secretary of State business database before filing.</div></div>
        </div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">Use an LLC designation</div><div class="req-item-desc">Your legal name should satisfy Montana's statutory naming requirements.</div></div>
        </div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">Make sure the name is distinguishable</div><div class="req-item-desc">Must be distinguishable from names already registered or reserved.</div></div>
        </div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">Check trademarks separately</div><div class="req-item-desc">State business-name availability does not establish federal trademark availability.</div></div>
        </div>
      </div>

      <div class="styled-table-wrap">
        <table class="styled-table">
          <thead><tr><th>Item</th><th>Detail</th></tr></thead>
          <tbody>
            <tr><td>Business-name search</td><td>Free</td></tr>
            <tr><td>Name reservation</td><td>$10 Optional</td></tr>
            <tr><td>Assumed business name</td><td>Separate filing</td></tr>
            <tr><td>Federal trademark</td><td>Separate federal filing</td></tr>
          </tbody>
        </table>
      </div>
      <p>A name reservation is not the same thing as forming an LLC. You still need to file Articles of Organization to create the legal entity.</p>

      <h2 id="agent">3. Your Montana Registered Agent</h2>
      <p>Every Montana LLC must have a <a href="registered-agent-guide.html">registered agent</a>. Montana requires the registered agent to have a physical Montana address and be available during business hours; a P.O. Box alone does not satisfy the physical-address requirement.</p>

      <div class="req-checklist">
        <div class="req-checklist-title">Who Can Be a Montana Registered Agent</div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">Montana resident</div><div class="req-item-desc">An eligible individual with a physical Montana address.</div></div>
        </div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">LLC member or owner</div><div class="req-item-desc">An owner can serve if they meet Montana's requirements.</div></div>
        </div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">Commercial registered-agent service</div><div class="req-item-desc"></div></div>
        </div>
        <div class="req-item">
          <div class="req-icon no">✗</div>
          <div><div class="req-item-title">P.O. Box only</div><div class="req-item-desc">A P.O. Box does not replace the required physical Montana address.</div></div>
        </div>
      </div>
      <p>A commercial registered agent may be particularly useful for owners who do not maintain a physical business presence in Montana or who prefer not to publish a personal address.</p>

      <h2 id="articles">4. Filing the Articles of Organization</h2>
      <p>The Articles of Organization create your Montana domestic LLC. The current Secretary of State fee is $35. Montana directs business owners to its online filing portal.</p>
      
      <ol>
        <li>Choose an available business name</li>
        <li>Select a registered agent</li>
        <li>Complete the Articles of Organization</li>
        <li>Choose the management structure &mdash; Member-managed or manager-managed.</li>
        <li>Submit the filing online &mdash; Pay the $35 filing fee.</li>
        <li>Wait for state approval</li>
      </ol>

      <div class="styled-table-wrap">
        <table class="styled-table">
          <thead><tr><th>Filing</th><th>Fee</th></tr></thead>
          <tbody>
            <tr><td>Domestic Articles of Organization</td><td>$35</td></tr>
            <tr><td>Name reservation</td><td>$10</td></tr>
            <tr><td>Articles of Amendment</td><td>$15</td></tr>
            <tr><td>Articles of Correction</td><td>$15</td></tr>
            <tr><td>Certificate of Existence</td><td>$5</td></tr>
            <tr><td>Articles of Termination</td><td>No fee</td></tr>
            <tr><td>24-hour processing</td><td>$20 additional</td></tr>
            <tr><td>1-hour processing</td><td>$100 additional</td></tr>
          </tbody>
        </table>
      </div>

      <h2 id="agreement">5. The Operating Agreement</h2>
      <p>Montana does not require an <a href="operating-agreement.html">operating agreement</a> to be filed with the Secretary of State. However, an operating agreement is an important internal document that can establish ownership, management responsibilities, voting procedures, distributions and procedures for changes in membership.</p>
      
      <div class="styled-table-wrap">
        <table class="styled-table">
          <thead><tr><th>Management Structure</th><th>Description</th></tr></thead>
          <tbody>
            <tr><td>Member-managed</td><td>Owners participate directly in management</td></tr>
            <tr><td>Manager-managed</td><td>One or more designated managers handle operations</td></tr>
          </tbody>
        </table>
      </div>

      <h2 id="ein">6. Getting Your EIN</h2>
      <p>An <a href="ein-guide.html">Employer Identification Number (EIN)</a> is a federal tax identification number issued by the IRS. After your Montana LLC has been approved, determine whether the business needs an EIN based on its ownership, tax classification and federal requirements.</p>

      <div class="styled-table-wrap">
        <table class="styled-table">
          <thead><tr><th>Option</th><th>Detail</th></tr></thead>
          <tbody>
            <tr><td>IRS online application</td><td>Free</td></tr>
            <tr><td>Form SS-4</td><td>Free</td></tr>
            <tr><td>Third-party EIN service</td><td>Optional paid service (Convenience only)</td></tr>
          </tbody>
        </table>
      </div>
      <p>If you apply through a third party, the company may charge a service fee even though the EIN itself is issued by the IRS without a federal application fee.</p>

      <h2 id="bank">7. Opening a Business Bank Account</h2>
      <p>After forming the LLC and obtaining the necessary federal tax information, consider opening a <a href="best-business-bank-accounts.html">dedicated business bank account</a>.</p>
      <p>Commonly requested documents: Approved Articles of Organization | EIN confirmation | Operating agreement | Government-issued identification | Ownership information</p>

      <h2 id="taxes">8. Montana LLC Taxes</h2>
      <p>Montana's tax treatment depends on <a href="how-are-llcs-taxed.html">how LLCs are taxed</a>. Montana does not impose a general sales tax, but an LLC can still have other state and federal tax obligations.</p>

      <div class="styled-table-wrap">
        <table class="styled-table">
          <thead><tr><th>Tax Type</th><th>Detail</th></tr></thead>
          <tbody>
            <tr><td>General state sales tax</td><td>No general state sales tax</td></tr>
            <tr><td>LLC income taxation</td><td>Depends on tax classification and circumstances</td></tr>
            <tr><td>Federal income tax</td><td>Applies according to federal classification</td></tr>
            <tr><td>Payroll taxes</td><td>Apply when the business has employees</td></tr>
            <tr><td>Other-state taxes</td><td>May apply when the LLC operates in another state</td></tr>
          </tbody>
        </table>
      </div>
      <p>Montana's lack of a general sales tax does not eliminate tax obligations created by operating in another state. A business with customers, employees, property or other activity outside Montana should review the rules of each relevant state.</p>
      <p><strong>Montana Individual Income Tax:</strong> Montana's individual income-tax system applies to taxable income according to the rates and rules in effect for the applicable tax year. LLC owners should use current Montana Department of Revenue guidance when determining their personal state tax obligations.</p>

      <h2 id="costs">9. Complete Montana LLC Cost Breakdown</h2>
      <p>The basic state cost to form a domestic Montana LLC is $35.</p>

      <div class="styled-table-wrap">
        <table class="styled-table">
          <thead><tr><th>Item</th><th>Cost</th></tr></thead>
          <tbody>
            <tr><td>Articles of Organization</td><td>$35</td></tr>
            <tr><td>Name reservation</td><td>$10 optional</td></tr>
            <tr><td>Annual report filed by April 15, 2026</td><td>$0</td></tr>
            <tr><td>Annual report filed after April 15, 2026</td><td>$35</td></tr>
            <tr><td>Registered-agent service</td><td>Varies by provider</td></tr>
            <tr><td>Operating agreement</td><td>$0 if prepared yourself</td></tr>
            <tr><td>EIN</td><td>Free from IRS</td></tr>
            <tr><td>Expedited 24-hour processing</td><td>$20 additional</td></tr>
            <tr><td>Expedited 1-hour processing</td><td>$100 additional</td></tr>
          </tbody>
        </table>
      </div>
      <div class="callout-yellow">The Secretary of State has specifically waived the annual-report filing fee for 2026 reports filed from January 1 through April 15. The current fee schedule lists $35 for annual reports filed after April 15.</div>

      <h2 id="compliance">10. Montana Annual Report and Ongoing Compliance</h2>
      <p>Every Montana LLC must file an annual report with the Secretary of State. For 2026, Montana has waived the annual-report fee for filings made between January 1 and April 15. After April 15, the current fee is $35.</p>

      <div class="styled-table-wrap">
        <table class="styled-table">
          <thead><tr><th>Rule</th><th>Detail</th></tr></thead>
          <tbody>
            <tr><td>Filing period</td><td>January 1–April 15</td></tr>
            <tr><td>Fee during waiver period</td><td>$0</td></tr>
            <tr><td>Fee after April 15</td><td>$35</td></tr>
            <tr><td>Filing method</td><td>Online</td></tr>
            <tr><td>Required for LLCs</td><td>Yes</td></tr>
          </tbody>
        </table>
      </div>
      <div class="callout-yellow"><strong>Important:</strong> Do not assume that the 2026 fee waiver means future annual reports will always be free. Check the Secretary of State's current fee schedule for the applicable year.</div>

      <h2 id="dissolve">11. Dissolving a Montana LLC</h2>
      <p>A Montana LLC that is no longer needed should follow the state's termination process and resolve outstanding obligations before closing.</p>
      
      <div class="dissolution-step"><div class="dissolution-num">1</div><div><div class="dissolution-title">Review the operating agreement</div><div class="dissolution-desc">Follow the procedures established for member approval and dissolution.</div></div></div>
      <div class="dissolution-step"><div class="dissolution-num">2</div><div><div class="dissolution-title">Resolve business obligations</div><div class="dissolution-desc">Pay outstanding debts, close contracts and address remaining liabilities.</div></div></div>
      <div class="dissolution-step"><div class="dissolution-num">3</div><div><div class="dissolution-title">File the required termination document</div><div class="dissolution-desc">Montana's current fee schedule lists no fee for Articles of Termination for a domestic LLC.</div></div></div>
      <div class="dissolution-step"><div class="dissolution-num">4</div><div><div class="dissolution-title">Handle final tax matters</div><div class="dissolution-desc"></div></div></div>
      <div class="dissolution-step"><div class="dissolution-num">5</div><div><div class="dissolution-title">Close business accounts</div><div class="dissolution-desc"></div></div></div>
      <div class="dissolution-step"><div class="dissolution-num">6</div><div><div class="dissolution-title">Address licenses and registrations</div><div class="dissolution-desc"></div></div></div>

      <h2 id="foreign">12. Montana Foreign LLC Registration</h2>
      <p>If an LLC was formed outside Montana but will transact business in Montana, it may need to register as a foreign LLC. The current Montana Secretary of State fee schedule lists a $70 Certificate of Authority fee for a foreign LLC.</p>

      <h2 id="series">13. Montana Series LLC</h2>
      <p>Montana recognizes a series LLC structure. A series LLC can establish separate series with separate assets, liabilities, members or managers under the applicable statutory framework. Series LLCs can be useful in certain investment or multi-asset structures, but they require more careful legal and tax planning than a standard single LLC. If a series LLC will operate in multiple states, confirm whether the other states recognize and appropriately treat the Montana structure.</p>

      <h2 id="vehicle">14. Montana LLC Vehicle Registration</h2>
      <p>Montana is widely associated with LLC-based vehicle registration because the state does not impose a general sales tax. However, forming a Montana LLC does not automatically eliminate taxes or registration obligations in another state. If a person lives in another state and primarily stores or uses a vehicle there, that home state may impose its own registration, use-tax or other requirements.</p>
      <div class="callout-red"><strong>Before Using a Montana LLC for a Vehicle — Consider:</strong> Where the vehicle is primarily stored | Where it is primarily used | Where the owner resides | Which state requires registration | Insurance requirements | Sales or use-tax rules | Whether the LLC has a legitimate business purpose | Whether the home state recognizes the proposed structure. The absence of a Montana sales tax should not be treated as permission to disregard another state's tax or registration laws. For a vehicle-registration LLC, obtain advice specific to both Montana and the state where the vehicle will actually be used.</div>

      <h2 id="timeline">15. Montana LLC Formation Timeline</h2>
      <div class="dissolution-step"><div class="dissolution-num">1</div><div><div class="dissolution-title">Choose Your Name</div><div class="dissolution-desc">Search the Montana Secretary of State database.</div></div></div>
      <div class="dissolution-step"><div class="dissolution-num">2</div><div><div class="dissolution-title">Choose a Registered Agent</div><div class="dissolution-desc"></div></div></div>
      <div class="dissolution-step"><div class="dissolution-num">3</div><div><div class="dissolution-title">File Articles of Organization</div><div class="dissolution-desc">$35 online.</div></div></div>
      <div class="dissolution-step"><div class="dissolution-num">4</div><div><div class="dissolution-title">Receive Approval</div><div class="dissolution-desc"></div></div></div>
      <div class="dissolution-step"><div class="dissolution-num">5</div><div><div class="dissolution-title">Create Your Operating Agreement</div><div class="dissolution-desc">Keep with internal records. Not filed with Secretary of State.</div></div></div>
      <div class="dissolution-step"><div class="dissolution-num">6</div><div><div class="dissolution-title">Obtain an EIN if Required</div><div class="dissolution-desc"></div></div></div>
      <div class="dissolution-step"><div class="dissolution-num">7</div><div><div class="dissolution-title">Open a Business Bank Account</div><div class="dissolution-desc"></div></div></div>
      <div class="dissolution-step"><div class="dissolution-num">8</div><div><div class="dissolution-title">Track Annual Compliance</div><div class="dissolution-desc">Set reminder for January 1–April 15 annual report period.</div></div></div>

      <h2 id="mistakes">16. Common Mistakes to Avoid</h2>
      <ol>
        <li><strong>Assuming $35 Is the Total Cost</strong></li>
        <li><strong>Treating the Annual Report as a Tax Return:</strong> Annual report updates business-registration information, not an income-tax return.</li>
        <li><strong>Assuming the Annual Report Is Always Free:</strong> 2026 filing fee waived only Jan 1–Apr 15. After April 15 = $35.</li>
        <li><strong>Using a P.O. Box as the Registered-Agent Address</strong></li>
        <li><strong>Assuming No Sales Tax Means No Other Taxes:</strong> Federal income taxes, Montana income taxes, payroll taxes still apply.</li>
        <li><strong>Using a Montana LLC for a Vehicle Without Checking Home-State Rules</strong></li>
        <li><strong>Treating an LLC as a Substitute for Professional Advice</strong></li>
      </ol>

      <div class="primary-sources-box">
        <div class="primary-src-eyebrow">Primary Sources</div>
        <div class="primary-src-grid">
          <div class="primary-src-item"><a href="https://sosmt.gov/" class="primary-src-link" target="_blank" rel="noopener">Montana Secretary of State</a></div>
          <div class="primary-src-item"><a href="https://sos.mt.gov/business" class="primary-src-link" target="_blank" rel="noopener">Montana Business Registration</a></div>
          <div class="primary-src-item"><a href="https://mtrevenue.gov/" class="primary-src-link" target="_blank" rel="noopener">Montana Department of Revenue</a></div>
          <div class="primary-src-item"><a href="https://leg.mt.gov/bills/mca/title_0350/chapter_0080/parts_index.html" class="primary-src-link" target="_blank" rel="noopener">Montana LLC Statutes</a></div>
        </div>
      </div>

      <h2 id="faq">17. Frequently Asked Questions</h2>
      <div class="faq-accordion-wrapper">
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">1</span><span>How much does it cost?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">$35 Articles. $10 optional name reservation. Other costs depend on registered-agent service, professional formation, expedited processing.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">2</span><span>Is the Montana annual report free?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">For 2026, fee waived for reports filed January 1–April 15. After April 15 = $35.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">3</span><span>When is the Montana LLC annual report due?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">Filed during annual reporting period ending April 15.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">4</span><span>Does Montana have a sales tax?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">No general state sales tax. A Montana business can still have federal tax obligations, Montana income-tax rules, and laws of other states.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">5</span><span>Does a Montana LLC need a registered agent?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">Yes. Must have physical Montana address and be available during business hours.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">6</span><span>Can I be my own Montana registered agent?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">Yes, if Montana requirements satisfied.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">7</span><span>Does Montana require an operating agreement?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">Does not have to be filed. State recommends maintaining as part of internal documents.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">8</span><span>How do I file a Montana LLC?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">Through Montana's online business-registration portal. Create account, select domestic form, complete required information, submit with $35 fee.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">9</span><span>Can I form a Montana LLC if I live in another state?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">Yes, but the business still needs a qualifying Montana registered agent. If LLC conducts business in another state, that state may also require foreign registration.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">10</span><span>Can a Montana LLC be used to register a vehicle?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">A Montana LLC can own and register a vehicle, but that does not automatically eliminate obligations in the owner's home state.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">11</span><span>Does Montana recognize series LLCs?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">Yes. Confirm rules in every state where the LLC or its assets will operate.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">12</span><span>What is the fastest way to form a Montana LLC?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">Montana provides expedited processing: $20 additional for 24-hour, $100 for 1-hour.</div>
        </details>
      </div>
'''
html2 = header_nav_footer.replace('{title}', mt_title).replace('{meta}', mt_meta).replace('{state}', mt_state) + mt_body + footer
write_file(r'd:\rename\how-to-start-llc-in-montana.html', html2)


# File 3: Nebraska
ne_title = 'How to Start an LLC in Nebraska (2026) | LLC Primer'
ne_meta = 'Complete guide to forming a Nebraska LLC in 2026. $100 online Certificate of Organization, required newspaper publication for 3 successive weeks, proof of publication $25, biennial report in odd years.'
ne_state = 'Nebraska'
ne_body = f'''
      <h1 style="font-size:clamp(2rem,4.5vw,3rem);font-weight:800;color:#12304A;line-height:1.2;margin-bottom:0.75rem;font-family:var(--font-heading);">How to Start an LLC in Nebraska in 2026</h1>
      <div class="source-banner-box"><strong>Last reviewed:</strong> October 2026 &nbsp;&middot;&nbsp; <strong>Primary sources:</strong> <a href="https://sos.nebraska.gov/" target="_blank" rel="noopener" style="color:#159A9C;font-weight:600;">Nebraska Secretary of State</a>, <a href="https://revenue.nebraska.gov/" target="_blank" rel="noopener" style="color:#159A9C;font-weight:600;">Nebraska Department of Revenue</a></div>

      <div class="key-numbers-card">
        <div class="card-eyebrow">Nebraska LLC at a Glance &mdash; 2026</div>
        <div class="key-numbers-grid">
          <div class="key-number-cell"><div class="key-number-label">Certificate of Organization</div><div class="key-number-value">$100</div><div class="key-number-sub">online</div></div>
          <div class="key-number-cell"><div class="key-number-label">Publication</div><div class="key-number-value">3 wks</div><div class="key-number-sub">successive weeks (required)</div></div>
          <div class="key-number-cell"><div class="key-number-label">Proof of Publication</div><div class="key-number-value">$25</div><div class="key-number-sub">online</div></div>
          <div class="key-number-cell"><div class="key-number-label">Biennial Report</div><div class="key-number-value">Odd</div><div class="key-number-sub">years</div></div>
          <div class="key-number-cell"><div class="key-number-label">Name Reservation</div><div class="key-number-value">$30</div><div class="key-number-sub"></div></div>
          <div class="key-number-cell"><div class="key-number-label">Registered Agent</div><div class="key-number-value">Required</div><div class="key-number-sub"></div></div>
        </div>
      </div>

      <p>Nebraska makes LLC formation relatively straightforward, but it has one requirement that makes the state different from most others: a domestic LLC must publish a notice of organization for three successive weeks in a qualifying legal newspaper near its designated office and then file proof of publication with the Nebraska Secretary of State.</p>

      <div class="callout-red"><strong>Nebraska LLC: $100 Online Filing + a Real Publication Requirement</strong> &mdash; Nebraska LLC at a Glance: Certificate of Organization $100 online | Publication 3 successive weeks | Proof of Publication $25 online | Biennial Report Odd-numbered years</div>

      <p>The biggest issue for Nebraska founders is not the Certificate of Organization itself. It is making sure the required publication is completed correctly and that proof is filed afterward.</p>
      <p>Nebraska Revised Statute §21-193 requires a notice of organization to be published for three successive weeks in a legal newspaper of general circulation near the LLC's designated office. The notice must contain the information required in the Certificate of Organization, and proof of publication must be filed with the Secretary of State.</p>
      <p>An important 2026 clarification: the current statute does not establish a general 45-day publication deadline. The law instead specifies the three-week publication requirement and provides a cure when required notice was not initially published but is later published for the required period and proof is filed.</p>
      
      <div class="callout-yellow"><strong>Why Nebraska Is Different:</strong> Nebraska is not difficult to use for ordinary LLC formation, but founders need to budget for more than the state filing fee. A domestic Nebraska LLC generally has three formation-related costs: 1. Certificate of Organization: $100 online or $110 in writing. 2. Newspaper publication: Cost varies by newspaper. 3. Proof of Publication: $25 online or $30 in-office. The newspaper charge is not a fixed government fee. Each qualifying newspaper sets its own legal-notice pricing.</div>

      <div class="toc-card-box">
        <h3>Nebraska LLC Guide &mdash; Everything Covered</h3>
        <ol class="toc-links-ol">
          <li><a href="#publication">1. Nebraska LLC Publication Requirement</a></li>
          <li><a href="#pub-steps">2. How to Complete Publication Correctly</a></li>
          <li><a href="#name">3. Choosing a Nebraska LLC Name</a></li>
          <li><a href="#agent">4. Registered Agent and Designated Office</a></li>
          <li><a href="#articles">5. Filing the Certificate of Organization</a></li>
          <li><a href="#agreement">6. Operating Agreement</a></li>
          <li><a href="#ein">7. EIN and Federal Requirements</a></li>
          <li><a href="#bank">8. Opening a Business Bank Account</a></li>
          <li><a href="#costs">9. Nebraska LLC Costs in 2026</a></li>
          <li><a href="#compliance">10. Nebraska Biennial Report</a></li>
          <li><a href="#checklist">11. Post-Formation Checklist</a></li>
          <li><a href="#taxes">12. Nebraska LLC Taxes</a></li>
          <li><a href="#foreign">13. Foreign LLCs in Nebraska</a></li>
          <li><a href="#mistakes">14. Common Nebraska LLC Mistakes</a></li>
          <li><a href="#faq">15. Nebraska LLC FAQ</a></li>
        </ol>
      </div>

      <h2 id="publication">1. Nebraska LLC Publication Requirement</h2>
      <p>Nebraska Revised Statute §21-193 requires a notice of organization to be published for three successive weeks in a legal newspaper of general circulation near the LLC's designated office. This requirement applies to a domestic Nebraska LLC. The statute also requires proof of publication to be filed with the Nebraska Secretary of State.</p>

      <ul>
        <li>Three successive weeks &mdash; The notice must run for three successive weeks.</li>
        <li>Qualifying legal newspaper &mdash; Publication must be in a legal newspaper of general circulation near the LLC's designated office.</li>
        <li>Notice of organization &mdash; The notice must contain the information required under Nebraska's Certificate of Organization rules.</li>
        <li>Proof filing &mdash; After publication, proof must be filed with the Nebraska Secretary of State.</li>
      </ul>

      <div class="callout-red"><strong>Important 2026 Correction: There Is No Verified 45-Day Rule</strong> &mdash; Many online Nebraska LLC guides repeat an old or unsupported statement that the publication must be completed within 45 days. The current text of §21-193 does not establish that 45-day deadline. The statute says the notice must be published for three successive weeks and that proof of publication must be filed with the Secretary of State. It also provides a specific cure: If the required notice was not initially given but is subsequently published for the required period and proof is filed, the statute states that the LLC's acts before and after publication remain valid.</div>

      <p>What Must the Nebraska LLC Notice Contain? Nebraska's publication statute points to the information required under §21-117(b): The LLC's legal name | The street and mailing addresses of the initial designated office | The name of the initial agent for service of process | The street and mailing addresses of the agent for service of process | The professional service, if the LLC is organized to provide a professional service</p>

      <h2 id="pub-steps">2. How to Complete Nebraska LLC Publication Correctly</h2>
      <p>Step 1 &mdash; Establish Your Nebraska Designated Office: A domestic Nebraska LLC must continuously maintain an office in Nebraska. Because the publication statute refers to a newspaper near the designated office, choose this address carefully.</p>
      <p>Step 2 &mdash; Find a Qualifying Legal Newspaper: The newspaper must meet the statutory description of a legal newspaper of general circulation near the LLC's designated office. Before paying for publication, ask the newspaper: Whether it qualifies as a legal newspaper of general circulation | Whether it serves the area near your designated office | Whether it regularly publishes Nebraska LLC notices | How much the three-week publication will cost | What proof or affidavit will be supplied after publication</p>
      <p>Step 3 &mdash; Submit the Notice: Provide the newspaper with accurate information from the LLC's formation documents. Review the notice carefully before publication begins. A spelling error in the LLC's legal name or an incorrect address can create unnecessary compliance problems.</p>
      <p>Step 4 &mdash; Publish for Three Successive Weeks</p>
      <p>Step 5 &mdash; Obtain Proof of Publication: After the publication period is complete, obtain the newspaper's affidavit or other proof of publication.</p>
      <p>Step 6 &mdash; File Proof With the Secretary of State: The Nebraska Secretary of State currently lists the Affidavit/Proof of Publication filing at $25 online or $30 in-office. The newspaper's publication charge is separate.</p>

      <h2 id="name">3. Choosing a Nebraska LLC Name</h2>
      <p>Before filing, choose a name that complies with Nebraska's LLC naming requirements and is distinguishable from existing business names. Search the Nebraska Secretary of State's business records before submitting your Certificate of Organization.</p>

      <div class="req-checklist">
        <div class="req-checklist-title">Nebraska LLC Name Checklist</div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">Check availability</div><div class="req-item-desc">Search the Nebraska business database before filing.</div></div>
        </div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">Use an appropriate LLC designation</div><div class="req-item-desc"></div></div>
        </div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">Avoid misleading government references</div><div class="req-item-desc"></div></div>
        </div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">Check trademarks separately</div><div class="req-item-desc"></div></div>
        </div>
      </div>
      <p><strong>Name Reservation:</strong> Nebraska currently lists the name reservation fee at $30. Optional.</p>

      <h2 id="agent">4. Registered Agent and Designated Office</h2>
      <p>Nebraska uses two related but separate concepts: Designated office and Agent for service of process. A domestic LLC must continuously maintain both in Nebraska.</p>
      <p>In a paragraph, link "<a href="registered-agent-guide.html">registered agent</a>" to registered-agent-guide.html.</p>
      <p><strong>Nebraska Designated Office:</strong> The LLC must maintain an office in Nebraska. Does not have to be where the company conducts its day-to-day activities.</p>
      <p><strong>Nebraska Agent for Service of Process:</strong> The agent must be an individual who is a Nebraska resident; or another person authorized to transact business in Nebraska. A professional registered-agent company can serve this role.</p>
      <div class="callout-blue"><strong>Registered Agent vs. Designated Office:</strong> These addresses and roles should not automatically be treated as identical. A professional registered-agent service may provide the agent address, while the LLC's designated office serves the separate statutory requirement.</div>

      <h2 id="articles">5. Filing the Certificate of Organization</h2>
      <p>A Nebraska domestic LLC is formed by filing a Certificate of Organization with the Nebraska Secretary of State.</p>
      <p>Information Required: LLC name | Initial designated office | Initial agent for service of process | Agent's address | Professional-service information when applicable</p>
      <div class="styled-table-wrap">
        <table class="styled-table">
          <thead><tr><th>Filing Method</th><th>Cost</th></tr></thead>
          <tbody>
            <tr><td>Online</td><td>$100</td></tr>
            <tr><td>Written / in-office</td><td>$110</td></tr>
          </tbody>
        </table>
      </div>

      <h2 id="agreement">6. Operating Agreement</h2>
      <p>Nebraska does not require you to file an <a href="operating-agreement.html">operating agreement</a> with the Secretary of State. However, an operating agreement is an important internal document for most LLCs.</p>
      <p>It can establish: Ownership percentages | Member contributions | Management authority | Voting rights | Profit and loss distributions | Procedures for adding members | Procedures when a member leaves | Transfer restrictions | Dissolution procedures</p>
      <p>Single-Member LLC: Still benefits from a written operating agreement as a written record showing how the company is structured.</p>
      <p>Multi-Member LLC: Should generally have a detailed agreement addressing ownership, voting, distributions, management and member exits.</p>

      <h2 id="ein">7. EIN and Federal Requirements</h2>
      <p>An <a href="ein-guide.html">EIN</a> is a federal tax identification number issued by the IRS. The IRS provides EIN applications directly at no charge.</p>
      <p>For a newly formed Nebraska LLC, it is generally practical to obtain the EIN after the LLC has been officially formed. Do not pay a third party simply for access to the standard IRS EIN application.</p>

      <h2 id="bank">8. Opening a Business Bank Account</h2>
      <p>A <a href="best-business-bank-accounts.html">dedicated business bank account</a> helps keep company transactions separate from personal finances.</p>
      <p>Banks commonly request: Approved Certificate of Organization | EIN confirmation | Operating agreement | Government-issued identification | Ownership information</p>

      <h2 id="costs">9. Nebraska LLC Costs in 2026</h2>
      <p>Nebraska's formation cost is more than the $100 state filing fee because domestic LLCs have the publication requirement.</p>
      <div class="styled-table-wrap">
        <table class="styled-table">
          <thead><tr><th>Item</th><th>Cost</th><th>Detail</th></tr></thead>
          <tbody>
            <tr><td>Certificate of Organization &mdash; online</td><td>$100</td><td>Required</td></tr>
            <tr><td>Certificate of Organization &mdash; written</td><td>$110</td><td>Required if filing in writing</td></tr>
            <tr><td>Newspaper publication</td><td>Varies</td><td>Required for domestic LLC</td></tr>
            <tr><td>Proof of Publication &mdash; online</td><td>$25</td><td>Required</td></tr>
            <tr><td>Proof of Publication &mdash; in-office</td><td>$30</td><td>Required if filing in-office</td></tr>
            <tr><td>Name reservation</td><td>$30</td><td>Optional</td></tr>
            <tr><td>Professional registered agent</td><td>Provider-specific</td><td>Optional</td></tr>
            <tr><td>Biennial report</td><td>$25 online / $30 written</td><td>Required in odd years</td></tr>
          </tbody>
        </table>
      </div>
      <div class="callout-green"><strong>Minimum Government Cost:</strong> For an LLC formed online and completing the proof filing online, the known state filing fees total $125 + newspaper publication cost. Because newspaper rates vary, there is no responsible universal publication price that applies to every Nebraska LLC.</div>

      <h2 id="compliance">10. Nebraska Biennial Report</h2>
      <p>Nebraska LLCs file a biennial report, not an annual report. The reporting cycle is based on odd-numbered years.</p>
      <p>The first biennial report is due between January 1 and April 1 of the odd-numbered year following the calendar year in which the LLC was formed. Subsequent reports are filed between January 1 and April 1 of each odd-numbered year.</p>
      <p>Example: If your Nebraska LLC is formed in 2026, its first biennial report is due between January 1 and April 1, 2027.</p>
      <p>Nebraska Biennial Report Fees: $25 electronic / $30 written</p>
      <div class="callout-yellow">Failure to maintain required filings can put the LLC's good standing at risk and may eventually result in administrative action.</div>

      <h2 id="checklist">11. Post-Formation Checklist</h2>
      <div class="req-checklist">
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">Complete publication</div><div class="req-item-desc">Publish the required notice for three successive weeks.</div></div>
        </div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">File proof of publication</div><div class="req-item-desc">Submit the required proof to the Secretary of State.</div></div>
        </div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">Create an operating agreement</div><div class="req-item-desc"></div></div>
        </div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">Obtain an EIN when needed</div><div class="req-item-desc"></div></div>
        </div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">Open a business bank account</div><div class="req-item-desc"></div></div>
        </div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">Register for applicable taxes</div><div class="req-item-desc"></div></div>
        </div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">Obtain required licenses</div><div class="req-item-desc"></div></div>
        </div>
        <div class="req-item">
          <div class="req-icon ok">✓</div>
          <div><div class="req-item-title">Track your biennial report</div><div class="req-item-desc">Put the next January 1–April 1 reporting window on your compliance calendar.</div></div>
        </div>
      </div>

      <h2 id="taxes">12. Nebraska LLC Taxes</h2>
      <p>For federal tax purposes, a single-member LLC is generally treated as a disregarded entity unless it makes another election. A multi-member LLC is generally treated as a partnership unless it elects another classification. See <a href="how-are-llcs-taxed.html">how LLCs are taxed</a>.</p>
      <p>Nebraska Sales Tax: Nebraska has a state sales tax and local jurisdictions can impose additional sales taxes. Whether your LLC needs to register for sales tax depends on what you sell, where you sell it and whether your activities create the applicable tax obligation.</p>
      <p>Nebraska Income Tax: Nebraska-source business income may create state income-tax obligations. Nonresident owners can have additional Nebraska reporting or withholding requirements.</p>

      <h2 id="foreign">13. Foreign LLCs in Nebraska</h2>
      <p>If your LLC was formed in another state and you need authority to transact business in Nebraska, you generally use Nebraska's foreign LLC registration process. The Nebraska Secretary of State currently lists the foreign LLC Certificate of Authority at $100 online + $10 certificate fee or $110 in-office + $10 certificate fee.</p>
      <div class="callout-blue"><strong>Do Not Confuse Domestic Formation With Foreign Qualification:</strong> A foreign LLC already exists under another state's law. Registering it in Nebraska gives it authority to conduct business in Nebraska; it does not create a second Nebraska domestic LLC.</div>

      <div class="callout-green"><strong>BOI / FinCEN Requirements for Nebraska LLCs in 2026:</strong> Under FinCEN's current rule, U.S.-created companies are exempt from federal Beneficial Ownership Information reporting. That means a domestic Nebraska LLC is not required to file a BOI report. The rule became effective August 14, 2026. Do not rely on older BOI checklists that tell every newly formed U.S. LLC to file a FinCEN report.</div>

      <h2 id="mistakes">14. Common Nebraska LLC Mistakes</h2>
      <ol>
        <li>Assuming the $100 Filing Fee Is the Entire Formation Cost &mdash; Budget for: $100 state filing + newspaper cost + $25 proof filing.</li>
        <li>Believing the Old 45-Day Publication Rule &mdash; Current §21-193 does not establish a 45-day deadline. The law requires three successive weeks.</li>
        <li>Choosing the Newspaper Based Only on Price &mdash; Nebraska requires a qualifying legal newspaper of general circulation near the LLC's designated office.</li>
        <li>Confusing the Registered Agent With the Designated Office &mdash; Nebraska requires both.</li>
        <li>Forgetting the Proof Filing &mdash; After publication, obtain proof and file with the Secretary of State.</li>
        <li>Treating a Biennial Report Like an Annual Report &mdash; Nebraska LLCs report in odd-numbered years, window is January 1–April 1.</li>
        <li>Assuming LLC Formation Handles Every License</li>
      </ol>

      <div class="primary-sources-box">
        <div class="primary-src-eyebrow">Primary Sources</div>
        <div class="primary-src-grid">
          <div class="primary-src-item"><a href="https://sos.nebraska.gov/" class="primary-src-link" target="_blank" rel="noopener">Nebraska Secretary of State</a></div>
          <div class="primary-src-item"><a href="https://www.nebraska.gov/sos/corp/" class="primary-src-link" target="_blank" rel="noopener">Nebraska Business Services</a></div>
          <div class="primary-src-item"><a href="https://revenue.nebraska.gov/" class="primary-src-link" target="_blank" rel="noopener">Nebraska Department of Revenue</a></div>
          <div class="primary-src-item"><a href="https://nebraskalegislature.gov/laws/statutes.php?statute=21-193" class="primary-src-link" target="_blank" rel="noopener">Nebraska Revised Statute §21-193</a></div>
        </div>
      </div>

      <div class="bottom-line-card">
        <div style="font-size:0.72rem;font-weight:800;text-transform:uppercase;letter-spacing:0.08em;color:rgba(255,255,255,0.5);margin-bottom:0.75rem;">THE BOTTOM LINE</div>
        <p style="color:#fff;margin:0;line-height:1.7;">Starting a Nebraska LLC involves a $100 online Certificate of Organization filing fee, plus a required newspaper publication for three successive weeks, and a $25 online proof-of-publication filing. The newspaper sets its own pricing, so the total formation cost varies. Nebraska also requires a biennial report in odd-numbered years ($25 online), filed between January 1 and April 1.</p>
      </div>

      <h2 id="faq">15. Nebraska LLC FAQ</h2>
      <div class="faq-accordion-wrapper">
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">1</span><span>What is the Nebraska LLC publication requirement?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">Nebraska requires a notice of organization to be published for three successive weeks in a legal newspaper of general circulation near the LLC's designated office.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">2</span><span>Is there a 45-day publication deadline in Nebraska?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">No, the current §21-193 does not establish a 45-day deadline, but it does require three successive weeks of publication and proof filed with the state.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">3</span><span>How much does it cost to start a Nebraska LLC?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">Certificate of Organization is $100 online. You must also pay for the newspaper publication (varies) and the proof of publication filing ($25 online).</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">4</span><span>Does Nebraska require an annual report for LLCs?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">No, Nebraska LLCs file a biennial report in odd-numbered years ($25 online) between January 1 and April 1.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">5</span><span>Can I be my own registered agent in Nebraska?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">Yes, the agent for service of process can be an individual who is a Nebraska resident, maintaining a physical address in the state.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">6</span><span>What is a designated office in Nebraska?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">An office maintained in Nebraska, which does not have to be where the company conducts its day-to-day activities, but must be continuously maintained.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">7</span><span>Is an operating agreement required in Nebraska?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">Nebraska does not require you to file an operating agreement with the Secretary of State, but it is highly recommended as an internal document.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">8</span><span>Do I need an EIN for a Nebraska LLC?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">Generally yes, especially if you have employees or a multi-member LLC. Obtain directly from the IRS at no charge.</div>
        </details>
      </div>
'''
html3 = header_nav_footer.replace('{title}', ne_title).replace('{meta}', ne_meta).replace('{state}', ne_state) + ne_body + footer
write_file(r'd:\rename\how-to-start-llc-in-nebraska.html', html3)
