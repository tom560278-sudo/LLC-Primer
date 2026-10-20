/* ==========================================================================
   LLC LAUNCHPAD — INTERACTIVE JAVASCRIPT APPLICATION (2026 EDITION)
   ========================================================================== */

const stateData = [
  {"name":"Alabama","code":"AL","slug":"alabama","fee":200,"paperFee":200,"initialExtras":28,"initialExtrasNote":"Mandatory name reservation ($28 online)","annual":"$0","annualFeeNum":0,"freq":"None (BPT separate)","due":"BPT due within 2.5 months of year start","penalty":"Penalties + interest under AL Dept of Revenue","tax":"$100 min Business Privilege Tax (BPT)","taxNum":100,"firstYearDue":"Formation fee + $28 reservation fee. Initial BPT return within 2.5 months.","speed":"Instant Online","region":"south","popular":false,"sosName":"Alabama Secretary of State","sosUrl":"https://www.sos.alabama.gov/business-services","portalUrl":"https://www.sos.alabama.gov/business-services","note":"$200 filing fee + $28 name reservation required before formation. Annual BPT return filed with AL Dept of Revenue.","lastChecked":"October 2026","expediteAvailable":true,"expediteFee":100,"expediteTier":"Expedited Service"},
  {"name":"Alaska","code":"AK","slug":"alaska","fee":250,"paperFee":250,"initialExtras":0,"initialExtrasNote":"None","annual":"$100 Biennial","annualFeeNum":100,"freq":"Biennial (every 2 yrs)","due":"January 2 of every other year (first report due Jan 2 after formation year)","penalty":"$37.50 late fee","tax":"None","taxNum":0,"firstYearDue":"Initial report due within 6 months of formation ($0). First biennial report due Jan 2 of following year.","speed":"Instant Online","region":"west","popular":false,"sosName":"Alaska Division of Corporations","sosUrl":"https://www.commerce.alaska.gov/cbp/main/search/entities","portalUrl":"https://www.commerce.alaska.gov/cbp/main/search/entities","note":"$250 filing fee. Biennial report $100 every 2 years. Free initial report within 6 months.","lastChecked":"October 2026","expediteAvailable":false,"expediteFee":0,"expediteTier":"Not Offered (Standard Online)"},
  {"name":"Arizona","code":"AZ","slug":"arizona","fee":50,"paperFee":50,"initialExtras":0,"initialExtrasNote":"Newspaper publication in counties other than Maricopa/Pima (~$30–$300)","annual":"$0","annualFeeNum":0,"freq":"None","due":"No annual report required for LLCs","penalty":"N/A","tax":"None","taxNum":0,"firstYearDue":"$50 formation fee. Publication in non-exempt counties within 60 days.","speed":"1-2 Weeks (or expedited)","region":"west","popular":true,"sosName":"Arizona Corporation Commission (eCorp)","sosUrl":"https://ecorp.azcc.gov/","portalUrl":"https://ecorp.azcc.gov/","note":"$50 filing fee. No annual report required for domestic LLCs. Maricopa/Pima counties exempt from publication.","lastChecked":"October 2026","expediteAvailable":true,"expediteFee":35,"expediteTier":"Expedited Service"},
  {"name":"Arkansas","code":"AR","slug":"arkansas","fee":45,"paperFee":50,"initialExtras":0,"initialExtrasNote":"None","annual":"$150 Franchise Tax","annualFeeNum":150,"freq":"Annual Tax","due":"May 1 annually","penalty":"$25 late fee + 10% interest/year","tax":"$150 Franchise Tax included","taxNum":0,"firstYearDue":"$45 online formation. Franchise tax due May 1 of the year following formation.","speed":"Instant Online","region":"south","popular":false,"sosName":"Arkansas Secretary of State","sosUrl":"https://www.sos.arkansas.gov/corps/search_all.php","portalUrl":"https://www.sos.arkansas.gov/corps/search_all.php","note":"$45 online Articles ($50 paper). Annual franchise tax is $150 due May 1 each year.","lastChecked":"October 2026","expediteAvailable":false,"expediteFee":0,"expediteTier":"Not Offered (Standard Online)"},
  {"name":"California","code":"CA","slug":"california","fee":70,"paperFee":70,"initialExtras":20,"initialExtrasNote":"Initial Statement of Information ($20) within 90 days","annual":"$20 Biennial","annualFeeNum":20,"freq":"Biennial ($20) + Annual Tax","due":"Initial Statement of Info: within 90 days ($20). $800 Annual Franchise Tax: due by 15th day of 4th month after formation (Year 1) & April 15 annually thereafter. Statement of Info: every 2 years ($20).","penalty":"$250 late penalty for Statement of Info; penalties/interest on franchise tax","tax":"$800 Annual Franchise Tax (due in Year 1 & annually)","taxNum":800,"firstYearDue":"$70 Articles of Organization + $20 Initial Statement of Info (within 90 days) + $800 Annual Franchise Tax (due 15th day of 4th month). $890 total mandatory first-year state obligations (AB 85 first-year tax exemption expired after 2023).","speed":"1-2 Days","region":"west","popular":true,"sosName":"California Secretary of State (bizfile)","sosUrl":"https://bizfileonline.sos.ca.gov/","portalUrl":"https://bizfileonline.sos.ca.gov/","note":"$70 filing fee + $20 initial statement of info (due within 90 days) + $800 annual franchise tax (due in Year 1 & annually thereafter; AB 85 first-year tax exemption expired after 2023). $20 statement of info every 2 years.","lastChecked":"October 2026","expediteAvailable":true,"expediteFee":350,"expediteTier":"24-Hour Expedited"},
  {"name":"Colorado","code":"CO","slug":"colorado","fee":50,"paperFee":50,"initialExtras":0,"initialExtrasNote":"None","annual":"$25 Periodic Report","annualFeeNum":25,"freq":"Annual","due":"Periodic Report due during 2-month window around formation anniversary","penalty":"$50 late fee ($75 total) if filed past grace period","tax":"None","taxNum":0,"firstYearDue":"$50 online Articles of Organization. First periodic report due on 1st anniversary.","speed":"Instant Online","region":"west","popular":true,"sosName":"Colorado Secretary of State","sosUrl":"https://www.sos.state.co.us/biz/BusinessEntityCriteriaExt.do","portalUrl":"https://www.sos.state.co.us/biz/BusinessEntityCriteriaExt.do","note":"$50 online filing fee. $25 annual periodic report filed online.","lastChecked":"October 2026","expediteAvailable":false,"expediteFee":0,"expediteTier":"Not Offered (Instant Online Filing)"},
  {"name":"Connecticut","code":"CT","slug":"connecticut","fee":120,"paperFee":120,"initialExtras":0,"initialExtrasNote":"None","annual":"$80","annualFeeNum":80,"freq":"Annual","due":"Due annually between Jan 1 and March 31 (starting year after formation)","penalty":"Loss of good standing / administrative dissolution","tax":"None","taxNum":0,"firstYearDue":"$120 Certificate of Organization. First annual report due March 31 of next year.","speed":"1-2 Days","region":"east","popular":false,"sosName":"Connecticut Secretary of the State (business.ct.gov)","sosUrl":"https://business.ct.gov/","portalUrl":"https://business.ct.gov/","note":"$120 online formation fee. $80 annual report due annually between Jan 1 and March 31.","lastChecked":"October 2026","expediteAvailable":true,"expediteFee":50,"expediteTier":"Expedited Service"},
  {"name":"Delaware","code":"DE","slug":"delaware","fee":110,"paperFee":110,"initialExtras":0,"initialExtrasNote":"None","annual":"$400 Franchise Tax","annualFeeNum":0,"freq":"Annual Tax (no report)","due":"June 1 annually","penalty":"$200 penalty + 1.5% monthly interest","tax":"$400 Annual Franchise Tax","taxNum":400,"firstYearDue":"$110 Certificate of Formation. First $400 franchise tax payment due June 1 of the year following formation.","speed":"1-2 Days","region":"east","popular":true,"sosName":"Delaware Division of Corporations","sosUrl":"https://corp.delaware.gov/","portalUrl":"https://corp.delaware.gov/paytaxes/","note":"$110 formation fee. Mandatory $400 annual franchise tax (HB 400) due every June 1st. No separate Secretary of State annual report fee required for LLCs.","lastChecked":"October 2026","expediteAvailable":true,"expediteFee":50,"expediteTier":"24-Hour Expedited"},
  {"name":"Florida","code":"FL","slug":"florida","fee":125,"paperFee":125,"initialExtras":0,"initialExtrasNote":"None ($100 filing + $25 registered agent fee included)","annual":"$138.75","annualFeeNum":138.75,"freq":"Annual","due":"May 1 annually (starting year after formation)","penalty":"Mandatory $400 late fee starting May 2; administrative dissolution on 3rd Friday of September","tax":"None","taxNum":0,"firstYearDue":"$125 Articles of Organization. First annual report ($138.75) due by May 1 of following year.","speed":"1-2 Days Online","region":"south","popular":true,"sosName":"Florida Division of Corporations (Sunbiz)","sosUrl":"https://search.sunbiz.org/Inquiry/CorporationSearch/ByName","portalUrl":"https://dos.myflorida.com/sunbiz/manage-business/efile/annual-report/","note":"$125 formation fee. $138.75 annual report due May 1. Strict $400 non-negotiable statutory late fee applied on May 2.","lastChecked":"October 2026","expediteAvailable":false,"expediteFee":0,"expediteTier":"Not Offered (Standard Online 1–2 Days)"},
  {"name":"Georgia","code":"GA","slug":"georgia","fee":110,"paperFee":110,"initialExtras":0,"initialExtrasNote":"None ($100 fee + $10 online service charge)","annual":"$60 Annual Registration","annualFeeNum":60,"freq":"Annual","due":"April 1 annually (between Jan 1 and Apr 1)","penalty":"$25 late fee","tax":"None","taxNum":0,"firstYearDue":"$110 online Articles of Organization. First $60 registration due April 1 of following year.","speed":"7 Business Days","region":"south","popular":true,"sosName":"Georgia Secretary of State (eCorp)","sosUrl":"https://ecorp.sos.ga.gov/BusinessSearch","portalUrl":"https://ecorp.sos.ga.gov/","note":"$110 online formation fee ($100 + $10 service charge). $60 annual registration due April 1.","lastChecked":"October 2026","expediteAvailable":true,"expediteFee":100,"expediteTier":"24-Hour Expedited"},
  {"name":"Hawaii","code":"HI","slug":"hawaii","fee":50,"paperFee":50,"initialExtras":1,"initialExtrasNote":"$1 archive fee","annual":"$15","annualFeeNum":15,"freq":"Annual","due":"Quarterly based on registration quarter","penalty":"$10 late fee","tax":"None","taxNum":0,"firstYearDue":"$51 ($50 + $1 archive fee). Annual report due in formation quarter of next year.","speed":"3-5 Days","region":"west","popular":false,"sosName":"Hawaii Business Registration Division (BREG)","sosUrl":"https://hbe.ehawaii.gov/bizsearch/","portalUrl":"https://hbe.ehawaii.gov/","note":"$51 online formation fee ($50 + $1 fee). $15 annual report.","lastChecked":"October 2026","expediteAvailable":true,"expediteFee":25,"expediteTier":"Expedited Review"},
  {"name":"Idaho","code":"ID","slug":"idaho","fee":100,"paperFee":120,"initialExtras":0,"initialExtrasNote":"None","annual":"$0","annualFeeNum":0,"freq":"Annual (Free)","due":"End of formation anniversary month","penalty":"Administrative dissolution after delinquency notice","tax":"None","taxNum":0,"firstYearDue":"$100 online Certificate of Organization. Free annual report on 1st anniversary.","speed":"Instant Online","region":"west","popular":false,"sosName":"Idaho Secretary of State","sosUrl":"https://sosbiz.idaho.gov/search/business","portalUrl":"https://sosbiz.idaho.gov/","note":"$100 online Certificate of Organization. Annual report is 100% free ($0).","lastChecked":"October 2026","expediteAvailable":true,"expediteFee":40,"expediteTier":"Expedited Processing"},
  {"name":"Illinois","code":"IL","slug":"illinois","fee":150,"paperFee":150,"initialExtras":0,"initialExtrasNote":"None","annual":"$75","annualFeeNum":75,"freq":"Annual","due":"First day of formation anniversary month","penalty":"$100 late penalty if filed more than 60 days late","tax":"None","taxNum":0,"firstYearDue":"$150 Articles of Organization. First annual report due on 1st anniversary.","speed":"1-2 Days Online","region":"midwest","popular":true,"sosName":"Illinois Secretary of State","sosUrl":"https://www.ilsos.gov/departments/business_services/corp.html","portalUrl":"https://www.ilsos.gov/","note":"$150 online formation fee. $75 annual report fee due on first day of formation anniversary month.","lastChecked":"October 2026","expediteAvailable":true,"expediteFee":100,"expediteTier":"24-Hour Expedited"},
  {"name":"Indiana","code":"IN","slug":"indiana","fee":95,"paperFee":100,"initialExtras":0,"initialExtrasNote":"None","annual":"$32 Biennial ($50 paper)","annualFeeNum":32,"freq":"Biennial (every 2 yrs)","due":"End of formation anniversary month every 2 years","penalty":"Administrative revocation notice","tax":"None","taxNum":0,"firstYearDue":"$95 online Articles of Organization. First biennial report due 2 years after formation.","speed":"Instant Online","region":"midwest","popular":false,"sosName":"Indiana Secretary of State (INBiz)","sosUrl":"https://bsd.sos.in.gov/publicbusinesssearch","portalUrl":"https://inbiz.in.gov/","note":"$95 online formation fee ($100 paper). $32 online biennial report every 2 years.","lastChecked":"October 2026","expediteAvailable":false,"expediteFee":0,"expediteTier":"Not Offered (Instant Online Filing)"},
  {"name":"Iowa","code":"IA","slug":"iowa","fee":50,"paperFee":50,"initialExtras":0,"initialExtrasNote":"None","annual":"$30 Biennial ($45 paper)","annualFeeNum":30,"freq":"Biennial (every 2 yrs in odd years)","due":"April 1 of odd-numbered years","penalty":"Delinquency notice / administrative dissolution","tax":"None","taxNum":0,"firstYearDue":"$50 Certificate of Organization. First biennial report due April 1 of next odd year.","speed":"1-2 Days","region":"midwest","popular":false,"sosName":"Iowa Secretary of State","sosUrl":"https://sos.iowa.gov/search/business/search.aspx","portalUrl":"https://sos.iowa.gov/","note":"$50 Certificate of Organization. $30 online biennial report due in odd-numbered years.","lastChecked":"October 2026","expediteAvailable":false,"expediteFee":0,"expediteTier":"Not Offered (Standard Online)"},
  {"name":"Kansas","code":"KS","slug":"kansas","fee":160,"paperFee":165,"initialExtras":0,"initialExtrasNote":"None","annual":"$50 Biennial ($55 paper)","annualFeeNum":50,"freq":"Biennial (every 2 yrs)","due":"April 15 of even or odd year matching formation year","penalty":"Loss of good standing + forfeiture","tax":"None","taxNum":0,"firstYearDue":"$160 online Articles. Biennial report $50 due on alternating years by April 15.","speed":"Instant Online","region":"midwest","popular":false,"sosName":"Kansas Secretary of State","sosUrl":"https://www.kansas.gov/bess/flow/setup","portalUrl":"https://www.sos.ks.gov/","note":"$160 online Articles of Organization. $50 biennial report filed every two years.","lastChecked":"October 2026","expediteAvailable":false,"expediteFee":0,"expediteTier":"Not Offered (Instant Online Filing)"},
  {"name":"Kentucky","code":"KY","slug":"kentucky","fee":40,"paperFee":40,"initialExtras":33,"initialExtrasNote":"County clerk recording fee (~$33 to $50 depending on county)","annual":"$15","annualFeeNum":15,"freq":"Annual","due":"June 30 annually","penalty":"Administrative dissolution after 60-day notice","tax":"Limited Liability Entity Tax (LLET, $175 min) may apply","taxNum":0,"firstYearDue":"$40 Articles + county recording fee. First $15 annual report due June 30 of next year.","speed":"1 Day Online","region":"south","popular":false,"sosName":"Kentucky Secretary of State","sosUrl":"https://web.sos.ky.gov/ftsearch/","portalUrl":"https://web.sos.ky.gov/","note":"$40 formation fee (one of the lowest in the U.S.). County clerk recording fee may apply. $15 annual report due June 30.","lastChecked":"October 2026","expediteAvailable":false,"expediteFee":0,"expediteTier":"Not Offered (Standard Online)"},
  {"name":"Louisiana","code":"LA","slug":"louisiana","fee":100,"paperFee":100,"initialExtras":0,"initialExtrasNote":"None","annual":"$35","annualFeeNum":35,"freq":"Annual","due":"Anniversary date of formation","penalty":"Revocation of charter","tax":"None","taxNum":0,"firstYearDue":"$100 Articles of Organization. Annual report ($35) due on 1st anniversary.","speed":"1-2 Days","region":"south","popular":false,"sosName":"Louisiana Secretary of State (geauxBIZ)","sosUrl":"https://coraweb.sos.la.gov/commercialsearch/commercialsearch.aspx","portalUrl":"https://geauxbiz.sos.la.gov/","note":"$100 Articles of Organization. $35 annual report due on formation anniversary.","lastChecked":"October 2026","expediteAvailable":true,"expediteFee":30,"expediteTier":"24-Hour Expedited"},
  {"name":"Maine","code":"ME","slug":"maine","fee":175,"paperFee":175,"initialExtras":0,"initialExtrasNote":"None","annual":"$85 ($150 paper)","annualFeeNum":85,"freq":"Annual","due":"June 1 annually","penalty":"$50 late fee","tax":"None","taxNum":0,"firstYearDue":"$175 Certificate of Formation. First $85 annual report due June 1 of following year.","speed":"5-10 Days","region":"east","popular":false,"sosName":"Maine Secretary of State","sosUrl":"https://icrs.informe.org/nei-sos-icrs/ICRS?MainPage=x","portalUrl":"https://www.maine.gov/sos/cec/corp/","note":"$175 formation fee. $85 annual report due June 1.","lastChecked":"October 2026","expediteAvailable":true,"expediteFee":50,"expediteTier":"24-Hour Expedited"},
  {"name":"Maryland","code":"MD","slug":"maryland","fee":100,"paperFee":100,"initialExtras":0,"initialExtrasNote":"None","annual":"$300 Annual Report","annualFeeNum":300,"freq":"Annual","due":"April 15 annually","penalty":"Loss of good standing / forfeiture","tax":"Personal Property Return ($300 included)","taxNum":0,"firstYearDue":"$100 Articles of Organization. Annual Report ($300) due April 15 of year after formation.","speed":"Instant Online","region":"east","popular":false,"sosName":"Maryland Department of Assessments & Taxation (Maryland Business Express)","sosUrl":"https://egov.maryland.gov/BusinessExpress/EntitySearch","portalUrl":"https://egov.maryland.gov/BusinessExpress/","note":"$100 online Articles of Organization. $300 annual report fee due April 15.","lastChecked":"October 2026","expediteAvailable":true,"expediteFee":50,"expediteTier":"Expedited Processing"},
  {"name":"Massachusetts","code":"MA","slug":"massachusetts","fee":500,"paperFee":500,"initialExtras":0,"initialExtrasNote":"None","annual":"$500","annualFeeNum":500,"freq":"Annual","due":"Anniversary date of formation","penalty":"Loss of good standing + administrative dissolution","tax":"None","taxNum":0,"firstYearDue":"$500 Certificate of Organization. Annual report ($500) due on 1st anniversary.","speed":"1-2 Days","region":"east","popular":false,"sosName":"Massachusetts Secretary of the Commonwealth","sosUrl":"https://corp.sec.state.ma.us/corpweb/CorpSearch/CorpSearch.aspx","portalUrl":"https://www.sec.state.ma.us/cor/","note":"$500 formation fee (highest standard initial fee in US). $500 annual report due on anniversary date.","lastChecked":"October 2026","expediteAvailable":false,"expediteFee":0,"expediteTier":"Not Offered (Standard Online 1–2 Days)"},
  {"name":"Michigan","code":"MI","slug":"michigan","fee":50,"paperFee":50,"initialExtras":0,"initialExtrasNote":"None","annual":"$25 Annual Statement","annualFeeNum":25,"freq":"Annual","due":"February 15 annually (formed after Sept 30 exempt in first following year)","penalty":"$50 late fee if past grace period","tax":"None","taxNum":0,"firstYearDue":"$50 Articles of Organization. First annual statement ($25) due Feb 15 of following year.","speed":"1-2 Days Online","region":"midwest","popular":true,"sosName":"Michigan Department of Licensing & Regulatory Affairs (LARA)","sosUrl":"https://cofs.lara.state.mi.us/Search/Search","portalUrl":"https://cofs.lara.state.mi.us/","note":"$50 Articles of Organization. $25 annual statement due February 15.","lastChecked":"October 2026","expediteAvailable":true,"expediteFee":50,"expediteTier":"24-Hour Expedited"},
  {"name":"Minnesota","code":"MN","slug":"minnesota","fee":155,"paperFee":135,"initialExtras":0,"initialExtrasNote":"None","annual":"$0 Annual Renewal","annualFeeNum":0,"freq":"Annual (Free)","due":"December 31 each calendar year","penalty":"Dissolution by state; $85 reinstatement fee","tax":"Minimum Fee $0–$12,830 applies only to partnerships with >$1.28M MN receipts","taxNum":0,"firstYearDue":"$155 online Articles ($135 mail). Free $0 annual renewal filed once every calendar year.","speed":"Instant Online","region":"midwest","popular":false,"sosName":"Minnesota Secretary of State (MBLS)","sosUrl":"https://mblsportal.sos.state.mn.us/Business/Search","portalUrl":"https://mblsportal.sos.state.mn.us/","note":"$155 online formation fee ($135 mail). Annual renewal is 100% free ($0).","lastChecked":"October 2026","expediteAvailable":false,"expediteFee":0,"expediteTier":"Included in Online Fee ($20 Expedited Differential)"},
  {"name":"Mississippi","code":"MS","slug":"mississippi","fee":50,"paperFee":50,"initialExtras":0,"initialExtrasNote":"None","annual":"$0 Annual Report","annualFeeNum":0,"freq":"Annual (Free)","due":"April 15 annually","penalty":"Administrative dissolution for unfiled reports","tax":"None","taxNum":0,"firstYearDue":"$50 Certificate of Formation. Free $0 annual report due April 15 of following year.","speed":"Instant Online","region":"south","popular":false,"sosName":"Mississippi Secretary of State","sosUrl":"https://corp.sos.ms.gov/corp/portal/c/page/corpBusinessIdSearch/portal.aspx","portalUrl":"https://corp.sos.ms.gov/","note":"$50 Certificate of Formation. Annual report is 100% free ($0) due April 15.","lastChecked":"October 2026","expediteAvailable":false,"expediteFee":0,"expediteTier":"Not Offered (Instant Online Filing)"},
  {"name":"Missouri","code":"MO","slug":"missouri","fee":50,"paperFee":105,"initialExtras":0,"initialExtrasNote":"None","annual":"$0","annualFeeNum":0,"freq":"None","due":"No annual report required for LLCs under MO law","penalty":"N/A","tax":"None","taxNum":0,"firstYearDue":"$50 online Articles of Organization ($105 paper). No annual report.","speed":"Instant Online","region":"midwest","popular":false,"sosName":"Missouri Secretary of State","sosUrl":"https://bsd.sos.mo.gov/BusinessEntity/BESearch.aspx?SearchType=0","portalUrl":"https://bsd.sos.mo.gov/","note":"$50 online Articles of Organization ($105 paper). No recurring annual report required for domestic LLCs.","lastChecked":"October 2026","expediteAvailable":false,"expediteFee":0,"expediteTier":"Not Offered (Instant Online Filing)"},
  {"name":"Montana","code":"MT","slug":"montana","fee":35,"paperFee":35,"initialExtras":0,"initialExtrasNote":"None","annual":"$0 (waived Jan 1–Apr 15) / $35 after","annualFeeNum":0,"freq":"Annual ($0 waived window)","due":"April 15 annually ($0 fee if filed by April 15; $35 late fee after)","penalty":"$35 fee after April 15; involuntary dissolution by Dec 1","tax":"None (No general state sales tax)","taxNum":0,"firstYearDue":"$35 Articles of Organization. Annual report is $0 if filed between Jan 1 and April 15 ($35 if late).","speed":"1-2 Days Online","region":"west","popular":true,"sosName":"Montana Secretary of State","sosUrl":"https://biz.sosmt.gov/search/business","portalUrl":"https://biz.sosmt.gov/","note":"$35 formation fee (lowest in US). Annual report fee is $0 if filed between Jan 1 and April 15 ($35 if late).","lastChecked":"October 2026","expediteAvailable":true,"expediteFee":20,"expediteTier":"24-Hour Expedited"},
  {"name":"Nebraska","code":"NE","slug":"nebraska","fee":100,"paperFee":110,"initialExtras":25,"initialExtrasNote":"Mandatory Proof of Publication state fee ($25). 3-week newspaper publication paid separately to qualifying local newspaper.","annual":"$10 Biennial ($13 online)","annualFeeNum":13,"freq":"Biennial (every 2 yrs in odd years)","due":"April 1 of odd-numbered years","penalty":"Loss of good standing / dissolution","tax":"None","taxNum":0,"firstYearDue":"$100 online Certificate of Organization + $25 Proof of Publication state fee. 3-week newspaper publication paid separately to local paper.","speed":"1-2 Days","region":"midwest","popular":false,"sosName":"Nebraska Secretary of State","sosUrl":"https://www.nebraska.gov/sos/corp/corpsearch.cgi","portalUrl":"https://www.nebraska.gov/sos/corp/","note":"$100 online Certificate of Organization. 3-week newspaper publication required + $25 proof fee. $13 biennial report in odd years.","lastChecked":"October 2026","expediteAvailable":false,"expediteFee":0,"expediteTier":"Not Offered (Standard Online)"},
  {"name":"Nevada","code":"NV","slug":"nevada","fee":75,"paperFee":75,"initialExtras":350,"initialExtrasNote":"Mandatory Initial List ($150) + State Business License ($200) due at formation","annual":"$350 Annual List ($150) + License ($200)","annualFeeNum":150,"freq":"Annual ($150 List + $200 License)","due":"Last day of formation anniversary month annually","penalty":"$100 late fee on List + $100 late fee on License ($200 total penalty)","tax":"$200 State Business License","taxNum":200,"firstYearDue":"$75 Articles + $150 Initial List + $200 Initial Business License = $425 total state initial fees.","speed":"Instant Online (SilverFlume)","region":"west","popular":true,"sosName":"Nevada Secretary of State (SilverFlume)","sosUrl":"https://esos.nv.gov/EntitySearch/OnlineEntitySearch","portalUrl":"https://www.nvsilverflume.gov/","note":"$75 formation fee + mandatory $150 Initial List + $200 Initial Business License ($425 total initial). Ongoing: $150 Annual List + $200 Business License ($350/yr).","lastChecked":"October 2026","expediteAvailable":true,"expediteFee":125,"expediteTier":"24-Hour Expedited"},
  {"name":"New Hampshire","code":"NH","slug":"new-hampshire","fee":100,"paperFee":100,"initialExtras":0,"initialExtrasNote":"None","annual":"$100","annualFeeNum":100,"freq":"Annual","due":"April 1 annually","penalty":"$50 late fee","tax":"Business Profits Tax / Business Enterprise Tax may apply depending on gross receipts","taxNum":0,"firstYearDue":"$100 Certificate of Formation. First $100 annual report due April 1 of following year.","speed":"2-3 Days","region":"east","popular":false,"sosName":"New Hampshire Department of State","sosUrl":"https://quickstart.sos.nh.gov/online/Account/LandingPage","portalUrl":"https://quickstart.sos.nh.gov/","note":"$100 Certificate of Formation. $100 annual report due April 1.","lastChecked":"October 2026","expediteAvailable":true,"expediteFee":25,"expediteTier":"Expedited Processing"},
  {"name":"New Jersey","code":"NJ","slug":"new-jersey","fee":125,"paperFee":125,"initialExtras":0,"initialExtrasNote":"Mandatory NJ-REG tax registration within 60 days ($0)","annual":"$75","annualFeeNum":75,"freq":"Annual","due":"Last day of formation anniversary month annually","penalty":"Revocation of charter after 2 delinquent years","tax":"None","taxNum":0,"firstYearDue":"$125 Certificate of Formation. First $75 annual report due on 1st anniversary.","speed":"Instant Online","region":"east","popular":true,"sosName":"New Jersey Division of Revenue","sosUrl":"https://www.njportal.com/DOR/BusinessNameSearch/","portalUrl":"https://www.njportal.com/DOR/BusinessRegistration","note":"$125 Public Records Filing. $75 annual report due on formation anniversary month.","lastChecked":"October 2026","expediteAvailable":true,"expediteFee":25,"expediteTier":"8.5-Hour Expedited"},
  {"name":"New Mexico","code":"NM","slug":"new-mexico","fee":50,"paperFee":50,"initialExtras":0,"initialExtrasNote":"None","annual":"$0","annualFeeNum":0,"freq":"None","due":"No annual report required for LLCs under NM law","penalty":"N/A","tax":"None","taxNum":0,"firstYearDue":"$50 online Articles of Organization. $0 recurring report costs.","speed":"1-2 Days Online","region":"west","popular":true,"sosName":"New Mexico Secretary of State","sosUrl":"https://portal.sos.state.nm.us/corps/(S(1ubdfbvgfdfu45f5j535d545))/CorpLookup/CorpSearch.aspx","portalUrl":"https://portal.sos.state.nm.us/","note":"$50 online Articles of Organization. Top privacy state: owner names not public, no annual report required.","lastChecked":"October 2026","expediteAvailable":false,"expediteFee":0,"expediteTier":"Not Offered (Standard Online)"},
  {"name":"New York","code":"NY","slug":"new-york","fee":200,"paperFee":200,"initialExtras":50,"initialExtrasNote":"Mandatory Certificate of Publication state filing fee ($50). County newspaper publication (~$300–$1,200) paid separately to local newspapers.","annual":"$9 Biennial","annualFeeNum":9,"freq":"Biennial (every 2 yrs)","due":"End of formation anniversary month every 2 years","penalty":"Suspension of authority to do business","tax":"None","taxNum":0,"firstYearDue":"$200 Articles of Organization + $50 Certificate of Publication state fee. Section 206 county newspaper publication (~$300–$1,200) required within 120 days.","speed":"1-2 Days","region":"east","popular":true,"sosName":"New York Department of State (Division of Corporations)","sosUrl":"https://apps.dos.ny.gov/publicInquiry/","portalUrl":"https://dos.ny.gov/e-statement-filing","note":"$200 Articles of Organization. Section 206 publication required within 120 days ($300-$1500). $9 biennial statement every 2 years.","lastChecked":"October 2026","expediteAvailable":true,"expediteFee":25,"expediteTier":"24-Hour Expedited"},
  {"name":"North Carolina","code":"NC","slug":"north-carolina","fee":125,"paperFee":125,"initialExtras":0,"initialExtrasNote":"None","annual":"$202 ($200 paper)","annualFeeNum":202,"freq":"Annual","due":"April 15 annually (starting year after formation)","penalty":"Administrative dissolution notice","tax":"None","taxNum":0,"firstYearDue":"$125 Articles of Organization. First $202 annual report due April 15 of following year.","speed":"3-5 Days","region":"south","popular":true,"sosName":"North Carolina Secretary of State","sosUrl":"https://www.sosnc.gov/search/index/corp","portalUrl":"https://www.sosnc.gov/","note":"$125 Articles of Organization. $202 online annual report ($200 paper) due April 15.","lastChecked":"October 2026","expediteAvailable":true,"expediteFee":100,"expediteTier":"24-Hour Expedited"},
  {"name":"North Dakota","code":"ND","slug":"north-dakota","fee":135,"paperFee":135,"initialExtras":0,"initialExtrasNote":"None","annual":"$50","annualFeeNum":50,"freq":"Annual","due":"November 15 annually","penalty":"$50 late fee ($100 total); involuntary dissolution if 1 year late","tax":"None","taxNum":0,"firstYearDue":"$135 Articles of Organization. First $50 annual report due Nov 15 of year after formation.","speed":"2-3 Days","region":"midwest","popular":false,"sosName":"North Dakota Secretary of State (FirstStop)","sosUrl":"https://firststop.sos.nd.gov/search/business","portalUrl":"https://firststop.sos.nd.gov/","note":"$135 online Articles of Organization. $50 annual report due November 15.","lastChecked":"October 2026","expediteAvailable":false,"expediteFee":0,"expediteTier":"Not Offered (Standard Online)"},
  {"name":"Ohio","code":"OH","slug":"ohio","fee":99,"paperFee":99,"initialExtras":0,"initialExtrasNote":"None","annual":"$0","annualFeeNum":0,"freq":"None","due":"No annual report required for domestic LLCs","penalty":"N/A","tax":"Commercial Activity Tax (CAT) only if Ohio taxable gross receipts exceed $3M (2026 threshold)","taxNum":0,"firstYearDue":"$99 Articles of Organization. $0 recurring state report fees.","speed":"1-2 Days Online","region":"midwest","popular":true,"sosName":"Ohio Secretary of State","sosUrl":"https://businesssearch.ohiosos.gov/","portalUrl":"https://www.ohiosos.gov/","note":"$99 online Articles of Organization. No annual report required for domestic Ohio LLCs.","lastChecked":"October 2026","expediteAvailable":true,"expediteFee":100,"expediteTier":"2-Day Expedited"},
  {"name":"Oklahoma","code":"OK","slug":"oklahoma","fee":100,"paperFee":100,"initialExtras":0,"initialExtrasNote":"None","annual":"$25 Annual Certificate","annualFeeNum":25,"freq":"Annual","due":"Anniversary date of formation annually","penalty":"Loss of good standing + administrative dissolution","tax":"None","taxNum":0,"firstYearDue":"$100 Articles of Organization. First $25 Annual Certificate due on 1st anniversary.","speed":"1-2 Days","region":"south","popular":false,"sosName":"Oklahoma Secretary of State","sosUrl":"https://www.sos.ok.gov/corp/corpInquiryFind.aspx","portalUrl":"https://www.sos.ok.gov/","note":"$100 Articles of Organization. $25 Annual Certificate due on anniversary date.","lastChecked":"October 2026","expediteAvailable":true,"expediteFee":25,"expediteTier":"Expedited Review"},
  {"name":"Oregon","code":"OR","slug":"oregon","fee":100,"paperFee":100,"initialExtras":0,"initialExtrasNote":"None","annual":"$100","annualFeeNum":100,"freq":"Annual","due":"Anniversary date of formation annually","penalty":"Administrative dissolution after 45 days past due","tax":"None","taxNum":0,"firstYearDue":"$100 Articles of Organization. First $100 annual report due on 1st anniversary.","speed":"1-2 Days","region":"west","popular":false,"sosName":"Oregon Secretary of State","sosUrl":"https://sos.oregon.gov/business/Pages/find.aspx","portalUrl":"https://sos.oregon.gov/","note":"$100 Articles of Organization. $100 annual report due on formation anniversary.","lastChecked":"October 2026","expediteAvailable":false,"expediteFee":0,"expediteTier":"Not Offered (Standard Online)"},
  {"name":"Pennsylvania","code":"PA","slug":"pennsylvania","fee":125,"paperFee":125,"initialExtras":0,"initialExtrasNote":"None","annual":"$7 Annual Report","annualFeeNum":7,"freq":"Annual (replaced decennial in 2025)","due":"September 30 annually","penalty":"Loss of good standing / administrative dissolution (enforcement begins 2027)","tax":"None","taxNum":0,"firstYearDue":"$125 Certificate of Organization. First $7 annual report due Sept 30.","speed":"2-3 Days","region":"east","popular":false,"sosName":"Pennsylvania Department of State","sosUrl":"https://www.corporations.pa.gov/search/corpsearch","portalUrl":"https://www.dos.pa.gov/","note":"$125 Certificate of Organization. PA switched from decennial to $7 annual report due Sept 30 under Act 122.","lastChecked":"October 2026","expediteAvailable":true,"expediteFee":100,"expediteTier":"Same-Day Expedited"},
  {"name":"Rhode Island","code":"RI","slug":"rhode-island","fee":150,"paperFee":150,"initialExtras":0,"initialExtrasNote":"None","annual":"$50 Annual Report","annualFeeNum":50,"freq":"Annual","due":"Between February 1 and May 1 annually","penalty":"$25 late fee","tax":"$400 minimum state corporate income tax applies to LLCs electing corporate status; verify pass-through status","taxNum":0,"firstYearDue":"$150 Articles of Organization. First $50 annual report due between Feb 1 & May 1 of next year.","speed":"1-2 Days","region":"east","popular":false,"sosName":"Rhode Island Department of State","sosUrl":"https://business.sos.ri.gov/CorpWeb/CorpSearch/CorpSearch.aspx","portalUrl":"https://business.sos.ri.gov/","note":"$150 Articles of Organization. $50 annual report due between Feb 1 and May 1.","lastChecked":"October 2026","expediteAvailable":false,"expediteFee":0,"expediteTier":"Not Offered (Standard Online)"},
  {"name":"South Carolina","code":"SC","slug":"south-carolina","fee":110,"paperFee":110,"initialExtras":0,"initialExtrasNote":"None","annual":"$0","annualFeeNum":0,"freq":"None","due":"No annual report required for domestic LLCs","penalty":"N/A","tax":"None","taxNum":0,"firstYearDue":"$110 Articles of Organization. $0 annual report fee.","speed":"1-2 Days Online","region":"south","popular":false,"sosName":"South Carolina Secretary of State","sosUrl":"https://businessfilings.sc.gov/BusinessFiling/Entity/Search","portalUrl":"https://businessfilings.sc.gov/","note":"$110 Articles of Organization. No annual report required for domestic LLCs.","lastChecked":"October 2026","expediteAvailable":false,"expediteFee":0,"expediteTier":"Not Offered (Standard Online)"},
  {"name":"South Dakota","code":"SD","slug":"south-dakota","fee":150,"paperFee":165,"initialExtras":0,"initialExtrasNote":"None","annual":"$50 ($65 paper)","annualFeeNum":50,"freq":"Annual","due":"First day of formation anniversary month annually","penalty":"$50 late fee","tax":"None (No corporate or individual income tax)","taxNum":0,"firstYearDue":"$150 online Articles ($165 paper). First $50 annual report due on 1st anniversary.","speed":"Instant Online","region":"midwest","popular":false,"sosName":"South Dakota Secretary of State","sosUrl":"https://sdsos.gov/business-services/business-entity-search/default.aspx","portalUrl":"https://sdsos.gov/","note":"$150 online Articles of Organization ($165 paper). $50 annual report due on anniversary month.","lastChecked":"October 2026","expediteAvailable":true,"expediteFee":50,"expediteTier":"Expedited Processing"},
  {"name":"Tennessee","code":"TN","slug":"tennessee","fee":300,"paperFee":300,"initialExtras":0,"initialExtrasNote":"None ($300 min up to 6 members, $50/member up to $3,000 max)","annual":"$300 min Annual Report","annualFeeNum":300,"freq":"Annual","due":"First day of 4th month following fiscal year end (April 1 for calendar year)","penalty":"Administrative dissolution notice","tax":"Franchise & Excise Tax ($100 minimum) filed with TN Dept of Revenue","taxNum":0,"firstYearDue":"$300 minimum Articles of Organization. First annual report ($300 min) due April 1 of next year.","speed":"1-2 Days","region":"south","popular":false,"sosName":"Tennessee Secretary of State (Tre Hargett)","sosUrl":"https://tnbear.tn.gov/Ecommerce/FilingSearch.aspx","portalUrl":"https://tnbear.tn.gov/","note":"$300 min Articles ($50/member, max $3,000). $300 min annual report due April 1.","lastChecked":"October 2026","expediteAvailable":false,"expediteFee":0,"expediteTier":"Not Offered (Standard Online)"},
  {"name":"Texas","code":"TX","slug":"texas","fee":300,"paperFee":300,"initialExtras":0,"initialExtrasNote":"None","annual":"$0 PIR (Franchise Tax Report)","annualFeeNum":0,"freq":"Annual (Free for most)","due":"May 15 annually","penalty":"$50 penalty + 5% interest","tax":"No franchise tax owed for LLCs at or below the $2.65M revenue threshold (2026–2027), but Public Information Report (PIR) is mandatory ($0)","taxNum":0,"firstYearDue":"$300 Certificate of Formation. No tax for revenue under $2.65M threshold; free PIR/OIR due May 15.","speed":"2-3 Days Online","region":"south","popular":true,"sosName":"Texas Secretary of State (SOSDirect)","sosUrl":"https://mycpa.cpa.state.tx.us/coa/","portalUrl":"https://comptroller.texas.gov/taxes/franchise/","note":"$300 Certificate of Formation. Annual Franchise Tax Report / PIR due May 15 ($0 for gross revenue ≤$2.65M). Former No Tax Due report discontinued.","lastChecked":"October 2026","expediteAvailable":true,"expediteFee":25,"expediteTier":"Expedited Review"},
  {"name":"Utah","code":"UT","slug":"utah","fee":59,"paperFee":59,"initialExtras":0,"initialExtrasNote":"None","annual":"$18 Annual Renewal","annualFeeNum":18,"freq":"Annual","due":"Anniversary date of formation annually","penalty":"$10 late fee","tax":"None","taxNum":0,"firstYearDue":"$59 Certificate of Organization (FY2026 fee schedule). First $18 annual renewal due on 1st anniversary.","speed":"1-2 Days Online","region":"west","popular":false,"sosName":"Utah Division of Corporations","sosUrl":"https://secure.utah.gov/bes/","portalUrl":"https://corporations.utah.gov/","note":"$59 Certificate of Organization (FY2026 fee schedule). $18 annual renewal due on formation anniversary.","lastChecked":"October 2026","expediteAvailable":true,"expediteFee":75,"expediteTier":"Expedited Processing"},
  {"name":"Vermont","code":"VT","slug":"vermont","fee":125,"paperFee":125,"initialExtras":0,"initialExtrasNote":"None","annual":"$35","annualFeeNum":35,"freq":"Annual","due":"Within 2.5 months after fiscal year end (March 15 for calendar year)","penalty":"Termination after grace period","tax":"None","taxNum":0,"firstYearDue":"$125 Articles of Organization. First $35 annual report due March 15 of following year.","speed":"2-3 Days","region":"east","popular":false,"sosName":"Vermont Secretary of State","sosUrl":"https://bizfilings.vermont.gov/online/BusinessInquire/","portalUrl":"https://sos.vermont.gov/","note":"$125 online Articles of Organization. $35 annual report due within 2.5 months of fiscal year end.","lastChecked":"October 2026","expediteAvailable":false,"expediteFee":0,"expediteTier":"Not Offered (Standard Online)"},
  {"name":"Virginia","code":"VA","slug":"virginia","fee":100,"paperFee":100,"initialExtras":0,"initialExtrasNote":"None","annual":"$50 Annual Registration Fee","annualFeeNum":50,"freq":"Annual","due":"Last day of formation anniversary month annually","penalty":"$25 late penalty; cancellation after 4 months delinquency","tax":"None","taxNum":0,"firstYearDue":"$100 Articles of Organization. First $50 registration fee due on 1st anniversary month.","speed":"Instant Online","region":"south","popular":true,"sosName":"Virginia State Corporation Commission (Clerk's Information System)","sosUrl":"https://cis.scc.virginia.gov/EntitySearch/Index","portalUrl":"https://cis.scc.virginia.gov/","note":"$100 online Articles of Organization. $50 annual registration fee due on anniversary month.","lastChecked":"October 2026","expediteAvailable":true,"expediteFee":100,"expediteTier":"Next-Day Expedited"},
  {"name":"Washington","code":"WA","slug":"washington","fee":200,"paperFee":180,"initialExtras":10,"initialExtrasNote":"Initial report due within 120 days ($10)","annual":"$70 ($60 paper)","annualFeeNum":70,"freq":"Annual","due":"Last day of formation anniversary month annually","penalty":"$25 late fee","tax":"Business & Occupation (B&O) tax may apply; no state income tax","taxNum":0,"firstYearDue":"$200 online Certificate + $10 initial report within 120 days. First $70 annual report on 1st anniversary.","speed":"1-2 Days Online","region":"west","popular":true,"sosName":"Washington Secretary of State (CCFS)","sosUrl":"https://ccfs.sos.wa.gov/#/BusinessSearch","portalUrl":"https://www.sos.wa.gov/corps","note":"$200 online Certificate of Formation ($180 mail). $10 initial report in 120 days. $70 annual report.","lastChecked":"October 2026","expediteAvailable":true,"expediteFee":50,"expediteTier":"Expedited Processing"},
  {"name":"West Virginia","code":"WV","slug":"west-virginia","fee":100,"paperFee":100,"initialExtras":0,"initialExtrasNote":"None (veterans exempt from fee)","annual":"$25","annualFeeNum":25,"freq":"Annual","due":"July 1 annually (between Jan 1 and July 1)","penalty":"Administrative dissolution","tax":"None","taxNum":0,"firstYearDue":"$100 Articles of Organization. First $25 annual report due July 1 of following year.","speed":"2-3 Days","region":"south","popular":false,"sosName":"West Virginia Secretary of State","sosUrl":"https://apps.sos.wv.gov/business/corporations/","portalUrl":"https://wvsos.gov/","note":"$100 Articles of Organization. $25 annual report due July 1.","lastChecked":"October 2026","expediteAvailable":true,"expediteFee":25,"expediteTier":"24-Hour Expedited"},
  {"name":"Wisconsin","code":"WI","slug":"wisconsin","fee":130,"paperFee":170,"initialExtras":0,"initialExtrasNote":"None","annual":"$25","annualFeeNum":25,"freq":"Annual","due":"Quarterly based on anniversary quarter","penalty":"Administrative dissolution after delinquency notice","tax":"None","taxNum":0,"firstYearDue":"$130 online Articles of Organization ($170 paper). First $25 annual report due in formation quarter of next year.","speed":"1 Day Online","region":"midwest","popular":false,"sosName":"Wisconsin Department of Financial Institutions (DFI)","sosUrl":"https://www.wdfi.org/apps/CorpSearch/Search.aspx","portalUrl":"https://www.wdfi.org/","note":"$130 online Articles of Organization ($170 mail). $25 annual report.","lastChecked":"October 2026","expediteAvailable":true,"expediteFee":25,"expediteTier":"Expedited Service"},
  {"name":"Wyoming","code":"WY","slug":"wyoming","fee":100,"paperFee":100,"initialExtras":2,"initialExtrasNote":"$2 online processing fee","annual":"$60 min License Tax","annualFeeNum":60,"freq":"Annual","due":"First day of formation anniversary month annually","penalty":"$25 late fee; administrative dissolution after 60 days","tax":"None (No state income tax)","taxNum":0,"firstYearDue":"$102 ($100 fee + $2 online convenience fee). First $60 annual report due on 1st day of anniversary month.","speed":"Instant Online (WyoBiz)","region":"west","popular":true,"sosName":"Wyoming Secretary of State (WyoBiz)","sosUrl":"https://wyobiz.wyo.gov/Business/FilingSearch.aspx","portalUrl":"https://wyobiz.wyo.gov/","note":"$102 online Articles of Organization. Top privacy and asset protection state. $60 annual report license tax due on anniversary month.","lastChecked":"October 2026","expediteAvailable":true,"expediteFee":50,"expediteTier":"Expedited Processing"}
];
document.addEventListener("DOMContentLoaded", () => {
  populateStateSelectors();
  initFaqAccordion();
  initMobileMenu();
  initCostCalculator();
  initQuizWizard();
  initSearch();
  initActiveNavHighlighting();
  initCookieConsent();
});

