---
layout: post
title: Network Security
subtitle: July 2024
categories: Module
tags: [module, cybersecurity, backups, resilience]
---

<section id="introduction">
  <h2>Network Security Module</h2>

  <p>
    This module sharpened how I design, evidence, and communicate secure backup and recovery—treating resilience as a <em>measurable outcome</em> rather than an aspiration. I translated risk findings into concrete controls (offline/immutable copies, independent key custody, admin-plane hardening) and operating procedures mapped to recognised guidance, so that recovery time and data loss can be forecast, tested, and governed (<a href="#ref-nist80034">NIST, 2010</a>; <a href="#ref-ncsc-offline">NCSC, 2019</a>; <a href="#ref-iso27031">ISO/IEC, 2011/2025</a>). A brief personal lens: in my SRE role at Cohesity—plus prior years supporting NetBackup at Veritas—I’ve seen first-hand that the difference between a <em>backup</em> and a <em>restore</em> is governance, testing cadence, and clean separation from the blast radius (<a href="#ref-nist-csf20">NIST, 2024</a>).
  </p>

  <h3>Learning Outcomes</h3>
  <ul>
    <li>Identify and prioritise backup-related risks (ransomware reach, weak identity on backup planes, recovery unknowns) and map them to proportionate controls such as 3-2-1 with an offline/immutable copy and MFA-protected admin access (<a href="#ref-ncsc-offline">NCSC, 2019</a>; <a href="#ref-ico-bcdr">ICO, 2023</a>).</li>
    <li>Design and justify resilient architectures (segregated credentials, encrypted data/keys, scheduled restore drills with RPO/RTO targets) aligned to contingency planning guidance (<a href="#ref-nist80034">NIST, 2010</a>).</li>
    <li>Connect technical measures to governance and assurance—using CSF&nbsp;2.0 outcomes to show ownership, metrics, and accountability at executive level (<a href="#ref-nist-csf20">NIST, 2024</a>).</li>
    <li>Frame backup and recovery within ICT-readiness and business continuity expectations (<a href="#ref-iso27031">ISO/IEC&nbsp;27031</a>) and GDPR reality (<a href="#ref-ico-bcdr">ICO, 2023</a>).</li>
  </ul>

  <h3>Artefacts and Feedback</h3>

  <h4>Assignment (Unit&nbsp;3) — Backup System Security Analysis &amp; Baseline</h4>
  <p>
    I assessed an estate against common failure modes: unencrypted media, shared credentials, always-hot replicas, and untested restores. The plan introduced offline/immutable copies, separated key custody, MFA on the backup control plane, and a restore-testing calendar with success-rate KPIs. Feedback praised the structure and standards alignment and asked for a sharper tools comparison and a clearer “finding → control → expected risk reduction” trace (<a href="#ref-ncsc-offline">NCSC, 2019</a>; <a href="#ref-nist80034">NIST, 2010</a>).
  </p>
  <ul>
    <li>
      File:
      <a href="https://github.com/diogoneno/diogoneno.github.io/blob/main/assets/NetworkSecurity/assignmentunit3.docx" target="_blank" rel="noopener" aria-label="Assignment Unit 3 DOCX">
        <strong>assignmentunit3.docx</strong>
      </a>
    </li>
  </ul>

  <h4>Executive Summary — OSS (Online Shopping System) Backup &amp; Recovery Posture</h4>
  <p>
    For non-technical stakeholders, I prioritised three moves: (1) close identity gaps on backup/admin interfaces; (2) enforce end-to-end encryption with independent key custody; (3) guarantee a timed offline/immutable copy with verified restores. Impact was framed in business terms (downtime, data loss, legal exposure) and each action was mapped to CSF&nbsp;2.0 categories with testable KPIs (restore-success&nbsp;%, MTTR, RPO hit-rate) (<a href="#ref-nist-csf20">NIST, 2024</a>; <a href="#ref-iso27031">ISO/IEC, 2011/2025</a>).
  </p>
  <ul>
    <li>
      File:
      <a href="https://github.com/diogoneno/diogoneno.github.io/blob/main/assets/NetworkSecurity/Executive%20Summary.docx" target="_blank" rel="noopener" aria-label="Executive Summary DOCX">
        <strong>Executive Summary.docx</strong>
      </a>
    </li>
  </ul>

  <h4>Reflective Piece — Method Choices, Multiple Perspectives, PDP</h4>
  <p>
    I critiqued my assumptions (e.g., over-reliance on cloud snapshots that remain logically “hot”) and incorporated literature on offline backups and GDPR-aligned continuity. I set a plan to include comparative tool analyses, ransomware case studies, and evidence packs for audits (test logs, chain-of-custody for keys). This tightened how I justify trade-offs and explain why “we have backups” ≠ “we can restore” (<a href="#ref-ncsc-offline">NCSC, 2019</a>; <a href="#ref-ico-bcdr">ICO, 2023</a>).
  </p>
  <ul>
    <li>
      File:
      <a href="https://github.com/diogoneno/diogoneno.github.io/blob/main/assets/NetworkSecurity/NSoctober2024ReflecPiec.docx" target="_blank" rel="noopener" aria-label="Reflective Piece DOCX">
        <strong>NSoctober2024ReflecPiec.docx</strong>
      </a>
    </li>
  </ul>

  <h3>Reflections and Learning Highlights</h3>
  <ul>
    <li><strong>Resilience is testable.</strong> A backup without scheduled restore drills is an assumption, not a control; I now treat success-rate, RPO hit-rate, and MTTR as non-negotiable metrics (<a href="#ref-nist80034">NIST, 2010</a>).</li>
    <li><strong>Modern 3-2-1.</strong> One copy must be offline/immutable, with identity controls that assume the adversary already has footholds (<a href="#ref-ncsc-offline">NCSC, 2019</a>). This mirrors what I’ve seen in incident calls: identity is the hinge.</li>
    <li><strong>Governance connects the layers.</strong> CSF&nbsp;2.0’s <em>GOVERN</em> function helped link technical detail to ownership, budget, and reporting—useful when briefing senior leaders (<a href="#ref-nist-csf20">NIST, 2024</a>).</li>
    <li><strong>Compliance nuance.</strong> GDPR expects protection and recoverability of personal data; where immediate deletion from backups is infeasible, retention control and “beyond-use” safeguards must be demonstrable (<a href="#ref-ico-bcdr">ICO, 2023</a>).</li>
  </ul>

  <h3>Professional Skills Matrix and Action Plan</h3>

  <h4>Skills Gained or Strengthened</h4>
  <ul>
    <li>Backup architecture &amp; contingency planning mapped to SP&nbsp;800-34 and ISO/IEC&nbsp;27031 (<a href="#ref-nist80034">NIST, 2010</a>; <a href="#ref-iso27031">ISO/IEC, 2011/2025</a>).</li>
    <li>Ransomware-resilient designs: offline/immutable copies, privileged-access hardening, restore-first KPIs (3-2-1 applied with identity controls) (<a href="#ref-ncsc-offline">NCSC, 2019</a>).</li>
    <li>Executive communication via CSF&nbsp;2.0 outcomes—connecting controls to risk appetite and measurable assurance (<a href="#ref-nist-csf20">NIST, 2024</a>).</li>
    <li>GDPR framing for backups (accountability, continuity, and practicable erasure patterns) (<a href="#ref-ico-bcdr">ICO, 2023</a>).</li>
    <li>Critical reflection integrated with practitioner experience (Cohesity SRE; prior Veritas/NetBackup support) to ground recommendations in real-world restore behaviour.</li>
  </ul>

  <h4>Action Plan</h4>
  <ul>
    <li><strong>Short term (4–6 weeks):</strong> Stand up a restore-testing calendar and dashboard (restore success&nbsp;%, MTTR, RPO adherence). Prove one offline/immutable path with segregated credentials and audited key custody (<a href="#ref-nist80034">NIST, 2010</a>; <a href="#ref-ncsc-offline">NCSC, 2019</a>).</li>
    <li><strong>Medium term (this term):</strong> Map current controls to CSF&nbsp;2.0 categories; produce a one-page scorecard for executives and run a table-top exercise using current ransomware guidance (<a href="#ref-nist-csf20">NIST, 2024</a>).</li>
    <li><strong>Long term:</strong> Align ICT-readiness with ISO/IEC&nbsp;27031; evidence GDPR-aligned continuity (retention, “beyond-use” controls), then schedule an annual contingency test (<a href="#ref-iso27031">ISO/IEC, 2011/2025</a>; <a href="#ref-ico-bcdr">ICO, 2023</a>).</li>
  </ul>

  <hr aria-hidden="true" />

  <h3 id="references">References</h3>
  <ul>
    <li id="ref-nist80034"><strong>NIST</strong> (2010) <em>SP&nbsp;800-34 Rev.1 — Contingency Planning Guide for Federal Information Systems</em>. National Institute of Standards and Technology. PDF: <a href="https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-34r1.pdf" target="_blank" rel="noopener">nvlpubs.nist.gov</a>. Overview: <a href="https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final" target="_blank" rel="noopener">csrc.nist.gov</a>.</li>
    <li id="ref-ncsc-offline"><strong>NCSC</strong> (2019) <em>Offline backups in an online world</em>. National Cyber Security Centre. <a href="https://www.ncsc.gov.uk/blog-post/offline-backups-in-an-online-world" target="_blank" rel="noopener">ncsc.gov.uk</a>.</li>
    <li id="ref-iso27031"><strong>ISO/IEC</strong> (2011/2025) <em>ISO/IEC&nbsp;27031 — ICT Readiness for Business Continuity</em>. Overview pages: <a href="https://www.iso.org/standard/44374.html" target="_blank" rel="noopener">iso.org/44374</a> and <a href="https://www.iso.org/standard/27031" target="_blank" rel="noopener">iso.org/27031</a>.</li>
    <li id="ref-nist-csf20"><strong>NIST</strong> (2024) <em>Cybersecurity Framework (CSF) 2.0</em>. PDF: <a href="https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf" target="_blank" rel="noopener">NIST.CSWP.29.pdf</a>. Site: <a href="https://www.nist.gov/cyberframework" target="_blank" rel="noopener">nist.gov/cyberframework</a>.</li>
    <li id="ref-ico-bcdr"><strong>ICO</strong> (2023) <em>Business continuity, disaster recovery and back-ups</em>. Information Commissioner’s Office. <a href="https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/accountability-framework/records-management-and-security/business-continuity-disaster-recovery-and-back-ups/" target="_blank" rel="noopener">ico.org.uk</a>.</li>
  </ul>

  <h3>Module Files</h3>
  <ul>
    <li>
      Folder:
      <a href="https://github.com/diogoneno/diogoneno.github.io/tree/main/assets/NetworkSecurity" target="_blank" rel="noopener" aria-label="Module folder">
        assets/NetworkSecurity
      </a>
    </li>
    <li>
      <a href="https://github.com/diogoneno/diogoneno.github.io/blob/main/assets/NetworkSecurity/assignmentunit3.docx" target="_blank" rel="noopener">assignmentunit3.docx</a>
      &nbsp;|&nbsp;
      <a href="https://github.com/diogoneno/diogoneno.github.io/blob/main/assets/NetworkSecurity/Executive%20Summary.docx" target="_blank" rel="noopener">Executive&nbsp;Summary.docx</a>
      &nbsp;|&nbsp;
      <a href="https://github.com/diogoneno/diogoneno.github.io/blob/main/assets/NetworkSecurity/NSoctober2024ReflecPiec.docx" target="_blank" rel="noopener">NSoctober2024ReflecPiec.docx</a>
    </li>
  </ul>
</section>

