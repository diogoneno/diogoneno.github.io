---
layout: page
title: Secure Systems Architecture
description: Designing resilient platforms through layered security patterns
nav-menu: true
nav-order: 7
summary: >-
  Architecture-led approach to threat modelling, control selection, and
  verification across complex systems.
---

<!-- Module Overview -->
<section style="max-width: 1100px; margin: 0 auto 3rem; padding: 2.5rem 2rem; background: #f4f6fb; border-radius: 14px; box-shadow: 0 10px 25px rgba(13, 41, 67, 0.08);">
  <div style="max-width: 860px; margin: 0 auto;">
    <div style="display: inline-block; background: #0b3c5d; color: #ffffff; padding: 0.35rem 1rem; border-radius: 999px; font-size: 0.8rem; letter-spacing: 0.05em; margin-bottom: 1.2rem;">
      SECURE SYSTEMS ARCHITECTURE MODULE
    </div>
    <h1 style="font-size: 2.4rem; margin-bottom: 1rem; color: #0b3c5d;">Secure Systems Architecture</h1>
    <p style="font-size: 1.05rem; line-height: 1.75; color: #334155; margin-bottom: 1.4rem;">
      This module concentrated on designing and evaluating secure systems-of-systems (SoS) in CPS/IoT contexts. It integrated architectural thinking (CIA triad with ABCDE characteristics), threat modelling (AD-Trees with quantitative scoring), and a secure IoT messaging prototype, emphasising defensible trade-offs, layered controls, and evidence-driven evaluation under real-world constraints (latency, loss, scale).
    </p>
    <p style="font-size: 1rem; line-height: 1.7; color: #475569; margin: 0;">
      Work spanned strategic design reviews, quantitative risk analysis, and hands-on development of authenticated encryption pipelines. Feedback drove refinements in diagram quality, risk traceability, and the presentation of cost–benefit considerations for blockchain-enabled IoT platforms.
    </p>
  </div>
</section>

<!-- Learning Outcomes -->
<section style="max-width: 1100px; margin: 0 auto 4rem;">
  <div style="text-align: center; margin-bottom: 2.5rem;">
    <h2 style="font-size: 2rem; margin-bottom: 0.6rem; color: #0b3c5d;">Learning Outcomes</h2>
    <div style="width: 60px; height: 3px; background: linear-gradient(90deg, #0b3c5d, #1d7db1); margin: 0 auto;"></div>
  </div>

  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.5rem;">
    <div style="background: white; border-radius: 12px; padding: 1.6rem; border: 1px solid #e2e8f0; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
      <h4 style="color: #0b3c5d; font-size: 1.1rem; margin-bottom: 0.6rem;">Architectural Alignment</h4>
      <p style="color: #475569; font-size: 0.95rem; line-height: 1.6;">
        Design secure CPS/IoT architectures by aligning CIA priorities with ABCDE characteristics and SoS constraints.
      </p>
    </div>
    <div style="background: white; border-radius: 12px; padding: 1.6rem; border: 1px solid #e2e8f0; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
      <h4 style="color: #0b3c5d; font-size: 1.1rem; margin-bottom: 0.6rem;">Quantitative Threat Modelling</h4>
      <p style="color: #475569; font-size: 0.95rem; line-height: 1.6;">
        Prioritise threats through AD-Trees and quantitative scoring (DREAD/DSS) to justify the sequencing of mitigations.
      </p>
    </div>
    <div style="background: white; border-radius: 12px; padding: 1.6rem; border: 1px solid #e2e8f0; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
      <h4 style="color: #0b3c5d; font-size: 1.1rem; margin-bottom: 0.6rem;">Secure Communications Engineering</h4>
      <p style="color: #475569; font-size: 0.95rem; line-height: 1.6;">
        Implement authenticated encryption with sound object-oriented design, integrating replay protection and resilience to loss.
      </p>
    </div>
    <div style="background: white; border-radius: 12px; padding: 1.6rem; border: 1px solid #e2e8f0; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
      <h4 style="color: #0b3c5d; font-size: 1.1rem; margin-bottom: 0.6rem;">Testing &amp; Quality Gates</h4>
      <p style="color: #475569; font-size: 0.95rem; line-height: 1.6;">
        Integrate automated testing, coverage targets, and security tooling to assure reliability under adverse conditions.
      </p>
    </div>
    <div style="background: white; border-radius: 12px; padding: 1.6rem; border: 1px solid #e2e8f0; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
      <h4 style="color: #0b3c5d; font-size: 1.1rem; margin-bottom: 0.6rem;">Evidence-led Communication</h4>
      <p style="color: #475569; font-size: 0.95rem; line-height: 1.6;">
        Communicate architectural decisions, trade-offs, and testing results to technical and non-technical audiences with supporting evidence.
      </p>
    </div>
  </div>