function initActiveNavHighlighting() {
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  
  // Highlight dropdown items and their parent nav-item
  const dropdownLinks = document.querySelectorAll('.nav-menu .dropdown-link');
  dropdownLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href && (href === currentPath || (currentPath === '' && href === 'index.html'))) {
      link.classList.add('active');
      link.style.color = '#159A9C';
      link.style.fontWeight = '700';

      const parentNavItem = link.closest('.nav-item');
      if (parentNavItem) {
        const parentLink = parentNavItem.querySelector('.nav-link');
        if (parentLink) {
          parentLink.classList.add('active');
          parentLink.style.color = 'var(--color-primary)';
          parentLink.style.fontWeight = '800';
        }
      }
    }
  });

  // Highlight direct top-level nav links
  const topNavLinks = document.querySelectorAll('.nav-menu > .nav-item > .nav-link');
  topNavLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href && href === currentPath && !link.classList.contains('active')) {
      link.classList.add('active');
      link.style.color = 'var(--color-primary)';
      link.style.fontWeight = '800';
    }
  });
}

function populateStateSelectors() {
  const stateSectionSelect = document.getElementById("mainStateSectionSelect");
  const ctaStateSelect = document.getElementById("ctaStateSelect");
  const bottomCtaStateSelect = document.getElementById("bottomCtaStateSelect");
  const calcStateSelect = document.getElementById("calcStateSelect");
  const modalCalcStateSelect = document.getElementById("modalCalcStateSelect");

  [stateSectionSelect, ctaStateSelect, bottomCtaStateSelect, calcStateSelect, modalCalcStateSelect].forEach(select => {
    if (!select) return;
    const isCostCalc = (select === calcStateSelect || select === modalCalcStateSelect);
    select.innerHTML = `<option value="">${isCostCalc ? "— Select a State to See Estimate —" : "— Select a State —"}</option>`;
    stateData.forEach(st => {
      const opt = document.createElement("option");
      opt.value = st.code;
      opt.textContent = isCostCalc ? `${st.name} ($${st.fee} filing fee)` : st.name;
      select.appendChild(opt);
    });
  });

  // Attach event listener for modal calculator
  if (modalCalcStateSelect) {
    modalCalcStateSelect.addEventListener("change", updateModalCost);
  }
  const modalAgent = document.getElementById("modalCalcAgentSelect");
  if (modalAgent) modalAgent.addEventListener("change", updateModalCost);
  const modalService = document.getElementById("modalCalcServiceSelect");
  if (modalService) modalService.addEventListener("change", updateModalCost);
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
  const modal = document.getElementById("stateModalOverlay");
  const emptyBox = document.getElementById("modalStateEmptyState");
  const contentBox = document.getElementById("modalStateContent");
  const st = stateData.find(s => s.code === code);

  if (modal) {
    if (st) {
      if (emptyBox) emptyBox.style.display = "none";
      if (contentBox) contentBox.style.display = "block";
      const nameEl = document.getElementById("modalStateName");
      const abbrEl = document.getElementById("modalStateAbbr");
      const feeEl = document.getElementById("modalStateFee");
      const speedEl = document.getElementById("modalStateSpeed");
      const annualEl = document.getElementById("modalStateAnnual");
      const noteEl = document.getElementById("modalStateNote");
      const guideBtn = document.getElementById("modalGuideBtn");

      if (nameEl) nameEl.textContent = st.name;
      if (abbrEl) abbrEl.textContent = st.code;
      if (feeEl) feeEl.textContent = (st.fee !== undefined && st.fee !== null) ? `$${st.fee}` : "Varies";
      if (speedEl) speedEl.textContent = st.speed ? st.speed : "Varies by filing method";
      if (annualEl) annualEl.textContent = st.annual || (st.annualFee !== undefined && st.annualFee !== null ? `$${st.annualFee}` : "Varies");
      if (noteEl) noteEl.textContent = st.note || `Official statutory filing with the ${st.sosName || (st.name + " Secretary of State")}.`;
      if (guideBtn) {
        guideBtn.disabled = false;
        guideBtn.style.opacity = "1";
        guideBtn.style.cursor = "pointer";
        guideBtn.textContent = `View ${st.name} Filing Guide →`;
        const slug = st.name.toLowerCase().replace(/\s+/g, '-');
        guideBtn.onclick = function() {
          closeStateModal();
          window.location.href = st.link || `how-to-start-llc-in-${slug}.html`;
        };
      }
    } else {
      if (emptyBox) emptyBox.style.display = "block";
      if (contentBox) contentBox.style.display = "none";
      const guideBtn = document.getElementById("modalGuideBtn");
      if (guideBtn) {
        guideBtn.disabled = true;
        guideBtn.style.opacity = "0.5";
        guideBtn.style.cursor = "not-allowed";
        guideBtn.onclick = null;
      }
    }
    modal.classList.add("active");
  } else if (code) {
    showInlineStateResult(code);
  }
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
      <div style="background: rgba(255, 255, 255, 0.04); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 8px; padding: 0.65rem 0.85rem; font-size: 0.8rem; color: #CBD5E1; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1rem;">
        <div>State Filing Fee: <strong style="color: #FFFFFF; font-size: 0.9rem;">$${st.fee}</strong></div>
        <div>Source: <a href="${sosLinkUrl}" target="_blank" rel="noopener" style="color: #159A9C; font-weight: 700; text-decoration: underline;">${sosLinkName}</a></div>
      </div>

      <div style="text-align: center;">
        <a href="${st.link || ('how-to-start-llc-in-' + st.name.toLowerCase().replace(/\s+/g, '-') + '.html')}" class="ls-btn ls-btn--emerald" style="display: block; text-align: center; width: 100%; padding: 0.75rem 1.25rem; font-weight: 700; text-decoration: none; border-radius: 9999px; justify-content: center;">
          View ${st.name} Filing Guide →
        </a>
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
    <button class="ls-btn ls-btn--emerald" onclick="window.location.href='${st.link || ('how-to-start-llc-in-' + st.name.toLowerCase().replace(/\\s+/g, '-') + '.html')}'">
      View ${st.name} Filing Guide →
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
  const menu = document.getElementById("primaryNavMenu") || document.querySelector(".nav-menu");

  if (!toggle || !menu) return;

  toggle.addEventListener("click", (e) => {
    e.stopPropagation();
    menu.classList.toggle("active");
    toggle.classList.toggle("active");
  });

  document.addEventListener("click", (e) => {
    if (menu.classList.contains("active") && !menu.contains(e.target) && !toggle.contains(e.target)) {
      menu.classList.remove("active");
      toggle.classList.remove("active");
    }
  });

  const navItems = menu.querySelectorAll(".nav-item");
  navItems.forEach(item => {
    const link = item.querySelector(".nav-link");
    const dropdown = item.querySelector(".dropdown-menu");
    if (dropdown && link) {
      link.addEventListener("click", (e) => {
        if (window.innerWidth <= 1140) {
          const isOpen = item.classList.contains("open");
          navItems.forEach(other => other.classList.remove("open"));
          if (!isOpen) {
            e.preventDefault();
            item.classList.add("open");
          }
        }
      });
    }
  });
}

