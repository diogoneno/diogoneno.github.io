---
layout: page
title: Secure Software Development
description: January 2025
nav-menu: true
---

<section aria-labelledby="ssd-title" class="prose max-w-none">
  <h2 id="ssd-title">Welcome to Secure Software Development module</h2>

  <p>
    This module addressed secure software development, covering management 
    practices, UML modeling, secure coding, automated testing, and evolving trends. 
    I treated security as an engineering objective, applying standards such as NIST 
    SSDF, ISO/IEC&nbsp;27034, and OWASP SAMM to produce actionable artefacts and 
    team workflows (NIST, 2022; ISO/IEC, 2011; OWASP SAMM, 2020–). Personal lens: 
    leveraging my experience as a Site Reliability Engineer and former full-stack 
    team lead, I targeted decisions that tangibly minimize attack surface—clear 
    ownership, secure defaults, and testable proof that controls function in 
    reality.
  </p>

  <h3>Learning Outcomes</h3>
  <p>I will be able to:</p>
  <ul>
    <li>Integrate security throughout agile SDLC activities and compare trade-
offs with traditional approaches, mapping work to SSDF and SAMM (NIST, 2022; 
OWASP SAMM, 2020–).</li>
    <li>Model systems with UML to communicate architecture, data flows, and 
trust boundaries during design and change (OMG, 2017).</li>
    <li>Apply secure coding and language best practices; use linters and SAST 
(e.g., Bandit) to detect common issues early (PyCQA, n.d.).</li>
    <li>Plan and automate security testing aligned to risks (e.g., OWASP Top 10)
 and organisational standards (e.g., ISO/IEC&nbsp;27034) (OWASP, 2021; ISO/IEC, 
2011).</li>
    <li>Present succinct executive-level summaries of security posture and next 
