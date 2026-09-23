/* ==========================================================================
   LLC LAUNCHPAD — INTERACTIVE JAVASCRIPT APPLICATION (2026 EDITION)
   ========================================================================== */

const stateData = [
  { name: "Alabama", code: "AL", fee: 208, annual: "$100 min PPT", speed: "2-3 Days", region: "south", popular: false, note: "Filing handled via Secretary of State portal.", sosName: "Alabama Secretary of State", sosUrl: "https://www.sos.alabama.gov/" },
  { name: "Alaska", code: "AK", fee: 250, annual: "$100 Biennial", speed: "1-2 Days", region: "west", popular: false, note: "Biennial report due every 2 years.", sosName: "Alaska Division of Corporations", sosUrl: "https://www.commerce.alaska.gov/web/cbpl/corporations.aspx" },
  { name: "Arizona", code: "AZ", fee: 50, annual: "$0", speed: "3-5 Days", region: "west", popular: true, note: "No annual report fee. Newspaper publication required in 3 counties.", sosName: "Arizona Corporation Commission", sosUrl: "https://ecorp.azcc.gov/" },
  { name: "Arkansas", code: "AR", fee: 45, annual: "$150", speed: "1-2 Days", region: "south", popular: false, note: "Low initial filing fee.", sosName: "Arkansas Secretary of State", sosUrl: "https://www.sos.arkansas.gov/" },
  { name: "California", code: "CA", fee: 70, annual: "$800 + $20", speed: "1 Day (Online)", region: "west", popular: true, note: "$800 minimum annual franchise tax after Year 1.", sosName: "California Secretary of State", sosUrl: "https://bizfileonline.sos.ca.gov/" },
  { name: "Colorado", code: "CO", fee: 50, annual: "$10", speed: "Instant Online", region: "west", popular: true, note: "Instant online registration.", sosName: "Colorado Secretary of State", sosUrl: "https://www.sos.state.co.us/" },
  { name: "Connecticut", code: "CT", fee: 120, annual: "$80", speed: "2-3 Days", region: "east", popular: false, note: "Annual report due every year.", sosName: "Connecticut Secretary of the State", sosUrl: "https://business.ct.gov/" },
  { name: "Delaware", code: "DE", fee: 140, annual: "$300", speed: "1-2 Days", region: "east", popular: true, note: "Preferred state for venture-backed entities and corporate privacy.", sosName: "Delaware Division of Corporations", sosUrl: "https://corp.delaware.gov/" },
  { name: "Florida", code: "FL", fee: 125, annual: "$138.75", speed: "1-2 Days", region: "south", popular: true, note: "Sunbiz portal. Annual report due May 1st.", sosName: "Florida Division of Corporations (Sunbiz)", sosUrl: "https://dos.fl.gov/sunbiz/" },
  { name: "Georgia", code: "GA", fee: 100, annual: "$50", speed: "2-3 Days", region: "south", popular: true, note: "Low ongoing annual fee.", sosName: "Georgia Secretary of State", sosUrl: "https://ecorp.sos.ga.gov/" },
  { name: "Hawaii", code: "HI", fee: 50, annual: "$15", speed: "3-5 Days", region: "west", popular: false, note: "Simple online system.", sosName: "Hawaii DCCA Business Registration", sosUrl: "https://hbe.ehawaii.gov/" },
  { name: "Idaho", code: "ID", fee: 100, annual: "$0", speed: "1-2 Days", region: "west", popular: false, note: "No annual report fee required.", sosName: "Idaho Secretary of State", sosUrl: "https://sos.idaho.gov/" },
  { name: "Illinois", code: "IL", fee: 150, annual: "$75", speed: "Instant Online", region: "midwest", popular: false, note: "Fast online processing.", sosName: "Illinois Secretary of State", sosUrl: "https://www.ilsos.gov/" },
  { name: "Indiana", code: "IN", fee: 98, annual: "$50 Biennial", speed: "1 Day", region: "midwest", popular: false, note: "Biennial business entity report.", sosName: "Indiana Secretary of State INBiz", sosUrl: "https://bsd.sos.in.gov/" },
  { name: "Iowa", code: "IA", fee: 50, annual: "$60 Biennial", speed: "1-2 Days", region: "midwest", popular: false, note: "Biennial report in odd years.", sosName: "Iowa Secretary of State", sosUrl: "https://sos.iowa.gov/" },
  { name: "Kansas", code: "KS", fee: 160, annual: "$55", speed: "1 Day", region: "midwest", popular: false, note: "Annual report due April 15th.", sosName: "Kansas Secretary of State", sosUrl: "https://sos.ks.gov/" },
  { name: "Kentucky", code: "KY", fee: 40, annual: "$15", speed: "1 Day", region: "south", popular: true, note: "One of the lowest state fees in America.", sosName: "Kentucky Secretary of State", sosUrl: "https://web.sos.ky.gov/" },
  { name: "Louisiana", code: "LA", fee: 100, annual: "$35", speed: "1-2 Days", region: "south", popular: false, note: "Affordable annual compliance.", sosName: "Louisiana Secretary of State geauxBiz", sosUrl: "https://geauxbiz.sos.la.gov/" },
  { name: "Maine", code: "ME", fee: 175, annual: "$85", speed: "3-5 Days", region: "east", popular: false, note: "Annual report due June 1st.", sosName: "Maine Secretary of State", sosUrl: "https://www.maine.gov/sos/cec/corp/" },
  { name: "Maryland", code: "MD", fee: 100, annual: "$300", speed: "Instant Online", region: "east", popular: false, note: "Annual personal property return required.", sosName: "Maryland Business Express", sosUrl: "https://egov.maryland.gov/businessexpress" },
  { name: "Massachusetts", code: "MA", fee: 500, annual: "$500", speed: "1-2 Days", region: "east", popular: false, note: "Highest initial filing fee.", sosName: "Massachusetts Corporations Division", sosUrl: "https://www.sec.state.ma.us/cor/" },
  { name: "Michigan", code: "MI", fee: 50, annual: "$25", speed: "1-2 Days", region: "midwest", popular: true, note: "Affordable startup and annual fees.", sosName: "Michigan LARA Corporations Online", sosUrl: "https://cfs.lara.state.mi.us/" },
  { name: "Minnesota", code: "MN", fee: 155, annual: "$0", speed: "1 Day", region: "midwest", popular: false, note: "No annual fee if filed on time.", sosName: "Minnesota Secretary of State", sosUrl: "https://mblsportal.sos.state.mn.us/" },
  { name: "Mississippi", code: "MS", fee: 50, annual: "$0", speed: "1 Day", region: "south", popular: false, note: "Free annual report filing.", sosName: "Mississippi Secretary of State", sosUrl: "https://www.sos.ms.gov/" },
  { name: "Missouri", code: "MO", fee: 50, annual: "$0", speed: "Instant Online", region: "midwest", popular: false, note: "No annual report required!", sosName: "Missouri Secretary of State", sosUrl: "https://bsd.sos.mo.gov/" },
  { name: "Montana", code: "MT", fee: 35, annual: "$20", speed: "1 Day", region: "west", popular: false, note: "Lowest initial state fee in America.", sosName: "Montana Secretary of State", sosUrl: "https://biz.sosmt.gov/" },
  { name: "Nebraska", code: "NE", fee: 100, annual: "$10 Biennial", speed: "2-3 Days", region: "midwest", popular: false, note: "Newspaper publication required.", sosName: "Nebraska Secretary of State", sosUrl: "https://www.nebraska.gov/sos/corp/" },
  { name: "Nevada", code: "NV", fee: 425, annual: "$350", speed: "1-2 Days", region: "west", popular: true, note: "Fee includes Articles ($75), Initial List ($150) & State License ($200).", sosName: "Nevada Secretary of State SilverFlume", sosUrl: "https://www.nvsos.gov/" },
  { name: "New Hampshire", code: "NH", fee: 100, annual: "$100", speed: "2-3 Days", region: "east", popular: false, note: "Annual report due April 1st.", sosName: "New Hampshire Department of State", sosUrl: "https://quickstart.sos.nh.gov/" },
  { name: "New Jersey", code: "NJ", fee: 125, annual: "$75", speed: "1 Day", region: "east", popular: true, note: "Annual report due on anniversary month.", sosName: "New Jersey Division of Revenue", sosUrl: "https://www.njportal.com/DOR/BusinessRegistration" },
  { name: "New Mexico", code: "NM", fee: 50, annual: "$0", speed: "1-2 Days", region: "west", popular: true, note: "Top privacy state with no public owner names or annual reports.", sosName: "New Mexico Secretary of State", sosUrl: "https://portal.sos.state.nm.us/" },
  { name: "New York", code: "NY", fee: 200, annual: "$9 Biennial", speed: "1-2 Days", region: "east", popular: true, note: "Section 206 newspaper publication requirement (~$300-$1000).", sosName: "New York Department of State", sosUrl: "https://dos.ny.gov/corps" },
  { name: "North Carolina", code: "NC", fee: 125, annual: "$200", speed: "3-5 Days", region: "south", popular: true, note: "Annual report due April 15th.", sosName: "North Carolina Secretary of State", sosUrl: "https://www.sosnc.gov/" },
  { name: "North Dakota", code: "ND", fee: 135, annual: "$50", speed: "2-3 Days", region: "midwest", popular: false, note: "Annual report due Nov 15th.", sosName: "North Dakota Secretary of State FirstStop", sosUrl: "https://firststop.sos.nd.gov/" },
  { name: "Ohio", code: "OH", fee: 99, annual: "$0", speed: "1-2 Days", region: "midwest", popular: true, note: "No annual report required!", sosName: "Ohio Secretary of State", sosUrl: "https://www.ohiosos.gov/" },
  { name: "Oklahoma", code: "OK", fee: 100, annual: "$25", speed: "1-2 Days", region: "south", popular: false, note: "Low annual compliance cost.", sosName: "Oklahoma Secretary of State", sosUrl: "https://www.sos.ok.gov/" },
  { name: "Oregon", code: "OR", fee: 100, annual: "$100", speed: "1 Day", region: "west", popular: false, note: "Annual report due on anniversary date.", sosName: "Oregon Secretary of State", sosUrl: "https://sos.oregon.gov/" },
  { name: "Pennsylvania", code: "PA", fee: 125, annual: "$70 Decennial", speed: "2-3 Days", region: "east", popular: false, note: "Decennial report due every 10 years.", sosName: "Pennsylvania Department of State", sosUrl: "https://www.dos.pa.gov/" },
  { name: "Rhode Island", code: "RI", fee: 150, annual: "$50", speed: "1-2 Days", region: "east", popular: false, note: "Annual report due between Feb 1 & Nov 1.", sosName: "Rhode Island Department of State", sosUrl: "https://ezcorp.sos.ri.gov/" },
  { name: "South Carolina", code: "SC", fee: 110, annual: "$0", speed: "1-2 Days", region: "south", popular: false, note: "No annual report fee.", sosName: "South Carolina Secretary of State", sosUrl: "https://sos.sc.gov/" },
  { name: "South Dakota", code: "SD", fee: 150, annual: "$50", speed: "Instant Online", region: "midwest", popular: false, note: "Online instant approval.", sosName: "South Dakota Secretary of State", sosUrl: "https://sdsos.gov/" },
  { name: "Tennessee", code: "TN", fee: 300, annual: "$300 min", speed: "1-2 Days", region: "south", popular: false, note: "$300 minimum initial filing fee.", sosName: "Tennessee Secretary of State Tre Hargett", sosUrl: "https://tnbear.tn.gov/" },
  { name: "Texas", code: "TX", fee: 300, annual: "$0 PIR", speed: "2-3 Days", region: "south", popular: true, note: "Public Information Report required.", sosName: "Texas Secretary of State", sosUrl: "https://www.sos.state.tx.us/corp/" },
  { name: "Utah", code: "UT", fee: 54, annual: "$18", speed: "1 Day", region: "west", popular: false, note: "Affordable overall state.", sosName: "Utah Division of Corporations", sosUrl: "https://corporations.utah.gov/" },
  { name: "Vermont", code: "VT", fee: 125, annual: "$35", speed: "2-3 Days", region: "east", popular: false, note: "Annual report due within 2.5 months of fiscal year end.", sosName: "Vermont Secretary of State", sosUrl: "https://sos.vermont.gov/" },
  { name: "Virginia", code: "VA", fee: 100, annual: "$50", speed: "Instant Online", region: "south", popular: true, note: "Fast instant online processing.", sosName: "Virginia State Corporation Commission", sosUrl: "https://cis.scc.virginia.gov/" },
  { name: "Washington", code: "WA", fee: 200, annual: "$60", speed: "1 Day", region: "west", popular: true, note: "Initial report due within 120 days ($10).", sosName: "Washington Secretary of State", sosUrl: "https://www.sos.wa.gov/corps" },
  { name: "West Virginia", code: "WV", fee: 100, annual: "$25", speed: "2-3 Days", region: "south", popular: false, note: "Fee waived for military veterans.", sosName: "West Virginia Secretary of State", sosUrl: "https://wvsos.gov/" },
  { name: "Wisconsin", code: "WI", fee: 130, annual: "$25", speed: "1 Day", region: "midwest", popular: false, note: "Low annual renewal fee.", sosName: "Wisconsin DFI", sosUrl: "https://www.wdfi.org/" },
  { name: "Wyoming", code: "WY", fee: 100, annual: "$60", speed: "Instant Online", region: "west", popular: true, note: "Top state for non-residents, asset protection, and zero state income tax.", sosName: "Wyoming Secretary of State", sosUrl: "https://wyobiz.wyo.gov/" }
];