</section>

<!-- Artefacts and Feedback -->
<section style="max-width: 1100px; margin: 0 auto 4rem;">
  <div style="text-align: center; margin-bottom: 2.5rem;">
    <h2 style="font-size: 2rem; margin-bottom: 0.6rem; color: #0b3c5d;">Artefacts and Feedback</h2>
    <div style="width: 60px; height: 3px; background: linear-gradient(90deg, #0b3c5d, #1d7db1); margin: 0 auto;"></div>
  </div>

  <article style="background: white; border-radius: 12px; padding: 2rem; margin-bottom: 2rem; border-left: 5px solid #0b3c5d; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.08);">
    <div style="display: flex; flex-direction: column; gap: 1rem;">
      <div>
        <h3 style="color: #0b3c5d; font-size: 1.35rem; margin-bottom: 0.6rem;">Unit 3 — Development Team Project: Design Document</h3>
        <p style="color: #475569; line-height: 1.7; margin-bottom: 1rem;">
          Architecture for a blockchain-integrated CPS/IoT system-of-systems identified key vulnerabilities and mapped mitigations via AD-Trees (client node, controller/hub, overall SoS). Controls included multi-factor authentication, Zero Trust patterns, and layered detection aligned to quantified DREAD/DSS scores.
        </p>
      </div>
      <div style="background: #e7f2fb; border-left: 4px solid #1d7db1; padding: 1rem 1.2rem; border-radius: 6px;">
        <p style="margin: 0; color: #0f3057; font-size: 0.95rem;">
          <strong>Feedback:</strong> Strong understanding of SoS security challenges and CIA/ABCDE framing; improve by explicitly linking each vulnerability to ABCDE traits and replacing placeholder diagrams with polished figures.
        </p>
      </div>
    </div>
  </article>

  <article style="background: white; border-radius: 12px; padding: 2rem; margin-bottom: 2rem; border-left: 5px solid #0b3c5d; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.08);">
    <div style="display: flex; flex-direction: column; gap: 1rem;">
      <div>
        <h3 style="color: #0b3c5d; font-size: 1.35rem; margin-bottom: 0.6rem;">Unit 6 — Development Individual Project: Code Development</h3>
        <p style="color: #475569; line-height: 1.7; margin-bottom: 1rem;">
          Built a modular Python simulation of secure IoT communication focused on confidentiality within the ABCDE model. Async components (controller, device, network, packet) used AES-GCM with unique nonces, injected loss and delay, and surfaced metrics. Bandit, Flake8, and Pytest underpinned quality assurance, with documentation detailing experiments and results.
        </p>
      </div>
      <div style="background: #e6f7f1; border-left: 4px solid #2f9e7c; padding: 1rem 1.2rem; border-radius: 6px;">
        <p style="margin: 0; color: #145c45; font-size: 0.95rem;">
          <strong>Feedback:</strong> Commended for clear structure, realistic mitigation rationale, and effective automation; next steps include adding replay detection, key rotation, and deeper chaos testing scenarios.
        </p>
      </div>
    </div>
  </article>

  <article style="background: white; border-radius: 12px; padding: 2rem; border-left: 5px solid #0b3c5d; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.08);">
    <div style="display: flex; flex-direction: column; gap: 1rem;">
      <div>
        <h3 style="color: #0b3c5d; font-size: 1.35rem; margin-bottom: 0.6rem;">Unit 6 — Individual Reflective Submission</h3>
        <p style="color: #475569; line-height: 1.7; margin-bottom: 1rem;">
          Captured lessons on secure architecture for blockchain-enabled CPS/IoT deployments, translating tutor feedback into an action plan for automated testing, AD-Tree enhancements, and tighter ABCDE linkage. Reflections examined team collaboration, delegation, and growth areas.
        </p>
      </div>
      <div style="background: #fff5e6; border-left: 4px solid #f4a261; padding: 1rem 1.2rem; border-radius: 6px;">
        <p style="margin: 0; color: #8a4b12; font-size: 0.95rem;">
          <strong>Feedback:</strong> Analytical tone and theory integration were strong; add concrete outcome examples, quantify improvements, and reference recent sources with consistent citation formatting.
        </p>
      </div>
    </div>
  </article>