function updateCost() {
  const calcStateSelect = document.getElementById("calcStateSelect");
  const calcOptAgentToggle = document.getElementById("calcOptAgentToggle");
  const calcOptFormationToggle = document.getElementById("calcOptFormationToggle");
  const calcAgentSelect = document.getElementById("calcAgentSelect");
  const calcExpeditedToggle = document.getElementById("calcExpeditedToggle");
  const calcExpeditedLabel = document.getElementById("calcExpeditedLabel");
  const calcExpeditedSubtext = document.getElementById("calcExpeditedSubtext");

  const tbody = document.getElementById("calcBreakdownTableBody");
  const totalSetupEl = document.getElementById("calcTotalSetup");
  const annualCompEl = document.getElementById("calcAnnualCompliance");

  const code = calcStateSelect ? calcStateSelect.value : "";
  const st = stateData.find(s => s.code === code);

  // Top header elements
  const headerStateEl = document.getElementById("calcCostHeaderState");
  const costBadgeEl = document.getElementById("calcCostBadge");
  const rowStateFeeEl = document.getElementById("calcRowStateFee");
  const rowInitialExtrasEl = document.getElementById("calcRowInitialExtras");
  const rowInitialExtrasLabelEl = document.getElementById("calcRowInitialExtrasLabel");
  const rowInitialExtrasValEl = document.getElementById("calcRowInitialExtrasVal");
  const rowFirstYearTaxEl = document.getElementById("calcRowFirstYearTax");
  const rowFirstYearTaxLabelEl = document.getElementById("calcRowFirstYearTaxLabel");
  const rowFirstYearTaxValEl = document.getElementById("calcRowFirstYearTaxVal");
  const rowExpeditedEl = document.getElementById("calcRowExpedited");
  const rowExpeditedLabelEl = document.getElementById("calcRowExpeditedLabel");
  const rowExpeditedValEl = document.getElementById("calcRowExpeditedVal");
  const rowAnnualReportEl = document.getElementById("calcRowAnnualReport");
  const rowAgentFeeEl = document.getElementById("calcRowAgentFee");
  const rowFormationServiceEl = document.getElementById("calcRowFormationService");
  const rowFranchiseTaxEl = document.getElementById("calcRowFranchiseTax");
  const rowFranchiseTaxValEl = document.getElementById("calcRowFranchiseTaxVal");
  const totalYear1El = document.getElementById("calcTotalYear1");
  const totalYear2El = document.getElementById("calcTotalYear2");
  const stateWarningBoxEl = document.getElementById("calcStateWarningBox");
  const variableNoticeEl = document.getElementById("calcVariableNotice");
  const guideBtnEl = document.getElementById("calcGuideBtn");

  // If no state is selected, display clear placeholder prompt
  if (!st) {
    if (headerStateEl) headerStateEl.textContent = "Select State";
    if (costBadgeEl) {
      costBadgeEl.textContent = "Select State Below";
      costBadgeEl.style.background = "rgba(21, 154, 156, 0.15)";
      costBadgeEl.style.color = "#6EE7B7";
      costBadgeEl.style.border = "1px solid #159A9C";
    }
    if (rowStateFeeEl) rowStateFeeEl.textContent = "—";
    if (rowInitialExtrasEl) rowInitialExtrasEl.style.display = "none";
    if (rowFirstYearTaxEl) rowFirstYearTaxEl.style.display = "none";
    if (rowExpeditedEl) rowExpeditedEl.style.display = "none";
    if (rowAnnualReportEl) rowAnnualReportEl.textContent = "—";
    if (rowAgentFeeEl) rowAgentFeeEl.textContent = "—";
    if (rowFormationServiceEl) rowFormationServiceEl.textContent = "—";
    if (rowFranchiseTaxEl) rowFranchiseTaxEl.style.display = "none";
    if (totalYear1El) totalYear1El.textContent = "Select State";
    if (totalYear2El) totalYear2El.textContent = "Select State";
    if (stateWarningBoxEl) stateWarningBoxEl.style.display = "none";
    if (variableNoticeEl) variableNoticeEl.style.display = "none";
    if (guideBtnEl) {
      guideBtnEl.textContent = "Select State to View Guide →";
      guideBtnEl.href = "start-llc.html";
    }
    if (calcExpeditedToggle) {
      calcExpeditedToggle.checked = false;
      calcExpeditedToggle.disabled = true;
    }
    if (calcExpeditedLabel) {
      calcExpeditedLabel.textContent = "Expedited Processing — Select a state to view options";
      calcExpeditedLabel.style.color = "#94A3B8";
      calcExpeditedLabel.style.cursor = "not-allowed";
    }
    if (calcExpeditedSubtext) {
      calcExpeditedSubtext.textContent = "State-specific fee where available";
    }
    if (tbody) {
      tbody.innerHTML = `
        <tr style="border-bottom: 1px solid rgba(255, 255, 255, 0.08); font-size: 0.85rem;">
          <td colspan="4" style="padding: 1.5rem 0.5rem; text-align: center; color: #94A3B8;">
            Select a state from the dropdown to see your customized government fees and compliance breakdown.
          </td>
        </tr>
      `;
    }
    if (totalSetupEl) {
      totalSetupEl.textContent = "—";
      totalSetupEl.style.fontSize = "1.25rem";
      totalSetupEl.style.color = "#94A3B8";
    }
    if (annualCompEl) {
      annualCompEl.textContent = "—";
      annualCompEl.style.fontSize = "1.25rem";
      annualCompEl.style.color = "#94A3B8";
    }
    return;
  }

  // --- STATE IS SELECTED ---
  const stateName = st.name;
  const stateFee = st.fee;

  // Optional toggles (OFF by default)
  const agentOptChecked = calcOptAgentToggle ? calcOptAgentToggle.checked : false;
  const formationOptChecked = calcOptFormationToggle ? calcOptFormationToggle.checked : false;

  // Legacy select support (for index.html table layout)
  const legacyAgentFee = calcAgentSelect ? (parseInt(calcAgentSelect.value) || 0) : 0;
  const isAgentIncluded = agentOptChecked || legacyAgentFee > 0;

  // 1. FORMATION SERVICE
  const formationServiceCost = formationOptChecked ? 39 : 0;

  // 2. REGISTERED AGENT COST
  let agentYr1Cost = 0;
  let agentYr2Cost = 0;
  let agentYr1Display = "$0 (DIY / Self)";

  if (isAgentIncluded) {
    if (formationOptChecked) {
      agentYr1Cost = 0;
      agentYr2Cost = 125;
      agentYr1Display = "$0 (Free Yr 1 w/ Northwest)";
    } else {
      agentYr1Cost = 125;
      agentYr2Cost = 125;
      agentYr1Display = "$125 (Professional Agent)";
    }
  }

  // 3. RECURRING ANNUAL REPORT FEE & BIENNIAL NORMALIZATION
  let annualReportFeeYr2 = 0;
  let annualReportDisplay = "$0";
  const isBiennial = (st.freq && st.freq.toLowerCase().includes("biennial")) || (st.annual && st.annual.toLowerCase().includes("biennial"));

  if (st.code === "DE") {
    // Delaware has NO SOS annual report fee. Only the $300 Franchise Tax.
    annualReportFeeYr2 = 0;
    annualReportDisplay = "$0 (No state report required)";
  } else if (st.code === "NV") {
    // Nevada has a $150 Annual List fee (separate from $200 Business License)
    annualReportFeeYr2 = 150;
    annualReportDisplay = "$150/yr (Annual List)";
  } else if (st.code === "MT") {
    // Montana: $0 timely fee (Jan 1 – Apr 15 waiver); $35 after April 15
    annualReportFeeYr2 = 0;
    annualReportDisplay = "$0 Timely (waived Jan 1–Apr 15) / $35 late";
  } else if (st.annualFeeNum > 0) {
    if (isBiennial) {
      const annualizedRate = st.annualFeeNum / 2;
      annualReportFeeYr2 = annualizedRate;
      annualReportDisplay = `${st.annual} ($${annualizedRate.toFixed(2)}/yr annualized)`;
    } else {
      annualReportFeeYr2 = st.annualFeeNum;
      annualReportDisplay = `$${st.annualFeeNum}/yr`;
    }
  } else {
    annualReportDisplay = "$0 (No state report fee)";
  }

  // 4. MANDATORY YEAR 1 EXTRAS AND SEPARATE STATE TAXES
  let initialMandatoryExtras = (st.initialExtras || 0);
  let initialMandatoryTax = 0;
  let initialExtrasLabel = st.initialExtrasNote || "Mandatory Initial Filings";
  let separateStateTaxYr2 = 0;
  let stateTaxDisplay = "$0/yr";
  let hasSeparateTax = false;
  let stateWarningText = "";
  let costBadgeText = "Standard Cost";

  if (st.code === "CA") {
    // California: $70 Articles + $20 Statement of Info + $800 Franchise Tax = $890 Year 1
    initialMandatoryExtras = 20;
    initialMandatoryTax = 800;
    initialExtrasLabel = "Initial Statement of Information (due in 90 days)";
    annualReportFeeYr2 = 10; // $20 Biennial = $10.00/yr annualized
    annualReportDisplay = "$20 Biennial ($10.00/yr annualized)";
    separateStateTaxYr2 = 800;
    stateTaxDisplay = "$800/yr (Annual Franchise Tax)";
    hasSeparateTax = true;
    stateWarningText = "⚠️ California: Mandatory first-year state obligations include the $70 filing fee, $20 Initial Statement of Information (due within 90 days), and the $800 Annual Franchise Tax (due by the 15th day of the 4th month after formation). The previous AB 85 first-year tax exemption expired after 2023. Ongoing annual compliance includes the $800 annual franchise tax (due April 15) and $20 Statement of Information every 2 years.";
    costBadgeText = "High Cost State";
  } else if (st.code === "DE") {
    // Delaware: $400 Annual Franchise Tax due June 1. No separate annual report fee.
    separateStateTaxYr2 = 400;
    stateTaxDisplay = "$400/yr (Franchise Tax)";
    hasSeparateTax = true;
    stateWarningText = "⚠️ Delaware: Mandatory $400/yr franchise tax due June 1st (HB 400). No separate Secretary of State annual report fee for LLCs. Great for VC-backed entities, but higher recurring tax for small businesses.";
    costBadgeText = "Above Average";
  } else if (st.code === "NV") {
    // Nevada: $150 Annual List + $200 Business License = $350/yr recurring
    separateStateTaxYr2 = 200;
    stateTaxDisplay = "$200/yr (State Business License)";
    hasSeparateTax = true;
    initialMandatoryExtras = 350; // $150 Initial List + $200 Initial License
    initialExtrasLabel = "Mandatory Initial List ($150) + Business License ($200)";
    stateWarningText = "⚠️ Nevada: Mandatory $150 Annual List + $200 State Business License required annually ($350/yr total ongoing state fees). Both are also required at initial formation ($425 total initial government fees).";
    costBadgeText = "High Ongoing Cost";
  } else if (st.code === "NY") {
    initialMandatoryExtras = 50;
    initialExtrasLabel = "Certificate of Publication State Filing Fee";
    stateWarningText = "⚠️ New York: Section 206 requires publishing a notice in 2 county newspapers for 6 weeks and filing a Certificate of Publication ($50 state fee + ~$300–$1,200 newspaper costs depending on county). Biennial statement is $9 every 2 years ($4.50/yr annualized).";
    costBadgeText = "High Startup Cost";
  } else if (st.code === "NE") {
    initialMandatoryExtras = 25;
    initialExtrasLabel = "Proof of Publication State Filing Fee";
    stateWarningText = "⚠️ Nebraska: Requires publishing notice for 3 consecutive weeks in a legal newspaper near the designated office (~$40–$250 depending on county) and filing Proof of Publication ($25 state fee). Biennial report is $13 online ($6.50/yr annualized) in odd years.";
    costBadgeText = "Standard Cost";
  } else if (st.code === "PA") {
    stateWarningText = "⚠️ Pennsylvania: Under Act 122 of 2022, PA switched from a 10-year decennial report to an annual report ($7 fee) due annually by September 30th.";
    costBadgeText = "Low Ongoing Cost";
  } else if (st.code === "TN") {
    separateStateTaxYr2 = 0;
    stateWarningText = "⚠️ Tennessee: Annual report fee is $300 minimum ($50/member, up to $3,000 max). State franchise/excise tax ($100 minimum) may also apply.";
    costBadgeText = "Above Average";
  } else if (st.code === "TX") {
    stateWarningText = "⚠️ Texas: $300 state formation fee. For the 2026–2027 franchise tax cycle, entities at or below the $2.65M no-tax-due threshold owe $0 franchise tax. Filing the annual Public Information Report (PIR) or Ownership Information Report (OIR) by May 15 is mandatory ($0).";
    costBadgeText = "Zero Recurring Tax";
  } else if (st.code === "WY") {
    costBadgeText = "Top Privacy State";
  } else if (stateFee <= 50) {
    costBadgeText = "Low Cost State";
  } else if (stateFee >= 200) {
    costBadgeText = "Above Average";
  }

  // 5. EXPEDITED PROCESSING OPTION (State-Specific Schedule)
  let expeditedFee = 0;
  if (calcExpeditedToggle) {
    if (st.expediteAvailable) {
      calcExpeditedToggle.disabled = false;
      if (calcExpeditedLabel) {
        calcExpeditedLabel.textContent = `${st.name} State Expedite: +$${st.expediteFee} (${st.expediteTier})`;
        calcExpeditedLabel.style.color = "#F8FAFC";
        calcExpeditedLabel.style.cursor = "pointer";
      }
      if (calcExpeditedSubtext) {
        calcExpeditedSubtext.textContent = `Official SOS turnaround: ${st.expediteTier}`;
      }
      if (calcExpeditedToggle.checked) {
        expeditedFee = st.expediteFee;
      }
    } else {
      calcExpeditedToggle.checked = false;
      calcExpeditedToggle.disabled = true;
      if (calcExpeditedLabel) {
        calcExpeditedLabel.textContent = `Expedited Processing — Not offered by ${st.name} SOS (standard online turnaround)`;
        calcExpeditedLabel.style.color = "#94A3B8";
        calcExpeditedLabel.style.cursor = "not-allowed";
      }
      if (calcExpeditedSubtext) {
        calcExpeditedSubtext.textContent = `Standard online filing turnaround only in ${st.name}`;
      }
      expeditedFee = 0;
    }
  }

  // 6. COMPUTE YEAR 1 AND YEAR 2 TOTALS (Exact sum of visible line items)
  const totalYear1 = stateFee + initialMandatoryExtras + initialMandatoryTax + formationServiceCost + agentYr1Cost + expeditedFee;
  const totalYear2 = annualReportFeeYr2 + separateStateTaxYr2 + agentYr2Cost;

  // --- UPDATE UI ELEMENTS ---
  if (headerStateEl) headerStateEl.textContent = stateName;
  if (costBadgeEl) {
    costBadgeEl.textContent = costBadgeText;
    costBadgeEl.style.background = "rgba(21, 154, 156, 0.2)";
    costBadgeEl.style.color = "#6EE7B7";
    costBadgeEl.style.border = "1px solid #159A9C";
  }
  
  if (rowStateFeeEl) rowStateFeeEl.textContent = `$${stateFee}`;
  
  if (rowInitialExtrasEl && rowInitialExtrasValEl) {
    if (initialMandatoryExtras > 0) {
      rowInitialExtrasEl.style.display = "flex";
      rowInitialExtrasValEl.textContent = `$${initialMandatoryExtras}`;
      if (rowInitialExtrasLabelEl) rowInitialExtrasLabelEl.textContent = `${initialExtrasLabel}:`;
    } else {
      rowInitialExtrasEl.style.display = "none";
    }
  }

  if (rowFirstYearTaxEl && rowFirstYearTaxValEl) {
    if (initialMandatoryTax > 0) {
      rowFirstYearTaxEl.style.display = "flex";
      rowFirstYearTaxValEl.textContent = `$${initialMandatoryTax}`;
      if (rowFirstYearTaxLabelEl) rowFirstYearTaxLabelEl.textContent = `${stateName} 1st-Year Franchise Tax:`;
    } else {
      rowFirstYearTaxEl.style.display = "none";
    }
  }

  if (rowExpeditedEl && rowExpeditedValEl) {
    if (expeditedFee > 0) {
      rowExpeditedEl.style.display = "flex";
      rowExpeditedValEl.textContent = `+$${expeditedFee}`;
      if (rowExpeditedLabelEl) rowExpeditedLabelEl.textContent = `${stateName} Expedite (${st.expediteTier}):`;
    } else {
      rowExpeditedEl.style.display = "none";
    }
  }

  if (rowAnnualReportEl) rowAnnualReportEl.textContent = annualReportDisplay;
  if (rowAgentFeeEl) rowAgentFeeEl.textContent = isAgentIncluded ? agentYr1Display : "$0 (DIY / Self)";
  if (rowFormationServiceEl) rowFormationServiceEl.textContent = formationOptChecked ? "$39" : "$0 (DIY)";

  if (rowFranchiseTaxEl && rowFranchiseTaxValEl) {
    if (hasSeparateTax) {
      rowFranchiseTaxEl.style.display = "flex";
      rowFranchiseTaxValEl.textContent = stateTaxDisplay;
    } else {
      rowFranchiseTaxEl.style.display = "none";
    }
  }

  if (totalYear1El) totalYear1El.textContent = `$${totalYear1.toFixed(2)}`;
  if (totalYear2El) totalYear2El.textContent = `$${totalYear2.toFixed(2)}/yr`;

  if (stateWarningBoxEl) {
    if (stateWarningText) {
      stateWarningBoxEl.style.display = "block";
      stateWarningBoxEl.innerHTML = stateWarningText;
    } else {
      stateWarningBoxEl.style.display = "none";
    }
  }

  // Variable licensing & publication expense notice
  if (variableNoticeEl) {
    variableNoticeEl.style.display = "block";
    if (st.code === "NY") {
      variableNoticeEl.innerHTML = `<strong>ℹ️ Variable County Publication:</strong> Section 206 requires publishing notice in 2 county newspapers for 6 weeks (~$300–$1,200 depending on county) paid directly to local newspapers within 120 days. Not included in state totals.`;
    } else if (st.code === "NE") {
      variableNoticeEl.innerHTML = `<strong>ℹ️ Variable County Publication:</strong> Nebraska requires 3 consecutive weeks notice in a qualifying county newspaper (~$40–$250 depending on county) paid directly to the newspaper. Not included in state totals.`;
    } else if (st.code === "AZ") {
      variableNoticeEl.innerHTML = `<strong>ℹ️ County Publication:</strong> Required in counties other than Maricopa and Pima (~$30–$300) paid directly to qualifying newspapers within 60 days. Not included in state totals.`;
    } else {
      variableNoticeEl.innerHTML = `<strong>ℹ️ Local Licensing &amp; Permits:</strong> City or county general business licenses ($50–$300) vary by municipality and industry and are paid separately to local authorities.`;
    }
  }

  // Fix Guide Button: Link DIRECTLY to specific state guide
  if (guideBtnEl) {
    guideBtnEl.textContent = `View Full ${stateName} LLC Guide →`;
    guideBtnEl.href = `how-to-start-llc-in-${st.slug}.html`;
  }

  // In-Page Breakdown Table (index.html layout)
  if (tbody) {
    let rowsHtml = `
      <tr style="border-bottom: 1px solid rgba(255, 255, 255, 0.08); font-size: 0.85rem;">
        <td style="padding: 0.75rem 0.5rem; color: #FFFFFF; font-weight: 500;">${stateName} Articles Filing Fee</td>
        <td style="padding: 0.75rem 0.5rem; color: #CBD5E1;">Mandatory State</td>
        <td style="padding: 0.75rem 0.5rem; color: #CBD5E1;">One-time (Year 1)</td>
        <td style="padding: 0.75rem 0.5rem; color: #FFFFFF; font-weight: 700; text-align: right;">$${stateFee.toFixed(2)}</td>
      </tr>
    `;

    if (initialMandatoryExtras > 0) {
      rowsHtml += `
        <tr style="border-bottom: 1px solid rgba(255, 255, 255, 0.08); font-size: 0.85rem;">
          <td style="padding: 0.75rem 0.5rem; color: #6EE7B7; font-weight: 500;">${stateName} ${initialExtrasLabel}</td>
          <td style="padding: 0.75rem 0.5rem; color: #CBD5E1;">Mandatory Initial</td>
          <td style="padding: 0.75rem 0.5rem; color: #CBD5E1;">Year 1</td>
          <td style="padding: 0.75rem 0.5rem; color: #6EE7B7; font-weight: 700; text-align: right;">$${initialMandatoryExtras.toFixed(2)}</td>
        </tr>
      `;
    }

    if (initialMandatoryTax > 0) {
      rowsHtml += `
        <tr style="border-bottom: 1px solid rgba(255, 255, 255, 0.08); font-size: 0.85rem;">
          <td style="padding: 0.75rem 0.5rem; color: #FCA5A5; font-weight: 500;">${stateName} Annual Franchise Tax (Year 1)</td>
          <td style="padding: 0.75rem 0.5rem; color: #CBD5E1;">Franchise Tax Board (due 15th day of 4th mo.)</td>
          <td style="padding: 0.75rem 0.5rem; color: #CBD5E1;">Year 1 (AB 85 expired)</td>
          <td style="padding: 0.75rem 0.5rem; color: #FCA5A5; font-weight: 700; text-align: right;">$${initialMandatoryTax.toFixed(2)}</td>
        </tr>
      `;
    }

    rowsHtml += `
      <tr style="border-bottom: 1px solid rgba(255, 255, 255, 0.08); font-size: 0.85rem;">
        <td style="padding: 0.75rem 0.5rem; color: #FFFFFF; font-weight: 500;">Registered Agent Service</td>
        <td style="padding: 0.75rem 0.5rem; color: #CBD5E1;">Privacy / Compliance</td>
        <td style="padding: 0.75rem 0.5rem; color: #CBD5E1;">Year 1</td>
        <td style="padding: 0.75rem 0.5rem; color: #FFFFFF; font-weight: 700; text-align: right;">$${agentYr1Cost.toFixed(2)}</td>
      </tr>
    `;

    if (formationOptChecked) {
      rowsHtml += `
        <tr style="border-bottom: 1px solid rgba(255, 255, 255, 0.08); font-size: 0.85rem;">
          <td style="padding: 0.75rem 0.5rem; color: #FFFFFF; font-weight: 500;">Formation Service (Northwest)</td>
          <td style="padding: 0.75rem 0.5rem; color: #CBD5E1;">Professional Filing</td>
          <td style="padding: 0.75rem 0.5rem; color: #CBD5E1;">One-time</td>
          <td style="padding: 0.75rem 0.5rem; color: #FFFFFF; font-weight: 700; text-align: right;">$39.00</td>
        </tr>
      `;
    }

    if (expeditedFee > 0) {
      rowsHtml += `
        <tr style="border-bottom: 1px solid rgba(255, 255, 255, 0.08); font-size: 0.85rem;">
          <td style="padding: 0.75rem 0.5rem; color: #FFFFFF; font-weight: 500;">${stateName} State Expedite Fee (${st.expediteTier})</td>
          <td style="padding: 0.75rem 0.5rem; color: #CBD5E1;">Government Expedite</td>
          <td style="padding: 0.75rem 0.5rem; color: #CBD5E1;">One-time (Setup)</td>
          <td style="padding: 0.75rem 0.5rem; color: #FFFFFF; font-weight: 700; text-align: right;">+$${expeditedFee.toFixed(2)}</td>
        </tr>
      `;
    }

    rowsHtml += `
      <tr style="border-bottom: 1px solid rgba(255, 255, 255, 0.08); font-size: 0.85rem;">
        <td style="padding: 0.75rem 0.5rem; color: #FFFFFF; font-weight: 500;">${stateName} Annual Report / Recurring State Fee</td>
        <td style="padding: 0.75rem 0.5rem; color: #CBD5E1;">Mandatory State</td>
        <td style="padding: 0.75rem 0.5rem; color: #CBD5E1;">Year 2+ (${st.freq})</td>
        <td style="padding: 0.75rem 0.5rem; color: #FFFFFF; font-weight: 700; text-align: right;">${annualReportDisplay}</td>
      </tr>
    `;

    if (hasSeparateTax) {
      rowsHtml += `
        <tr style="border-bottom: 1px solid rgba(255, 255, 255, 0.08); font-size: 0.85rem;">
          <td style="padding: 0.75rem 0.5rem; color: #FCA5A5; font-weight: 500;">${stateName} State Franchise Tax / License</td>
          <td style="padding: 0.75rem 0.5rem; color: #CBD5E1;">State Tax / Revenue</td>
          <td style="padding: 0.75rem 0.5rem; color: #CBD5E1;">Year 2+ Annual</td>
          <td style="padding: 0.75rem 0.5rem; color: #FCA5A5; font-weight: 700; text-align: right;">$${separateStateTaxYr2.toFixed(2)}</td>
        </tr>
      `;
    }

    tbody.innerHTML = rowsHtml;
  }

  if (totalSetupEl) {
    totalSetupEl.textContent = `$${totalYear1.toFixed(2)}`;
    totalSetupEl.style.fontSize = "1.65rem";
    totalSetupEl.style.color = "#FFFFFF";
    totalSetupEl.style.fontWeight = "800";
  }

  if (annualCompEl) {
    annualCompEl.textContent = `$${totalYear2.toFixed(2)}/yr`;
    annualCompEl.style.fontSize = "1.65rem";
    annualCompEl.style.color = "var(--color-primary)";
    annualCompEl.style.fontWeight = "800";
  }
}