document.addEventListener("DOMContentLoaded", () => {
  populateStateSelectors();
  initFaqAccordion();
  initMobileMenu();
  initCostCalculator();
  initQuizWizard();
  initSearch();
});

function populateStateSelectors() {
  const stateSectionSelect = document.getElementById("mainStateSectionSelect");
  const ctaStateSelect = document.getElementById("ctaStateSelect");
  const bottomCtaStateSelect = document.getElementById("bottomCtaStateSelect");
  const calcStateSelect = document.getElementById("calcStateSelect");

  const defaultOptionText = "-- Select Your State --";

  [stateSectionSelect, ctaStateSelect, bottomCtaStateSelect, calcStateSelect].forEach(select => {
    if (!select) return;
    select.innerHTML = `<option value="">${defaultOptionText}</option>`;
    stateData.forEach(st => {
      const opt = document.createElement("option");
      opt.value = st.code;
      opt.textContent = st.name;
      select.appendChild(opt);
    });
  });

  if (ctaStateSelect) {
    ctaStateSelect.addEventListener("change", (e) => onStateSelectedInCta(e.target.value));
  }
  if (bottomCtaStateSelect) {
    bottomCtaStateSelect.addEventListener("change", (e) => onStateSelectedInCta(e.target.value));
  }
}

