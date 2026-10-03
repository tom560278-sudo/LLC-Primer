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
      <strong style="color:#12304A;">New Hampshire</strong>
    </div>
    <article class="guide-article">
      <h1 style="font-size:clamp(2rem,4.5vw,3rem);font-weight:800;color:#12304A;line-height:1.2;margin-bottom:0.75rem;font-family:var(--font-heading);">How to Start an LLC in New Hampshire in 2026</h1>
      <div class="source-banner-box"><strong>Last reviewed:</strong> October 2026 &nbsp;&middot;&nbsp; <strong>Primary sources:</strong> <a href="https://www.sos.nh.gov/" target="_blank" rel="noopener" style="color:#159A9C;font-weight:600;">New Hampshire Secretary of State</a>, <a href="https://www.revenue.nh.gov/" target="_blank" rel="noopener" style="color:#159A9C;font-weight:600;">NH Department of Revenue Administration</a></div>

      <p>If you want to start an LLC in New Hampshire, the state has a relatively simple formation process and no general individual income tax. However, New Hampshire is not simply a "no-tax" state for businesses. LLC owners should understand the state's filing fees, annual report requirement, Business Profits Tax (BPT), Business Enterprise Tax (BET), and any local or industry-specific requirements that may apply.</p>
      <p>The standard New Hampshire LLC Certificate of Formation costs $100 when filed on paper. Online filings carry the state's additional $2 electronic handling charge, making the standard online filing cost $102. New Hampshire also requires LLCs to file an annual report and pay a $100 annual report fee.</p>
      <p>New Hampshire does not have a general statewide sales tax or a broad individual income tax. The former Interest and Dividends Tax was repealed for tax periods beginning January 1, 2025. However, qualifying businesses can still be subject to the Business Profits Tax and Business Enterprise Tax.</p>
      <div class="callout-yellow"><strong>New Hampshire's tax picture is more nuanced than "zero taxes."</strong> New Hampshire does not impose a broad individual income tax, but qualifying businesses may owe BPT and BET. The state's annual LLC filing requirement also continues even when the business has little or no taxable income.</div>

      <div class="styled-table-wrap">
        <table class="styled-table">
          <thead><tr><th>New Hampshire LLC at a Glance</th><th>Details</th></tr></thead>
          <tbody>
            <tr><td>Certificate of Formation</td><td>$100</td></tr>
            <tr><td>Online filing charge</td><td>$102 total</td></tr>
            <tr><td>Annual Report</td><td>$100 / year</td></tr>
            <tr><td>Annual Report deadline</td><td>April 1</td></tr>
            <tr><td>Late fee</td><td>$50</td></tr>
            <tr><td>Sales tax</td><td>No general statewide sales tax</td></tr>
            <tr><td>Individual income tax</td><td>No broad individual income tax</td></tr>
            <tr><td>BPT filing threshold</td><td>More than $109,000 gross business income</td></tr>
            <tr><td>BET filing threshold</td><td>More than $298,000 gross receipts or enterprise value tax base</td></tr>
          </tbody>
        </table>
      </div>

      <div class="key-numbers-card">
        <div class="card-eyebrow">New Hampshire LLC at a Glance &mdash; 2026</div>
        <div class="key-numbers-grid">
          <div class="key-number-cell"><div class="key-number-label">Certificate of Formation</div><div class="key-number-value">$100</div><div class="key-number-sub">Paper</div></div>
          <div class="key-number-cell"><div class="key-number-label">Online Filing</div><div class="key-number-value">$102</div><div class="key-number-sub">(+ $2 charge)</div></div>
          <div class="key-number-cell"><div class="key-number-label">Annual Report</div><div class="key-number-value">$100</div><div class="key-number-sub">Due every year</div></div>
          <div class="key-number-cell"><div class="key-number-label">Annual Report Deadline</div><div class="key-number-value">April 1</div><div class="key-number-sub">Following registration</div></div>
          <div class="key-number-cell"><div class="key-number-label">Late Fee</div><div class="key-number-value">$50</div><div class="key-number-sub">For annual report</div></div>
          <div class="key-number-cell"><div class="key-number-label">BPT Rate</div><div class="key-number-value">7.5%</div><div class="key-number-sub">Business Profits Tax</div></div>
        </div>
      </div>

      <div class="toc-card-box">
        <h3>New Hampshire LLC Guide</h3>
        <ol class="toc-links-ol">
          <li><a href="#name">1. Choose a Name</a></li>
          <li><a href="#agent">2. Appoint a Registered Agent</a></li>
          <li><a href="#certificate">3. File the Certificate of Formation</a></li>
          <li><a href="#agreement">4. Create an Operating Agreement</a></li>
          <li><a href="#ein">5. Get an EIN</a></li>
          <li><a href="#bank">6. Open a Business Bank Account</a></li>
          <li><a href="#licenses">7. Licenses and Permits</a></li>
          <li><a href="#taxes">8. New Hampshire LLC Taxes</a></li>
          <li><a href="#costs">9. New Hampshire LLC Costs</a></li>
          <li><a href="#compliance">10. Annual Report and Ongoing Compliance</a></li>
          <li><a href="#timeline">11. Formation Timeline</a></li>
          <li><a href="#mistakes">12. Common Mistakes</a></li>
          <li><a href="#faq">13. Frequently Asked Questions</a></li>
        </ol>
      </div>

      <h2 id="name">Step 1: Choose a Name</h2>
      <p>Your New Hampshire LLC name must satisfy the state's naming requirements and be distinguishable from existing business names in the Secretary of State's records. The name should use an accepted LLC designation, such as "Limited Liability Company," "LLC," or "L.L.C." The name also cannot create a misleading impression of government affiliation or use restricted terminology without any approval required by law.</p>
      <p>Search the New Hampshire business records through the state's official business search system: <a href="https://quickstart.sos.nh.gov/online/BusinessInquire" target="_blank" rel="noopener">NH QuickStart</a></p>
      <p><strong>Name Reservation &mdash; Optional:</strong> New Hampshire allows an available name to be reserved for 120 days for $15.</p>
      <div class="styled-table-wrap">
        <table class="styled-table">
          <thead><tr><th>Option</th><th>Fee</th><th>Details</th></tr></thead>
          <tbody>
            <tr><td>File Certificate of Formation</td><td>$100</td><td>Formation filing</td></tr>
            <tr><td>Optional name reservation</td><td>$15</td><td>120 days</td></tr>
          </tbody>
        </table>
      </div>

      <h2 id="agent">Step 2: Appoint a Registered Agent</h2>
      <p>Every New Hampshire LLC must maintain a <a href="registered-agent-guide.html">registered agent</a> and registered office in the state. The registered office must provide a physical New Hampshire address suitable for receiving service of process.</p>
      <p><strong>Registered Agent Options:</strong></p>
      <ul>
        <li>Yourself</li>
        <li>Another New Hampshire resident</li>
        <li>Professional registered agent service</li>
      </ul>
      <p>A professional service can be useful for owners who do not maintain a suitable New Hampshire address or who prefer not to use a personal address for the registered-office role.</p>

      <h2 id="certificate">Step 3: File the Certificate of Formation</h2>
      <p>The Certificate of Formation is the document that creates your New Hampshire LLC. New Hampshire uses Form LLC-1 for a domestic LLC. The current Secretary of State filing fee is $100, while electronic filings receive an additional $2 handling charge.</p>
      <p><strong>Information Included:</strong> LLC name | Principal office information | Registered agent and registered office | Business purpose information | Management information | Organizer information</p>
      <div class="styled-table-wrap">
        <table class="styled-table">
          <thead><tr><th>Filing Options</th><th>Fee</th><th>Details</th></tr></thead>
          <tbody>
            <tr><td>Online</td><td>$102</td><td>$100 filing fee + $2 electronic handling charge</td></tr>
            <tr><td>Paper / mail</td><td>$100</td><td>Standard filing fee</td></tr>
            <tr><td>Expedited service</td><td>Additional fee</td><td>Check NH SOS for current info</td></tr>
          </tbody>
        </table>
      </div>
      <p>NH QuickStart &mdash; Official Business Filing Portal: <a href="https://quickstart.sos.nh.gov/" target="_blank" rel="noopener">NH QuickStart</a></p>
      <div class="callout-blue">The Secretary of State states that processing times vary. If timing is important, check the current processing information in NH QuickStart.</div>

      <h2 id="agreement">Step 4: Create an Operating Agreement</h2>
      <p>New Hampshire does not require you to file an operating agreement with the Secretary of State as part of normal LLC formation. Nevertheless, an <a href="operating-agreement.html">operating agreement</a> can document: Ownership percentages | Member contributions | Management structure | Voting rights | Profit and loss distributions | Member responsibilities | Transfer rules | Procedures for adding or removing members | Dissolution procedures.</p>
      <p>For a multi-member LLC, a written agreement can be particularly useful. Keep the signed agreement with the LLC's business records.</p>

      <h2 id="ein">Step 5: Get an EIN</h2>
      <p>An <a href="ein-guide.html">Employer Identification Number (EIN)</a> is a federal tax identification number issued by the IRS. Whether an LLC needs an EIN depends on its federal tax situation and business activities.</p>
      <p>IRS EIN application is free: <a href="https://www.irs.gov/businesses/small-businesses-self-employed/apply-for-an-employer-identification-number-ein-online" target="_blank" rel="noopener">Apply for EIN online</a></p>

      <h2 id="bank">Step 6: Open a Business Bank Account</h2>
      <p>After formation, establish a <a href="best-business-bank-accounts.html">dedicated business bank account</a> for the LLC's business income and expenses.</p>
      <p><strong>Banks commonly request:</strong> Approved Certificate of Formation | EIN confirmation, if applicable | Operating agreement | Government-issued identification | Business address information</p>

      <h2 id="licenses">Step 7: Get Business Licenses and Permits</h2>
      <p>New Hampshire does not impose one universal statewide business license on every LLC simply because it is formed. However, your business may still need: Professional licenses | Industry-specific permits | Local business approvals | Zoning approval | Building or occupancy permits | Food or health permits | Environmental permits | Other regulatory registrations</p>

      <h2 id="taxes">8. New Hampshire LLC Taxes Explained</h2>
      <p>New Hampshire's tax structure is often described as business-friendly, but "no personal income tax" does not mean every LLC owes no state taxes. The most important state-level business taxes for qualifying companies are the Business Profits Tax (BPT) and Business Enterprise Tax (BET). Learn more about <a href="how-are-llcs-taxed.html">how LLCs are taxed</a>.</p>
      <div class="styled-table-wrap">
        <table class="styled-table">
          <thead><tr><th>New Hampshire LLC Tax Overview</th><th>Details</th></tr></thead>
          <tbody>
            <tr><td>Individual income tax</td><td>No broad individual income tax</td></tr>
            <tr><td>Sales tax</td><td>No general statewide sales tax</td></tr>
            <tr><td>Business Profits Tax</td><td>7.5%</td></tr>
            <tr><td>BPT filing threshold</td><td>More than $109,000 gross business income</td></tr>
            <tr><td>Business Enterprise Tax</td><td>0.55%</td></tr>
            <tr><td>BET filing threshold</td><td>More than $298,000 gross receipts or enterprise value tax base</td></tr>
            <tr><td>Annual Report</td><td>$100</td></tr>
          </tbody>
        </table>
      </div>
      <p><strong>Business Profits Tax:</strong> For taxable periods ending on or after December 31, 2023, the BPT rate is 7.5%. For tax years beginning January 1, 2025, businesses with gross business income of more than $109,000 generally must file a BPT return. The filing threshold is not the same thing as saying that every dollar of gross income above the threshold is taxed at 7.5%.</p>
      <p><strong>Business Enterprise Tax:</strong> The BET is calculated using the state's enterprise value tax base. The current rate is 0.55%. For taxable periods beginning on or after January 1, 2025, the filing threshold is more than $298,000 of gross receipts or more than $298,000 of enterprise value tax base. BET paid can generally be used as a credit against BPT.</p>
      <p><strong>Individual Income Tax:</strong> New Hampshire's Interest and Dividends Tax was repealed for tax periods beginning on or after January 1, 2025. That does not eliminate federal income-tax obligations or business-level New Hampshire taxes.</p>
      <p><strong>Sales Tax:</strong> New Hampshire does not have a general statewide sales tax. However, businesses can still have other state or local tax obligations depending on their activity, including meals and rooms tax and business taxes.</p>

      <h2 id="costs">9. New Hampshire LLC Costs and Fees</h2>
      <div class="styled-table-wrap">
        <table class="styled-table">
          <thead><tr><th>Formation Costs</th><th>Details</th></tr></thead>
          <tbody>
            <tr><td>Certificate of Formation &mdash; paper</td><td>$100</td></tr>
            <tr><td>Certificate of Formation &mdash; online</td><td>$102</td></tr>
            <tr><td>EIN</td><td>Free</td></tr>
            <tr><td>Operating Agreement</td><td>DIY: potentially $0</td></tr>
            <tr><td>Registered Agent</td><td>Depends on provider</td></tr>
            <tr><td>Optional name reservation</td><td>$15</td></tr>
            <tr><td>Annual Report</td><td>$100</td></tr>
            <tr><td>Annual Report late fee</td><td>$50</td></tr>
          </tbody>
        </table>
      </div>
      <div class="callout-green"><strong>Minimum State Filing Cost:</strong> If you file the Certificate of Formation by mail and do not purchase optional services, the basic state formation filing is $100. If you file electronically, the standard total is $102. This does not include registered-agent service, professional licenses, local permits, banking costs, tax obligations, or other business expenses.</div>

      <h2 id="compliance">10. Annual Report and Ongoing Compliance</h2>
      <p>New Hampshire LLCs must file an Annual Report and pay the required fee by April 1 each year following the year of registration. The annual report fee is $100.</p>
      <p><strong>Annual Report Basics:</strong> Fee $100 | Deadline April 1 | Late fee $50</p>
      <p>For an LLC managed by its members, New Hampshire requires at least one member to be listed on the annual report. For a manager-managed LLC, at least one manager must be listed.</p>
      <div class="callout-red"><strong>What Happens If You Miss the Deadline?</strong> The Secretary of State states that an LLC that does not file its annual report and fee by April 1 is placed into Not in Good Standing status. If the business fails to file for two consecutive years, the Secretary of State can administratively dissolve the domestic LLC. Set a recurring calendar reminder well before April 1.</div>

      <h2 id="timeline">11. Formation Timeline</h2>
      <div class="dissolution-step"><div class="dissolution-num">1</div><div><div class="dissolution-title">Choose Your Name</div><div class="dissolution-desc">Search New Hampshire's business records and confirm distinguishable name.</div></div></div>
      <div class="dissolution-step"><div class="dissolution-num">2</div><div><div class="dissolution-title">Choose a Registered Agent</div><div class="dissolution-desc">Appoint a qualified registered agent in NH.</div></div></div>
      <div class="dissolution-step"><div class="dissolution-num">3</div><div><div class="dissolution-title">File the Certificate of Formation</div><div class="dissolution-desc">Submit Form LLC-1 through NH QuickStart or by paper.</div></div></div>
      <div class="dissolution-step"><div class="dissolution-num">4</div><div><div class="dissolution-title">Receive Approval</div><div class="dissolution-desc">Processing time varies. Check NH QuickStart.</div></div></div>
      <div class="dissolution-step"><div class="dissolution-num">5</div><div><div class="dissolution-title">Create Your Operating Agreement</div><div class="dissolution-desc">Document ownership and management rules after formation.</div></div></div>
      <div class="dissolution-step"><div class="dissolution-num">6</div><div><div class="dissolution-title">Obtain an EIN if Needed</div><div class="dissolution-desc">Apply for a federal employer identification number.</div></div></div>
      <div class="dissolution-step"><div class="dissolution-num">7</div><div><div class="dissolution-title">Open a Business Bank Account</div><div class="dissolution-desc">Keep your finances separate.</div></div></div>
      <div class="dissolution-step"><div class="dissolution-num">8</div><div><div class="dissolution-title">Handle Licenses and Taxes</div><div class="dissolution-desc">Review federal, state, local, professional, payroll and industry-specific requirements.</div></div></div>
      <div class="dissolution-step"><div class="dissolution-num">9</div><div><div class="dissolution-title">Ongoing</div><div class="dissolution-desc">File your Annual Report and $100 fee by April 1 each year.</div></div></div>

      <h2 id="mistakes">12. Common Mistakes</h2>
      <ol>
        <li><strong>Assuming "No Income Tax" Means No Business Taxes</strong> &mdash; New Hampshire does not impose a broad individual income tax, but qualifying businesses can still be subject to BPT and BET.</li>
        <li><strong>Forgetting the April 1 Annual Report</strong> &mdash; The annual report is a separate compliance requirement from income-tax filings. Current fee is $100, with a $50 late fee.</li>
        <li><strong>Budgeting Only for the $100 Formation Fee</strong> &mdash; Registered-agent services, licenses, permits, banking, tax obligations and other expenses can increase the total startup cost.</li>
        <li><strong>Treating an LLC as Automatically Anonymous</strong> &mdash; New Hampshire's public business records can include member or manager information through annual reporting requirements.</li>
        <li><strong>Applying for an EIN Without Checking Whether You Need One</strong> &mdash; Not every single-member LLC automatically needs an EIN.</li>
      </ol>

      <div class="primary-sources-box">
        <div class="primary-src-eyebrow">Primary Sources</div>
        <div class="primary-src-grid">
          <div class="primary-src-item"><a href="https://www.sos.nh.gov/" class="primary-src-link" target="_blank" rel="noopener">New Hampshire Secretary of State &rarr;</a></div>
          <div class="primary-src-item"><a href="https://quickstart.sos.nh.gov/" class="primary-src-link" target="_blank" rel="noopener">NH QuickStart Business Filing Portal &rarr;</a></div>
          <div class="primary-src-item"><a href="https://www.revenue.nh.gov/" class="primary-src-link" target="_blank" rel="noopener">NH Department of Revenue Administration &rarr;</a></div>
          <div class="primary-src-item"><a href="https://www.revenue.nh.gov/business-tax-forms/business-profits-tax" class="primary-src-link" target="_blank" rel="noopener">NH Business Profits Tax &rarr;</a></div>
          <div class="primary-src-item"><a href="https://www.revenue.nh.gov/business-tax-forms/business-enterprise-tax" class="primary-src-link" target="_blank" rel="noopener">NH Business Enterprise Tax &rarr;</a></div>
        </div>
      </div>

      <div class="bottom-line-card">
        <div style="font-size:0.72rem;font-weight:800;text-transform:uppercase;letter-spacing:0.08em;color:rgba(255,255,255,0.5);margin-bottom:0.75rem;">THE BOTTOM LINE</div>
        <p style="color:#fff;margin:0;line-height:1.7;">Starting a New Hampshire LLC has a straightforward state filing process. The Certificate of Formation costs $100, or $102 when filed electronically because of the state's $2 electronic handling charge. The ongoing state compliance requirement is the $100 Annual Report due April 1 each year, with a $50 late fee. New Hampshire also has no broad individual income tax and no general statewide sales tax, but qualifying businesses can owe BPT and BET.</p>
      </div>

      <h2 id="faq">13. Frequently Asked Questions</h2>
      <div class="faq-accordion-wrapper">
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">1</span><span>How much does it cost to start an LLC in New Hampshire?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">$100 paper, $102 online (+$2 electronic handling charge). Optional: registered-agent service, name reservation, licenses, permits, professional assistance.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">2</span><span>How much is the New Hampshire LLC annual report?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">$100 fee. Deadline April 1. Late fee $50.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">3</span><span>Does New Hampshire have an individual income tax?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">New Hampshire repealed its Interest and Dividends Tax for tax periods beginning January 1, 2025. Federal taxes and applicable business-level state taxes still apply.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">4</span><span>Does New Hampshire have a sales tax?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">No general statewide sales tax. Businesses can have other tax obligations depending on their activities.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">5</span><span>What is the New Hampshire Business Profits Tax?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">BPT is a state business tax on taxable business profits. Current rate 7.5% for taxable periods ending on or after December 31, 2023. Filing threshold more than $109,000 gross business income for tax years beginning January 1, 2025.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">6</span><span>What is the Business Enterprise Tax?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">BET based on enterprise value tax base. Current rate 0.55%. Filing threshold more than $298,000 gross receipts or enterprise value tax base for taxable periods beginning January 1, 2025.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">7</span><span>When is the New Hampshire LLC Annual Report due?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">April 1 each year following year of registration.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">8</span><span>What happens if I miss the April 1 deadline?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">$50 late fee and Not in Good Standing status. Failure to file for two consecutive years can result in administrative dissolution.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">9</span><span>Do I have to reserve my LLC name before filing?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">No. Name reservation is optional, $15 fee.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">10</span><span>Do I need an operating agreement?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">Not required to file. A written agreement can document ownership, management, voting and other internal LLC rules.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">11</span><span>Is a New Hampshire LLC anonymous?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">Do not treat as completely anonymous. Member-managed LLCs must list at least one member on the annual report; manager-managed LLCs must list at least one manager.</div>
        </details>
      </div>
""" + footer

html_content = html_content.replace(
    '<title>How to Start an LLC in Michigan (2026) | LLC Primer</title>',
    '<title>How to Start an LLC in New Hampshire (2026) | LLC Primer</title>'
)
html_content = html_content.replace(
    '<meta name="description" content="Complete guide to forming a Michigan LLC in 2026. $50 Articles of Organization via LARA, $25 Annual Statement by February 15, 4.25% income tax, expedited options, veteran fee waiver available.">',
    '<meta name="description" content="Complete guide to forming a New Hampshire LLC in 2026. $100 Certificate of Formation ($102 online), $100 annual report due April 1, Business Profits Tax 7.5%, Business Enterprise Tax 0.55%, no broad individual income tax or sales tax.">'
)

with open(r'd:\rename\how-to-start-llc-in-new-hampshire.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