steps tied to measurable outcomes (NIST, 2022).</li>
  </ul>

  <h3>Artefacts and Feedback</h3>

  <h4>Unit&nbsp;1 — Foundations of Secure SDLC</h4>
  <p>
    I compared waterfall and agile methodologies for security alignment, then 
    implemented an agile approach that integrates security stories and acceptance 
    criteria into sprints, mapped to SSDF tasks and SAMM maturity activities (NIST, 
    2022; OWASP SAMM, 2020–).
  </p>

  <h4>Unit&nbsp;2 — UML Modelling to Support Secure Planning</h4>
  <p>
    I decomposed activities into tasks and used UML to illustrate deployments 
    and system interactions. Early modeling pinpointed trust boundaries, RBAC 
    requirements, and audit needs, improving stakeholder communication (OMG, 
    2017).
  </p>

  <h4>Unit&nbsp;3 — Programming Languages &amp; Secure Practices</h4>
  <p>
    We examined language paradigms and mitigation strategies using Python 
    examples. I combined secure coding guidelines with automated checks so issues 
    such as hard-coded secrets and unsafe calls were detected in CI (PyCQA, n.d.).
  </p>

  <h4>Unit&nbsp;4 — Testing for Security</h4>
  <p>
    I developed a security-focused test plan. I aligned techniques such as unit,
    integration, dependency scanning, and fuzzing to priority risks. I automated 
    key elements using Python linters and Bandit to enable earlier detection (OWASP,
    2021; PyCQA, n.d.).
  </p>

  <h4>Unit&nbsp;5 — Future Trends</h4>
  <p>
    I explored secure design for fog and edge computing, IoT, and cyber-physical
    systems, and discussed how SSDF and SAMM can guide DevSecOps adoption as 
    technologies advance (NIST, 2022; OWASP SAMM, 2020–).
  </p>

  <h4>Unit&nbsp;6 — Security of Programming Languages (Debate)</h4>
  <p>
    I evaluated Python, Rust, Swift, and F# for common vulnerabilities and 
    secure-by-default features, recommending language selection based on threat 
    models and ecosystem security rather than syntax. I then aligned these 
    recommendations with SSDF control families (NIST, 2022).
  </p>

  <h4>Team Design Document — Secure Artefact Platform</h4>
  <p>
    Our team designed a secure application for copyright artefacts, 
    incorporating encryption, RBAC, checksums, and audit logging, communicated 
    through UML diagrams. Feedback highlighted strong research and diagramming, and 
    suggested clearer initial security features and stronger links between use 
    cases, which I addressed in the revision.
  </p>

  <h4>Reflective Piece</h4>
  <p>
    Applying Rolfe’s “What? So what? Now what?” framework, I synthesized 
    learning across units by integrating security into agile processes, using UML to
    clarify risks, implementing automated testing, and planning continuous 
    improvement based on literature and peer feedback (Rolfe, Freshwater and Jasper,
    2001).
  </p>

  <h3>Reflections and Learning Highlights</h3>
  <ul>
    <li><strong>Security across the lifecycle.</strong> SSDF and SAMM embedded 
    security into planning, development, and verification—avoiding relegation to the
    final step (NIST, 2022; OWASP SAMM, 2020–). UML exposed hidden assumptions 
    (roles, data flows, trust boundaries), and automation with Bandit and linters 
    surfaced known issues in CI, freeing time for higher-value manual testing (OMG, 
    2017; PyCQA, n.d.).</li>
    <li><strong>Risk-focused testing.</strong> Concentrating on the OWASP 
    Top&nbsp;10 prioritized the most critical defects likely to impact production 
    (OWASP, 2021).</li>
    <li><strong>Operationalising practice.</strong> I begin work items with a 
    documented risk note and a plain-language misuse case. Tracked outcomes include 
    SAST-triggered failed builds and the number of critical issues remediated per 
    sprint, reported for executive visibility.</li>
  </ul>

  <h3>Professional Skills Matrix and Action Plan</h3>

  <h4>Skills Gained or Strengthened</h4>
  <ul>
    <li>SSDF/SAMM-aligned secure SDLC planning and evidence capture for audits 
    (NIST, 2022; OWASP SAMM, 2020–).</li>
    <li>UML-driven design communication (use-case, class, sequence) (OMG, 
    2017).</li>
    <li>Secure coding and CI integration of Bandit and linters (PyCQA, 
    n.d.).</li>
    <li>Risk-based security testing mapped to OWASP Top&nbsp;10 (OWASP, 
    2021).</li>
    <li>Concise executive summaries with measurable outcomes tied to backlog and
    release gates (NIST, 2022).</li>
  </ul>

  <h4>Action Plan</h4>
  <ul>
    <li><strong>Short-term (next 4–6&nbsp;weeks):</strong> Add SSDF tags to user
    stories; introduce a lightweight threat-modelling checklist at refinement; enforce Bandit in CI with a fail-on-critical policy (NIST, 2022; PyCQA, 
    n.d.).</li>
    <li><strong>Medium-term (this term):</strong> Map team practices to SAMM 
    domains; pilot an application-level security KPI set (e.g., time-to-fix high 
    vulns, test coverage of Top&nbsp;10 risks); baseline against ISO/IEC&nbsp;27034 
    guidance (OWASP SAMM, 2020–; ISO/IEC, 2011).</li>
    <li><strong>Long-term:</strong> Institutionalise a secure coding standard 
    and secure design reviews at release gates; review annually against SSDF updates 
    and emerging AI-aware secure-development practices (NIST, 2022).</li>
  </ul>

  <h3>Module Files</h3>
  <ul>
    <li>
      Folder:
      <a href="https://github.com/diogoneno/diogoneno.github.io/tree/main/assets
/SoftwareDev" target="_blank" rel="noopener">
        assets/SoftwareDev
      </a>
    </li>
    <li>
      <a href="https://github.com/diogoneno/diogoneno.github.io/blob/main/assets
/SoftwareDev/Reflective%20Piece%20for%20Secure%20Software%20Development.pdf" 
target="_blank" rel="noopener">
        Reflective Piece for Secure Software Development.pdf
      </a>
      &nbsp;|&nbsp;
      <a href="https://github.com/diogoneno/diogoneno.github.io/blob/main/assets
