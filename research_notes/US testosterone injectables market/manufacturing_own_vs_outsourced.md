# US Testosterone Cypionate / Enanthate Vials: Who Makes Them In-House, Who Uses a CMO, and Where the API Comes From

Method note: The core data was pulled straight from primary FDA/NLM systems on 21 Oct 2026:
- the DailyMed SPL API (current labels plus every past label version for each set ID);
- openFDA Drugs@FDA and the NDC Directory;
- the FDA Type II DMF list (3Q2026 Excel);
- eCFR (Title 21 as of 1 Oct 2026).

SPL "establishment" blocks list each registered site with its DUNS number and its operations (API MANUFACTURE, MANUFACTURE, PACK and so on). They are more reliable than the free-text "Manufactured by" line, and they sometimes name the API source. Note that SPL establishment listings are optional and often pared down over time. A site missing from a label does not prove it is not used.

## 1. Labeler by labeler: what the DailyMed label says, and which site makes the product

### Takeaway
There are about 9 distinct finished-product manufacturing sources behind roughly 15 current US testosterone cypionate/enanthate vial labels. The most-used site is Hikma Farmacêutica in Terrugem, Portugal. It makes Hikma's own cypionate and enanthate, and it is also the source behind the Cipla and Padagis cypionate labels sold under Hikma's ANDA 091244.

Only Pfizer (Kalamazoo) lists API plus finished-product manufacture at one site it owns. The other sites are:
- Sun (Halol, India) and Eugia/Aurobindo (Hyderabad, India): own plants.
- American Regent (Shirley, NY; sold by Alvogen): own plant.
- BPI Labs (Largo, FL; also sold by Ajenat): own plant.
- Insud/Chemo's Laboratorios Farmalán (León, Spain; sold by Xiromed and Northstar): a group plant.
- LSNE-León, Spain (a PCI Pharma Services CMO; makes Cipla's own ANDA and Azurity's Azmiro).
- Pii (Cockeysville, MD; a CMO for Wilshire).

Most of the labelers named in the brief do not currently sell testosterone cypionate or enanthate vials in the US: Teva/Actavis, Sandoz, Amneal, Slayback, Somerset, Gland, Lupin, Zydus, Steriscience, Endo/Par and Medisca.

### Cited Findings