</section>

<!-- Action Plan -->
<section style="max-width: 1100px; margin: 0 auto 4rem;">
  <div style="text-align: center; margin-bottom: 2.5rem;">
    <h2 style="font-size: 2rem; margin-bottom: 0.6rem; color: #0b3c5d;">Action Plan (next 6–8 weeks)</h2>
    <div style="width: 60px; height: 3px; background: linear-gradient(90deg, #0b3c5d, #1d7db1); margin: 0 auto;"></div>
    <p style="color: #64748b; margin-top: 1rem; font-size: 0.95rem;">Prioritised improvements driven by feedback and observed gaps.</p>
  </div>

  <div style="overflow-x: auto; border-radius: 12px; box-shadow: 0 8px 20px rgba(15, 23, 42, 0.08);">
    <table style="width: 100%; border-collapse: collapse; min-width: 720px;">
      <thead>
        <tr style="background: #0b3c5d; color: white;">
          <th style="padding: 1rem; text-align: left; font-weight: 600;">Action area</th>
          <th style="padding: 1rem; text-align: left; font-weight: 600;">What will be done</th>
          <th style="padding: 1rem; text-align: left; font-weight: 600;">Evidence of completion</th>
          <th style="padding: 1rem; text-align: left; font-weight: 600;">Target date</th>
        </tr>
      </thead>
      <tbody>
        <tr style="background: white; border-bottom: 1px solid #e2e8f0;">
          <td style="padding: 1rem; font-weight: 600; color: #0b3c5d;">ABCDE linkage &amp; visuals</td>
          <td style="padding: 1rem; color: #475569;">Map each vulnerability to ABCDE attributes, regenerate AD-Trees via Graphviz or diagram tooling, remove placeholder artefacts, and standardise figure styling.</td>
          <td style="padding: 1rem; color: #475569;">Appendix table (vulnerability → ABCDE) and refreshed diagram set in the design document.</td>
          <td style="padding: 1rem; color: #475569;">Week 2</td>
        </tr>
        <tr style="background: #f8fafc; border-bottom: 1px solid #e2e8f0;">
          <td style="padding: 1rem; font-weight: 600; color: #0b3c5d;">Trade-off analysis</td>
          <td style="padding: 1rem; color: #475569;">Add quantified discussion on blockchain scalability, latency, and mitigation costs, including sensitivity analysis of DREAD/DSS inputs.</td>
          <td style="padding: 1rem; color: #475569;">New trade-off subsection plus revised scores with sensitivity commentary.</td>
          <td style="padding: 1rem; color: #475569;">Week 3</td>
        </tr>
        <tr style="background: white; border-bottom: 1px solid #e2e8f0;">
          <td style="padding: 1rem; font-weight: 600; color: #0b3c5d;">Comms hardening</td>
          <td style="padding: 1rem; color: #475569;">Introduce replay detection (sequence numbers), periodic key rotation, and X25519-based session key agreement layered on AES-GCM.</td>
          <td style="padding: 1rem; color: #475569;">Passing automated tests, code diffs, and updated README crypto notes.</td>
          <td style="padding: 1rem; color: #475569;">Week 4</td>
        </tr>
        <tr style="background: #f8fafc; border-bottom: 1px solid #e2e8f0;">
          <td style="padding: 1rem; font-weight: 600; color: #0b3c5d;">Reliability testing</td>
          <td style="padding: 1rem; color: #475569;">Extend chaos scenarios (duplication, reordering, burst loss) and add Hypothesis property tests plus coverage targets.</td>
          <td style="padding: 1rem; color: #475569;">CI badge, ≥85% coverage reports, and chaos test execution logs or screenshots.</td>
          <td style="padding: 1rem; color: #475569;">Week 4</td>
        </tr>
        <tr style="background: white; border-bottom: 1px solid #e2e8f0;">
          <td style="padding: 1rem; font-weight: 600; color: #0b3c5d;">CI &amp; quality gates</td>
          <td style="padding: 1rem; color: #475569;">Implement pre-commit hooks (Black, Flake8, Bandit, Pytest) and GitHub Actions with artefact capture and metric trending.</td>
          <td style="padding: 1rem; color: #475569;">Committed pre-commit config, CI pipeline history, and trend chart exports.</td>
          <td style="padding: 1rem; color: #475569;">Week 3</td>
        </tr>
        <tr style="background: #f8fafc; border-bottom: 1px solid #e2e8f0;">
          <td style="padding: 1rem; font-weight: 600; color: #0b3c5d;">Documentation polish</td>
          <td style="padding: 1rem; color: #475569;">Produce updated architecture and sequence diagrams, operating runbook, and Cite-Them-Right references with consistent styling.</td>
          <td style="padding: 1rem; color: #475569;">Updated README/design document and alphabetised reference list.</td>
          <td style="padding: 1rem; color: #475569;">Week 3</td>
        </tr>
        <tr style="background: white;">
          <td style="padding: 1rem; font-weight: 600; color: #0b3c5d;">Reflection updates</td>
          <td style="padding: 1rem; color: #475569;">Add concrete collaboration examples, measurable impacts, and broadened perspectives backed by recent citations.</td>
          <td style="padding: 1rem; color: #475569;">Revised reflective submission with in-text citations and word count noted.</td>
          <td style="padding: 1rem; color: #475569;">Week 2</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<!-- Professional Skills Matrix -->