function updateModalCost() {
  const stateSelect = document.getElementById("modalCalcStateSelect");
  const agentSelect = document.getElementById("modalCalcAgentSelect");
  const serviceSelect = document.getElementById("modalCalcServiceSelect");
  const govFeeEl = document.getElementById("modalCalcLiveGovFee");
  const govFeeLineEl = document.getElementById("modalCalcGovFeeLine");
  const totalFeeEl = document.getElementById("modalCalcLiveTotalFee");
  const guideBtn = document.getElementById("modalCalcGuideBtn");

  if (!stateSelect || !totalFeeEl) return;

  const code = stateSelect.value;
  const st = stateData.find(s => s.code === code);

  if (!st) {
    if (govFeeLineEl) {
      govFeeLineEl.textContent = "Required state fees and optional service costs will appear after you select a state.";
    } else if (govFeeEl) {
      govFeeEl.textContent = "—";
    }
    totalFeeEl.textContent = "Select a state to see your estimated costs.";
    totalFeeEl.style.fontSize = "0.95rem";
    totalFeeEl.style.color = "#94A3B8";
    if (guideBtn) {
      guideBtn.disabled = true;
      guideBtn.style.opacity = "0.5";
      guideBtn.style.cursor = "not-allowed";
      guideBtn.textContent = "View State Filing Guide →";
    }
    return;
  }

  let govFee = st.fee;
  if (st.code === "CA") {
    govFee = 70 + 20 + 800; // $70 Articles + $20 Initial Statement + $800 Annual Franchise Tax (Year 1)
  } else if (st.code === "NV") {
    govFee = 75 + 350; // $75 Articles + $150 List + $200 License
  } else if (st.initialExtras) {
    govFee += st.initialExtras;
  }

  const agentFee = agentSelect ? (parseInt(agentSelect.value) || 0) : 0;
  const serviceFee = serviceSelect ? (parseInt(serviceSelect.value) || 0) : 0;

  if (govFeeLineEl) {
    govFeeLineEl.innerHTML = `Required Fee: <b id="modalCalcLiveGovFee" style="color: #FFF;">$${govFee}</b>`;
  } else if (govFeeEl) {
    govFeeEl.textContent = `$${govFee}`;
  }
  totalFeeEl.textContent = `$${govFee + agentFee + serviceFee}`;
  totalFeeEl.style.fontSize = "2.25rem";
  totalFeeEl.style.color = "var(--color-accent)";

  if (guideBtn) {
    guideBtn.disabled = false;
    guideBtn.style.opacity = "1";
    guideBtn.style.cursor = "pointer";
    guideBtn.textContent = `View ${st.name} Filing Guide →`;
  }
}