function selectStateInSection(code) {
  selectStateAndOpenModal(code);
}

function submitStateSelection() {
  const select = document.getElementById("mainStateSectionSelect");
  const code = select ? select.value : "";
  if (!code) {
    alert("Please select a state from the dropdown menu first.");
    return;
  }
  showInlineStateResult(code);
}

function selectStateAndOpenModal(code) {
  const select = document.getElementById("mainStateSectionSelect");
  if (select) select.value = code;
  showInlineStateResult(code);
  const section = document.getElementById("states-section");
  if (section) {
    section.scrollIntoView({ behavior: "smooth" });
  }
}

function openStateModal(code) {
  showInlineStateResult(code);
}

function closeStateModal() {
  const modal = document.getElementById("stateModalOverlay");
  if (modal) {
    modal.classList.remove("active");
  }
}

function showInlineStateResult(code) {
  const st = stateData.find(s => s.code === code);
  if (!st) return;

  const popularCard = document.getElementById("popularStatesCard");
  if (popularCard) {
    popularCard.style.display = "none";
  }

  const resultBox = document.getElementById("inlineStateResult");
  if (!resultBox) return;

  const sosLinkName = st.sosName || (st.name + " Secretary of State");
  const sosLinkUrl = st.sosUrl || "https://www.sos.state.wy.us";

  resultBox.innerHTML = `
    <div style="background: rgba(13, 35, 54, 0.95); border: 1.5px solid var(--color-primary); border-radius: 18px; padding: 1.5rem; position: relative; box-shadow: 0 10px 30px rgba(21, 154, 156, 0.2); animation: inlineResultFade 0.4s ease-out;">
      
      <!-- Result Header with Back Button -->
      <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.75rem; border-bottom: 1px solid rgba(255, 255, 255, 0.1); padding-bottom: 0.85rem; margin-bottom: 1.15rem;">
        <div style="display: flex; align-items: center; gap: 0.65rem;">
          <span style="background: var(--color-primary-gradient); color: #FFFFFF; font-weight: 800; font-size: 1rem; padding: 0.3rem 0.75rem; border-radius: 8px;">${st.code}</span>
          <div>
            <h3 style="margin: 0; color: #FFFFFF; font-size: 1.25rem; font-weight: 700;">${st.name} LLC Details</h3>
            <span style="font-size: 0.75rem; color: #94A3B8;">2026 SOS Filing Overview</span>
          </div>
        </div>
        <button onclick="restorePopularStates()" style="font-size: 0.75rem; color: #159A9C; background: rgba(21, 154, 156, 0.12); border: 1px solid rgba(21, 154, 156, 0.35); border-radius: 6px; padding: 0.35rem 0.75rem; font-weight: 700; cursor: pointer;">
          ← Popular States
        </button>
      </div>

      <!-- Result Cards Grid -->
      <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.85rem; margin-bottom: 1.15rem;">
        
        <!-- State Fee -->
        <div style="background: #0D2336; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 12px; padding: 1rem;">
          <div style="font-size: 0.725rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--color-primary); font-weight: 700; margin-bottom: 0.3rem;">🏛️ Initial State Fee</div>
          <div style="font-size: 1.75rem; font-weight: 800; color: #FFFFFF; line-height: 1;">$${st.fee}</div>
          <div style="font-size: 0.725rem; color: #94A3B8; margin-top: 0.35rem;">Mandatory state fee</div>
        </div>

        <!-- Annual Fee -->
        <div style="background: #0D2336; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 12px; padding: 1rem;">
          <div style="font-size: 0.725rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--color-primary); font-weight: 700; margin-bottom: 0.3rem;">📅 Annual Report</div>
          <div style="font-size: 1.35rem; font-weight: 800; color: #F8FAFC; line-height: 1.1;">${st.annual}</div>
          <div style="font-size: 0.725rem; color: #94A3B8; margin-top: 0.35rem;">Ongoing requirement</div>
        </div>

        <!-- Approval Speed -->
        <div style="background: #0D2336; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 12px; padding: 1rem; grid-column: span 2;">
          <div style="font-size: 0.725rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--color-primary); font-weight: 700; margin-bottom: 0.3rem;">⚡ Approval Speed</div>
          <div style="font-size: 1.15rem; font-weight: 700; color: #159A9C; line-height: 1.1;">${st.speed}</div>
          <div style="font-size: 0.725rem; color: #94A3B8; margin-top: 0.35rem;">Estimated SOS turnaround</div>
        </div>
      </div>

      <!-- State Note / Rule -->
      <div style="background: rgba(21, 154, 156, 0.1); border-left: 3px solid var(--color-primary); padding: 0.85rem 1rem; border-radius: 0 8px 8px 0; margin-bottom: 0.85rem;">
        <div style="font-size: 0.825rem; color: #CBD5E1; line-height: 1.5;">
          <strong style="color: var(--color-primary);">State Note:</strong> ${st.note}
        </div>
      </div>

      <!-- Small Official Source Box -->
      <div style="background: rgba(255, 255, 255, 0.04); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 8px; padding: 0.65rem 0.85rem; font-size: 0.8rem; color: #CBD5E1; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.5rem;">
        <div>State Filing Fee: <strong style="color: #FFFFFF; font-size: 0.9rem;">$${st.fee}</strong></div>
        <div>Source: <a href="${sosLinkUrl}" target="_blank" rel="noopener" style="color: #159A9C; font-weight: 700; text-decoration: underline;">${sosLinkName}</a></div>
      </div>

    </div>
  `;

  resultBox.style.display = "block";
}

