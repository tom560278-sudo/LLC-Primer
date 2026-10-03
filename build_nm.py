import re

template_path = r'd:\rename\how-to-start-llc-in-michigan.html'
with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

header_match = re.search(r'(.*?<main class="guide-content-container">)', template, re.DOTALL)
header = header_match.group(1)

footer_match = re.search(r'(</article>\s*</main>\s*<footer class="site-footer">.*)', template, re.DOTALL)
footer = footer_match.group(1)

html_content = header + """
    <div style="font-size:0.85rem;color:#64748B;margin-top:1.5rem;margin-bottom:1rem;">
      <a href="index.html" style="color:#64748B;text-decoration:none;">LLC Primer</a> &nbsp;/&nbsp;
      <a href="start-llc.html" style="color:#64748B;text-decoration:none;">How to Start an LLC</a> &nbsp;/&nbsp;
      <strong style="color:#12304A;">New Mexico</strong>
    </div>
    <article class="guide-article">
      <h1 style="font-size:clamp(2rem,4.5vw,3rem);font-weight:800;color:#12304A;line-height:1.2;margin-bottom:0.75rem;font-family:var(--font-heading);">How to Start an LLC in New Mexico in 2026</h1>
      <div class="source-banner-box"><strong>Last reviewed:</strong> October 2026 &nbsp;&middot;&nbsp; <strong>Primary sources:</strong> <a href="https://www.sos.state.nm.us/" target="_blank" rel="noopener" style="color:#159A9C;font-weight:600;">New Mexico Secretary of State</a>, <a href="https://www.tax.newmexico.gov/" target="_blank" rel="noopener" style="color:#159A9C;font-weight:600;">New Mexico Taxation and Revenue Department</a></div>

      <p>New Mexico charges $50 to form a domestic LLC. Unlike many states, New Mexico does not require LLCs to file an annual or biennial report with the Secretary of State, so there is no recurring Secretary of State annual-report fee for a standard New Mexico LLC. That does not mean the LLC has no ongoing obligations: it must maintain a registered agent and may have state tax registration and filing obligations depending on its activities.</p>
      
      <p>To start an LLC in New Mexico, you file Articles of Organization through the New Mexico Secretary of State's online business filing system and pay the $50 state filing fee. New Mexico moved business filings into its online portal in December 2024, and paper business filings are no longer accepted.</p>
      
      <p>New Mexico's LLC formation documents do not require the names of members or managers in the statutory Articles of Organization. The Secretary of State's online system can, however, allow additional information to be entered, and information submitted through the system should be treated as potentially public. This makes New Mexico's public-record requirements different from states that require member or manager information directly in their formation documents, but it should not be described as complete or universal owner anonymity.</p>
      
      <p>New Mexico also has a Gross Receipts Tax (GRT) rather than a conventional retail-sales-tax system. GRT is imposed on businesses and can apply to sales of property, leasing or licensing, and services performed in New Mexico, subject to exemptions, deductions, sourcing rules, and other exceptions. The combined rate depends on the applicable location and tax period.</p>

      <div class="key-numbers-card">
        <div class="card-eyebrow">New Mexico LLC at a Glance &mdash; 2026</div>
        <div class="key-numbers-grid">
          <div class="key-number-cell"><div class="key-number-label">Filing Fee</div><div class="key-number-value">$50</div><div class="key-number-sub">Online only</div></div>
          <div class="key-number-cell"><div class="key-number-label">Paper Filing</div><div class="key-number-value">No</div><div class="key-number-sub">Not accepted</div></div>
          <div class="key-number-cell"><div class="key-number-label">Annual Report</div><div class="key-number-value">None</div><div class="key-number-sub">For NM LLCs</div></div>
          <div class="key-number-cell"><div class="key-number-label">Registered Agent</div><div class="key-number-value">Required</div><div class="key-number-sub">In-state address</div></div>
          <div class="key-number-cell"><div class="key-number-label">Name Reservation</div><div class="key-number-value">$20</div><div class="key-number-sub">Optional</div></div>
          <div class="key-number-cell"><div class="key-number-label">GRT Rate</div><div class="key-number-value">Varies</div><div class="key-number-sub">Location-dependent</div></div>
        </div>
      </div>

      <div class="styled-table-wrap">
        <table class="styled-table">
          <thead><tr><th>New Mexico LLC at a Glance</th><th>Details</th></tr></thead>
          <tbody>
            <tr><td>Filing Fee</td><td>$50</td></tr>
            <tr><td>Processing Time</td><td>Varies &mdash; check New Mexico Secretary of State portal</td></tr>
            <tr><td>Annual Report</td><td>None for New Mexico LLCs</td></tr>
            <tr><td>Registered Agent</td><td>Required &mdash; must maintain a New Mexico registered office</td></tr>
            <tr><td>Owner Information</td><td>Member/manager names not required in statutory Articles</td></tr>
            <tr><td>Franchise Tax</td><td>$50 corporate franchise tax applies to corporations and ... (Content Truncated)</td></tr>
          </tbody>
        </table>
      </div>
""" + footer

html_content = html_content.replace(
    '<title>How to Start an LLC in Michigan (2026) | LLC Primer</title>',
    '<title>How to Start an LLC in New Mexico (2026) | LLC Primer</title>'
)
html_content = html_content.replace(
    '<meta name="description" content="Complete guide to forming a Michigan LLC in 2026. $50 Articles of Organization via LARA, $25 Annual Statement by February 15, 4.25% income tax, expedited options, veteran fee waiver available.">',
    '<meta name="description" content="Complete guide to forming a New Mexico LLC in 2026. $50 Articles of Organization filed online only (no paper filing since Dec 2024), no annual report required, Gross Receipts Tax instead of sales tax, registered agent required.">'
)

with open(r'd:\rename\how-to-start-llc-in-new-mexico.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
