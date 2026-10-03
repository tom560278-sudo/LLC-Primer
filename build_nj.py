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
      <strong style="color:#12304A;">New Jersey</strong>
    </div>
    <article class="guide-article">
      <h1 style="font-size:clamp(2rem,4.5vw,3rem);font-weight:800;color:#12304A;line-height:1.2;margin-bottom:0.75rem;font-family:var(--font-heading);">How to Start an LLC in New Jersey in 2026</h1>
      <div class="source-banner-box"><strong>Last reviewed:</strong> October 2026 &nbsp;&middot;&nbsp; <strong>Primary sources:</strong> <a href="https://www.nj.gov/treasury/revenue/gettingregistered.shtml" target="_blank" rel="noopener" style="color:#159A9C;font-weight:600;">NJ Division of Revenue and Enterprise Services</a>, <a href="https://www.nj.gov/treasury/taxation/" target="_blank" rel="noopener" style="color:#159A9C;font-weight:600;">NJ Division of Taxation</a></div>

      <p>If you want to start an LLC in New Jersey, the current state formation fee for a domestic LLC is $100. New Jersey also requires businesses to complete state tax and employer registration through NJ-REG after formation when applicable. For-profit LLCs are instructed by the New Jersey Division of Revenue and Enterprise Services (DORES) to obtain a federal EIN before filing the formation document.</p>
      <p>The practical sequence is generally: choose an available LLC name, obtain an EIN, designate a New Jersey registered agent, file the Certificate of Formation, complete NJ-REG, then establish business banking, licenses, permits and ongoing compliance procedures that apply to the business.</p>
      <div class="callout-yellow"><strong>2026 Fee Update:</strong> New Jersey's current DORES fee schedule lists the domestic LLC Certificate of Formation at $100. Older guides may still show the previous $125 filing fee.</div>

      <div class="styled-table-wrap">
        <table class="styled-table">
          <thead><tr><th>New Jersey LLC &mdash; Key Facts</th><th>Details</th></tr></thead>
          <tbody>
            <tr><td>Formation Fee</td><td>$100</td></tr>
            <tr><td>Registered Agent</td><td>Required</td></tr>
            <tr><td>EIN</td><td>Obtain before NJ filing</td></tr>
            <tr><td>NJ-REG</td><td>After formation</td></tr>
            <tr><td>Annual Report</td><td>$75 each year</td></tr>
            <tr><td>General Statewide License</td><td>No blanket license</td></tr>
          </tbody>
        </table>
      </div>

      <div class="key-numbers-card">
        <div class="card-eyebrow">New Jersey LLC at a Glance &mdash; 2026</div>
        <div class="key-numbers-grid">
          <div class="key-number-cell"><div class="key-number-label">Formation Fee</div><div class="key-number-value">$100</div><div class="key-number-sub">Current state fee</div></div>
          <div class="key-number-cell"><div class="key-number-label">Annual Report</div><div class="key-number-value">$75</div><div class="key-number-sub">Due every year</div></div>
          <div class="key-number-cell"><div class="key-number-label">Annual Report Due</div><div class="key-number-value">Last day</div><div class="key-number-sub">of anniversary month</div></div>
          <div class="key-number-cell"><div class="key-number-label">NJ-REG</div><div class="key-number-value">Required</div><div class="key-number-sub">After formation</div></div>
          <div class="key-number-cell"><div class="key-number-label">EIN</div><div class="key-number-value">Before filing</div><div class="key-number-sub">(for-profit LLCs)</div></div>
          <div class="key-number-cell"><div class="key-number-label">Name Reservation</div><div class="key-number-value">$50</div><div class="key-number-sub">Optional</div></div>
        </div>
      </div>

      <div class="toc-card-box">
        <h3>New Jersey LLC Guide</h3>
        <ol class="toc-links-ol">
          <li><a href="#name">1. Choose an Available LLC Name</a></li>
          <li><a href="#ein">2. Get an EIN From the IRS</a></li>
          <li><a href="#agent">3. Choose a New Jersey Registered Agent</a></li>
          <li><a href="#certificate">4. File the New Jersey Certificate of Formation</a></li>
          <li><a href="#nj-reg">5. Complete NJ-REG</a></li>
          <li><a href="#agreement">6. Create an Operating Agreement</a></li>
          <li><a href="#bank">7. Separate the LLC's Finances</a></li>
          <li><a href="#licenses">8. Check Licenses and Permits</a></li>
          <li><a href="#costs">9. New Jersey LLC Costs</a></li>
          <li><a href="#taxes">10. New Jersey LLC Taxes</a></li>
          <li><a href="#compliance">11. Annual Compliance</a></li>
          <li><a href="#change">12. Change of Registered Agent or Office</a></li>
          <li><a href="#guides">13. New Jersey Task Guides</a></li>
          <li><a href="#faq">14. FAQ</a></li>
        </ol>
      </div>

      <h2 id="name">1. Choose an Available New Jersey LLC Name</h2>
      <p>Your New Jersey LLC name must comply with New Jersey's naming requirements and be distinguishable from existing business names in the state's records. The name should also include an appropriate limited-liability-company designator, such as LLC, L.L.C., or Limited Liability Company.</p>
      <p>Before filing, search New Jersey's business records to identify potentially conflicting names. A name that appears available in a search is not necessarily guaranteed to be approved.</p>
      <p><strong>New Jersey LLC Naming Rules:</strong> The name should be distinguishable from existing entities registered with New Jersey DORES. Certain words or names may require additional approval, particularly where they could imply a regulated professional activity or government affiliation.</p>
      <p>Use the official New Jersey Business Entity Name Search: <a href="https://www.njportal.com/dor/businessnamesearch" target="_blank" rel="noopener">Business Name Search</a></p>
      <p><strong>Name Reservation &mdash; Optional:</strong> New Jersey does not require you to reserve an LLC name before filing. If you are not ready to form the LLC but want to reserve an available name, the current state fee is $50.</p>
      <div class="styled-table-wrap">
        <table class="styled-table">
          <thead><tr><th>Option</th><th>Fee</th><th>Details</th></tr></thead>
          <tbody>
            <tr><td>File Certificate of Formation</td><td>$100</td><td>Form the LLC now</td></tr>
            <tr><td>Name Reservation</td><td>$50</td><td>Hold an available name before formation</td></tr>
          </tbody>
        </table>
      </div>
      <div class="callout-blue"><strong>Before filing:</strong> If the LLC will operate under a different public-facing name, check New Jersey's requirements for alternate or trade names separately. A domain-name registration is also separate from state business-name approval.</div>

      <h2 id="ein">2. Get an EIN From the IRS</h2>
      <p>A federal <a href="ein-guide.html">Employer Identification Number (EIN)</a> is issued by the IRS and is free to obtain directly from the federal government. For-profit New Jersey LLCs are instructed by DORES to obtain an EIN before filing the Certificate of Formation. The EIN is also commonly needed for federal tax administration, hiring employees and business banking.</p>
      <p>U.S.-based applicants who qualify for the IRS online application can generally receive an EIN electronically. The EIN itself has no IRS application fee.</p>

      <h2 id="agent">3. Choose a New Jersey Registered Agent</h2>
      <p>A New Jersey LLC must maintain a registered office in New Jersey and designate an agent for service of process. An individual serving as the agent must meet New Jersey's residency requirements. The registered office must be a physical location in New Jersey rather than simply a P.O. box.</p>
      <p>Learn more about appointing a <a href="registered-agent-guide.html">registered agent</a>.</p>
      <p><strong>Registered Agent Options:</strong></p>
      <ul>
        <li>Yourself &mdash; You may serve as the registered agent if you meet New Jersey's requirements. The address becomes part of the business's state record.</li>
        <li>Another Qualified New Jersey Resident</li>
        <li>Professional Registered Agent Service &mdash; A commercial service can provide a qualifying New Jersey address and receive service of process.</li>
      </ul>
      <p>A professional registered agent can be useful for owners who do not maintain a suitable New Jersey address or who prefer not to use a personal address in the public business record.</p>

      <h2 id="certificate">4. File the New Jersey Certificate of Formation</h2>
      <p>The Certificate of Formation is the state filing that creates a domestic New Jersey LLC. The current New Jersey state filing fee is $100.</p>
      <p>Before filing, have your LLC name, EIN, registered-agent information and other required business details ready. Use the current New Jersey filing system.</p>
      <p>Official New Jersey Business Formation Service: <a href="https://www.njportal.com/dor/businessformation" target="_blank" rel="noopener">NJ Business Formation Portal</a></p>
      <div class="callout-yellow"><strong>2026 Filing Fee: $100</strong> &mdash; The $100 fee is the current state fee listed by New Jersey DORES for a domestic LLC Certificate of Formation.</div>

      <h2 id="nj-reg">5. Complete NJ-REG Before Starting Business Activity</h2>
      <p>Creating the LLC and registering the business for New Jersey tax and employer purposes are separate steps. After formation, the LLC receives a New Jersey 10-digit Entity ID. Use that information, along with the EIN, when completing NJ-REG.</p>
      <p>New Jersey's Division of Taxation currently instructs businesses to complete NJ-REG at least 15 business days before doing business in New Jersey or opening an additional New Jersey location.</p>
      <p><strong>What NJ-REG Does:</strong> Can establish New Jersey tax and employer accounts &mdash; Sales Tax registration | Employer withholding | Other New Jersey tax accounts</p>
      <p>Official New Jersey Tax / Employer Registration: <a href="https://www.njportal.com/dor/businessregistration" target="_blank" rel="noopener">NJ-REG Portal</a></p>
      <p><strong>Business Registration Certificate:</strong> After completing registration, the business can obtain a Business Registration Certificate (BRC) when applicable. A BRC is evidence of New Jersey business registration and is required for certain purposes, including some public contracting. It is not a universal business license.</p>

      <h2 id="agreement">6. Create an Operating Agreement</h2>
      <p>An <a href="operating-agreement.html">operating agreement</a> is the internal document that explains how your New Jersey LLC will be owned and managed. New Jersey does not require you to file an operating agreement with the state.</p>
      <p>A written agreement can help document: Ownership percentages | Member contributions | Management responsibilities | Voting rights | Profit and loss distributions | Transfers of membership interests | Member withdrawal procedures | Dispute procedures | Dissolution procedures.</p>

      <h2 id="bank">7. Separate the LLC's Finances</h2>
      <p>After formation, maintain a <a href="best-business-bank-accounts.html">dedicated business bank account</a> for the LLC's business income and expenses.</p>
      <p><strong>What a Bank May Request:</strong> Certificate of Formation or formation confirmation | EIN confirmation | Government-issued identification | Ownership information | Operating agreement | Business address information</p>

      <h2 id="licenses">8. Check Licenses and Permits</h2>
      <p>New Jersey does not require every LLC to purchase one general statewide business license simply because the LLC was formed. Licensing requirements depend on the business's activities, profession, location.</p>
      <p><strong>State-Level Requirements:</strong> Certain professions and industries are regulated. Depending on business: Construction | Health care | Child care | Real estate | Food services | Professional services | Transportation | Financial services</p>
      <p><strong>Local Requirements:</strong> Zoning approval | Certificate of occupancy | Building permits | Fire inspections | Health permits | Sign permits | Local business registrations</p>

      <h2 id="costs">9. New Jersey LLC Costs and Fees</h2>
      <div class="styled-table-wrap">
        <table class="styled-table">
          <thead><tr><th>Item</th><th>Cost</th><th>Details</th></tr></thead>
          <tbody>
            <tr><td>Certificate of Formation</td><td>$100</td><td>Required to create a domestic NJ LLC</td></tr>
            <tr><td>Annual Report</td><td>$75</td><td>Required each year</td></tr>
            <tr><td>LLC Name Reservation</td><td>$50</td><td>Optional before formation</td></tr>
            <tr><td>Change Registered Agent / Office</td><td>$25</td><td>If you later change the registered record</td></tr>
          </tbody>
        </table>
      </div>
      <p>The state formation fee does not include professional services, registered-agent services, insurance, local permits or applicable taxes.</p>

      <h2 id="taxes">10. New Jersey LLC Taxes Explained</h2>
      <p>An LLC is a legal business structure, but it does not automatically determine one universal tax treatment. For federal and New Jersey tax purposes, the treatment depends on factors such as the number of owners, federal tax classification, elections, New Jersey-source activity, employees and the type of income earned. Learn more about <a href="how-are-llcs-taxed.html">how LLCs are taxed</a>.</p>
      <p><strong>New Jersey Partnership Filing Fee:</strong> Certain LLCs treated as partnerships for federal tax purposes may be subject to New Jersey's partnership filing fee. For example, a partnership with New Jersey-source income or loss and more than two owners can generally be subject to a $150 filing fee per owner, subject to the state's maximum amount. This is not a blanket $150 tax on every multi-member LLC.</p>
      <p><strong>Pass-Through Business Alternative Income Tax:</strong> Eligible pass-through businesses can elect New Jersey's Pass-Through Business Alternative Income Tax (PTE/BAIT). Single-member LLCs are not eligible for the BAIT election.</p>
      <p><strong>New Jersey Sales Tax:</strong> New Jersey imposes Sales Tax on taxable goods and services at the applicable state rate. NJ-REG is used to register the business for applicable tax accounts.</p>

      <h2 id="compliance">11. Annual Compliance</h2>
      <p>The primary recurring state filing for a New Jersey LLC is the Annual Report. The current annual report fee is $75. New Jersey generally ties the LLC's annual report due date to the last day of the LLC's formation-anniversary month.</p>
      <p>For example, an LLC formed on June 15 would generally have its annual report due by the last day of June each year.</p>
      <div class="callout-red"><strong>Missing Annual Reports</strong> &mdash; Failing to maintain required annual reports can affect the LLC's status with the state. New Jersey can place a domestic LLC on the inactive list when required annual reports are not filed for the applicable period.</div>

      <h2 id="change">12. Change of Registered Agent or Office</h2>
      <p>Change of Registered Agent or Office: New Jersey currently lists a $25 filing fee for the applicable change.</p>
      
      <h2 id="guides">13. New Jersey Task Guides</h2>
      <p>Make sure to keep your business records organized and consider using a professional service if you have questions.</p>

      <div class="primary-sources-box">
        <div class="primary-src-eyebrow">Primary Sources</div>
        <div class="primary-src-grid">
          <div class="primary-src-item"><a href="https://www.nj.gov/treasury/revenue/gettingregistered.shtml" class="primary-src-link" target="_blank" rel="noopener">NJ Division of Revenue &amp; Enterprise Services &rarr;</a></div>
          <div class="primary-src-item"><a href="https://www.nj.gov/treasury/revenue/fees.shtml" class="primary-src-link" target="_blank" rel="noopener">NJ DORES Registry Fee Schedule &rarr;</a></div>
          <div class="primary-src-item"><a href="https://business.nj.gov/pages/register-your-business" class="primary-src-link" target="_blank" rel="noopener">Business.NJ.gov &rarr;</a></div>
          <div class="primary-src-item"><a href="https://www.nj.gov/treasury/taxation/br1.shtml" class="primary-src-link" target="_blank" rel="noopener">NJ Division of Taxation &rarr;</a></div>
          <div class="primary-src-item"><a href="https://www.njportal.com/dor/businessformation" class="primary-src-link" target="_blank" rel="noopener">Official New Jersey Business Formation Service &rarr;</a></div>
          <div class="primary-src-item"><a href="https://www.njportal.com/dor/businessregistration" class="primary-src-link" target="_blank" rel="noopener">Official New Jersey Tax/Employer Registration &rarr;</a></div>
        </div>
      </div>

      <div class="bottom-line-card">
        <div style="font-size:0.72rem;font-weight:800;text-transform:uppercase;letter-spacing:0.08em;color:rgba(255,255,255,0.5);margin-bottom:0.75rem;">THE BOTTOM LINE</div>
        <p style="color:#fff;margin:0;line-height:1.7;">For a new domestic New Jersey LLC, the current state formation fee is $100. For-profit LLCs should obtain an EIN before filing according to the state's current registration instructions, then complete the Certificate of Formation, NJ-REG and the other registrations that apply to the business. After formation, maintain a qualifying New Jersey registered agent, keep business and personal finances separate, obtain required licenses or permits, and file the $75 annual report by the last day of the LLC's formation-anniversary month.</p>
      </div>

      <h2 id="faq">14. FAQ</h2>
      <div class="faq-accordion-wrapper">
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">1</span><span>How much does it cost to start an LLC in New Jersey?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">Current state fee $100. Name reservation, registered-agent service, professional assistance, licenses, insurance and other expenses are separate. Annual report currently $75.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">2</span><span>Do I need an EIN before forming a New Jersey LLC?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">For-profit LLCs are instructed by New Jersey DORES to obtain an EIN before filing the Certificate of Formation. EIN issued by IRS at no charge.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">3</span><span>When should I file NJ-REG?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">After LLC formed and has received New Jersey Entity ID. At least 15 business days before doing business in New Jersey.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">4</span><span>Does every New Jersey LLC need a business license?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">No. Specific professional licenses, tax registrations and local permits can apply depending on business activity and location.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">5</span><span>How much is the New Jersey LLC annual report?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">$75. Generally due by the last day of the LLC's formation-anniversary month.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">6</span><span>When is the New Jersey LLC annual report due?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">Last day of the LLC's formation-anniversary month. LLC formed in October has annual report due by October 31 each year.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">7</span><span>What happens if I do not file the annual report?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">Can affect LLC's status. New Jersey can place a domestic LLC on the inactive list.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">8</span><span>What if my LLC was formed in another state?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">May need to obtain authority to conduct business in New Jersey as a foreign LLC.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">9</span><span>Can I form a New Jersey LLC if I live outside New Jersey?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">Living outside New Jersey does not by itself prevent formation. LLC must satisfy New Jersey's registered-office and registered-agent requirements.</div>
        </details>
        <details class="faq-accordion-item">
          <summary class="faq-accordion-question">
            <div class="faq-q-badge-title"><span class="faq-q-badge">10</span><span>Can I form a New Jersey LLC as a non-U.S. resident?</span></div>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="faq-accordion-answer">A non-U.S. resident can generally form a New Jersey LLC, but federal tax, EIN and banking requirements can differ. New Jersey registered agent still required.</div>
        </details>
      </div>
""" + footer

html_content = html_content.replace(
    '<title>How to Start an LLC in Michigan (2026) | LLC Primer</title>',
    '<title>How to Start an LLC in New Jersey (2026) | LLC Primer</title>'
)
html_content = html_content.replace(
    '<meta name="description" content="Complete guide to forming a Michigan LLC in 2026. $50 Articles of Organization via LARA, $25 Annual Statement by February 15, 4.25% income tax, expedited options, veteran fee waiver available.">',
    '<meta name="description" content="Complete guide to forming a New Jersey LLC in 2026. $100 Certificate of Formation (updated from $125), EIN required before filing, NJ-REG after formation, $75 annual report due last day of anniversary month.">'
)

with open(r'd:\rename\how-to-start-llc-in-new-jersey.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