function restorePopularStates() {
  const popularCard = document.getElementById("popularStatesCard");
  const resultBox = document.getElementById("inlineStateResult");
  if (popularCard) popularCard.style.display = "block";
  if (resultBox) resultBox.style.display = "none";
}

function onStateSelectedInCta(code) {
  const output = document.getElementById("ctaStateOutput");
  if (!code) {
    if (output) output.style.display = "none";
    return;
  }

  const st = stateData.find(s => s.code === code);
  if (!st) return;

  output.innerHTML = `
    <div style="font-size: 1.1rem; font-weight: 700; color: #FFFFFF; margin-bottom: 0.5rem;">
      Ready to form your ${st.name} LLC?
    </div>
    <div style="font-size: 0.9rem; color: var(--text-secondary); margin-bottom: 1rem;">
      State Filing Fee: <b style="color:#FFFFFF">$${st.fee}</b> · Speed: <b style="color:var(--color-primary)">${st.speed}</b> · Annual Report: <b style="color:#FFFFFF">${st.annual}</b>
    </div>
    <button class="ls-btn ls-btn--emerald" onclick="alert('Navigating to ${st.name} step-by-step formation checklist...')">
      Start ${st.name} LLC Filing Now →
    </button>
  `;

  if (output) output.style.display = "block";
}

