---
layout: null
title: Security & Risk Management
description: Translating socio-technical risk analysis into prescriptive, GDPR-aligned controls
nav-menu: true
nav-order: 4
summary: >-
  Identified, modelled, and quantified risk across socio-technical systems, then
  translated insight into prescriptive controls, continuity strategies, and
  executive-ready communication.
topic_tags:
  - Risk Governance
  - Compliance Strategy
---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{{ page.summary | strip_newlines | strip }}">
    <title>Security &amp; Risk Management | MSc Portfolio</title>
    {% include shared-styles.html %}
    <style>
        .module-hero {
            padding: 8rem 5% 4rem;
            position: relative;
        }

        .module-hero-content {
            max-width: 1400px;
            margin: 0 auto;
            background: linear-gradient(135deg, rgba(0, 212, 255, 0.1), rgba(124, 58, 237, 0.1));
            border-radius: 24px;
            padding: 4rem 3rem;
            border: 1px solid rgba(255, 255, 255, 0.1);
            position: relative;
            overflow: hidden;
        }

        .module-hero-content::before {
            content: '';
            position: absolute;
            top: -50%;
            right: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(0, 212, 255, 0.1), transparent);
            animation: rotate 20s linear infinite;
        }

        @keyframes rotate {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }

        .module-hero-content > * {
            position: relative;
            z-index: 1;
        }

        .module-badge {
            display: inline-block;
            background: rgba(0, 212, 255, 0.2);
            color: var(--primary);
            padding: 0.5rem 1.5rem;
            border-radius: 50px;
            font-size: 0.9rem;
            font-weight: 600;
            margin-bottom: 1.5rem;
            border: 1px solid rgba(0, 212, 255, 0.3);
        }

        .module-hero h1 {
            font-size: clamp(2.5rem, 5vw, 4rem);
            font-weight: 800;
            margin-bottom: 1.5rem;
            background: linear-gradient(135deg, #fff 0%, var(--primary) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .module-hero p {
            font-size: 1.15rem;
            color: var(--text-secondary);
            max-width: 900px;
            line-height: 1.8;
            margin-bottom: 1rem;
        }

        .main-content {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 5% 6rem;
        }

        section {
            margin-bottom: 5rem;
        }

        .section-header {
            text-align: center;
            margin-bottom: 3rem;
        }

        .section-header h2 {
            font-size: clamp(1.8rem, 3vw, 2.5rem);
            font-weight: 700;
            margin-bottom: 1rem;
            background: linear-gradient(135deg, #fff, var(--primary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .divider {
            width: 60px;
            height: 3px;
            background: linear-gradient(90deg, var(--primary), var(--accent));
            margin: 1rem auto;
            border-radius: 2px;
        }

        .section-header p {
            color: var(--text-secondary);
            font-size: 1.1rem;
        }

        /* Generic prose card */
        .prose-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 2.5rem;
        }

        .prose-card p {
            color: var(--text-secondary);
            line-height: 1.8;
            margin-bottom: 1rem;
        }

        .prose-card p:last-child { margin-bottom: 0; }

        /* Learning Objectives */
        .objectives-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.5rem;
        }

        .objective-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 2rem;
            transition: all 0.3s ease;
        }

        .objective-card:hover {
            transform: translateY(-4px);
            border-color: rgba(0, 212, 255, 0.3);
            background: rgba(0, 212, 255, 0.05);
        }

        .objective-icon {
            font-size: 2rem;
            margin-bottom: 1rem;
        }

        .objective-card h4 {
            color: var(--primary);
            font-size: 1.05rem;
            margin-bottom: 0.6rem;
            font-weight: 600;
        }

        .objective-card p {
            color: var(--text-secondary);
            line-height: 1.7;
            font-size: 0.95rem;
        }

        /* Artefacts */
        .artefact {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 2rem;
            margin-bottom: 1.5rem;
            transition: all 0.3s ease;
        }

        .artefact:hover {
            border-color: rgba(0, 212, 255, 0.3);
            background: rgba(0, 212, 255, 0.03);
        }

        .artefact-header {
            display: flex;
            align-items: flex-start;
            gap: 1rem;
            margin-bottom: 1rem;
            flex-wrap: wrap;
        }

        .artefact-icon {
            font-size: 2rem;
            flex-shrink: 0;
        }

        .artefact-title {
            flex: 1;
            min-width: 200px;
        }

        .artefact-title h3 {
            font-size: 1.15rem;
            font-weight: 600;
            margin-bottom: 0.4rem;
            color: #fff;
        }

        .badge-row {
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
            align-items: center;
        }

        .unit-badge {
            display: inline-block;
            background: rgba(124, 58, 237, 0.2);
            color: var(--accent);
            padding: 0.2rem 0.8rem;
            border-radius: 50px;
            font-size: 0.75rem;
            font-weight: 700;
            border: 1px solid rgba(124, 58, 237, 0.3);
        }

        .artefact-content p {
            color: var(--text-secondary);
            line-height: 1.7;
            margin-bottom: 1rem;
        }

        .evidence-box {
            background: rgba(0, 212, 255, 0.05);
            border: 1px solid rgba(0, 212, 255, 0.2);
            border-radius: 8px;
            padding: 1rem 1.2rem;
            margin-bottom: 0.8rem;
        }

        .evidence-box p { margin-bottom: 0; }

        .evidence-box strong { color: var(--primary); }

        .feedback-box {
            background: rgba(245, 158, 11, 0.05);
            border: 1px solid rgba(245, 158, 11, 0.2);
            border-radius: 8px;
            padding: 1rem 1.2rem;
        }

        .feedback-box p { margin-bottom: 0; color: var(--text-secondary); }

        .feedback-box strong { color: var(--warning); }

        /* Reflections (unit-card grid) */
        .units-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
        }

        .unit-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 1.8rem;
            transition: all 0.3s ease;
        }

        .unit-card:hover {
            transform: translateY(-4px);
            border-color: rgba(124, 58, 237, 0.3);
            background: rgba(124, 58, 237, 0.05);
        }

        .unit-card-header {
            display: flex;
            align-items: center;
            gap: 0.8rem;
            margin-bottom: 1rem;
        }

        .unit-card-header .icon {
            font-size: 1.5rem;
        }

        .unit-card h3 {
            font-size: 1rem;
            font-weight: 600;
            color: #fff;
            line-height: 1.4;
            margin: 0;
        }

        .unit-card p {
            color: var(--text-secondary);
            font-size: 0.93rem;
            line-height: 1.7;
            margin: 0;
        }

        /* Skills Matrix Table */
        .matrix-wrap {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 1.5rem;
            overflow-x: auto;
        }

        table.skills-matrix {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.92rem;
            min-width: 640px;
        }

        table.skills-matrix th,
        table.skills-matrix td {
            padding: 0.85rem 1rem;
            text-align: left;
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
        }

        table.skills-matrix th {
            color: var(--primary);
            font-weight: 700;
            text-transform: uppercase;
            font-size: 0.78rem;
            letter-spacing: 0.05em;
            border-bottom: 2px solid rgba(0, 212, 255, 0.3);
        }

        table.skills-matrix td {
            color: var(--text-secondary);
        }

        table.skills-matrix td.skill-name {
            color: var(--primary);
            font-weight: 600;
        }

        table.skills-matrix tr:hover td {
            background: rgba(0, 212, 255, 0.03);
            color: var(--text);
        }

        /* Action Plan list */
        .action-list {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 2rem 2.5rem;
            counter-reset: action-counter;
            list-style: none;
        }

        .action-list li {
            counter-increment: action-counter;
            position: relative;
            padding: 1.2rem 0 1.2rem 3.5rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
            color: var(--text-secondary);
            line-height: 1.7;
        }

        .action-list li:last-child { border-bottom: none; }

        .action-list li::before {
            content: counter(action-counter);
            position: absolute;
            left: 0;
            top: 1.2rem;
            width: 2.5rem;
            height: 2.5rem;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            color: #fff;
            font-weight: 800;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .action-list li strong { color: var(--text); }

        .action-list li .target {
            display: inline-block;
            margin-left: 0.5rem;
            padding: 0.15rem 0.6rem;
            background: rgba(16, 185, 129, 0.15);
            color: var(--success);
            border: 1px solid rgba(16, 185, 129, 0.3);
            border-radius: 50px;
            font-size: 0.75rem;
            font-weight: 600;
        }

        /* Conclusion card */
        .conclusion-card {
            background: linear-gradient(135deg, rgba(0, 212, 255, 0.05), rgba(124, 58, 237, 0.05));
            border: 1px solid rgba(0, 212, 255, 0.2);
            border-radius: 16px;
            padding: 2.5rem;
        }

        .conclusion-card p {
            color: var(--text-secondary);
            line-height: 1.8;
            margin: 0;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .module-hero-content { padding: 2.5rem 1.5rem; }
            .objectives-grid,
            .units-grid { grid-template-columns: 1fr; }
            .prose-card,
            .action-list,
            .conclusion-card { padding: 1.5rem; }
            table.skills-matrix { font-size: 0.82rem; }
            table.skills-matrix th,
            table.skills-matrix td { padding: 0.6rem 0.5rem; }
        }
    </style>
</head>
<body>
    <div class="animated-bg"></div>

    <nav>
        <div class="container">
            <a href="/" class="logo">DIOGO • CYBER SEC</a>
            <ul class="nav-links">
                <li><a href="/">Home</a></li>
                <li><a href="/about-me.html">About Me</a></li>
                <li><a href="#overview">Overview</a></li>
                <li><a href="#objectives">Outcomes</a></li>
                <li><a href="#artefacts">Artefacts</a></li>
                <li><a href="#reflections">Reflections</a></li>
                <li><a href="#skills-matrix">Skills</a></li>
                <li><a href="#action-plan">Action Plan</a></li>
            </ul>
            <button class="mobile-menu-btn" aria-label="Open navigation menu">&#9776;</button>
        </div>
    </nav>
    {% include mobile-nav.html %}

    <section class="module-hero">
        <div class="module-hero-content">
            <span class="module-badge">SECURITY &amp; RISK MANAGEMENT MODULE</span>
            <h1>Security &amp; Risk Management</h1>
            <p>
                This module focused on identifying, modelling, and quantifying risk in socio-technical systems, then
                translating analysis into proportionate controls and continuity strategies. It covered NIST CSF and
                STRIDE for threat modelling, FMEA and probability–impact matrices for prioritisation, EMV and Monte
                Carlo for quantitative modelling, and GDPR-aligned governance with explicit RTO/RPO targets for BC/DR.
            </p>
        </div>
    </section>

    <div class="main-content">

        <!-- Module Overview -->
        <section id="overview">
            <div class="section-header">
                <h2>Module Overview</h2>
                <div class="divider"></div>
                <p>Defensible, metrics-driven risk management across the socio-technical stack</p>
            </div>

            <div class="prose-card">
                <p>
                    This module synthesised my approach to defensible, metrics-driven risk management: coherent threat
                    modelling, quantitative justification of investment, prescriptive controls with ownership, and
                    verifiable continuity. Tutor feedback directly shaped the action plan to improve control specificity,
                    model transparency, resilience evidence, and GDPR operationalisation.
                </p>
            </div>
        </section>

        <!-- Module Learning Outcomes -->
        <section id="objectives">
            <div class="section-header">
                <h2>Module Learning Outcomes</h2>
                <div class="divider"></div>
                <p>The five outcomes assessed by this module</p>
            </div>

            <div class="objectives-grid">
                <div class="objective-card">
                    <div class="objective-icon">🧩</div>
                    <h4>Threat &amp; Risk Analysis</h4>
                    <p>Identify and analyse threats using STRIDE; prioritise risks with FMEA and probability–impact techniques.</p>
                </div>

                <div class="objective-card">
                    <div class="objective-icon">📈</div>
                    <h4>Quantitative Modelling</h4>
                    <p>Quantify risk with Expected Monetary Value and Monte Carlo simulations to justify security investment.</p>
                </div>

                <div class="objective-card">
                    <div class="objective-icon">🛡️</div>
                    <h4>Prescriptive Control Design</h4>
                    <p>Design controls mapped to risk appetite, KPIs (MTTD/MTTR), ownership, and GDPR (privacy by design/by default).</p>
                </div>

                <div class="objective-card">
                    <div class="objective-icon">🔄</div>
                    <h4>Resilience &amp; Continuity</h4>
                    <p>Develop BC/DR strategies with explicit RTO/RPO targets and tested failover procedures.</p>
                </div>

                <div class="objective-card">
                    <div class="objective-icon">🗣️</div>
                    <h4>Executive Communication</h4>
                    <p>Communicate findings to technical and executive audiences via structured reports and summaries.</p>
                </div>
            </div>
        </section>

        <!-- Key Artefacts -->
        <section id="artefacts">
            <div class="section-header">
                <h2>Key Artefacts</h2>
                <div class="divider"></div>
                <p>Summative submissions and tutor feedback</p>
            </div>

            <article class="artefact">
                <div class="artefact-header">
                    <span class="artefact-icon">🤝</span>
                    <div class="artefact-title">
                        <h3>Team Project — Pampered Pets Risk Identification Report (Group D)</h3>
                        <div class="badge-row">
                            <span class="unit-badge">TEAM SUMMATIVE</span>
                        </div>
                    </div>
                </div>
                <div class="artefact-content">
                    <p>
                        I contributed to a comprehensive risk assessment for a fictional digital transformation, framing
                        capabilities with NIST CSF and modelling threats via STRIDE, then using FMEA to prioritise
                        remediation. We addressed compliance, data protection, operational continuity, and stakeholder
                        engagement, proposing next steps for mitigation planning, testing, and continuous monitoring.
                    </p>
                    <div class="feedback-box">
                        <p>
                            <strong>📝 Feedback:</strong> Commended structure; strengthen by making controls more
                            prescriptive and explicitly linking each control to a risk, KPI, and owner.
                        </p>
                    </div>
                </div>
            </article>

            <article class="artefact">
                <div class="artefact-header">
                    <span class="artefact-icon">📊</span>
                    <div class="artefact-title">
                        <h3>Individual Executive Summary — Security Risk Management</h3>
                        <div class="badge-row">
                            <span class="unit-badge">INDIVIDUAL SUMMATIVE</span>
                        </div>
                    </div>
                </div>
                <div class="artefact-content">
                    <p>
                        I integrated prior units into an executive-level report that quantified disruption and
                        quality-risk exposure using EMV and a 10,000-run Monte Carlo. Outputs informed a budget-aware
                        roadmap: QMS uplift and training, zero-trust enhancements, supplier diversification, and an
                        active-active BC/DR pattern aligned to sub-minute RTO/RPO.
                    </p>
                    <div class="feedback-box">
                        <p>
                            <strong>📝 Feedback:</strong> Clear linkage from analysis to actions; strong justification
                            of investment through quantitative evidence.
                        </p>
                    </div>
                </div>
            </article>

            <article class="artefact">
                <div class="artefact-header">
                    <span class="artefact-icon">🪞</span>
                    <div class="artefact-title">
                        <h3>Reflective Review — Professional Growth</h3>
                        <div class="badge-row">
                            <span class="unit-badge">REFLECTIVE</span>
                        </div>
                    </div>
                </div>
                <div class="artefact-content">
                    <p>
                        I evaluated my progression from a tool-centred practitioner to a strategy-oriented professional,
                        integrating ethics, analytics, and communication. I emphasised stakeholder engagement,
                        horizon-scanning, and pairing technical controls with compliance and user awareness.
                    </p>
                    <div class="feedback-box">
                        <p>
                            <strong>📝 Feedback:</strong> Recognised progress in integrating ethics, analytics, and
                            communication into a coherent professional narrative.
                        </p>
                    </div>
                </div>
            </article>
        </section>

        <!-- Reflections and Notes -->
        <section id="reflections">
            <div class="section-header">
                <h2>Reflections and Notes</h2>
                <div class="divider"></div>
                <p>Key takeaways shaping ongoing practice</p>
            </div>

            <div class="units-grid">
                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="icon">🧭</span>
                        <h3>Control traceability</h3>
                    </div>
                    <p>Added a STRIDE → control mapping with KPIs (e.g., % encryption coverage, MTTD/MTTR) and owners.</p>
                </div>

                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="icon">📐</span>
                        <h3>Quantitative rigour</h3>
                    </div>
                    <p>Documented Monte Carlo inputs, ranges, correlations, and sensitivity checks to support decisions.</p>
                </div>

                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="icon">🧪</span>
                        <h3>Resilience evidence</h3>
                    </div>
                    <p>Defined RTO/RPO targets and scheduled failover drills with logs for verification.</p>
                </div>

                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="icon">⚖️</span>
                        <h3>Governance &amp; GDPR</h3>
                    </div>
                    <p>Reinforced privacy-by-design practices through DPIAs, training, and periodic audits.</p>
                </div>
            </div>
        </section>

        <!-- Skills Matrix -->
        <section id="skills-matrix">
            <div class="section-header">
                <h2>Professional Skills Matrix (Learnt)</h2>
                <div class="divider"></div>
                <p>Capabilities developed through the module</p>
            </div>

            <div class="matrix-wrap">
                <table class="skills-matrix">
                    <thead>
                        <tr>
                            <th>Skill</th>
                            <th>Summary</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="skill-name">Risk Identification &amp; Modelling</td>
                            <td>Applied NIST CSF, STRIDE, and FMEA to surface and prioritise risks.</td>
                        </tr>
                        <tr>
                            <td class="skill-name">Quantitative Risk Analysis</td>
                            <td>Built EMV and Monte Carlo models; interpreted distributions and sensitivity findings.</td>
                        </tr>
                        <tr>
                            <td class="skill-name">Control Design &amp; KPIs</td>
                            <td>Linked controls to risks; defined ownership and measurable outcomes (MTTD/MTTR).</td>
                        </tr>
                        <tr>
                            <td class="skill-name">Resilience &amp; Continuity</td>
                            <td>Set RTO/RPO targets; planned and evaluated failover and restoration drills.</td>
                        </tr>
                        <tr>
                            <td class="skill-name">Governance &amp; Compliance</td>
                            <td>Embedded GDPR privacy-by-design/default; maintained audit-ready artefacts.</td>
                        </tr>
                        <tr>
                            <td class="skill-name">Executive Communication</td>
                            <td>Produced concise executive summaries and action-oriented roadmaps.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

        <!-- Action Plan -->
        <section id="action-plan">
            <div class="section-header">
                <h2>Action Plan</h2>
                <div class="divider"></div>
                <p>Concrete, time-bound goals derived from tutor feedback</p>
            </div>

            <ol class="action-list">
                <li>
                    <strong>Control specificity &amp; ownership.</strong>
                    Map each control to a STRIDE risk, KPI, and accountable owner; publish traceability.
                    <span class="target">Target: Dec 2025</span>
                </li>
                <li>
                    <strong>Quantitative model transparency.</strong>
                    Publish Monte Carlo assumptions, ranges, correlations, and sensitivity analysis.
                    <span class="target">Target: Dec 2025</span>
                </li>
                <li>
                    <strong>BC/DR evidence cadence.</strong>
                    Run quarterly failover tests; track RTO/RPO results and remediation actions.
                    <span class="target">Target: Jan 2026</span>
                </li>
                <li>
                    <strong>GDPR-by-design checklist.</strong>
                    Adopt a DPIA template and a one-page control checklist; audit quarterly.
                    <span class="target">Target: Jan 2026</span>
                </li>
            </ol>
        </section>

        <!-- Conclusion -->
        <section id="conclusion">
            <div class="section-header">
                <h2>Conclusion</h2>
                <div class="divider"></div>
            </div>

            <div class="conclusion-card">
                <p>
                    This module synthesised my approach to defensible, metrics-driven risk management: coherent threat
                    modelling, quantitative justification of investment, prescriptive controls with ownership, and
                    verifiable continuity. Tutor feedback directly shaped the action plan to improve control
                    specificity, model transparency, resilience evidence, and GDPR operationalisation.
                </p>
            </div>
        </section>

        <!-- References -->
        <section id="references">
            <div class="section-header">
                <h2>References</h2>
                <div class="divider"></div>
            </div>

            <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 16px; padding: 2rem 2.5rem;">
                <p style="color: var(--text-secondary); line-height: 1.7; font-size: 0.92rem; padding: 0.8rem 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); margin: 0;">ISO/IEC (2022) <em style="color: var(--text);">ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements</em>. Geneva: International Organization for Standardization.</p>
                <p style="color: var(--text-secondary); line-height: 1.7; font-size: 0.92rem; padding: 0.8rem 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); margin: 0;">ISO/IEC (2022) <em style="color: var(--text);">ISO/IEC 27005:2022 Information security, cybersecurity and privacy protection — Guidance on managing information security risks</em>. Geneva: International Organization for Standardization.</p>
                <p style="color: var(--text-secondary); line-height: 1.7; font-size: 0.92rem; padding: 0.8rem 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); margin: 0;">National Institute of Standards and Technology (2024) <em style="color: var(--text);">The NIST Cybersecurity Framework (CSF) 2.0</em>. NIST CSWP 29. Gaithersburg: NIST. Available at: <a href="https://doi.org/10.6028/NIST.CSWP.29" target="_blank" rel="noopener" style="color: var(--primary); text-decoration: none;">https://doi.org/10.6028/NIST.CSWP.29</a></p>
                <p style="color: var(--text-secondary); line-height: 1.7; font-size: 0.92rem; padding: 0.8rem 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); margin: 0;">Council of the European Union (2016) <em style="color: var(--text);">Regulation (EU) 2016/679 of the European Parliament and of the Council on the protection of natural persons with regard to the processing of personal data (General Data Protection Regulation)</em>. Brussels.</p>
                <p style="color: var(--text-secondary); line-height: 1.7; font-size: 0.92rem; padding: 0.8rem 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); margin: 0;">Hubbard, D.W. and Seiersen, R. (2016) <em style="color: var(--text);">How to Measure Anything in Cybersecurity Risk</em>. Hoboken: Wiley.</p>
                <p style="color: var(--text-secondary); line-height: 1.7; font-size: 0.92rem; padding: 0.8rem 0; margin: 0;">Shostack, A. (2014) <em style="color: var(--text);">Threat Modeling: Designing for Security</em>. Indianapolis: Wiley.</p>
            </div>
        </section>

    </div>

    <footer style="text-align: center; padding: 3rem 5%; border-top: 1px solid rgba(255,255,255,0.08); color: var(--text-secondary); font-size: 0.9rem;">
        <p>MSc Cyber Security Portfolio &mdash; Diogo Neno</p>
    </footer>

    <script>
        const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
        if (mobileMenuBtn) {
            mobileMenuBtn.addEventListener('click', () => {
                const overlay = document.getElementById('mobile-nav-overlay');
                if (overlay) {
                    overlay.classList.add('open');
                    document.body.style.overflow = 'hidden';
                    var firstLink = overlay.querySelector('a, button');
                    if (firstLink) firstLink.focus();
                }
            });
        }
    </script>
</body>
</html>