function onModalCalcGuideClick() {
  const stateSelect = document.getElementById("modalCalcStateSelect");
  const code = stateSelect ? stateSelect.value : "";
  if (!code) return;
  const st = stateData.find(s => s.code === code);
  closeCostCalculatorModal();
  if (st && st.link) {
    window.location.href = st.link;
  } else if (st) {
    const slug = st.name.toLowerCase().replace(/\s+/g, '-');
    window.location.href = `how-to-start-llc-in-${slug}.html`;
  } else {
    window.location.href = "#states-section";
  }
}


function initCostCalculator() {
  const calcStateSelect = document.getElementById("calcStateSelect");
  const calcOptAgentToggle = document.getElementById("calcOptAgentToggle");
  const calcOptFormationToggle = document.getElementById("calcOptFormationToggle");
  const calcAgentSelect = document.getElementById("calcAgentSelect");
  const calcExpeditedToggle = document.getElementById("calcExpeditedToggle");

  [calcStateSelect, calcOptAgentToggle, calcOptFormationToggle, calcAgentSelect, calcExpeditedToggle].forEach(el => {
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

function ensureSearchModalExists() {
  let overlay = document.getElementById("searchModalOverlay");
  if (!overlay) {
    overlay = document.createElement("div");
    overlay.className = "modal-overlay";
    overlay.id = "searchModalOverlay";
    overlay.setAttribute("role", "dialog");
    overlay.setAttribute("aria-modal", "true");
    overlay.setAttribute("aria-labelledby", "searchModalTitle");
    overlay.innerHTML = `
      <div class="modal-card">
        <button class="modal-close" onclick="closeSearchModal()" aria-label="Close search">&times;</button>
        <h3 id="searchModalTitle" style="color: #FFFFFF; margin-bottom: 1rem;">Search 50-State LLC Fees &amp; Guides</h3>
        <input type="text" id="searchInput" placeholder="Type state name (e.g. Wyoming, Texas, Florida)..." class="state-select-box" style="margin-bottom: 1rem;" aria-label="Search state guides" autocomplete="off">
        <div id="searchResults" style="max-height: 250px; overflow-y: auto;"></div>
      </div>
    `;
    document.body.appendChild(overlay);
    initSearch();
  }
  return overlay;
}

function initSearch() {
  const searchInput = document.getElementById("searchInput");
  const overlay = document.getElementById("searchModalOverlay");
  if (!searchInput) return;

  if (searchInput.dataset.searchBound === "true") return;
  searchInput.dataset.searchBound = "true";

  const stateGuideUrls = {
    'Alabama':'how-to-start-llc-in-alabama.html','Alaska':'how-to-start-llc-in-alaska.html',
    'Arizona':'how-to-start-llc-in-arizona.html','Arkansas':'how-to-start-llc-in-arkansas.html',
    'California':'how-to-start-llc-in-california.html','Colorado':'how-to-start-llc-in-colorado.html',
    'Connecticut':'how-to-start-llc-in-connecticut.html','Delaware':'how-to-start-llc-in-delaware.html',
    'Florida':'how-to-start-llc-in-florida.html','Georgia':'how-to-start-llc-in-georgia.html',
    'Hawaii':'how-to-start-llc-in-hawaii.html','Idaho':'how-to-start-llc-in-idaho.html',
    'Illinois':'how-to-start-llc-in-illinois.html','Indiana':'how-to-start-llc-in-indiana.html',
    'Iowa':'how-to-start-llc-in-iowa.html','Kansas':'how-to-start-llc-in-kansas.html',
    'Kentucky':'how-to-start-llc-in-kentucky.html','Louisiana':'how-to-start-llc-in-louisiana.html',
    'Maine':'how-to-start-llc-in-maine.html','Maryland':'how-to-start-llc-in-maryland.html',
    'Massachusetts':'how-to-start-llc-in-massachusetts.html','Michigan':'how-to-start-llc-in-michigan.html',
    'Minnesota':'how-to-start-llc-in-minnesota.html','Mississippi':'how-to-start-llc-in-mississippi.html',
    'Missouri':'how-to-start-llc-in-missouri.html','Montana':'how-to-start-llc-in-montana.html',
    'Nebraska':'how-to-start-llc-in-nebraska.html','Nevada':'how-to-start-llc-in-nevada.html',
    'New Hampshire':'how-to-start-llc-in-new-hampshire.html','New Jersey':'how-to-start-llc-in-new-jersey.html',
    'New Mexico':'how-to-start-llc-in-new-mexico.html','New York':'how-to-start-llc-in-new-york.html',
    'North Carolina':'how-to-start-llc-in-north-carolina.html','North Dakota':'how-to-start-llc-in-north-dakota.html',
    'Ohio':'how-to-start-llc-in-ohio.html','Oklahoma':'how-to-start-llc-in-oklahoma.html',
    'Oregon':'how-to-start-llc-in-oregon.html','Pennsylvania':'how-to-start-llc-in-pennsylvania.html',
    'Rhode Island':'how-to-start-llc-in-rhode-island.html','South Carolina':'how-to-start-llc-in-south-carolina.html',
    'South Dakota':'how-to-start-llc-in-south-dakota.html','Tennessee':'how-to-start-llc-in-tennessee.html',
    'Texas':'how-to-start-llc-in-texas.html','Utah':'how-to-start-llc-in-utah.html',
    'Vermont':'how-to-start-llc-in-vermont.html','Virginia':'how-to-start-llc-in-virginia.html',
    'Washington':'how-to-start-llc-in-washington.html','West Virginia':'how-to-start-llc-in-west-virginia.html',
    'Wisconsin':'how-to-start-llc-in-wisconsin.html','Wyoming':'how-to-start-llc-in-wyoming.html'
  };

  searchInput.addEventListener("input", (e) => {
    const q = e.target.value.toLowerCase().trim();
    const resultsContainer = document.getElementById("searchResults");
    if (!resultsContainer) return;

    if (!q) {
      resultsContainer.innerHTML = "";
      return;
    }

    const matches = (typeof stateData !== "undefined" ? stateData : []).filter(s =>
      s.name.toLowerCase().includes(q) || s.code.toLowerCase().includes(q)
    );

    if (matches.length === 0) {
      resultsContainer.innerHTML = `<div style="color:var(--text-muted); padding:0.5rem;">No matching state guides found.</div>`;
      return;
    }

    resultsContainer.innerHTML = matches.map(s => {
      const guideUrl = (s.slug ? `how-to-start-llc-in-${s.slug}.html` : (stateGuideUrls[s.name] || '#'));
      return `
        <a href="${guideUrl}" class="search-result-row" style="display:block; padding:0.6rem 0.75rem; border-bottom:1px solid rgba(255,255,255,0.07); text-decoration:none; color:inherit; border-radius:6px; transition: background 0.15s ease;">
          <strong style="color:#FFFFFF">${s.name} LLC</strong> &mdash; <span style="color:var(--color-primary)">$${s.fee} State Fee</span> <span style="color:#94A3B8;font-size:0.8rem;">(${s.speed})</span>
        </a>
      `;
    }).join("");
  });

  // Handle Enter key to navigate to first result, and Escape to close
  searchInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      const resultsContainer = document.getElementById("searchResults");
      const firstLink = resultsContainer ? resultsContainer.querySelector("a") : null;
      if (firstLink && firstLink.href) {
        window.location.href = firstLink.href;
      }
    } else if (e.key === "Escape") {
      closeSearchModal();
    }
  });

  // Close modal when clicking backdrop
  if (overlay && !overlay.dataset.backdropBound) {
    overlay.dataset.backdropBound = "true";
    overlay.addEventListener("click", (e) => {
      if (e.target === overlay) {
        closeSearchModal();
      }
    });
  }
}