function initFaqAccordion() {
  const faqItems = document.querySelectorAll(".faq-accordion-item");
  faqItems.forEach(item => {
    item.addEventListener("toggle", () => {
      if (item.open) {
        faqItems.forEach(other => {
          if (other !== item && other.open) {
            other.open = false;
          }
        });
      }
    });
  });
}

function initMobileMenu() {
  const toggle = document.getElementById("mobileNavToggle");
  const menu = document.getElementById("primaryNavMenu");

  if (!toggle || !menu) return;

  toggle.addEventListener("click", () => {
    const isOpen = menu.style.display === "flex";
    menu.style.display = isOpen ? "none" : "flex";
    menu.style.flexDirection = "column";
    menu.style.position = "absolute";
    menu.style.top = "100%";
    menu.style.left = "0";
    menu.style.right = "0";
    menu.style.background = "#090D14";
    menu.style.padding = "1.5rem";
    menu.style.borderBottom = "1px solid var(--border-color)";
  });
}

function updateCost() {
  const calcStateSelect = document.getElementById("calcStateSelect");
  const calcAgentSelect = document.getElementById("calcAgentSelect");
  const calcExpeditedToggle = document.getElementById("calcExpeditedToggle");

  const tbody = document.getElementById("calcBreakdownTableBody");
  const totalSetupEl = document.getElementById("calcTotalSetup");
  const annualCompEl = document.getElementById("calcAnnualCompliance");

  const code = calcStateSelect ? calcStateSelect.value : "";
  const st = stateData.find(s => s.code === code);

  const stateName = st ? st.name : "";
  const stateFee = st ? st.fee : 0;

  // Annual Report Fee Extraction
  let annualFeeNum = 0;
  let annualTextDisplay = "$0.00";
  if (st) {
    if (!st.annual || st.annual === "$0" || st.annual === "$0 PIR" || st.annual.includes("$0")) {
      annualFeeNum = 0;
      annualTextDisplay = "$0.00";
    } else {
      const match = st.annual.match(/[\d\.]+/);
      if (match) {
        annualFeeNum = parseFloat(match[0]) || 0;
        annualTextDisplay = `$${annualFeeNum.toFixed(2)}`;
      } else {
        annualTextDisplay = st.annual;
      }
    }
  }

  // Agent Fee
  const agentFee = calcAgentSelect ? parseInt(calcAgentSelect.value) || 0 : 0;
  const agentLabel = agentFee > 0 ? "Commercial Registered Agent" : "Self Registered Agent";
  const agentCostDisplay = `$${agentFee.toFixed(2)}`;

  // Toggles
  const includeExpedited = calcExpeditedToggle ? calcExpeditedToggle.checked : false;

  // Compute Totals
  const totalSetup = stateFee + (includeExpedited ? 75 : 0);
  const totalAnnual = annualFeeNum + agentFee;

  // Generate Table Rows
  let rowsHtml = "";

  if (!st) {
    rowsHtml = `
      <tr style="border-bottom: 1px solid rgba(255, 255, 255, 0.08); font-size: 0.85rem;">
        <td colspan="4" style="padding: 1.25rem 0.5rem; text-align: center; color: #94A3B8;">
          👇 Select a state to calculate estimated government filing fees and compliance costs.
        </td>
      </tr>
    `;
  } else {
    rowsHtml = `
      <tr style="border-bottom: 1px solid rgba(255, 255, 255, 0.08); font-size: 0.85rem;">
        <td style="padding: 0.75rem 0.5rem; color: #FFFFFF; font-weight: 500;">${stateName} State Filing Fee</td>
        <td style="padding: 0.75rem 0.5rem; color: #CBD5E1;">Mandatory Government</td>
        <td style="padding: 0.75rem 0.5rem; color: #CBD5E1;">One-time (Setup)</td>
        <td style="padding: 0.75rem 0.5rem; color: #FFFFFF; font-weight: 700; text-align: right;">$${stateFee.toFixed(2)}</td>
      </tr>
      <tr style="border-bottom: 1px solid rgba(255, 255, 255, 0.08); font-size: 0.85rem;">
        <td style="padding: 0.75rem 0.5rem; color: #FFFFFF; font-weight: 500;">${agentLabel}</td>
        <td style="padding: 0.75rem 0.5rem; color: #CBD5E1;">Third-Party / Compliance</td>
        <td style="padding: 0.75rem 0.5rem; color: #CBD5E1;">Annual Recurring</td>
        <td style="padding: 0.75rem 0.5rem; color: #FFFFFF; font-weight: 700; text-align: right;">${agentCostDisplay}</td>
      </tr>
      <tr style="border-bottom: 1px solid rgba(255, 255, 255, 0.08); font-size: 0.85rem;">
        <td style="padding: 0.75rem 0.5rem; color: #FFFFFF; font-weight: 500;">${stateName} Annual Report / Franchise Tax</td>
        <td style="padding: 0.75rem 0.5rem; color: #CBD5E1;">Mandatory Government</td>
        <td style="padding: 0.75rem 0.5rem; color: #CBD5E1;">Annual Recurring</td>
        <td style="padding: 0.75rem 0.5rem; color: #FFFFFF; font-weight: 700; text-align: right;">${annualTextDisplay}</td>
      </tr>
    `;

    if (includeExpedited) {
      rowsHtml += `
        <tr style="border-bottom: 1px solid rgba(255, 255, 255, 0.08); font-size: 0.85rem;">
          <td style="padding: 0.75rem 0.5rem; color: #FFFFFF; font-weight: 500;">Expedited Processing Surcharge</td>
          <td style="padding: 0.75rem 0.5rem; color: #CBD5E1;">Government Expedite</td>
          <td style="padding: 0.75rem 0.5rem; color: #CBD5E1;">One-time (Setup)</td>
          <td style="padding: 0.75rem 0.5rem; color: #FFFFFF; font-weight: 700; text-align: right;">$75.00</td>
        </tr>
      `;
    }
  }

  if (tbody) tbody.innerHTML = rowsHtml;
  
  if (totalSetupEl) {
    if (st) {
      totalSetupEl.textContent = `$${totalSetup.toFixed(2)}`;
      totalSetupEl.style.fontSize = "1.65rem";
      totalSetupEl.style.color = "#FFFFFF";
      totalSetupEl.style.fontWeight = "800";
    } else {
      totalSetupEl.textContent = "Select a state to calculate";
      totalSetupEl.style.fontSize = "0.825rem";
      totalSetupEl.style.color = "#94A3B8";
      totalSetupEl.style.fontWeight = "600";
    }
  }

  if (annualCompEl) {
    if (st) {
      annualCompEl.textContent = `$${totalAnnual.toFixed(2)}`;
      annualCompEl.style.fontSize = "1.65rem";
      annualCompEl.style.color = "#159A9C";
      annualCompEl.style.fontWeight = "800";
    } else {
      annualCompEl.textContent = "Select a state to calculate";
      annualCompEl.style.fontSize = "0.825rem";
      annualCompEl.style.color = "#94A3B8";
      annualCompEl.style.fontWeight = "600";
    }
  }
}