/SoftwareDev/Secure%20Enclave%20for%20Musical%20Artefacts.pdf" target="_blank" 
rel="noopener">
        Secure Enclave for Musical Artefacts.pdf
      </a>
    </li>
    <li>
      Folder:
      <a href="https://github.com/diogoneno/diogoneno.github.io/tree/main/assets
/SoftwareDev/final" target="_blank" rel="noopener">
        assets/SoftwareDev/final
      </a>
      <ul>
        <li><a href="https://github.com/diogoneno/diogoneno.github.io/blob/main/
assets/SoftwareDev/final/README.txt" target="_blank" 
rel="noopener">README.txt</a></li>
        <li><a href="https://github.com/diogoneno/diogoneno.github.io/blob/main/
assets/SoftwareDev/final/Secure%20Endave%20for%20Musical%20Artefacts.pdf" 
target="_blank" rel="noopener">Secure Endave for Musical Artefacts.pdf</a></li>
        <li><a href="https://github.com/diogoneno/diogoneno.github.io/blob/main/
assets/SoftwareDev/final/app.py" target="_blank" rel="noopener">app.py</a></li>
        <li><a href="https://github.com/diogoneno/diogoneno.github.io/blob/main/
assets/SoftwareDev/final/bandit_report.txt" target="_blank" 
rel="noopener">bandit_report.txt</a></li>
        <li><a href="https://github.com/diogoneno/diogoneno.github.io/blob/main/
assets/SoftwareDev/final/flake8_report.txt" target="_blank" 
rel="noopener">flake8_report.txt</a></li>
        <li><a href="https://github.com/diogoneno/diogoneno.github.io/blob/main/
assets/SoftwareDev/final/pylint_report.txt" target="_blank" 
rel="noopener">pylint_report.txt</a></li>
        <li><a href="https://github.com/diogoneno/diogoneno.github.io/blob/main/
assets/SoftwareDev/final/testproofconcept.pdf" target="_blank" 
rel="noopener">testproofconcept.pdf</a></li>
      </ul>
    </li>
  </ul>

  <hr aria-hidden="true" />

  <h3 id="references">References</h3>
  <ul>
    <li><strong>NIST (2022)</strong> Secure Software Development Framework 
(SSDF) v1.1. Available at: <a href="https://csrc.nist.gov/pubs/sp/800/218/final"
 target="_blank" rel="noopener">CSRC page</a> and <a 
 href="https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-218.pdf"
 target="_blank" rel="noopener">PDF</a>.</li>
    <li><strong>ISO/IEC (2011)</strong> 27034-1: Application security — Overview
 and concepts. Available at: <a href="https://www.iso.org/standard/44378.html" 
 target="_blank" rel="noopener">iso.org</a>.</li>
    <li><strong>OWASP (2021)</strong> Top 10 Web Application Security Risks. 
 Available at: <a href="https://owasp.org/Top10/" target="_blank" 
 rel="noopener">owasp.org/Top10</a>.</li>
    <li><strong>OWASP SAMM (2020–)</strong> Software Assurance Maturity Model. 
 Available at: <a href="https://owaspsamm.org/model/" target="_blank" 
 rel="noopener">owaspsamm.org/model</a>.</li>
    <li><strong>OMG (2017)</strong> UML 2.5.1 Specification. Available at: <a 
 href="https://www.omg.org/spec/UML/2.5.1/About-UML" target="_blank" 
 rel="noopener">omg.org/spec/UML/2.5.1</a>.</li>
    <li><strong>PyCQA (n.d.)</strong> Bandit — Security linter for Python. 
 Available at: <a href="https://bandit.readthedocs.io/" target="_blank" 
 rel="noopener">bandit.readthedocs.io</a>.</li>
    <li><strong>Rolfe, G., Freshwater, D. &amp; Jasper, M. (2001)</strong> 
 Reflective model “What? So what? Now what?” (summary). Available at: <a href="https://my.cumbria.ac.uk/media/MyCumbria/Documents/ReflectiveModelRolfe.pdf" 
 target="_blank" rel="noopener">my.cumbria.ac.uk</a>.</li>
  </ul>
</section>