// Global keyboard listeners: Escape to close modal, Ctrl+K / Cmd+K to open search
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") {
    const searchModal = document.getElementById("searchModalOverlay");
    if (searchModal && searchModal.classList.contains("active")) {
      closeSearchModal();
    }
  } else if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
    const searchBtn = document.querySelector(".search-trigger");
    if (searchBtn || document.getElementById("searchModalOverlay")) {
      e.preventDefault();
      openSearchModal();
    }
  }
});

function openSearchModal() {
  const overlay = ensureSearchModalExists();
  overlay.classList.add("active");
  const input = document.getElementById("searchInput");
  if (input) {
    input.value = "";
    const resultsContainer = document.getElementById("searchResults");
    if (resultsContainer) resultsContainer.innerHTML = "";
    setTimeout(() => input.focus(), 50);
  }
}

function closeSearchModal() {
  const overlay = document.getElementById("searchModalOverlay");
  if (overlay) {
    overlay.classList.remove("active");
  }
}

function openCostCalculatorModal() {
  const modal = document.getElementById("costCalcModalOverlay");
  if (modal) {
    modal.classList.add("active");
    updateModalCost();
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

// --------------------------------------------------------------------------
// LIGHTWEIGHT ASYNCHRONOUS COOKIE CONSENT TOAST (GDPR / CCPA COMPLIANT)
// Non-blocking floating corner message that slides in from the side
// --------------------------------------------------------------------------
function initCookieConsent() {
  if (typeof window === "undefined" || !window.localStorage) return;

  try {
    const consent = localStorage.getItem("llcprimer_cookie_consent");
    if (consent === "accepted") return;
  } catch (e) {
    return;
  }

  // Defer initialization so crawler bots and initial page render are never blocked
  setTimeout(() => {
    if (document.getElementById("cookieConsentToast")) return;

    const toast = document.createElement("div");
    toast.id = "cookieConsentToast";
    toast.setAttribute("role", "region");
    toast.setAttribute("aria-label", "Privacy & Cookie Notice");
    toast.style.cssText = `
      position: fixed;
      bottom: 1.5rem;
      right: 1.5rem;
      max-width: 360px;
      width: calc(100% - 3rem);
      background: #0D2336;
      border: 1.5px solid #159A9C;
      border-radius: 16px;
      color: #F8FAFC;
      padding: 1.25rem 1.35rem;
      z-index: 9999;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.45), 0 0 0 1px rgba(21, 154, 156, 0.25);
      font-family: inherit;
      transform: translateX(130%);
      opacity: 0;
      transition: transform 0.45s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.45s ease;
    `;

    toast.innerHTML = `
      <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.5rem;">
        <div style="display: flex; align-items: center; gap: 0.5rem;">
          <span style="font-size: 1.15rem;">🛡️</span>
          <strong style="color: #FFFFFF; font-size: 0.95rem;">Privacy &amp; Cookies</strong>
        </div>
        <button id="closeCookieConsentBtn" aria-label="Dismiss notice" style="background: none; border: none; color: #94A3B8; font-size: 1.2rem; cursor: pointer; padding: 0.2rem; line-height: 1; transition: color 0.2s ease;">
          ✕
        </button>
      </div>
      <p style="font-size: 0.825rem; color: #CBD5E1; line-height: 1.55; margin: 0 0 1rem 0;">
        We use essential browser mechanisms to ensure security and proper site functionality. We do not use third-party advertising or tracking cookies. Learn more in our
        <a href="privacy-policy.html" style="color: #159A9C; font-weight: 600; text-decoration: underline;">Privacy Policy</a>.
      </p>
      <button id="acceptCookieConsentBtn" style="width: 100%; background: linear-gradient(135deg, #159A9C 0%, #0E7490 100%); color: #FFFFFF; border: none; border-radius: 9999px; padding: 0.65rem 1.25rem; font-size: 0.85rem; font-weight: 700; cursor: pointer; box-shadow: 0 4px 14px rgba(21, 154, 156, 0.35); text-align: center; transition: transform 0.2s ease, box-shadow 0.2s ease;">
        Got It / Accept
      </button>
    `;

    document.body.appendChild(toast);

    // Slide in from side after mount
    requestAnimationFrame(() => {
      setTimeout(() => {
        toast.style.transform = "translateX(0)";
        toast.style.opacity = "1";
      }, 50);
    });

    const dismissToast = () => {
      try {
        localStorage.setItem("llcprimer_cookie_consent", "accepted");
      } catch (e) {}
      toast.style.transform = "translateX(130%)";
      toast.style.opacity = "0";
      setTimeout(() => toast.remove(), 450);
    };

    const acceptBtn = document.getElementById("acceptCookieConsentBtn");
    if (acceptBtn) acceptBtn.addEventListener("click", dismissToast);

    const closeBtn = document.getElementById("closeCookieConsentBtn");
    if (closeBtn) closeBtn.addEventListener("click", dismissToast);
  }, 400);
}