function initCostCalculator() {
  const calcStateSelect = document.getElementById("calcStateSelect");
  const calcAgentSelect = document.getElementById("calcAgentSelect");
  const calcExpeditedToggle = document.getElementById("calcExpeditedToggle");

  [calcStateSelect, calcAgentSelect, calcExpeditedToggle].forEach(el => {
    if (el) {
      el.addEventListener("change", updateCost);
      el.addEventListener("input", updateCost);
    }
  });

  updateCost();
}

// --------------------------------------------------------------------------
// QUIZ WIZARD ENGINE (Q1 to Q5 Flow)
// --------------------------------------------------------------------------
let quizState = {
  currentQuestion: 1,
  need: "start_llc",
  base: "us",
  physicallyOperate: "yes",
  handling: "guided"
};

function initQuizWizard() {
  updateQuizUI();
}

function selectQuizOption(key, val, el) {
  quizState[key] = val;
  const parent = el.parentElement;
  if (parent) {
    parent.querySelectorAll(".quiz-option-card").forEach(c => c.classList.remove("selected"));
    el.classList.add("selected");
  }
}

function nextQuizQuestion() {
  if (quizState.currentQuestion < 4) {
    quizState.currentQuestion++;
    updateQuizUI();
  } else {
    quizState.currentQuestion = 5;
    updateQuizUI();
  }
}

