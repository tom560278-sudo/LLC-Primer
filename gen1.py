import os

template_path = r'd:\rename\zenbusiness-vs-northwest.html'
with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

# Extract header (up to the Breadcrumb start, or up to the section tag)
header_split = template.split('<!-- BREADCRUMB NAVIGATION -->')
header_part1 = header_split[0]

# Replace title and meta in header_part1
def set_title_meta(header, title, meta):
    import re
    header = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', header, flags=re.DOTALL)
    header = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{meta}">', header, flags=re.DOTALL)
    return header

footer_split = template.split('</main>')
footer_part = '</main>' + footer_split[1]

# Now, we define the content for each page
pages = []

# FILE 1: series-llc.html
content1 = """<!-- BREADCRUMB NAVIGATION -->
      <div style="font-size: 0.85rem; color: #64748B; margin-bottom: 1.25rem; display: flex; align-items: center; gap: 0.4rem; flex-wrap: wrap;">
        <a href="index.html" style="color: #64748B; text-decoration: none; font-weight: 500;">Home</a>
        <span style="color: #CBD5E1;">/</span>
        <a href="llc-guide.html" style="color: #64748B; text-decoration: none; font-weight: 500;">LLC Guide</a>
        <span style="color: #CBD5E1;">/</span>
        <span style="color: #12304A; font-weight: 700;">Series LLC</span>
      </div>
      
      <!-- Verification Banner -->
      <div class="review-check-banner">
        <div style="display: flex; align-items: flex-start; gap: 0.85rem; position: relative; z-index: 2;">
          <div>
            <div style="color: #FFFFFF; font-weight: 800; font-size: 1.05rem; margin-bottom: 0.35rem;">
              Last reviewed: October 5, 2026
            </div>
            <p style="margin: 0; color: #E2E8F0; font-size: 0.95rem; line-height: 1.6;">
              Official sources: State statutes, Secretary of State agency materials, and federal sources where applicable. Series LLC rules are primarily determined by state law.
            </p>
          </div>
        </div>
      </div>

      <h1 style="font-size: clamp(2.1rem, 3.5vw, 2.8rem); font-weight: 900; color: #12304A; margin-bottom: 0.75rem; line-height: 1.18;">
        Series LLC (2026): How It Works, States &amp; Rules
      </h1>
      <p style="font-size: 1.05rem; color: #334155; line-height: 1.65; margin-bottom: 1.5rem; max-width: 860px;">
        A Series LLC is not one standardized legal structure. In 2026, states use different approaches to series, including protected series, registered series, designated series and series created under a parent LLC's governing documents.
      </p>
      <p style="font-size: 1.05rem; color: #334155; line-height: 1.65; margin-bottom: 1.5rem; max-width: 860px;">
        <strong>The rule that matters most:</strong> Series LLC law is state-specific. Formation procedures, public filings, recordkeeping requirements, recurring obligations, tax treatment and liability protections can differ substantially. Do not assume that a Series LLC formed under one state's law will operate the same way in another state.
      </p>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-bottom: 2rem;">
        <div class="quick-comp-card" style="display:block; text-align:center;">
          <div style="font-size: 1.5rem; font-weight: 900; color: #12304A;">52</div>
          <div style="font-size: 0.85rem; color: #64748B;">Jurisdictions reviewed</div>
        </div>
        <div class="quick-comp-card" style="display:block; text-align:center;">
          <div style="font-size: 1.5rem; font-weight: 900; color: #12304A;">24</div>
          <div style="font-size: 0.85rem; color: #64748B;">Jurisdictions with domestic series framework</div>
        </div>
        <div class="quick-comp-card" style="display:block; text-align:center;">
          <div style="font-size: 1.5rem; font-weight: 900; color: #12304A;">4</div>
          <div style="font-size: 0.85rem; color: #64748B;">Series structures explained</div>
        </div>
        <div class="quick-comp-card" style="display:block; text-align:center;">
          <div style="font-size: 1.5rem; font-weight: 900; color: #12304A;">0</div>
          <div style="font-size: 0.85rem; color: #64748B;">Universal filing rules assumed</div>
        </div>
      </div>
    </div>
  </section>

  <main class="guide-article">
    <div class="guide-content-container">

      <section>
        <h2>Four Series LLC Models</h2>
        <div class="styled-table-wrap">
          <table class="styled-table">
            <thead>
              <tr>
                <th>Legal model</th>
                <th>How it generally works</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Parent-document series</strong></td>
                <td>Parent LLC's formation documents and operating agreement establish authority to create series</td>
              </tr>
              <tr>
                <td><strong>Protected-series designation</strong></td>
                <td>Series created or activated through state-specific designation or similar filing under protected-series statute</td>
              </tr>
              <tr>
                <td><strong>Registered or designated series</strong></td>
                <td>Series uses separate public filing or certificate connected to parent LLC</td>
              </tr>
              <tr>
                <td><strong>Dual protected + registered system</strong></td>
                <td>Jurisdiction provides more than one series mechanism with different formation, filing and legal consequences</td>
              </tr>
            </tbody>
          </table>
        </div>
        <p>For broader entity comparisons, explore our guides on <a href="llc-vs-corporation.html">LLC vs corporation</a> and <a href="what-is-an-llc.html">what is an LLC</a>.</p>
      </section>

      <section>
        <h2>Which States Allow a Series LLC in 2026?</h2>
        <p><em>Editorial test — does the jurisdiction provide a domestic statutory framework for creating a Series LLC, protected series or comparable domestic series structure? Foreign-series recognition alone does not count.</em></p>

        <!-- Table 1 -->
        <h3>Alabama &ndash; Delaware</h3>
        <div class="styled-table-wrap">
          <table class="styled-table">
            <thead>
              <tr><th>Jurisdiction</th><th>Domestic 2026 regime?</th><th>Current framework</th><th>Official source link</th></tr>
            </thead>
            <tbody>
              <tr><td>Alabama</td><td>YES</td><td>Series permitted under the Alabama LLC Act</td><td><a href="https://alison.legislature.state.al.us/code-of-alabama?section=10A-5A-11.16">Link</a></td></tr>
              <tr><td>Alaska</td><td>NO</td><td>Current domestic LLC framework does not provide a comparable Series LLC regime</td><td><a href="https://www.commerce.alaska.gov/web/cbpl/Corporations">Link</a></td></tr>
              <tr><td>Arizona</td><td>NO</td><td>Foreign-series provisions do not establish a comparable domestic Series LLC regime</td><td><a href="https://www.azleg.gov/ars/29/03102.htm">Link</a></td></tr>
              <tr><td>Arkansas</td><td>YES</td><td>Series/protected-series framework</td><td><a href="https://www.sos.arkansas.gov/">Link</a></td></tr>
              <tr><td>California</td><td>NO</td><td>California does not provide a domestic Series LLC formation mechanism</td><td><a href="https://www.ftb.ca.gov/file/business/types/limited-liability-company/series-limited-liability-company.html">Link</a></td></tr>
              <tr><td>Colorado</td><td>NO</td><td>Current law does not provide a domestic protected-series formation regime</td><td><a href="https://leg.colorado.gov">Link</a></td></tr>
              <tr><td>Connecticut</td><td>NO</td><td>Current LLC law does not provide a comparable domestic protected-series regime</td><td><a href="https://www.cga.ct.gov">Link</a></td></tr>
              <tr><td>Delaware</td><td>YES</td><td>Protected and registered series</td><td><a href="https://delcode.delaware.gov/title6/c018/sc02/">Link</a></td></tr>
            </tbody>
          </table>
        </div>

        <!-- Table 2 -->
        <h3>Florida &ndash; Kansas</h3>
        <div class="styled-table-wrap">
          <table class="styled-table">
            <thead>
              <tr><th>Jurisdiction</th><th>Domestic 2026 regime?</th><th>Current framework</th><th>Official source link</th></tr>
            </thead>
            <tbody>
              <tr><td>Florida</td><td>YES</td><td>Protected-series provisions effective July 1, 2026</td><td><a href="https://dos.fl.gov/sunbiz/forms/limited-liability-company/florida-series-llc/">Link</a></td></tr>
              <tr><td>Georgia</td><td>NO</td><td>Current law does not provide the comparable domestic protected/registered-series framework</td><td><a href="https://www.legis.ga.gov/">Link</a></td></tr>
              <tr><td>Hawaii</td><td>NO</td><td>Recognition of certain foreign structures does not create a comparable domestic Series LLC regime</td><td><a href="https://data.capitol.hawaii.gov/">Link</a></td></tr>
              <tr><td>Idaho</td><td>NO</td><td>Current domestic LLC framework does not provide a comparable protected-series regime</td><td><a href="https://sos.idaho.gov/">Link</a></td></tr>
              <tr><td>Illinois</td><td>YES</td><td>Series LLC and designated-series framework</td><td><a href="https://www.ilsos.gov/departments/business-services/">Link</a></td></tr>
              <tr><td>Indiana</td><td>YES</td><td>Domestic Series LLC framework</td><td><a href="https://www.in.gov/sos/business/">Link</a></td></tr>
              <tr><td>Iowa</td><td>YES</td><td>Uniform Protected Series Act framework</td><td><a href="https://www.legis.iowa.gov/">Link</a></td></tr>
              <tr><td>Kansas</td><td>YES</td><td>Domestic series framework</td><td><a href="https://www.sos.ks.gov/">Link</a></td></tr>
            </tbody>
          </table>
        </div>

        <!-- Table 3 -->
        <h3>Kentucky &ndash; Mississippi</h3>
        <div class="styled-table-wrap">
          <table class="styled-table">
            <thead>
              <tr><th>Jurisdiction</th><th>Domestic 2026 regime?</th><th>Current framework</th><th>Official source link</th></tr>
            </thead>
            <tbody>
              <tr><td>Kentucky</td><td>NO</td><td>Recognition of certain protected-series concepts does not create a general domestic Series LLC formation regime</td><td><a href="https://apps.legislature.ky.gov/">Link</a></td></tr>
              <tr><td>Louisiana</td><td>NO</td><td>Current domestic LLC law does not provide the comparable Series LLC framework</td><td><a href="https://www.legis.la.gov/">Link</a></td></tr>
              <tr><td>Maine</td><td>NO</td><td>Foreign designated-series structures are recognized, but this is not domestic Series LLC authorization</td><td><a href="https://legislature.maine.gov/">Link</a></td></tr>
              <tr><td>Maryland</td><td>NO</td><td>Foreign series recognition only</td><td><a href="https://mgaleg.maryland.gov/">Link</a></td></tr>
              <tr><td>Massachusetts</td><td>NO</td><td>Current Chapter 156C does not provide a comparable protected-series formation regime</td><td><a href="https://malegislature.gov/">Link</a></td></tr>
              <tr><td>Michigan</td><td>NO</td><td>Current Michigan LLC Act does not provide a protected-series creation regime</td><td><a href="https://www.legislature.mi.gov/">Link</a></td></tr>
              <tr><td>Minnesota</td><td>NO</td><td>Classes or series of membership interests are not treated as a protected-series liability regime</td><td><a href="https://www.revisor.mn.gov/">Link</a></td></tr>
              <tr><td>Mississippi</td><td>NO</td><td>Current LLC law addresses classes/series of financial interests rather than the protected-series model</td><td><a href="https://sos.ms.gov/">Link</a></td></tr>
            </tbody>
          </table>
        </div>

        <!-- Table 4 -->
        <h3>Missouri &ndash; New York</h3>
        <div class="styled-table-wrap">
          <table class="styled-table">
            <thead>
              <tr><th>Jurisdiction</th><th>Domestic 2026 regime?</th><th>Current framework</th><th>Official source link</th></tr>
            </thead>
            <tbody>
              <tr><td>Missouri</td><td>YES</td><td>Designated-series framework</td><td><a href="https://revisor.mo.gov/main/OneSection.aspx?section=347.186">Link</a></td></tr>
              <tr><td>Montana</td><td>YES</td><td>Series LLC framework</td><td><a href="https://sosmt.gov/business/">Link</a></td></tr>
              <tr><td>Nebraska</td><td>YES</td><td>Uniform Protected Series Act</td><td><a href="https://nebraskalegislature.gov/">Link</a></td></tr>
              <tr><td>Nevada</td><td>YES</td><td>Series under Chapter 86</td><td><a href="https://www.leg.state.nv.us/">Link</a></td></tr>
              <tr><td>New Hampshire</td><td>NO</td><td>Current domestic LLC law does not provide the comparable protected-series framework</td><td><a href="https://gc.nh.gov/">Link</a></td></tr>
              <tr><td>New Jersey</td><td>NO</td><td>Current domestic LLC framework does not provide the comparable protected-series regime</td><td><a href="https://pub.njleg.state.nj.us/">Link</a></td></tr>
              <tr><td>New Mexico</td><td>NO</td><td>Current Limited Liability Company Act does not provide the comparable domestic protected-series regime</td><td><a href="https://www.sos.nm.gov/">Link</a></td></tr>
              <tr><td>New York</td><td>NO</td><td>Current LLC Law does not provide the comparable domestic Series LLC regime</td><td><a href="https://www.nysenate.gov/legislation/laws/LLC">Link</a></td></tr>
            </tbody>
          </table>
        </div>

        <!-- Table 5 -->
        <h3>North Carolina &ndash; South Carolina</h3>
        <div class="styled-table-wrap">
          <table class="styled-table">
            <thead>
              <tr><th>Jurisdiction</th><th>Domestic 2026 regime?</th><th>Current framework</th><th>Official source link</th></tr>
            </thead>
            <tbody>
              <tr><td>North Carolina</td><td>NO</td><td>Current Chapter 57D does not provide a comparable protected-series regime</td><td><a href="https://library.ncleg.gov/">Link</a></td></tr>
              <tr><td>North Dakota</td><td>YES</td><td>Series under the North Dakota LLC Act</td><td><a href="https://ndlegis.gov/">Link</a></td></tr>
              <tr><td>Ohio</td><td>YES</td><td>Statutory series under ORC &sect;1706.761</td><td><a href="https://codes.ohio.gov/">Link</a></td></tr>
              <tr><td>Oklahoma</td><td>YES</td><td>Protected and registered series</td><td><a href="https://www.oklegislature.gov/">Link</a></td></tr>
              <tr><td>Oregon</td><td>NO</td><td>Current Chapter 63 does not provide a comparable Series LLC/protected-series regime</td><td><a href="https://www.oregonlegislature.gov/">Link</a></td></tr>
              <tr><td>Pennsylvania</td><td>NO</td><td>Current Chapter 88 does not provide the comparable protected-series regime</td><td><a href="https://www.legis.state.pa.us/">Link</a></td></tr>
              <tr><td>Rhode Island</td><td>NO</td><td>Current law does not provide the comparable domestic protected-series regime</td><td><a href="https://webserver.rilegislature.gov/">Link</a></td></tr>
              <tr><td>South Carolina</td><td>NO</td><td>Current LLC Act does not provide a comparable protected-series regime</td><td><a href="https://www.scstatehouse.gov/">Link</a></td></tr>
            </tbody>
          </table>
        </div>

        <!-- Table 6 -->
        <h3>South Dakota &ndash; Puerto Rico</h3>
        <div class="styled-table-wrap">
          <table class="styled-table">
            <thead>
              <tr><th>Jurisdiction</th><th>Domestic 2026 regime?</th><th>Current framework</th><th>Official source link</th></tr>
            </thead>
            <tbody>
              <tr><td>South Dakota</td><td>YES</td><td>Parent LLC and series structure</td><td><a href="https://sdsos.gov/">Link</a></td></tr>
              <tr><td>Tennessee</td><td>YES</td><td>Protected-series framework</td><td><a href="https://www.capitol.tn.gov/">Link</a></td></tr>
              <tr><td>Texas</td><td>YES</td><td>Protected and registered series</td><td><a href="https://www.sos.state.tx.us/">Link</a></td></tr>
              <tr><td>Utah</td><td>YES</td><td>Statutory series</td><td><a href="https://le.utah.gov/">Link</a></td></tr>
              <tr><td>Vermont</td><td>NO</td><td>Foreign series recognition does not establish a comparable domestic mechanism</td><td><a href="https://legislature.vermont.gov/">Link</a></td></tr>
              <tr><td>Virginia</td><td>YES</td><td>Protected-series framework</td><td><a href="https://www.scc.virginia.gov/">Link</a></td></tr>
              <tr><td>Washington</td><td>NO</td><td>Current Chapter 25.15 does not provide a comparable Series LLC regime</td><td><a href="https://app.leg.wa.gov/">Link</a></td></tr>
              <tr><td>West Virginia</td><td>YES</td><td>Protected-series framework</td><td><a href="https://code.wvlegislature.gov/31B-14/">Link</a></td></tr>
              <tr><td>Wisconsin</td><td>NO</td><td>Classes/series provisions do not create the comparable protected-series liability structure</td><td><a href="https://docs.legis.wisconsin.gov/">Link</a></td></tr>
              <tr><td>Wyoming</td><td>YES</td><td>Series LLC</td><td><a href="https://sos.wyo.gov/">Link</a></td></tr>
              <tr><td>District of Columbia</td><td>YES</td><td>Series under D.C. Code &sect;29-802.06</td><td><a href="https://code.dccouncil.gov/">Link</a></td></tr>
              <tr><td>Puerto Rico</td><td>YES</td><td>Series LLC framework</td><td><a href="https://transicion2016.pr.gov/">Link</a></td></tr>
            </tbody>
          </table>
        </div>

        <div class="callout-blue">
          <strong>Note:</strong> Not every statute that mentions a 'series' creates a Series LLC with internal liability segregation. LLC Primer does not count every reference to 'series' as domestic Series LLC authorization.
        </div>
      </section>

      <section>
        <h2>How Series LLC Filing Mechanics Vary</h2>
        <p>Some states require public filing for each series: Florida's new provisions (effective July 1, 2026) allow existing active Florida LLC to file a Designation of Protected Series online for $25. Protected series does not file separate annual report; parent LLC continues to file its annual report.</p>
        <p>Other states rely more heavily on parent documents and records: Delaware provides protected-series framework where separate asset records, provisions in LLC agreement, and notice in certificate of formation are among the statutory conditions.</p>
        <p>Delaware, Texas and Oklahoma: distinguish between protected series and registered series. Delaware defines and regulates both. This distinction affects filing requirements, public records, recurring costs and legal characteristics.</p>
        <p>Recurring compliance can be parent-level or series-level: a new series may create a separate designation fee, additional annual/biennial filing obligations, separate tax/registration requirements, additional bookkeeping requirements.</p>
      </section>

      <section>
        <h2>Internal Liability Separation is Conditional</h2>
        <p>The protection is statutory and conditional. Not created simply by naming something 'Series 1' or 'Protected Series.'</p>
        <p>Separate records are an important statutory requirement in some jurisdictions (Delaware requires records to account for assets associated with a protected series separately).</p>
        <p>Requirements can include: separate or identifiable records, provisions in operating agreement, statements in parent formation document, public series designation, proper identification of assets, compliance with the state's series statute.</p>
        <p>Separate banking and bookkeeping are practical safeguards.</p>
        <div class="callout-yellow">
          <strong>Does forming a Series LLC guarantee that a creditor can never reach another series?</strong> NO. The liability separation depends on the governing state's statute and compliance with its conditions. Cross-state activity can create additional questions.
        </div>
      </section>

      <section>
        <h2>Series LLC Costs</h2>
        <p>Illinois can impose series-level costs. Nebraska and Virginia can also create series-specific obligations. Delaware distinguishes parent and registered-series obligations. Florida's 2026 system: parent LLC files annual report; protected series does not file separate annual report; designation fee is $25.</p>
      </section>

      <section>
        <h2>Federal and State Tax Treatment</h2>
        <p>The IRS issued proposed regulations (REG-119921-09) concerning federal tax classification of series LLCs. This is a notice of proposed rulemaking, not a final regulation.</p>
        <p>A private letter ruling is not universal precedent.</p>
        <p>Do not assume one federal return for every series. Questions involving EINs, employment taxes, partnership returns, corporate elections, disregarded-entity treatment, and information reporting should be evaluated for the actual structure.</p>
        <p>State tax treatment can be different from federal treatment. California, for example, does not provide domestic Series LLC formation but addresses qualifying foreign Series LLC structures. Texas uses its own franchise-tax framework.</p>
      </section>

      <section>
        <h2>Series LLC vs. Multiple Separate LLCs</h2>
        <div class="styled-table-wrap">
          <table class="styled-table">
            <thead>
              <tr>
                <th>Question</th>
                <th>Series LLC</th>
                <th>Separate LLCs</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>State availability</td>
                <td>Available only where domestic series framework exists</td>
                <td>Available under laws of all states</td>
              </tr>
              <tr>
                <td>Formation of additional businesses</td>
                <td>May allow additional series under one parent</td>
                <td>Each business uses its own LLC</td>
              </tr>
              <tr>
                <td>Recurring fees</td>
                <td>May be parent-level, series-level or both</td>
                <td>Each LLC has its own state obligations</td>
              </tr>
              <tr>
                <td>Liability separation</td>
                <td>Depends on statutory requirements</td>
                <td>Each LLC is a separate legal entity</td>
              </tr>
              <tr>
                <td>Multi-state complexity</td>
                <td>Can become complicated</td>
                <td>More conventional, easier to explain to third parties</td>
              </tr>
              <tr>
                <td>Tax administration</td>
                <td>Requires additional series-specific analysis</td>
                <td>Still requires classification analysis</td>
              </tr>
              <tr>
                <td>Banking and records</td>
                <td>Strong internal separation important</td>
                <td>Each LLC naturally has its own identity</td>
              </tr>
            </tbody>
          </table>
        </div>
        <p>Appropriate comparison depends on: formation state, number of planned series, state filing fees, annual/biennial obligations, tax treatment, accounting requirements, banking, insurance, ownership differences, lender requirements, whether foreign qualification required.</p>
      </section>

      <section>
        <h2>Safer Series LLC Formation Workflow</h2>
        <ol>
          <li>Confirm domestic availability</li>
          <li>Identify the state's specific series model (protected, registered, designated, parent-document, or dual)</li>
          <li>Form or review the parent LLC</li>
          <li>Complete every required series filing</li>
          <li>Build the operating agreement around the statute</li>
          <li>Maintain separate records</li>
          <li>Map recurring obligations before creating additional series</li>
          <li>Check federal and state tax treatment before operating in multiple states</li>
        </ol>
        <p>Check out our <a href="llc-guide.html">LLC Guide</a> for general formation planning.</p>
      </section>

      <section>
        <h2>When a Series LLC May Fit &mdash; and When Separate LLCs May Be Cleaner</h2>
        <p><strong>Series LLC may be worth evaluating when:</strong></p>
        <ul>
          <li>Formation state clearly authorizes the structure</li>
          <li>Managing multiple related assets or business activities</li>
          <li>Ownership structure compatible with parent-and-series arrangement</li>
          <li>Can maintain separate records consistently</li>
          <li>Legal and tax advisers comfortable with structure</li>
        </ul>
        <p><strong>Separate LLCs may be cleaner when:</strong></p>
        <ul>
          <li>Important assets/businesses operate in states without domestic Series LLC framework</li>
          <li>Lenders, investors or counterparties expect conventional standalone entities</li>
          <li>Ownership differs substantially between businesses</li>
          <li>Series-level filing/recurring costs eliminate expected savings</li>
          <li>Simpler administration more important</li>
        </ul>
      </section>

      <section id="faq-section" style="margin-top: 3rem;">
        <h2 style="font-size: 1.65rem; font-weight: 800; color: #12304A; margin-bottom: 1.25rem;">Frequently Asked Questions</h2>
        <div class="faq-accordion-wrapper">
          <details class="faq-accordion-item">
            <summary class="faq-accordion-question">
              <div class="faq-q-badge-title">
                <span class="faq-q-badge">01</span>
                <span>Can different series have different owners?</span>
              </div>
              <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
            </summary>
            <div class="faq-accordion-answer">
              Possibly, depending on governing state's statute and operating agreement. Ownership rights should be structured consistently with applicable law.
            </div>
          </details>
          <details class="faq-accordion-item">
            <summary class="faq-accordion-question">
              <div class="faq-q-badge-title">
                <span class="faq-q-badge">02</span>
                <span>Does each series need its own bank account?</span>
              </div>
              <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
            </summary>
            <div class="faq-accordion-answer">
              Not every state statute uses identical banking language. Separate accounts can be a practical way to maintain clear records. Governing statute and professional advice should control.
            </div>
          </details>
          <details class="faq-accordion-item">
            <summary class="faq-accordion-question">
              <div class="faq-q-badge-title">
                <span class="faq-q-badge">03</span>
                <span>Can one series sign a contract without binding the others?</span>
              </div>
              <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
            </summary>
            <div class="faq-accordion-answer">
              A protected series may have separate rights and liabilities under the governing statute, but result depends on applicable law, contract language and how the series is structured.
            </div>
          </details>
          <details class="faq-accordion-item">
            <summary class="faq-accordion-question">
              <div class="faq-q-badge-title">
                <span class="faq-q-badge">04</span>
                <span>Can a Series LLC own real estate in more than one state?</span>
              </div>
              <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
            </summary>
            <div class="faq-accordion-answer">
              Potentially, but owning or operating property in another state can trigger foreign-qualification, recording, tax and recognition issues.
            </div>
          </details>
          <details class="faq-accordion-item">
            <summary class="faq-accordion-question">
              <div class="faq-q-badge-title">
                <span class="faq-q-badge">05</span>
                <span>Does every series need a separate EIN?</span>
              </div>
              <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
            </summary>
            <div class="faq-accordion-answer">
              Not automatically. Federal tax identification depends on federal tax classification and circumstances. IRS proposed Series LLC regulations should not be treated as a final universal EIN rule.
            </div>
          </details>
          <details class="faq-accordion-item">
            <summary class="faq-accordion-question">
              <div class="faq-q-badge-title">
                <span class="faq-q-badge">06</span>
                <span>Can one series be closed without terminating the parent LLC?</span>
              </div>
              <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
            </summary>
            <div class="faq-accordion-answer">
              Many Series LLC statutes allow individual series to be terminated without terminating the parent, but exact procedure is state-specific.
            </div>
          </details>
          <details class="faq-accordion-item">
            <summary class="faq-accordion-question">
              <div class="faq-q-badge-title">
                <span class="faq-q-badge">07</span>
                <span>Can I convert an ordinary LLC into a Series LLC?</span>
              </div>
              <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
            </summary>
            <div class="faq-accordion-answer">
              Depends on formation state's law. Some states allow existing LLC to establish a protected series through a designation. Florida states that an existing active Florida LLC becomes a Florida Series LLC when it designates its first protected series.
            </div>
          </details>
        </div>
      </section>
"""

t1 = "Series LLC (2026): How It Works, States & Rules | LLC Primer"
m1 = "Complete guide to Series LLCs in 2026. Learn which 24 states allow series LLCs, how filing mechanics differ, liability separation rules, tax treatment, and when separate LLCs may be better."
with open(r'd:\rename\series-llc.html', 'w', encoding='utf-8') as f:
    f.write(set_title_meta(header_part1, t1, m1) + content1 + footer_part)
