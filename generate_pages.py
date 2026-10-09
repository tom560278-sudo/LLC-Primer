import os
import re

template_head = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=2.0">
  <title>{title}</title>
  <meta name="description" content="{meta}">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="styles.css">
  <style>
    .guide-content-container {
      max-width: 1080px;
      margin: 0 auto;
      padding: 0 1.5rem 0.05rem 1.5rem;
      width: 100%;
    }

    .guide-article h2 {
      font-size: clamp(1.75rem, 3.2vw, 2.3rem);
      font-weight: 800;
      color: #12304A;
      margin: 2.75rem 0 1.25rem 0;
      font-family: var(--font-heading);
      line-height: 1.25;
    }

    .guide-article h3 {
      font-size: clamp(1.25rem, 2.3vw, 1.55rem);
      font-weight: 700;
      color: #12304A;
      margin: 2rem 0 1rem 0;
      font-family: var(--font-heading);
      line-height: 1.3;
    }

    .guide-article p {
      font-size: 1rem;
      line-height: 1.75;
      color: #334155;
      margin-bottom: 1.25rem;
    }

    .guide-article ul {
      padding-left: 1.65rem !important;
      margin-bottom: 1.5rem !important;
    }
    .guide-article ul li {
      margin-bottom: 0.65rem !important;
      line-height: 1.7 !important;
      color: #334155 !important;
    }

    .guide-article a {
      color: #159A9C;
      font-weight: 600;
      text-decoration: underline;
    }
    .guide-article a:hover { color: #0E7490; }

    .review-check-banner {
      background: radial-gradient(circle at 85% 20%, rgba(21, 154, 156, 0.28) 0%, transparent 60%), radial-gradient(circle at 15% 85%, rgba(15, 118, 110, 0.22) 0%, transparent 50%), linear-gradient(135deg, #0d2336 0%, #0e7490 100%);
      color: #F8FAFC;
      border-radius: 20px;
      padding: 1.75rem 2rem;
      font-size: 0.875rem;
      line-height: 1.6;
      margin-top: 1rem;
      margin-bottom: 1.5rem;
      position: relative;
      overflow: hidden;
      box-shadow: 0 12px 35px rgba(18, 48, 74, 0.22);
      border: 1.5px solid rgba(21, 154, 156, 0.4);
    }
    .review-check-banner a {
      color: #94def3;
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(110, 231, 183, 0.25);
      padding: 0.2rem 0.65rem;
      border-radius: 6px;
      text-decoration: none;
      font-weight: 600;
      transition: all 0.2s ease;
      display: inline-block;
    }

    .verdict-box {
      background: linear-gradient(135deg, #0d2336 0%, #0e7490 100%);
      border: 1.5px solid #159A9C;
      border-radius: 16px;
      padding: 1.35rem 1.65rem;
      color: #FFFFFF;
      margin-bottom: 2rem;
      box-shadow: 0 8px 24px rgba(18, 48, 74, 0.15);
    }

    .styled-table-wrap {
      background: #FFFFFF;
      border: 1.5px solid #CBD5E1;
      border-radius: 16px;
      overflow: hidden;
      box-shadow: 0 8px 24px rgba(18, 48, 74, 0.06);
      margin: 1.75rem 0;
    }
    .styled-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.875rem;
    }
    .styled-table th {
      background: #12304A;
      color: #FFFFFF;
      padding: 0.95rem 1.15rem;
      font-size: 0.785rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .styled-table td {
      padding: 0.95rem 1.15rem;
      border-bottom: 1px solid #E2E8F0;
      color: #334155;
    }
    .styled-table tr:last-child td { border-bottom: none; }
    .styled-table tr:nth-child(even) { background: #F8FAFC; }

    .callout-green {
      background: #ECFDF5;
      border: 1.5px solid #10B981;
      border-left: 5px solid #059669;
      border-radius: 14px;
      padding: 1.15rem 1.4rem;
      color: #065F46;
      margin: 1.75rem 0;
    }
    .callout-yellow {
      background: #FFFBEB;
      border: 1.5px solid #F59E0B;
      border-left: 5px solid #D97706;
      border-radius: 14px;
      padding: 1.15rem 1.4rem;
      color: #78350F;
      margin: 1.75rem 0;
    }
    .callout-blue {
      background: #F0F9FF;
      border: 1.5px solid #0284C7;
      border-left: 5px solid #0369A1;
      border-radius: 14px;
      padding: 1.15rem 1.4rem;
      color: #0C4A6E;
      margin: 1.75rem 0;
    }

    .faq-accordion-wrapper {
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
      margin-bottom: 2rem;
      width: 100% !important;
    }
    .faq-accordion-item {
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: 16px;
      overflow: hidden;
      box-shadow: 0 4px 16px rgba(18, 48, 74, 0.04);
      transition: border-color 0.25s ease;
      width: 100% !important;
    }
    .faq-accordion-item:hover { border-color: #159A9C; }
    .faq-accordion-question {
      padding: 1.25rem 1.65rem;
      font-weight: 700;
      font-size: 1.05rem;
      color: #12304A;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      user-select: none;
      list-style: none;
      font-family: var(--font-heading);
    }
    .faq-accordion-question::-webkit-details-marker { display: none; }
    .faq-accordion-answer {
      padding: 0 1.65rem 1.35rem 1.65rem;
      font-size: 0.95rem;
      color: #475569;
      line-height: 1.7;
      border-top: 1px dashed #F1F5F9;
      margin-top: 0.25rem;
      padding-top: 1rem;
    }
  </style>
</head>
<body>
  <header class="site-header">
    <div class="container header-container">
      <a href="index.html" class="site-logo" aria-label="LLC Primer Homepage" style="display: flex; align-items: center;">
        <img src="logo.png" alt="LLC Primer Logo" style="height: 56px; width: auto; object-fit: contain;">
      </a>

      <nav class="nav-menu" id="primaryNavMenu" aria-label="Main Navigation">
        <div class="nav-item">
          <a href="start-llc.html" class="nav-link">
            Start an LLC
          </a>
        </div>
        <div class="nav-item">
          <a href="best-llc-services.html" class="nav-link">
            LLC Services
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </a>
          <div class="dropdown-menu">
            <a href="northwest-registered-agent-review.html" class="dropdown-link">Northwest Registered Agent</a>
            <a href="zenbusiness-vs-northwest.html" class="dropdown-link">ZenBusiness vs Northwest</a>
            <a href="best-registered-agent-services.html" class="dropdown-link">Best Registered Agent</a>
            <a href="best-llc-formation-services.html" class="dropdown-link">Best LLC Formation Services</a>
          </div>
        </div>
        <div class="nav-item">
          <a href="llc-guide.html" class="nav-link active">
            LLC Guides
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </a>
          <div class="dropdown-menu">
            <a href="what-is-an-llc.html" class="dropdown-link">What is an LLC</a>
            <a href="best-state-to-form-an-llc.html" class="dropdown-link">Best State for LLC</a>
            <a href="how-much-does-an-llc-cost.html" class="dropdown-link">How Much Does An LLC Cost</a>
            <a href="how-are-llcs-taxed.html" class="dropdown-link">How Are LLCs Taxed</a>
            <a href="operating-agreement.html" class="dropdown-link">LLC Operating Agreement</a>
            <a href="registered-agent-guide.html" class="dropdown-link">Registered Agent Guide</a>
          </div>
        </div>
        <div class="nav-item">
          <a href="business-setup.html" class="nav-link">
            Business Setup
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </a>
          <div class="dropdown-menu">
            <a href="ein-guide.html" class="dropdown-link">Federal EIN (SS-4 Tax ID)</a>
            <a href="best-business-bank-accounts.html" class="dropdown-link">Best Bank Accounts</a>
            <a href="virtual-business-address.html" class="dropdown-link">Virtual Business Address</a>
            <a href="llc-business-insurance.html" class="dropdown-link">LLC Business Insurance</a>
          </div>
        </div>
        <div class="nav-item">
          <a href="tools.html" class="nav-link">
            Tools
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </a>
          <div class="dropdown-menu">
            <a href="llc-cost-calculator.html" class="dropdown-link">LLC Cost Calculator</a>
            <a href="llc-startup-cost-estimator.html" class="dropdown-link">LLC Startup Cost Estimator</a>
            <a href="sos-search.html" class="dropdown-link">Secretary of State Search</a>
            <a href="quiz.html" class="dropdown-link">Business Structure Quiz</a>
            <a href="llc-vs-scorp.html" class="dropdown-link">LLC vs S-Corp Calculator</a>
            <a href="llc-annual-report-tracker.html" class="dropdown-link">Annual Report Tracker</a>
          </div>
        </div>
        <div class="nav-item">
          <a href="non-resident-llc-guide.html" class="nav-link">
            Non-Residents
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </a>
          <div class="dropdown-menu">
            <a href="best-state-for-non-us-residents.html" class="dropdown-link">Best State</a>
            <a href="ein-guide-for-non-residents.html" class="dropdown-link">EIN Guide</a>
            <a href="llc-cost-for-non-residents.html" class="dropdown-link">LLC Cost</a>
            <a href="bank-account-for-non-residents.html" class="dropdown-link">Bank Account</a>
          </div>
        </div>
      </nav>

      <div class="header-actions">
        <button class="search-trigger" onclick="openSearchModal()" aria-label="Open Search" title="Search state guides (Ctrl+K)">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        </button>
        <a href="quiz.html" class="ls-btn ls-btn--emerald" style="padding: 0.6rem 1.35rem; font-size: 0.875rem; background: var(--color-primary-gradient);">
          Build LLC Plan →
        </a>
        <button class="mobile-toggle" id="mobileNavToggle" aria-label="Toggle Menu">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
        </button>
      </div>
    </div>
  </header>
"""

template_footer = """
  <footer class="site-footer">
    <div class="container footer-container">
      <div class="footer-grid">
        <div class="footer-col brand-col">
          <a href="index.html" class="footer-logo">
            <img src="logo.png" alt="LLC Primer Logo" style="height: 48px; width: auto; object-fit: contain;">
          </a>
          <p class="footer-tagline">
            LLC Primer provides 2026 state guides, filing fee calculators, and step-by-step resources to help founders form, manage, and maintain an LLC in any U.S. state.
          </p>
        </div>

        <div class="footer-col">
          <h4 class="footer-heading">Popular States</h4>
          <ul class="footer-links">
            <li><a href="best-state-to-form-an-llc.html">Wyoming LLC Guide</a></li>
            <li><a href="best-state-to-form-an-llc.html">Delaware LLC Guide</a></li>
            <li><a href="best-state-to-form-an-llc.html">Florida LLC Guide</a></li>
            <li><a href="best-state-to-form-an-llc.html">Texas LLC Guide</a></li>
            <li><a href="best-state-to-form-an-llc.html">California LLC Guide</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4 class="footer-heading">Free Calculators</h4>
          <ul class="footer-links">
            <li><a href="llc-annual-report-tracker.html">Annual Report Tracker</a></li>
            <li><a href="quiz.html">10-Question Diagnostic Quiz</a></li>
            <li><a href="llc-cost-calculator.html">State Fee Calculator (Popup)</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4 class="footer-heading">Post-Formation</h4>
          <ul class="footer-links">
            <li><a href="business-setup.html">Post-LLC Setup</a></li>
            <li><a href="ein-guide.html">EIN Application Guide</a></li>
            <li><a href="operating-agreement.html">Operating Agreement</a></li>
            <li><a href="best-business-bank-accounts.html">Business Banking</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom-bar">
        <p class="footer-disclaimer">
          <b>Disclaimer:</b> LLC Primer is an independent informational website, not a law firm or government agency, and is not affiliated with any Secretary of State office. Nothing on this site constitutes legal or tax advice. Always verify current fees, requirements, and forms with your state's official website or a qualified professional. Some links on this site may be affiliate links, which means LLC Primer may earn a commission at no additional cost to you. See our Affiliate Disclosure.
        </p>
        <div class="footer-copyright">
          &copy; 2026 LLC Primer. All rights reserved. | <a href="#privacy">Privacy Policy</a> | <a href="#terms">Terms of Service</a>
        </div>
      </div>
    </div>
  </footer>

  <div class="modal-overlay" id="searchModalOverlay">
    <div class="modal-card">
      <button class="modal-close" onclick="closeSearchModal()">✕</button>
      <h3 style="color: #FFFFFF; margin-bottom: 1rem;">Search 50-State LLC Fees & Guides</h3>
      <input type="text" id="searchInput" placeholder="Type state name (e.g. Wyoming, Texas, Florida)..." class="state-select-box" style="margin-bottom: 1rem;">
      <div id="searchResults" style="max-height: 250px; overflow-y: auto;"></div>
    </div>
  </div>
  <script src="app.js"></script>
</body>
</html>
"""

def generate_file_content(title, meta, breadcrumb, review_banner, h1, intro_html, main_content_html):
    bc_parts = breadcrumb.replace("Breadcrumb: ", "").split(" / ")
    bc_html = ""
    for i, part in enumerate(bc_parts):
        if i < len(bc_parts) - 1:
            if part == "Home":
                link = "index.html"
            elif part == "LLC Guide":
                link = "llc-guide.html"
            else:
                link = "#"
            bc_html += f'<a href="{link}" style="color: #64748B; text-decoration: none; font-weight: 500;">{part}</a>\\n        <span style="color: #CBD5E1;">/</span>\\n        '
        else:
            bc_html += f'<span style="color: #12304A; font-weight: 700;">{part}</span>'

    banner_text = review_banner.replace("Review banner: ", "")

    body_content = f"""
  <section style="background: white; padding: 1.5rem 0 0rem 0;">
    <div class="guide-content-container">
      <div style="font-size: 0.85rem; color: #64748B; margin-bottom: 1.25rem; display: flex; align-items: center; gap: 0.4rem; flex-wrap: wrap;">
        {bc_html}
      </div>
      <div class="review-check-banner">
        <div style="display: flex; align-items: flex-start; gap: 0.85rem; position: relative; z-index: 2;">
          <div>
            <div style="font-size: 0.75rem; font-weight: 800; color: #F59E0B; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 0.25rem;">
              VERIFIED EDITORIAL METHODOLOGY
            </div>
            <div style="color: #FFFFFF; font-weight: 800; font-size: 1.05rem; margin-bottom: 0.35rem;">
              How This Guide Was Checked
            </div>
            <p style="margin: 0; color: #E2E8F0; font-size: 0.95rem; line-height: 1.6;">
              {banner_text}
            </p>
          </div>
        </div>
      </div>

      <h1 style="font-size: clamp(2.1rem, 3.5vw, 2.8rem); font-weight: 900; color: #12304A; margin-bottom: 0.75rem; line-height: 1.18;">
        {h1}
      </h1>
      {intro_html}
    </div>
  </section>

  <main class="guide-article">
    <div class="guide-content-container">
{main_content_html}
    </div>
  </main>
"""
    return template_head.format(title=title, meta=meta) + body_content + template_footer

def write_out(path, html):
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

print("Helper script ready.")