**Pfizer / Pharmacia & Upjohn (Depo-Testosterone, ANDA 085635) and Hospira (Pfizer's authorized-generic label, same ANDA)**
- The Depo-Testosterone SPL lists one establishment, Pharmacia & Upjohn Company LLC (DUNS 618054084). That site performs "analysis, API manufacture, label, manufacture, pack" for NDCs 0009-0347 and 0009-0417. The label text says only "Distributed by Pharmacia & Upjohn Co, Division of Pfizer Inc" and has no separate "Manufactured by" line. — [DailyMed setid cfbb53d4-b868-4a28-8436-f9112eb01c39](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=cfbb53d4-b868-4a28-8436-f9112eb01c39); [DailyMed setid 735b5bf3-4464-412c-a072-1bd02f2e5380](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=735b5bf3-4464-412c-a072-1bd02f2e5380)
- Hospira's testosterone cypionate (NDC 0409-6557/6562) uses the same ANDA 085635. Its establishment is the same Pharmacia & Upjohn DUNS 618054084 with the same API-plus-finished-product operations. Every version from 2016 to 2025 reads "Distributed by: Hospira, a Pfizer Company, Lake Forest, IL." — [DailyMed setid 6909596e-4bf7-4e11-8029-b89740a30aec](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=6909596e-4bf7-4e11-8029-b89740a30aec)
- A Pfizer letter dated 13 April 2015 says the "Pfizer Kalamazoo site has investigated the product complaints on Depo-Testosterone regarding crystallization." It describes the 200 mg/mL strength as a "supersaturated sterile solution" in cottonseed oil with benzyl alcohol. — [Pfizer letter](https://cdn.pfizer.com/pfizercom/products/Depo-Testosterone_USI729509-02C.pdf)
- Pfizer, as Pharmacia & Upjohn, holds active Type II DMFs for Testosterone Cypionate USP (DMF 4245, 1981) and Testosterone USP (DMF 3190, 1978). — [FDA DMF list 3Q2026](https://www.fda.gov/media/192069/download?attachment)

**Hikma (cypionate ANDA 091244, holder "Hikma Farmaceutica"; enanthate ANDA 091120)**
- The labels say "Manufactured by: HIKMA FARMACÊUTICA (PORTUGAL), S.A., Estrada do Rio da Mó, 8, 8A e 8B – Fervença – 2705-906 Terrugem SNT, PORTUGAL. Distributed by: Hikma Pharmaceuticals USA Inc., Berkeley Heights, NJ." The establishment is Hikma Farmacêutica (Portugal), DUNS 452742943: analysis, label, manufacture, pack. — [DailyMed setid f60c5520-b336-44a2-95d5-f274939fa595](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=f60c5520-b336-44a2-95d5-f274939fa595); [Novaplus version, setid 5ca67491-4b30-4a47-af0a-be250215d1f0](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=5ca67491-4b30-4a47-af0a-be250215d1f0)
- The enanthate label (NDC 0143-9750, 200 mg/mL, 5 mL multi-dose vial) names the same Portugal site and establishment. It has said so since the first version in 2012, which was distributed by West-Ward. — [DailyMed setid e89d6458-428c-4256-97a3-f1fa851293c1](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=e89d6458-428c-4256-97a3-f1fa851293c1)
- Every version of the cypionate label since version 1 in June 2012 (West-Ward Eatontown) names Hikma Portugal as manufacturer. — [DailyMed SPL history, setid f60c5520](https://dailymed.nlm.nih.gov/dailymed/services/v2/spls/f60c5520-b336-44a2-95d5-f274939fa595/history.json)
- Drugs@FDA lists ANDA 091244 (Hikma Farmaceutica, 200 mg/mL, approved 1 May 2012), ANDA 091120 (enanthate, approved 18 Sep 2012) and a second Hikma cypionate ANDA, 090387 (100 and 200 mg/mL, approved 15 Jul 2010), all with "Prescription" status. — [openFDA Drugs@FDA query](https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22TESTOSTERONE+CYPIONATE%22&limit=100)
- No current NDC Directory listing maps to ANDA 090387. All Hikma cypionate NDCs (0143-9659, 0143-9726, 0143-9005) are listed under ANDA 091244. — [openFDA NDC query](https://api.fda.gov/drug/ndc.json?search=generic_name:%22testosterone+cypionate%22&limit=1000)

**Cipla USA: two different products**
- *(a) Cipla's own ANDA 210362 (approved 19 Jun 2018).*
  - The current label reads "Manufactured by: Cipla Ltd. At M/s LSNE-León SLU, C/Nicostrato Vela s/n, 24009 León, Spain. Manufactured for: Cipla USA, Inc., Warren, NJ."
  - The establishments are LSNE-LEON SLU (DUNS 464038373: analysis, manufacture) and **Aspen Oss B.V. (DUNS 491013870: API manufacture)**.
  - Source: [DailyMed setid 78d55bad-4a5b-4e21-aeb8-a4c6346208be](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=78d55bad-4a5b-4e21-aeb8-a4c6346208be)
- *Manufacturing history for ANDA 210362.*
  - Versions 1 (Jun 2018) to 4 (Aug 2020) read "Manufactured by: Cipla Ltd., Verna Goa, India." Their establishments are "Cipla Ltd.- Goa [manufacture]; Aspen Oss B.V. [api manufacture]."
  - From version 7 (15 Sep 2023) the label switches to LSNE-León. Aspen Oss remains the API source throughout.
  - Source: [DailyMed archived versions, setid 78d55bad](https://dailymed.nlm.nih.gov/dailymed/getFile.cfm?setid=78d55bad-4a5b-4e21-aeb8-a4c6346208be&type=zip&version=1)
- *(b) Cipla distributes Hikma's ANDA 091244 (NDC 69097-802).*
  - The label reads "Manufactured by: HIKMA FARMACÊUTICA (PORTUGAL), S.A. … Terrugem … Distributed by: Cipla USA, Inc."
  - The establishments are Hikma Farmacêutica Portugal (analysis, label, manufacture, pack) and Hikma Pharmaceuticals USA Inc. (DUNS 946499746: label, pack).
  - This has been unchanged since version 1 (Mar 2019).
  - Source: [DailyMed setid b8ac5e07-b7e3-4a60-b0d1-8b1f3ad0c478](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=b8ac5e07-b7e3-4a60-b0d1-8b1f3ad0c478)
- Cipla's FDA approval in June 2018 was reported as an AO-rated generic of Pfizer's Depo-Testosterone at 100 and 200 mg/mL. — [Business Standard, Jun 2018](https://www.business-standard.com/article/news-cm/cipla-receives-final-approval-for-testosterone-cypionate-injection-118062100140_1.html)

**Padagis (formerly Perrigo/Paddock): two products**
- *(a) ANDA 040530 (Padagis is the holder; approved 31 Jan 2005; 200 mg/mL; NDC 0574-0820).* The current label (versions 22–23, May–Jun 2025) says only "Manufactured for Padagis®, Minneapolis, MN." It names no manufacturer and lists no establishment. — [DailyMed setid 4195516a-c8e6-457c-b805-43c9a3ca8b77](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=4195516a-c8e6-457c-b805-43c9a3ca8b77)
- *Manufacturing history for ANDA 040530 (always a CMO):*
  - Version 1 (2006): "Manufactured by: Draxis Pharma Inc., Kirkland, Quebec, Canada. Manufactured for: Paddock Laboratories."
  - Versions 3–16 (2008–2017): "Manufactured by: PharmaForce, Inc., Hilliard, OH."
  - Versions 10 and 19–21 (2015, then 2021–Feb 2024): "Manufactured By: Grand River Aseptic Manufacturing, Grand Rapids, MI 49504."
  - From version 22 (May 2025): manufacturer statement dropped.
  - Source: [DailyMed archived versions, setid 4195516a](https://dailymed.nlm.nih.gov/dailymed/services/v2/spls/4195516a-c8e6-457c-b805-43c9a3ca8b77/history.json)
- *(b) Padagis also distributes Hikma's ANDA 091244 (NDC 0574-0827).* The label reads "Manufactured by: HIKMA FARMACÊUTICA (PORTUGAL), S.A. … Distributed By Padagis, Minneapolis, MN." Earlier versions from 2015 onward read "Distributed by Perrigo." — [DailyMed setid e3e2da65-4b2a-4210-a6ff-cc08c8567381](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=e3e2da65-4b2a-4210-a6ff-cc08c8567381)

**Sun Pharma (ANDA 201720; Sun Pharm Inds Ltd; approved 3 Jun 2013)**
- The label reads "Distributed by: Sun Pharmaceutical Industries, Inc., Cranbury, NJ. Manufactured by: Sun Pharmaceutical Industries Ltd., Halol-Baroda Highway, Halol-389 350, Gujarat, India" (revised 06/2025). The establishment is Sun Pharmaceutical Industries Limited, DUNS 725959238: analysis, manufacture. No API establishment is listed. — [DailyMed setid 3653a602-4551-4e6c-84a7-31861f5dc482](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=3653a602-4551-4e6c-84a7-31861f5dc482)
- Sun's own establishment has been listed since 2013. In 2014 the label was distributed by Caraco Pharmaceutical Laboratories, Detroit, and the Halol site address has appeared since 2015. — [DailyMed SPL history, setid 3653a602](https://dailymed.nlm.nih.gov/dailymed/services/v2/spls/3653a602-4551-4e6c-84a7-31861f5dc482/history.json)
- Conflict: Drugs@FDA (via openFDA) shows both ANDA 201720 strengths as "Discontinued". The NDC Directory still lists Sun NDCs 62756-015/016/017, and the DailyMed label was updated in June 2025. — [openFDA Drugs@FDA](https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22TESTOSTERONE+CYPIONATE%22&limit=100); [openFDA NDC](https://api.fda.gov/drug/ndc.json?search=generic_name:%22testosterone+cypionate%22&limit=1000)
- Sun holds an active Type II DMF for Testosterone USP (DMF 27447, 2013). This covers the base steroid, not the cypionate ester. — [FDA DMF list 3Q2026](https://www.fda.gov/media/192069/download?attachment)

**Eugia US / Aurobindo (cypionate ANDA 211817, approved 20 Oct 2023; enanthate ANDA 212659, approved 28 Feb 2024)**
- The cypionate label reads "Distributed by: Eugia US LLC, E. Windsor, NJ. Manufactured by: Eugia Pharma Specialities Limited, Hyderabad – 500032, India." The establishment is EUGIA Pharma Specialities Limited (DUNS 872201704): analysis, manufacture, pack. — [DailyMed setid f901e2b2-f143-4237-8e95-0d134585490b](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=f901e2b2-f143-4237-8e95-0d134585490b)
- **Version 1 of Eugia's cypionate SPL (effective 24/25 Oct 2023) listed "Symbiotec Pharmalab Private Limited" (ID 677604336) as "API MANUFACTURE"** for NDCs 55150-276/277/278. Version 2 (Mar 2025) and later list only Eugia. — [FDA-hosted SPL v1](https://www.accessdata.fda.gov/spl/data/f901e2b2-f143-4237-8e95-0d134585490b/f901e2b2-f143-4237-8e95-0d134585490b.xml); [DailyMed archived v1](https://dailymed.nlm.nih.gov/dailymed/getFile.cfm?setid=f901e2b2-f143-4237-8e95-0d134585490b&type=zip&version=1)
- The enanthate label (NDC 55150-336, 1,000 mg/5 mL) reads "Manufactured by: Eugia Pharma Specialities Limited, Hyderabad." Even version 1 (Mar 2024) listed only Eugia (analysis, manufacture, pack) and no API establishment. — [DailyMed setid 82a98132-9d5f-40a5-8c4f-f52f2a5de60e](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=82a98132-9d5f-40a5-8c4f-f52f2a5de60e)
- Aurobindo's press release of 23 Oct 2023 says Eugia received final approval "to manufacture and market" testosterone cypionate in 100 mg/mL and 200 mg/mL multi-dose vials and a 200 mg/mL single-dose vial, with launch expected in November 2023. It gives the IQVIA market size as US$226.8 million for the 12 months to August 2023, and calls this the 169th ANDA approval from Eugia Pharma Speciality Group facilities. — [Aurobindo filing to NSE/BSE](https://www.aurobindo.com/api/uploads/corporateannouncements/Fy24_TESTOSTERONE%20CYPRIONATE%20INJ%20APPROVAL.pdf)

**Xiromed (ANDA 215351, approved 13 Apr 2023) and Northstar Rx (McKesson), which sells the same ANDA**
- The Xiromed label reads "Distributed by: Xiromed LLC, Florham Park, NJ … Made in Spain." The registrant is Xiromed Pharma España, S.L., and the manufacturing establishment is **"Laboratorios Farmalan, S.A. (Chemo)" (DUNS 468284866: manufacture)**. — [DailyMed setid cab949ca-fde9-c5a9-5561-21e98d86d078](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=cab949ca-fde9-c5a9-5561-21e98d86d078)
- The Northstar label (NDC 72603-286; marketing started 1 Nov 2024) reads "Manufactured for: Northstar Rx LLC, Memphis, TN. Manufactured by: Laboratorios Farmalan SA 24193." — [DailyMed setid 9ced69c7-cd37-efb6-1bf9-e21c01e56f5b](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=9ced69c7-cd37-efb6-1bf9-e21c01e56f5b)
- Insud Pharma describes its León site, run by Laboratorios Farmalán, as a hormone injectable plant. Its forms include oily solutions, aqueous suspensions and lyophilized products, and one Insud page gives capacity as 15 million vials and 30 million syringes. Xiromed is Insud/Chemo's US generics arm. — [Insud Pharma, Injectable León](https://www.insudpharma.com/en/sede/injectable-leon/); [Insud hormone injectable plant](https://www.insudpharma.com/en/?p=1115); [Drug Store News, Xiromed fulvestrant made at Farmalán León](https://drugstorenews.com/xiromed-launches-generic-faslodex)

**Alvogen (ANDA 207742, held by American Regent; approved 16 Jun 2017; Alvogen NDC start 2 Nov 2022)**
- The label reads "Manufactured by: American Regent, Inc., Shirley, NY 11967. Distributed by: Alvogen, Inc., Morristown, NJ" in every version from v1 (Nov 2022) to v5 (Aug 2026). — [DailyMed setid ed65346b-31bc-f872-516d-78d5ab70229e](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=ed65346b-31bc-f872-516d-78d5ab70229e)
- Drugs@FDA lists the ANDA 207742 sponsor as "AM REGENT". — [openFDA Drugs@FDA](https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22TESTOSTERONE+CYPIONATE%22&limit=100)

**Wilshire Pharmaceuticals (ANDA 206368, approved 24 Apr 2019; 200 mg/mL)**
- The label reads "Manufactured for: Wilshire Pharmaceuticals, Inc., Atlanta, GA. Manufactured by: Pharmaceutics International, Inc. (Pii), Cockeysville, MD 21030." It has been unchanged since 2019. — [DailyMed setid 58ff6e0d-cc0a-4455-8254-d883d26a3b6d](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=58ff6e0d-cc0a-4455-8254-d883d26a3b6d)
- Several repackagers (A-S Medication, Asclemed, Bryant Ranch, NuCare) list NDCs under ANDA 206368. — [openFDA NDC](https://api.fda.gov/drug/ndc.json?search=generic_name:%22testosterone+cypionate%22&limit=1000)

**Azurity (Azmiro, NDA 216318, 505(b)(2), approved 2 Jun 2022; NDC start 4 Oct 2024)**
- The label reads "Manufactured for: Azurity Pharmaceuticals, Inc., Woburn, MA. Manufactured by: LSNE-LEON SLU, Calle Nicostrato Vela … León, 24009, Spain." The version 1 establishment was LSNE-LEON SLU (analysis, manufacture, pack). — [DailyMed setid 235b5625-570d-3fba-e063-6394a90aa2d1](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=235b5625-570d-3fba-e063-6394a90aa2d1)
- Conflict: Drugs@FDA shows Azmiro as "Discontinued", while the NDC Directory still lists NDCs 24338-055/056. — [openFDA Drugs@FDA](https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22TESTOSTERONE+CYPIONATE%22&limit=100)
- LSNE (Lyophilization Services of New England) was sold by Permira to PCI Pharma Services, a deal announced in October 2021. Under Permira, LSNE had entered Europe through an acquisition in León, Spain. — [Permira announcement, 12 Oct 2021](https://www.permira.com/news-and-insights/announcements/permira-agrees-to-sale-of-lsne-to-pci-pharma-services)
- The NDC Directory lists LSNE, Inc. testosterone cypionate 200 mg/mL "DRUG FOR FURTHER PROCESSING" (1 mL vials) under NDC 73301-014 (start 13 Jun 2022) and 73301-015 (start 15 Sep 2023). — [openFDA NDC](https://api.fda.gov/drug/ndc.json?search=generic_name:%22testosterone+cypionate%22&limit=1000)

**BPI Labs (ANDA 219478, approved 3 Sep 2026; NDC start 14 Sep 2026) and Ajenat Pharmaceuticals, which sells the same ANDA**
- The BPI label reads "Manufactured by: BPI Labs, LLC, 12393 Belcher Rd S, Suite 450, Largo, FL 33773 USA" (revised Sep 2026). — [DailyMed setid 375dd035-b792-4cb7-9fe6-bb367b87bdba](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=375dd035-b792-4cb7-9fe6-bb367b87bdba)
- The Ajenat label reads "Distributed by: Ajenat Pharmaceuticals, LLC, Tampa, FL." Its establishment is BPI Labs, LLC (DUNS 078627620: analysis, manufacture). — [DailyMed setid cd57648c-ce53-459a-9f14-3984fc464428](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=cd57648c-ce53-459a-9f14-3984fc464428)
- Fierce Pharma reported BPI as a wholly owned subsidiary of Belcher Pharmaceuticals. It said BPI opened a US$17 million, 20,000 sq ft sterile facility in Largo with robotic aseptic filling and gloveless isolators. — [Fierce Pharma](https://www.fiercepharma.com/manufacturing/south-florida-drugmaker-opens-sterile-drug-facility)

**Antares / Halozyme (Xyosted, testosterone enanthate subcutaneous autoinjector, NDA 209863). This is not a vial, but it is the main branded enanthate product.**
- The current label reads "Manufactured For: Antares Pharma, Inc., Ewing, NJ." Version 16 (Apr 2026) lists **Bayer de Mexico, S.A. de C.V. (DUNS 812807317) as "API manufacture"**. Versions 1–11 (2018–Apr 2025) also carried "Manufactured by: Antares Pharma, Inc., Ewing, NJ." — [DailyMed setid 8a3d204c-be26-49e0-8599-0ac12a272e81](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8a3d204c-be26-49e0-8599-0ac12a272e81)

**Labelers in the brief with no current US testosterone cypionate/enanthate vial product found**
- Drugs@FDA lists 21 testosterone cypionate applications and 14 testosterone enanthate applications. None is held by Sandoz, Amneal, Slayback, Somerset, Gland, Lupin, Zydus, Steriscience or Par.
- All Watson Labs/Watson Pharms ANDAs (now Teva/Actavis) are "Discontinued": cypionate 084401, 086029, 086030 and the combination 085603; enanthate 083667, 085598, 085599 and the combinations 085860/085865.
- Other discontinued applications: Endo's Delatestryl NDA 009165; Rising's ANDA 040652 (cypionate) and 040647 (enanthate); **Caplin One Labs' ANDA 040615 (cypionate)**; Quad Pharms; Savage.
- Source: [openFDA Drugs@FDA, cypionate](https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22TESTOSTERONE+CYPIONATE%22&limit=100); [openFDA Drugs@FDA, enanthate](https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22TESTOSTERONE+ENANTHATE%22&limit=100)
- **Nexus** holds enanthate ANDA 040575 (approved 14 Jun 2006), listed as "Prescription" in Drugs@FDA. However, no current Nexus SPL appears in DailyMed and no Nexus NDC appears in the NDC Directory for testosterone enanthate. — [openFDA Drugs@FDA, enanthate](https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22TESTOSTERONE+ENANTHATE%22&limit=100); [DailyMed SPL search](https://dailymed.nlm.nih.gov/dailymed/services/v2/spls.json?drug_name=testosterone%20enanthate)
- **Medisca** appears in the NDC Directory only as a "BULK INGREDIENT FOR HUMAN PRESCRIPTION COMPOUNDING" listing (NDC 38779-0164, powder). It has no finished-vial listing. PCCA, Letco and AX Pharmaceutical have similar bulk listings. — [openFDA NDC](https://api.fda.gov/drug/ndc.json?search=generic_name:%22testosterone+cypionate%22&limit=1000)
- The only enanthate vials currently on DailyMed are Hikma's (ANDA 091120) and Eugia's (ANDA 212659), plus Xyosted (an autoinjector). — [DailyMed SPL search](https://dailymed.nlm.nih.gov/dailymed/services/v2/spls.json?drug_name=testosterone%20enanthate)

### Inferences
- Hikma Portugal (Terrugem) is effectively the largest single source of generic testosterone cypionate. It supplies three labels: Hikma, Cipla's 69097-802 and Padagis's 0574-0827. It is also one of only two generic enanthate vial sources.
- Cipla and Padagis are partly "marketers of someone else's ANDA" rather than manufacturers. This pattern (a big ANDA holder supplying distributors) could also be open to a new entrant such as Symbiotec, as a supply partner rather than a labeler.
- The LSNE NDC 73301-015 start date (15 Sep 2023) matches exactly the date Cipla's ANDA 210362 label switched to LSNE-León (v7, 15 Sep 2023) and Cipla's NDC 69097-536/537 marketing start (15 Sep 2023). The 73301-014 start (13 Jun 2022) is close to Azmiro's approval (2 Jun 2022). This strongly suggests LSNE-León is the bulk/vial filler for both. This is inference from date matching.
- For Padagis ANDA 040530, the manufacturer statement was removed in 2025 after about 10 years of naming Grand River Aseptic Manufacturing. That points to a CMO switch or a decision to stop disclosing, not a move in-house. The current site is unverified.
- Pfizer's DUNS 618054084 is almost certainly the Kalamazoo, MI complex. The 2015 Pfizer letter ties Kalamazoo to Depo-Testosterone investigations, but no source found here prints the DUNS-to-address mapping directly.

### Gaps
- The current manufacturer for Padagis ANDA 040530 is not disclosed on the 2025 label. It could be confirmed through FDA's Drug Establishments Current Registration Site or the FDA Data Dashboard, which were not reachable/queried here.
- Whether Hikma's second cypionate ANDA (090387) is marketed, and where it would be made, is unknown.
- Whether Nexus's enanthate ANDA 040575 is actively marketed, and by which site, is unknown. No SPL was found.
- Market-share split by labeler (IQVIA units) was not researched in this workstream.
- Sun (ANDA 201720) and Azmiro (NDA 216318) show conflicting status between Drugs@FDA ("Discontinued") and the NDC Directory/DailyMed (active listings). Orange Book patent/exclusivity data and current Orange Book status were not checked directly.

## 2. Who is vertically integrated (own sterile plant and/or own API) vs CMO-dependent

### Takeaway
Pfizer is the only player whose label lists API manufacture plus finished-product manufacture at one site it owns (Pharmacia & Upjohn, Kalamazoo). It also holds its own testosterone cypionate DMF.

The other players fall into three groups:
- **Own sterile plant, but no API establishment of their own listed in the SPL:** Hikma (Portugal), Sun (Halol), Eugia/Aurobindo (Hyderabad; API bought from Symbiotec at launch), American Regent (Shirley, NY), BPI Labs (Largo, FL), and Xiromed through Insud's Farmalán León plant.
- **CMO-dependent:** Cipla's own ANDA (LSNE-León CMO, Aspen Oss API), Padagis (a US/Canadian CMO for about 20 years), Wilshire (Pii), and Azurity (LSNE-León).
- **Pure distributors of another company's ANDA:** Cipla and Padagis for Hikma's ANDA, Alvogen (American Regent), Northstar (Xiromed/Farmalán), Ajenat (BPI) and Hospira (Pfizer).

None of the Indian finished-product players (Sun, Eugia, Cipla) lists its own testosterone ester API in the SPL.

### Cited Findings
- **Pfizer: full integration.** The Pharmacia & Upjohn establishment (DUNS 618054084) is listed for "API manufacture", "manufacture", "label" and "pack" on the same NDCs. Pfizer also holds active DMF 4245 (testosterone cypionate) and DMF 3190 (testosterone). — [DailyMed setid cfbb53d4](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=cfbb53d4-b868-4a28-8436-f9112eb01c39); [FDA DMF list 3Q2026](https://www.fda.gov/media/192069/download?attachment)
- **Hikma: own finished-product plant, API not disclosed.** The Hikma Portugal establishment covers analysis, label, manufacture and pack, with no API establishment in any version from 2012 to 2026. Hikma holds no testosterone DMF in the FDA list. — [DailyMed setid f60c5520](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=f60c5520-b336-44a2-95d5-f274939fa595); [FDA DMF list 3Q2026](https://www.fda.gov/media/192069/download?attachment)
- **Sun: own finished-product plant (Halol).** Sun holds a Testosterone USP DMF (27447) but no cypionate ester DMF. — [DailyMed setid 3653a602](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=3653a602-4551-4e6c-84a7-31861f5dc482); [FDA DMF list 3Q2026](https://www.fda.gov/media/192069/download?attachment)
- **Eugia/Aurobindo: own finished-product plant (Hyderabad), API bought from Symbiotec** (SPL v1, Oct 2023). There is no Aurobindo testosterone DMF in the FDA list. — [FDA-hosted SPL v1](https://www.accessdata.fda.gov/spl/data/f901e2b2-f143-4237-8e95-0d134585490b/f901e2b2-f143-4237-8e95-0d134585490b.xml); [FDA DMF list 3Q2026](https://www.fda.gov/media/192069/download?attachment)
- **Cipla: moved from in-house to a CMO.** ANDA 210362 was made at Cipla Goa (2018–2020 labels) and moved to the LSNE-León CMO by Sep 2023. API came from Aspen Oss B.V. throughout. Cipla's own Testosterone USP DMF 21546 is listed as inactive ("I"). — [DailyMed archived versions, setid 78d55bad](https://dailymed.nlm.nih.gov/dailymed/services/v2/spls/78d55bad-4a5b-4e21-aeb8-a4c6346208be/history.json); [FDA DMF list 3Q2026](https://www.fda.gov/media/192069/download?attachment)
- **Padagis: a CMO throughout** (Draxis → PharmaForce → Grand River Aseptic Manufacturing; currently undisclosed). — [DailyMed SPL history, setid 4195516a](https://dailymed.nlm.nih.gov/dailymed/services/v2/spls/4195516a-c8e6-457c-b805-43c9a3ca8b77/history.json)
- **Wilshire: CMO** (Pharmaceutics International Inc., Cockeysville, MD). — [DailyMed setid 58ff6e0d](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=58ff6e0d-cc0a-4455-8254-d883d26a3b6d)
- **Azurity: CMO** (LSNE-León SLU, Spain). — [DailyMed setid 235b5625](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=235b5625-570d-3fba-e063-6394a90aa2d1)
- **Xiromed: a group plant.** Laboratorios Farmalán (Chemo/Insud group), León. Drug Store News reports that the API for Xiromed's fulvestrant is made at Industriale Chimica, Saronno, Italy (an Insud-linked API source; group ownership not verified here). However, the FDA DMF list has no Industriale Chimica testosterone DMF. — [DailyMed setid cab949ca](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=cab949ca-fde9-c5a9-5561-21e98d86d078); [Drug Store News](https://drugstorenews.com/xiromed-launches-generic-faslodex); [FDA DMF list 3Q2026](https://www.fda.gov/media/192069/download?attachment)
- **American Regent:** ANDA holder and manufacturer (Shirley, NY); **Alvogen** is the distributor. — [DailyMed setid ed65346b](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=ed65346b-31bc-f872-516d-78d5ab70229e)
- **BPI Labs:** ANDA holder and manufacturer (Largo, FL); **Ajenat** is the distributor. — [DailyMed setid cd57648c](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=cd57648c-ce53-459a-9f14-3984fc464428)

### Inferences
- The market is structurally "asset-light" at the labeler level. Roughly half the labels (Cipla x2, Padagis x2, Alvogen, Northstar, Ajenat, Wilshire, Azmiro) depend on someone else's sterile plant. This suggests that controlling a US-approved oil-based sterile fill line is the scarcer asset, not the US label.
- Testosterone cypionate/enanthate vials are oily (cottonseed or sesame oil), benzyl-alcohol-preserved solutions. They need steroid/hormone-segregated sterile filling. Several finished-product sources (Farmalán León "hormone injectable plant"; Hikma Portugal) are dedicated or hormone-capable facilities. The hormone-segregation point is inferred from the Insud plant description and general GMP practice.
- Apart from Pfizer, API integration is absent among finished-product players. That is supportive for merchant API makers like Symbiotec, and also a sign that a Symbiotec forward-integration move would make it the second fully integrated US player after Pfizer, assuming its Mhow sterile site gets FDA approval.
- Cipla's move from Goa to a Spanish CMO suggests that an Indian sterile site was not the preferred long-term source for this product. Possible reasons include site compliance, cost, and DEA import logistics. The cause is not disclosed.

### Gaps
- API sources for Hikma, Sun, Padagis, American Regent, Pii/Wilshire, Xiromed/Farmalán, BPI Labs and Eugia's enanthate are not disclosed in current SPLs. They could only be found from ANDA DMF reference letters (not public) or trade data.
- Whether Eugia still sources cypionate API from Symbiotec after the March 2025 SPL change (which dropped the API establishment) is unknown.

## 3. Testosterone cypionate / enanthate API DMF holders, and which API feeds which finished product

### Takeaway
The FDA 3Q2026 DMF list shows **9 active Type II DMFs for testosterone cypionate**:
- Aspen Oss
- Pfizer
- Trifarma
- Symbiotec
- Zhejiang Xianju
- Curia Spain
- Steroid S.p.A.
- Farmabios (new in 2025)
- Hubei Zhuxi Humanwell (new in 2025)

It shows **4 active Type II DMFs for testosterone enanthate**:
- Bayer AG
- Aspen Oss
- Symbiotec
- Steroid S.p.A.

Symbiotec is the only Indian holder for either ester. The disclosed API-to-finished-product links are Pfizer → itself, Aspen Oss → Cipla (ANDA 210362), Symbiotec → Eugia (ANDA 211817, at launch) and Bayer de Mexico → Xyosted.

### Cited Findings
- **Testosterone cypionate, active ("A") Type II DMFs** — [FDA DMF list 3Q2026 Excel](https://www.fda.gov/media/192069/download?attachment) (landing page: [FDA List of DMFs](https://www.fda.gov/drugs/drug-master-files-dmfs/list-drug-master-files-dmfs)):

| DMF | Holder | Submitted |
|---|---|---|
| 3857 | Aspen Oss BV | 21 May 1980 |
| 4245 | Pharmacia and Upjohn Co LLC (Pfizer) | 13 Aug 1981 |
| 21091 | Trifarma SpA | 21 Nov 2007 |
| 29023 | **Symbiotec Pharmalab Ltd** | 20 Jan 2015 |
| 30741 | Zhejiang Xianju Pharmaceutical Co Ltd | 11 Jul 2016 |
| 31860 | Curia Spain SAU | 18 Aug 2017 |
| 32932 | Steroid SpA | 29 Jun 2018 |
| 42305 | Farmabios SpA | 22 Jul 2025 |
| 42497 | Hubei Zhuxi Humanwell Pharmaceutical Co Ltd | 22 Sep 2025 |

  Inactive ("I") cypionate DMFs: Diosynth BV (2994), Roussel Uclaf (3220) and FIS Fabbrica Italiana Sintetici (33411, 2018).

- **Testosterone enanthate, active Type II DMFs** — [FDA DMF list 3Q2026 Excel](https://www.fda.gov/media/192069/download?attachment):

| DMF | Holder | Submitted |
|---|---|---|
| 3391 | Bayer AG | 31 Oct 1978 |
| 3877 | Aspen Oss BV | 25 Jun 1980 |
| 26166 | **Symbiotec Pharmalab Ltd** | 19 Jun 2012 |
| 32765 | Steroid SpA | 27 Apr 2018 |

  Inactive enanthate DMFs: Roussel Uclaf (3781), Pharmacia and Upjohn (4239), Biovet (23920) and Zhejiang Xianju (27431).

- **Related active testosterone-family DMFs** (useful as markers of backward-integration capability) — [FDA DMF list 3Q2026 Excel](https://www.fda.gov/media/192069/download?attachment):
  - Testosterone USP/base: Pfizer (3190), Aspen Oss (11826), Bayer AG (15077), Dr. Reddy's (23671), Sun Pharma (27447), Symbiotec (29869, micronized), Lupin (30377), Curia Spain (32817, micronized), Hubei Goto Biotechnology (33118), Hubei Zhuxi Humanwell (37074), Sightlead Pharmaceutical (44479, Aug 2026), Zhejiang Xianju (44681, Sep 2026).
  - Symbiotec also holds testosterone undecanoate (25534) and testosterone propionate (25535).
- **US NDC Directory "BULK INGREDIENT" listings for testosterone cypionate** (entities registered to ship API into the US):
  - Symbiotec Pharmalab Limited (NDC 22552-0010), Aspen Oss B.V., Curia Spain S.A.U., F.I.S., Farmabios, Hubei Zhuxi Humanwell, Jiangsu Jiaerke Pharmaceuticals, Steroid S.p.A., Trifarma, Zhejiang Xianju, Pharmacia and Upjohn (0009-0027), ASG Biochem, Shakti Lifescience, Brichem Sciences and SCH Global Services.
  - For enanthate: Symbiotec (22552-0014), Aspen Oss, Bayer de Mexico, F.I.S., Jiangsu Jiaerke, Steroid S.p.A., ASG Biochem, Shakti, Brichem and SCH Global.
  - Source: [openFDA NDC, cypionate](https://api.fda.gov/drug/ndc.json?search=generic_name:%22testosterone+cypionate%22&limit=1000); [openFDA NDC, enanthate](https://api.fda.gov/drug/ndc.json?search=generic_name:%22testosterone+enanthate%22&limit=1000)
- **Disclosed API-to-finished-product links (SPL establishment "API MANUFACTURE"):**
  - Pfizer/Pharmacia & Upjohn → Depo-Testosterone and Hospira. — [DailyMed cfbb53d4](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=cfbb53d4-b868-4a28-8436-f9112eb01c39)
  - Aspen Oss B.V. → Cipla ANDA 210362, both when made at Cipla Goa (2018–2020) and when made at LSNE-León (2023–2025). — [DailyMed 78d55bad](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=78d55bad-4a5b-4e21-aeb8-a4c6346208be)
  - Symbiotec Pharmalab Private Limited → Eugia ANDA 211817 (SPL v1, Oct 2023). — [FDA-hosted SPL v1](https://www.accessdata.fda.gov/spl/data/f901e2b2-f143-4237-8e95-0d134585490b/f901e2b2-f143-4237-8e95-0d134585490b.xml)
  - Bayer de Mexico S.A. de C.V. → Xyosted (enanthate). — [DailyMed 8a3d204c](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8a3d204c-be26-49e0-8599-0ac12a272e81)
- A secondary source (PharmaCompass) lists Symbiotec among testosterone cypionate API manufacturers. — [PharmaCompass, Testosterone Cypionate API](https://www.pharmacompass.com/listed-active-pharmaceutical-ingredients/testosterone-cypionate)

### Inferences
- European suppliers (Aspen Oss, Steroid, Trifarma, Farmabios, Curia Spain) and Bayer dominate the DMF base historically. The Chinese cypionate DMFs (Zhejiang Xianju 2016; Hubei Zhuxi Humanwell 2025) and the new 2025–2026 testosterone base DMFs (Sightlead, Xianju) point to rising Chinese competition at the API level, which Symbiotec will face both as a merchant supplier and in any finished-product cost race.
- Symbiotec holds active DMFs for both esters and supplied Eugia at launch. It therefore already has a disclosed foothold in at least one US generic (Eugia, approved 2023). Losing Eugia, or Eugia dual-sourcing (the API establishment disappeared from the Mar 2025 SPL), would be a relevant monitorable. The SPL change alone does not prove a supplier switch.
- DMF status "A" only means active. It does not mean the DMF has passed FDA's GDUFA completeness assessment or is "available for reference"; that is a separate FDA list that was not checked here.

### Gaps
- API sources for Hikma, Sun, Padagis, American Regent, Wilshire/Pii, Xiromed, BPI and Eugia-enanthate are not disclosed in SPLs.
- The FDA "DMFs available for reference" (completeness-assessed) list was not checked for these DMFs.
- No trade (import/export) data was reviewed to quantify Symbiotec's US testosterone API share.

## 4. DEA requirements for a US marketer/importer of testosterone vials, and whether importing finished vials made in India is a barrier

### Takeaway
Testosterone and its esters are Schedule III non-narcotic anabolic steroids (DEA code 4000). Importing finished vials made in India requires a DEA-registered US importer, plus a **DEA Form 236 import declaration for every shipment**, filed online at least 15 calendar days before customs release. An import permit is not required.

Testosterone is **not** subject to DEA production/procurement quotas, which apply only to Schedule I/II. It does not trigger the Federal Register notice-and-hearing process for importer registration (Schedule I/II only), and it is not ARCOS-reportable.

The DEA layer is therefore an administrative and logistics hurdle, not a quota or licensing moat. The main entry barriers remain FDA (an approved ANDA and an approved sterile site) and commercial factors.

### Cited Findings
- Anabolic steroids, "including its salts, esters and ethers", are Schedule III under 21 CFR 1308.13(f), with Administration Controlled Substances Code Number 4000. — [eCFR 21 CFR 1308.13](https://www.ecfr.gov/current/title-21/chapter-II/part-1308/section-1308.13)
- 21 CFR 1312.11(b): no one may import any non-narcotic Schedule III–V substance (other than those requiring permits) "unless and until such person is properly registered under the Act … and has filed an import declaration … in accordance with § 1312.18." Under 1312.11(c), "A separate permit or declaration is required for each shipment." — [eCFR 21 CFR 1312.11](https://www.ecfr.gov/current/title-21/chapter-II/part-1312/section-1312.11)
- 21 CFR 1312.18 sets out what the importer must do:
  - File DEA Form 236 "through the DEA Diversion Control Division secure network application not later than 15 calendar days prior to the anticipated date of release by a customs officer."
  - The declaration "is not deemed filed, and therefore is not valid, until the Administration has issued a transaction identification number."
  - The final destination "must be the importer's registered location."
  - The form must include the drug's NDC number, the DEA Controlled Substances Code Number, package counts, and the foreign consignor's name, address and any licence numbers.
  - Source: [eCFR 21 CFR 1312.18](https://www.ecfr.gov/current/title-21/chapter-II/part-1312/section-1312.18)
- 21 CFR 1312.30 lists the only Schedule III–V non-narcotics designated as needing an import/export *permit*: dronabinol in sesame oil, marijuana/marijuana extract and naturally derived delta-9-THC in FDA-approved products. Testosterone and anabolic steroids are not listed, so a declaration (not a permit) applies. — [eCFR 21 CFR 1312.30](https://www.ecfr.gov/current/title-21/chapter-II/part-1312/section-1312.30)
- 21 CFR 1301.34 (Federal Register notice of an importer application, comment from bulk manufacturers, and a possible hearing) applies only to importers of "a controlled substance listed in Schedule I or II." — [eCFR 21 CFR 1301.34](https://www.ecfr.gov/current/title-21/chapter-II/part-1301/section-1301.34)
- 21 CFR 1303.11 aggregate production quotas cover "each basic class of controlled substance listed in Schedule I or II". No quota mechanism applies to Schedule III testosterone. — [eCFR 21 CFR 1303.11](https://www.ecfr.gov/current/title-21/chapter-II/part-1303/section-1303.11)
- 21 CFR 1304.33(c) ARCOS reporting covers "Schedules I, II, narcotic controlled substances in Schedule III, and gamma-hydroxybutyric acid drug product[s]". Non-narcotic Schedule III testosterone is therefore not ARCOS-reportable. — [eCFR 21 CFR 1304.33](https://www.ecfr.gov/current/title-21/chapter-II/part-1304/section-1304.33)
- All current testosterone cypionate/enanthate vial labels carry the "CIII" designation, for example the Eugia, Hikma and BPI labels. — [DailyMed f901e2b2](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=f901e2b2-f143-4237-8e95-0d134585490b); [DailyMed 375dd035](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=375dd035-b792-4cb7-9fe6-bb367b87bdba)

### Inferences
- **Indian-made finished vials have a working precedent.** Sun (Halol) and Eugia (Hyderabad) already import Schedule III testosterone vials into the US. The DEA pathway for Indian-made vials is therefore proven and routine, not a novel barrier.
- **What a new entrant like Symbiotec would need on the DEA side:**
  - a DEA importer registration, either its own US subsidiary or a partner/3PL that is the importer of record;
  - a DEA distributor registration at the US warehouse;
  - DEA security, recordkeeping and biennial-inventory compliance;
  - a per-shipment Form 236 lead time of at least 15 days, which adds working capital and inventory buffer.

  The registration requirement comes from 1312.11. The distributor, security and recordkeeping details are general DEA practice under 21 CFR 1301 and 1304 and were not individually verified here.
- **Practical friction for importers.** Per-shipment declarations need the product's NDC number. The labeler's NDC and FDA listing must therefore be in place before the first import.
- **No quota, so no supply cap.** Unlike Schedule II opioids or stimulants, a new testosterone entrant cannot be quota-limited by DEA. Volumes are constrained only by commercial demand and FDA site status.
- **Existing players already carry this cost.** Partnering with a labeler that already has DEA registrations (for example Cipla, Padagis, Northstar, Alvogen or Ajenat, which already distribute third-party testosterone ANDAs) would shortcut the DEA set-up for a new manufacturer.
- **Likely no export authorization from India.** Testosterone is controlled in the US by domestic law (the Anabolic Steroid Control Act), not under the UN 1971 Psychotropic Convention schedules. So an INCB-style export authorization from India is probably not needed. This is unverified in this workstream.

### Gaps
- DEA registration processing times, and any DEA pre-registration inspection practice for new Schedule III importers, were not verified.
- Whether India's CDSCO or narcotics authorities require any export NOC for anabolic steroid finished products was not verified.
- DEA Diversion guidance pages on Form 236 (beyond the CFR text) were not reviewed.

## 5. Recent ANDA/NDA approvals (2022–2026) for testosterone cypionate/enanthate, and who makes them

### Takeaway
Since 2022, FDA has approved:
- Azurity's Azmiro NDA (Jun 2022; made at LSNE-León, Spain);
- Xiromed's ANDA (Apr 2023; Farmalán/Chemo, León, Spain);
- Eugia/Aurobindo's cypionate ANDA (Oct 2023) and enanthate ANDA (Feb 2024), both made in-house in Hyderabad, India;
- BPI Labs' cypionate ANDA (Sep 2026; made in-house in Largo, FL).

Alvogen (Nov 2022, American Regent ANDA) and Northstar (Nov 2024, Xiromed ANDA) launched as new distributor labels.

Eugia is the only Indian company with a 2022–2026 approval. No Chinese company holds a finished-product approval. No approvals were found for Gland, Caplin, MSN, Alembic, Zydus or Lupin.

### Cited Findings
- Drugs@FDA original approval dates — [openFDA Drugs@FDA, cypionate](https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22TESTOSTERONE+CYPIONATE%22&limit=100); [openFDA Drugs@FDA, enanthate](https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22TESTOSTERONE+ENANTHATE%22&limit=100):

| Application | Holder | Approved | Product |
|---|---|---|---|
| NDA 216318 | Azurity (Azmiro) | 2 Jun 2022 | — |
| ANDA 215351 | Xiromed | 13 Apr 2023 | 100 and 200 mg/mL |
| ANDA 211817 | Eugia Pharma | 20 Oct 2023 | 100 and 200 mg/mL |
| ANDA 212659 | Eugia Pharma | 28 Feb 2024 | enanthate 200 mg/mL |
| ANDA 219478 | BPI Labs | 3 Sep 2026 | 200 mg/mL |

  Earlier approvals still marketed: Cipla ANDA 210362 (19 Jun 2018), Wilshire ANDA 206368 (24 Apr 2019), American Regent ANDA 207742 (16 Jun 2017).

- Manufacturers of these products, per their labels:
  - Azmiro: LSNE-León, Spain. — [DailyMed 235b5625](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=235b5625-570d-3fba-e063-6394a90aa2d1)
  - Xiromed: Laboratorios Farmalán (Chemo), Spain. — [DailyMed cab949ca](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=cab949ca-fde9-c5a9-5561-21e98d86d078)
  - Eugia: Eugia Pharma Specialities, Hyderabad. — [DailyMed f901e2b2](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=f901e2b2-f143-4237-8e95-0d134585490b); [DailyMed 82a98132](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=82a98132-9d5f-40a5-8c4f-f52f2a5de60e)
  - BPI: BPI Labs, Largo, FL. — [DailyMed 375dd035](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=375dd035-b792-4cb7-9fe6-bb367b87bdba)
- New distributor-label launches, by NDC marketing start date:
  - Alvogen (American Regent-made): 2 Nov 2022.
  - Cipla's LSNE-made ANDA 210362 NDCs: 15 Sep 2023.
  - Eugia: 20 Oct 2023.
  - Northstar (Xiromed/Farmalán-made): 1 Nov 2024.
  - Azmiro: 4 Oct 2024.
  - BPI and Ajenat: 14 Sep 2026.
  - Source: [openFDA NDC](https://api.fda.gov/drug/ndc.json?search=generic_name:%22testosterone+cypionate%22&limit=1000)
- Aurobindo announced the Eugia approval on 23 Oct 2023, with launch expected in November 2023 and an IQVIA market size of US$226.8 million. — [Aurobindo/NSE filing](https://nsearchives.nseindia.com/corporate/AUROPHARMA_23102023125152_LtrToSEsPREugiaUSFDATestosteroneCypionateInjection23102023.pdf); [Business Standard](https://www.business-standard.com/companies/news/aurobindo-pharma-arm-receives-fda-nod-for-testosterone-cypionate-injection-123102300453_1.html)
- A web search for 2025–2026 Indian testosterone cypionate ANDA approvals found none. This is consistent with Drugs@FDA. — [Business Standard (Aurobindo 2023)](https://www.business-standard.com/companies/news/aurobindo-pharma-arm-receives-fda-nod-for-testosterone-cypionate-injection-123102300453_1.html)
- Caplin One Labs (a Caplin Steriles affiliate) holds testosterone cypionate ANDA 040615 (originally approved 10 Aug 2006, 100 and 200 mg/mL). Both strengths are "Discontinued". — [openFDA Drugs@FDA](https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22TESTOSTERONE+CYPIONATE%22&limit=100)

### Inferences
- The 2022–2026 approval flow has been slow: about one new finished-product source per year. It is dominated by European (Spanish) and own-plant manufacturers, not by Indian CMOs such as Gland or Steriscience. Testosterone cypionate is not yet a crowded Indian injectable generic, which suits a new Indian entrant.
- Caplin holds a discontinued ANDA 040615, which could in principle be revived through a supplement and site transfer. That is a possible fast route for Caplin. This is speculative; there is no evidence of plans.
- BPI's September 2026 approval adds a US-made source at the moment Symbiotec would be planning entry. It increases competitive intensity, but that is unquantified.

### Gaps
- Tentative approvals and pending ANDAs (for example from Gland, MSN, Alembic, Zydus or Caplin) are not visible in openFDA. They were not confirmed or ruled out.
- openFDA Drugs@FDA can lag by a few weeks, so approvals in late September–October 2026 might be missing.

## 6. Has Symbiotec disclosed plans for finished dosage, injectables, US testosterone vials or partnerships?

### Takeaway
Public summaries of Symbiotec's Red Herring Prospectus (RHP, dated 18 Aug 2026; IPO open 24–27 Aug 2026) disclose a new **complex-injectables vertical**. It contributed 3.80% of FY26 revenue from the newly commissioned Mhow facility, which has capacity for 20 million double-chamber vials a year. The Mhow and Ujjain sites are still at pilot scale with regulatory approvals "in process."

None of the sources reviewed mentions a US ANDA or US testosterone vial plan, or a named finished-product partner. The only public evidence of Symbiotec's role in US testosterone vials is as the **API supplier** listed on Eugia's 2023 SPL.

### Cited Findings
- Symbiotec filed a DRHP with SEBI for an IPO of up to ₹2,180 crore. — [BioSpectrum India](https://www.biospectrumindia.com/news/16/27105/symbiotec-pharmalab-files-drhp-with-sebi-for-ipo-aggregating-upto-rs-2180-cr.html); [IPO Central](https://ipocentral.in/symbiotec-pharmalab-ipo-drhp-filing/)
- **RHP terms.** Dated 18 Aug 2026. Issue open 24 Aug and close 27 Aug 2026, price band ₹938–988. Total size ₹1,757 crore, made up of a ₹150 crore fresh issue and a ₹1,607 crore offer for sale. Listing was tentatively set for 1 Sep 2026 on NSE/BSE. — [Bajaj Broking](https://www.bajajbroking.in/blog/symbiotec-pharmalab-ipo); [Cofacto Substack](https://cofacto.substack.com/p/symbiotec-pharmalab-ipo-what-investors)
- **Complex injectables.** They were 3.80% of FY2026 revenue from operations, described as "its first year of commercial contribution, following the commissioning of the Mhow Facility." Mhow can produce up to 20 million double-chamber vials a year. The Mhow and Ujjain facilities "remain at pilot-scale operation as of the RHP filing date" and their regulatory approvals "are still in process." — [Bajaj Broking](https://www.bajajbroking.in/blog/symbiotec-pharmalab-ipo)
- **Concentration and scale:**
  - API sales were 96.07% of FY26 revenue (99.10% in FY25; 100% in FY24).
  - The top 5 APIs were 62.27% of FY26 revenue.
  - Testosterone has a 76.4% global volume market share in FY26, per the company-commissioned Frost & Sullivan report.
  - Symbiotec holds 43 US DMFs and 23 CEPs as of 31 Mar 2026.
  - International markets were 67.04% of FY26 revenue.
  - CDMO services were 0.13% of revenue.
  - Sources: [Bajaj Broking](https://www.bajajbroking.in/blog/symbiotec-pharmalab-ipo); [Cofacto Substack](https://cofacto.substack.com/p/symbiotec-pharmalab-ipo-what-investors)
- Development pipelines cited in the RHP summaries are fermentation, GLP-1, insulin and conjugated estrogens. US testosterone finished products are not mentioned. — [Cofacto Substack](https://cofacto.substack.com/p/symbiotec-pharmalab-ipo-what-investors)
- Symbiotec Pharmalab Private Limited was listed as the API manufacturer on Eugia's testosterone cypionate SPL v1 (Oct 2023). — [FDA-hosted SPL v1](https://www.accessdata.fda.gov/spl/data/f901e2b2-f143-4237-8e95-0d134585490b/f901e2b2-f143-4237-8e95-0d134585490b.xml)
- No finished-product (non-bulk) testosterone NDC or ANDA held by Symbiotec appears in the NDC Directory or Drugs@FDA. Symbiotec appears only as a bulk ingredient labeler (NDC 22552-0010 cypionate; 22552-0014 enanthate). — [openFDA NDC](https://api.fda.gov/drug/ndc.json?search=generic_name:%22testosterone+cypionate%22&limit=1000); [openFDA Drugs@FDA](https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22TESTOSTERONE+CYPIONATE%22&limit=100)

### Inferences
- **Mhow is not yet a US-approved site.** It is built around double-chamber vials (a complex-injectables format) and remains pilot-scale. Any Symbiotec US testosterone vial ANDA would need either a US-approved filling line at Mhow, which would take years given the ANDA plus pre-approval inspection, or a partner/CMO route.
- **Precedent for the partner/CMO route.** Cipla uses LSNE-León, Wilshire uses Pii, and Padagis uses US CMOs. Distributor models (Northstar/Xiromed, Alvogen/American Regent, Ajenat/BPI) show partner economics are viable.
- **Symbiotec's edge would be API cost and control.** Pfizer is today the only API-integrated player. A Symbiotec-made vial with captive API would be the second, but Symbiotec would be competing against its own API customers, Eugia and possibly others. That channel-conflict risk is relevant.
- **Size of the opportunity.** With testosterone at 76.4% global volume share (company-commissioned data), Symbiotec likely already supplies API to several US finished-product makers. The only such link verified here is Eugia.

### Gaps
- The DRHP/RHP primary text was not reviewed. Only secondary summaries were, and those contain some internal inconsistencies, for example FY24 revenue given as ₹716.25 crore vs ₹723.33 crore. Any disclosure about US finished-product plans, named customers or testosterone revenue share needs checking against the RHP itself on SEBI/NSE/BSE.
- No press release, interview or exchange filing was found that confirms Symbiotec's stated intention to enter the US testosterone vials market, as the brief describes. It may be in management commentary not indexed.
- Post-listing developments (September–October 2026), such as the listing outcome or analyst-call commentary on US injectables, were not found.