<section style="max-width: 1100px; margin: 0 auto 4rem;">
  <div style="text-align: center; margin-bottom: 2.5rem;">
    <h2 style="font-size: 2rem; margin-bottom: 0.6rem; color: #0b3c5d;">Professional Skills Matrix (snapshot)</h2>
    <div style="width: 60px; height: 3px; background: linear-gradient(90deg, #0b3c5d, #1d7db1); margin: 0 auto;"></div>
    <p style="color: #64748b; margin-top: 1rem; font-size: 0.95rem;">Current strengths with planned improvements aligned to feedback.</p>
  </div>

  <div style="overflow-x: auto; border-radius: 12px; box-shadow: 0 8px 20px rgba(15, 23, 42, 0.08);">
    <table style="width: 100%; border-collapse: collapse; min-width: 720px;">
      <thead>
        <tr style="background: #0b3c5d; color: white;">
          <th style="padding: 1rem; text-align: left; font-weight: 600;">Competency</th>
          <th style="padding: 1rem; text-align: left; font-weight: 600;">Current level</th>
          <th style="padding: 1rem; text-align: left; font-weight: 600;">Evidence</th>
          <th style="padding: 1rem; text-align: left; font-weight: 600;">Planned improvement</th>
        </tr>
      </thead>
      <tbody>
        <tr style="background: white; border-bottom: 1px solid #e2e8f0;">
          <td style="padding: 1rem; font-weight: 600; color: #0b3c5d;">Systems architecture (CPS/IoT, SoS)</td>
          <td style="padding: 1rem; color: #475569;">Proficient</td>
          <td style="padding: 1rem; color: #475569;">Coherent SoS design with CIA + ABCDE framing and comprehensive vulnerability analysis.</td>
          <td style="padding: 1rem; color: #475569;">Explicit vulnerability-to-ABCDE mapping, polished diagrams, and deeper scalability trade-offs.</td>
        </tr>
        <tr style="background: #f8fafc; border-bottom: 1px solid #e2e8f0;">
          <td style="padding: 1rem; font-weight: 600; color: #0b3c5d;">Threat modelling &amp; quantification</td>
          <td style="padding: 1rem; color: #475569;">Proficient</td>
          <td style="padding: 1rem; color: #475569;">AD-Trees for client, hub, and SoS layers with DREAD/DSS prioritisation.</td>
          <td style="padding: 1rem; color: #475569;">Regenerate original figures, add sensitivity analysis, and clarify risk acceptance criteria.</td>
        </tr>
        <tr style="background: white; border-bottom: 1px solid #e2e8f0;">
          <td style="padding: 1rem; font-weight: 600; color: #0b3c5d;">Secure comms engineering (Python)</td>
          <td style="padding: 1rem; color: #475569;">Proficient</td>
          <td style="padding: 1rem; color: #475569;">Modular asyncio/websockets simulation with AES-GCM and resilient packet abstraction.</td>
          <td style="padding: 1rem; color: #475569;">Add replay protection, key rotation with forward secrecy, and extended chaos scenarios.</td>
        </tr>
        <tr style="background: #f8fafc; border-bottom: 1px solid #e2e8f0;">
          <td style="padding: 1rem; font-weight: 600; color: #0b3c5d;">Testing &amp; assurance</td>
          <td style="padding: 1rem; color: #475569;">Proficient</td>
          <td style="padding: 1rem; color: #475569;">Bandit, Flake8, Pytest, and scenario testing under packet loss and latency.</td>
          <td style="padding: 1rem; color: #475569;">CI with quality gates, property-based tests, and ≥85% coverage tracking.</td>
        </tr>
        <tr style="background: white; border-bottom: 1px solid #e2e8f0;">
          <td style="padding: 1rem; font-weight: 600; color: #0b3c5d;">Documentation &amp; academic practice</td>
          <td style="padding: 1rem; color: #475569;">Proficient</td>
          <td style="padding: 1rem; color: #475569;">Clear README and design rationale with referenced sources.</td>
          <td style="padding: 1rem; color: #475569;">Standardise diagram styles, apply Cite-Them-Right, and expand trade-off exposition.</td>
        </tr>
        <tr style="background: #f8fafc;">
          <td style="padding: 1rem; font-weight: 600; color: #0b3c5d;">Collaboration &amp; reflective practice</td>
          <td style="padding: 1rem; color: #475569;">Proficient</td>
          <td style="padding: 1rem; color: #475569;">Reflection linked theory to practice with actionable responses to feedback.</td>
          <td style="padding: 1rem; color: #475569;">Include specific outcome metrics, cite impacts on delivery quality, and broaden perspectives.</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<!-- Reflection Highlights -->
<section style="max-width: 900px; margin: 0 auto 4rem; background: #0b3c5d; color: white; border-radius: 12px; padding: 2.5rem; box-shadow: 0 12px 28px rgba(11, 60, 93, 0.35);">
  <h2 style="font-size: 1.8rem; margin-bottom: 1rem; font-weight: 700;">Reflection Highlights</h2>
  <p style="font-size: 1.05rem; line-height: 1.8; margin-bottom: 1.2rem;">
    The module underscored the importance of connecting architectural artefacts with quantifiable risk arguments. Tutor feedback highlighted the need for better diagram polish and clearer ABCDE traceability, which now drive specific improvements in modelling collateral.
  </p>
  <p style="font-size: 1.05rem; line-height: 1.8; margin: 0;">
    Implementing authenticated encryption with measurable chaos testing reinforced the value of automation and telemetry in CPS/IoT environments. The next iteration will emphasise forward secrecy, evidence-backed trade-off narratives, and showcasing the measurable impact of collaborative changes.
  </p>
</section>