function prevQuizQuestion() {
  if (quizState.currentQuestion > 1) {
    quizState.currentQuestion--;
    updateQuizUI();
  }
}

function updateQuizUI() {
  const q1 = document.getElementById("quizQStep1");
  const q2 = document.getElementById("quizQStep2");
  const q3 = document.getElementById("quizQStep3");
  const q4 = document.getElementById("quizQStep4");
  const q5 = document.getElementById("quizQStep9");
  const fill = document.getElementById("quizProgressFill");

  if (q1) q1.style.display = quizState.currentQuestion === 1 ? "block" : "none";
  if (q2) q2.style.display = quizState.currentQuestion === 2 ? "block" : "none";
  if (q3) q3.style.display = quizState.currentQuestion === 3 ? "block" : "none";
  if (q4) q4.style.display = quizState.currentQuestion === 4 ? "block" : "none";
  if (q5) q5.style.display = quizState.currentQuestion === 5 ? "block" : "none";

  if (fill) {
    const pct = quizState.currentQuestion === 1 ? 25 : quizState.currentQuestion === 2 ? 50 : quizState.currentQuestion === 3 ? 75 : quizState.currentQuestion === 4 ? 90 : 100;
    fill.style.width = `${pct}%`;
  }

  if (quizState.currentQuestion === 5) {
    generateQuizResults();
  }
}

function generateQuizResults() {
  const container = document.getElementById("quizResultsContainer");
  if (!container) return;

  let title = "Your Custom LLC Action Plan";
  let recText = "";
  let serviceName = "Northwest Registered Agent ($39 + State Fee)";
  let link = "https://www.northwestregisteredagent.com";

  if (quizState.base === "non_us" || quizState.need === "non_us") {
    title = "Non-US Resident Remote Formation Route";
    recText = "For international founders without a US Social Security Number, we recommend forming a Wyoming LLC. Wyoming has low annual fees ($60), zero state income tax, and allows remote EIN acquisition via IRS Form SS-4 fax.";
    serviceName = "doola Non-US Founder Formation Package";
  } else {
    recText = "Forming in your home state is usually your best option. Registering in Wyoming or Delaware when operating in another state requires foreign qualification, resulting in double state fees.";
  }

  container.innerHTML = `
    <div style="background: rgba(16, 185, 129, 0.12); border: 1px solid var(--color-primary); border-radius: var(--radius-lg); padding: 2rem; text-align: left;">
      <h3 style="color: #FFFFFF; margin-bottom: 0.5rem;">🚀 ${title}</h3>
      <p style="color: var(--text-secondary); margin-bottom: 1.25rem;">${recText}</p>
      
      <div style="font-size: 0.9rem; color: var(--color-primary); font-weight: 700; margin-bottom: 1.25rem;">
        Recommended Service Provider: <b>${serviceName}</b>
      </div>

      <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
        <a href="${link}" target="_blank" rel="noopener" class="ls-btn ls-btn--emerald">
          Launch Recommended Path →
        </a>
      </div>
    </div>
  `;
}

function initSearch() {
  const searchInput = document.getElementById("searchInput");
  if (!searchInput) return;

  searchInput.addEventListener("input", (e) => {
    const q = e.target.value.toLowerCase().trim();
    const resultsContainer = document.getElementById("searchResults");
    if (!resultsContainer) return;

    if (!q) {
      resultsContainer.innerHTML = "";
      return;
    }

    const matches = stateData.filter(s => s.name.toLowerCase().includes(q) || s.code.toLowerCase().includes(q));
    if (matches.length === 0) {
      resultsContainer.innerHTML = `<div style="color:var(--text-muted); padding:0.5rem;">No matching state guides found.</div>`;
      return;
    }

    resultsContainer.innerHTML = matches.map(s => `
      <div style="padding:0.6rem; border-bottom:1px solid rgba(255,255,255,0.05); cursor:pointer;" onclick="closeSearchModal(); selectStateInSection('${s.code}'); location.href='#states-section';">
        <strong style="color:#FFFFFF">${s.name} LLC</strong> — <span style="color:var(--color-primary)">$${s.fee} State Fee</span> (${s.speed})
      </div>
    `).join("");
  });
}

function openSearchModal() {
  document.getElementById("searchModalOverlay")?.classList.add("active");
  document.getElementById("searchInput")?.focus();
}
function closeSearchModal() {
  document.getElementById("searchModalOverlay")?.classList.remove("active");
}

function openCostCalculatorModal() {
  const modal = document.getElementById("costCalcModalOverlay");
  if (modal) {
    modal.classList.add("active");
    updateCost();
  }
}
function closeCostCalculatorModal() {
  const modal = document.getElementById("costCalcModalOverlay");
  if (modal) {
    modal.classList.remove("active");
  }
}

function openQuizModal() {
  document.getElementById("quizModalOverlay")?.classList.add("active");
}
function closeQuizModal() {
  document.getElementById("quizModalOverlay")?.classList.remove("active");
}
