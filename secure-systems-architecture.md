---
layout: null
title: Secure Systems Architecture
description: Designing resilient platforms through layered security patterns
nav-menu: true
nav-order: 7
summary: >-
  Architecture-led approach to threat modelling, control selection, and
  verification across complex CPS/IoT systems-of-systems.
topic_tags:
  - Systems Design
  - Zero Trust
---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{{ page.summary | strip_newlines | strip }}">
    <title>Secure Systems Architecture | MSc Portfolio</title>
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
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
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
            font-size: 1.05rem;
            font-weight: 600;
            color: #fff;
            margin-bottom: 0.6rem;
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
            font-size: 1.1rem;
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

        .evidence-box p { margin-bottom: 0; color: var(--text-secondary); }

        .evidence-box strong { color: var(--primary); }

        .feedback-box {
            background: rgba(245, 158, 11, 0.05);
            border: 1px solid rgba(245, 158, 11, 0.2);
            border-radius: 8px;
            padding: 1rem 1.2rem;
            margin-top: 0.6rem;
        }

        .feedback-box p { margin-bottom: 0; color: var(--text-secondary); line-height: 1.7; }

        .feedback-box strong { color: var(--warning); }

        .feedback-success {
            background: rgba(16, 185, 129, 0.06);
            border-color: rgba(16, 185, 129, 0.25);
        }

        .feedback-success strong { color: var(--success); }

        .feedback-info {
            background: rgba(0, 212, 255, 0.05);
            border-color: rgba(0, 212, 255, 0.25);
        }

        .feedback-info strong { color: var(--primary); }

        /* Tables (Action Plan + Skills Matrix) */
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
            font-size: 0.9rem;
            min-width: 720px;
        }

        table.skills-matrix th,
        table.skills-matrix td {
            padding: 0.85rem 1rem;
            text-align: left;
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
            vertical-align: top;
        }

        table.skills-matrix th {
            color: var(--primary);
            font-weight: 700;
            text-transform: uppercase;
            font-size: 0.78rem;
            letter-spacing: 0.05em;
            border-bottom: 2px solid rgba(0, 212, 255, 0.3);
            white-space: nowrap;
        }

        table.skills-matrix td {
            color: var(--text-secondary);
            line-height: 1.6;
        }

        table.skills-matrix td strong { color: var(--text); }

        table.skills-matrix tr:hover td {
            background: rgba(0, 212, 255, 0.03);
            color: var(--text);
        }

        table.skills-matrix th button {
            background: none;
            border: none;
            font: inherit;
            color: inherit;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            padding: 0;
            text-transform: inherit;
            letter-spacing: inherit;
        }

        table.skills-matrix th button:hover {
            color: var(--accent);
        }

        table.skills-matrix th button:focus-visible {
            outline: 2px solid var(--primary);
            outline-offset: 2px;
            border-radius: 4px;
        }

        .level {
            display: inline-block;
            padding: 0.15rem 0.6rem;
            border-radius: 50px;
            font-size: 0.78rem;
            font-weight: 600;
        }

        .level.proficient { background: rgba(16, 185, 129, 0.15); color: var(--success); border: 1px solid rgba(16, 185, 129, 0.3); }

        .proficiency-bar {
            width: 100%;
            max-width: 160px;
            height: 6px;
            background: rgba(255, 255, 255, 0.08);
            border-radius: 999px;
            overflow: hidden;
            margin-top: 0.5rem;
        }

        .proficiency-fill {
            height: 100%;
            background: linear-gradient(90deg, var(--primary), var(--accent));
            border-radius: 999px;
            transition: width 0.6s ease-out;
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

        /* Reflection Highlights panel */
        .reflection-panel {
            background: linear-gradient(135deg, rgba(0, 212, 255, 0.08), rgba(124, 58, 237, 0.1));
            border: 1px solid rgba(0, 212, 255, 0.2);
            border-radius: 16px;
            padding: 2.5rem;
        }

        .reflection-panel p {
            color: var(--text-secondary);
            line-height: 1.8;
            margin-bottom: 1.2rem;
            font-size: 1.02rem;
        }

        .reflection-panel p:last-child { margin-bottom: 0; }

        /* References */
        .references {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 2rem 2.5rem;
        }

        .references p {
            color: var(--text-secondary);
            line-height: 1.7;
            font-size: 0.92rem;
            padding: 0.8rem 0;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }

        .references p:last-child { border-bottom: none; }

        .references em { color: var(--text); }

        /* Responsive */
        @media (max-width: 768px) {
            .module-hero-content { padding: 2.5rem 1.5rem; }
            .objectives-grid { grid-template-columns: 1fr; }
            .prose-card,
            .action-list,
            .references,
            .reflection-panel { padding: 1.5rem; }
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
                <li><a href="#learning-outcomes">Outcomes</a></li>
                <li><a href="#artefacts">Artefacts</a></li>
                <li><a href="#action-plan">Action Plan</a></li>
                <li><a href="#skills-matrix">Skills</a></li>
                <li><a href="#reflection">Reflection</a></li>
            </ul>
            <button class="mobile-menu-btn" aria-label="Open navigation menu">&#9776;</button>
        </div>
    </nav>
    {% include mobile-nav.html %}

    <section class="module-hero">
        <div class="module-hero-content">
            <span class="module-badge">SECURE SYSTEMS ARCHITECTURE MODULE</span>
            <h1>Secure Systems Architecture</h1>
            <p>
                This module concentrated on designing and evaluating secure systems-of-systems (SoS) in CPS/IoT contexts. It integrated architectural thinking (CIA triad with ABCDE characteristics), threat modelling (AD-Trees with quantitative scoring), and a secure IoT messaging prototype, emphasising defensible trade-offs, layered controls, and evidence-driven evaluation under real-world constraints (latency, loss, scale).
            </p>
            <p>
                Work spanned strategic design reviews, quantitative risk analysis, and hands-on development of authenticated encryption pipelines. Feedback drove refinements in diagram quality, risk traceability, and the presentation of cost-benefit considerations for blockchain-enabled IoT platforms.
            </p>
        </div>
    </section>

    <div class="main-content">

        <!-- Module Overview -->
        <section id="overview">
            <div class="section-header">
                <h2>Module Overview</h2>
                <div class="divider"></div>
                <p>Architecture, threat modelling, and authenticated encryption for CPS/IoT systems</p>
            </div>

            <div class="prose-card">
                <p>
                    The module brought together strategic and engineering perspectives on securing complex
                    systems-of-systems. Strategic work mapped CIA priorities to the ABCDE characteristics
                    (Autonomy, Belonging, Connectivity, Diversity, Emergence) for blockchain-integrated CPS/IoT
                    platforms, while engineering work produced a Python simulation of AES-GCM authenticated
                    encryption with realistic loss, latency, and adversarial conditions.
                </p>
                <p>
                    Standards and frameworks referenced across the artefacts include <strong>ISO 27001</strong>,
                    the <strong>NIST Cybersecurity Framework</strong>, <strong>GDPR</strong>, and the
                    <strong>CIA triad</strong>. Threat modelling used Attack-Defence Trees with quantitative
                    DREAD/DSS scoring to justify mitigation sequencing, and assurance was driven by Bandit,
                    Flake8, and Pytest with coverage tracking.
                </p>
            </div>
        </section>

        <!-- Module Learning Outcomes -->
        <section id="learning-outcomes">
            <div class="section-header">
                <h2>Module Learning Outcomes</h2>
                <div class="divider"></div>
                <p>Core competencies developed through the module</p>
            </div>

            <div class="objectives-grid">
                <div class="objective-card">
                    <div class="objective-icon">🏛️</div>
                    <h4>Architectural Alignment</h4>
                    <p>Design secure CPS/IoT architectures by aligning CIA priorities with ABCDE characteristics and SoS constraints.</p>
                </div>
                <div class="objective-card">
                    <div class="objective-icon">📊</div>
                    <h4>Quantitative Threat Modelling</h4>
                    <p>Prioritise threats through AD-Trees and quantitative scoring (DREAD/DSS) to justify the sequencing of mitigations.</p>
                </div>
                <div class="objective-card">
                    <div class="objective-icon">🔐</div>
                    <h4>Secure Communications Engineering</h4>
                    <p>Implement authenticated encryption with sound object-oriented design, integrating replay protection and resilience to loss.</p>
                </div>
                <div class="objective-card">
                    <div class="objective-icon">✅</div>
                    <h4>Testing &amp; Quality Gates</h4>
                    <p>Integrate automated testing, coverage targets, and security tooling to assure reliability under adverse conditions.</p>
                </div>
                <div class="objective-card">
                    <div class="objective-icon">🗣️</div>
                    <h4>Evidence-led Communication</h4>
                    <p>Communicate architectural decisions, trade-offs, and testing results to technical and non-technical audiences with supporting evidence.</p>
                </div>
            </div>
        </section>

        <!-- Key Artefacts -->
        <section id="artefacts">
            <div class="section-header">
                <h2>Key Artefacts</h2>
                <div class="divider"></div>
                <p>Deliverables with tutor commentary and growth actions</p>
            </div>

            <article class="artefact">
                <div class="artefact-header">
                    <span class="artefact-icon">🧱</span>
                    <div class="artefact-title">
                        <h3>Development Team Project — Design Document</h3>
                        <div class="badge-row">
                            <span class="unit-badge">UNIT 3</span>
                        </div>
                    </div>
                </div>
                <div class="artefact-content">
                    <p>
                        Architecture for a blockchain-integrated CPS/IoT system-of-systems identified key
                        vulnerabilities and mapped mitigations via AD-Trees (client node, controller/hub, overall
                        SoS). Controls included multi-factor authentication, Zero Trust patterns, and layered
                        detection aligned to quantified DREAD/DSS scores.
                    </p>
                    <div class="feedback-box feedback-info">
                        <p>
                            <strong>Feedback.</strong> Strong understanding of SoS security challenges and CIA/ABCDE
                            framing; improve by explicitly linking each vulnerability to ABCDE traits and replacing
                            placeholder diagrams with polished figures.
                        </p>
                    </div>
                </div>
            </article>

            <article class="artefact">
                <div class="artefact-header">
                    <span class="artefact-icon">💻</span>
                    <div class="artefact-title">
                        <h3>Development Individual Project — Code Development</h3>
                        <div class="badge-row">
                            <span class="unit-badge">UNIT 6</span>
                        </div>
                    </div>
                </div>
                <div class="artefact-content">
                    <p>
                        Built a modular Python simulation of secure IoT communication focused on confidentiality
                        within the ABCDE model. Async components (controller, device, network, packet) used AES-GCM
                        with unique nonces, injected loss and delay, and surfaced metrics. Bandit, Flake8, and Pytest
                        underpinned quality assurance, with documentation detailing experiments and results.
                    </p>
                    <div class="feedback-box feedback-success">
                        <p>
                            <strong>Feedback.</strong> Commended for clear structure, realistic mitigation rationale,
                            and effective automation; next steps include adding replay detection, key rotation, and
                            deeper chaos testing scenarios.
                        </p>
                    </div>
                </div>
            </article>

            <article class="artefact">
                <div class="artefact-header">
                    <span class="artefact-icon">📝</span>
                    <div class="artefact-title">
                        <h3>Individual Reflective Submission</h3>
                        <div class="badge-row">
                            <span class="unit-badge">UNIT 6</span>
                        </div>
                    </div>
                </div>
                <div class="artefact-content">
                    <p>
                        Captured lessons on secure architecture for blockchain-enabled CPS/IoT deployments,
                        translating tutor feedback into an action plan for automated testing, AD-Tree enhancements,
                        and tighter ABCDE linkage. Reflections examined team collaboration, delegation, and growth
                        areas.
                    </p>
                    <div class="feedback-box">
                        <p>
                            <strong>Feedback.</strong> Analytical tone and theory integration were strong; add
                            concrete outcome examples, quantify improvements, and reference recent sources with
                            consistent citation formatting.
                        </p>
                    </div>
                </div>
            </article>
        </section>

        <!-- Action Plan -->
        <section id="action-plan">
            <div class="section-header">
                <h2>Action Plan (next 6–8 weeks)</h2>
                <div class="divider"></div>
                <p>Prioritised improvements driven by feedback and observed gaps</p>
            </div>

            <div class="matrix-wrap">
                <table class="skills-matrix" id="action-table">
                    <thead>
                        <tr>
                            <th scope="col">
                                <button type="button" data-sort="area" aria-label="Sort by action area">
                                    Action area
                                    <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg>
                                </button>
                            </th>
                            <th scope="col">What will be done</th>
                            <th scope="col">Evidence of completion</th>
                            <th scope="col">
                                <button type="button" data-sort="date" aria-label="Sort by target date">
                                    Target date
                                    <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg>
                                </button>
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>ABCDE linkage &amp; visuals</strong></td>
                            <td>Map each vulnerability to ABCDE attributes, regenerate AD-Trees via Graphviz or diagram tooling, remove placeholder artefacts, and standardise figure styling.</td>
                            <td>Appendix table (vulnerability → ABCDE) and refreshed diagram set in the design document.</td>
                            <td data-date="2">Week 2</td>
                        </tr>
                        <tr>
                            <td><strong>Trade-off analysis</strong></td>
                            <td>Add quantified discussion on blockchain scalability, latency, and mitigation costs, including sensitivity analysis of DREAD/DSS inputs.</td>
                            <td>New trade-off subsection plus revised scores with sensitivity commentary.</td>
                            <td data-date="3">Week 3</td>
                        </tr>
                        <tr>
                            <td><strong>Comms hardening</strong></td>
                            <td>Introduce replay detection (sequence numbers), periodic key rotation, and X25519-based session key agreement layered on AES-GCM.</td>
                            <td>Passing automated tests, code diffs, and updated README crypto notes.</td>
                            <td data-date="4">Week 4</td>
                        </tr>
                        <tr>
                            <td><strong>Reliability testing</strong></td>
                            <td>Extend chaos scenarios (duplication, reordering, burst loss) and add Hypothesis property tests plus coverage targets.</td>
                            <td>CI badge, ≥85% coverage reports, and chaos test execution logs or screenshots.</td>
                            <td data-date="4">Week 4</td>
                        </tr>
                        <tr>
                            <td><strong>CI &amp; quality gates</strong></td>
                            <td>Implement pre-commit hooks (Black, Flake8, Bandit, Pytest) and GitHub Actions with artefact capture and metric trending.</td>
                            <td>Committed pre-commit config, CI pipeline history, and trend chart exports.</td>
                            <td data-date="3">Week 3</td>
                        </tr>
                        <tr>
                            <td><strong>Documentation polish</strong></td>
                            <td>Produce updated architecture and sequence diagrams, operating runbook, and Cite-Them-Right references with consistent styling.</td>
                            <td>Updated README/design document and alphabetised reference list.</td>
                            <td data-date="3">Week 3</td>
                        </tr>
                        <tr>
                            <td><strong>Reflection updates</strong></td>
                            <td>Add concrete collaboration examples, measurable impacts, and broadened perspectives backed by recent citations.</td>
                            <td>Revised reflective submission with in-text citations and word count noted.</td>
                            <td data-date="2">Week 2</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

        <!-- Professional Skills Matrix -->
        <section id="skills-matrix">
            <div class="section-header">
                <h2>Professional Skills Matrix (snapshot)</h2>
                <div class="divider"></div>
                <p>Current strengths with planned improvements aligned to feedback</p>
            </div>

            <div class="matrix-wrap">
                <table class="skills-matrix" id="skills-table">
                    <thead>
                        <tr>
                            <th scope="col">
                                <button type="button" data-sort="competency" aria-label="Sort by competency">
                                    Competency
                                    <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg>
                                </button>
                            </th>
                            <th scope="col">Current level</th>
                            <th scope="col">Evidence</th>
                            <th scope="col">Planned improvement</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>Systems architecture (CPS/IoT, SoS)</strong></td>
                            <td>
                                <span class="level proficient">Proficient</span>
                                <div class="proficiency-bar"><div class="proficiency-fill" style="width: 75%"></div></div>
                            </td>
                            <td>Coherent SoS design with CIA + ABCDE framing and comprehensive vulnerability analysis.</td>
                            <td>Explicit vulnerability-to-ABCDE mapping, polished diagrams, and deeper scalability trade-offs.</td>
                        </tr>
                        <tr>
                            <td><strong>Threat modelling &amp; quantification</strong></td>
                            <td>
                                <span class="level proficient">Proficient</span>
                                <div class="proficiency-bar"><div class="proficiency-fill" style="width: 75%"></div></div>
                            </td>
                            <td>AD-Trees for client, hub, and SoS layers with DREAD/DSS prioritisation.</td>
                            <td>Regenerate original figures, add sensitivity analysis, and clarify risk acceptance criteria.</td>
                        </tr>
                        <tr>
                            <td><strong>Secure comms engineering (Python)</strong></td>
                            <td>
                                <span class="level proficient">Proficient</span>
                                <div class="proficiency-bar"><div class="proficiency-fill" style="width: 80%"></div></div>
                            </td>
                            <td>Modular asyncio/websockets simulation with AES-GCM and resilient packet abstraction.</td>
                            <td>Add replay protection, key rotation with forward secrecy, and extended chaos scenarios.</td>
                        </tr>
                        <tr>
                            <td><strong>Testing &amp; assurance</strong></td>
                            <td>
                                <span class="level proficient">Proficient</span>
                                <div class="proficiency-bar"><div class="proficiency-fill" style="width: 75%"></div></div>
                            </td>
                            <td>Bandit, Flake8, Pytest, and scenario testing under packet loss and latency.</td>
                            <td>CI with quality gates, property-based tests, and ≥85% coverage tracking.</td>
                        </tr>
                        <tr>
                            <td><strong>Documentation &amp; academic practice</strong></td>
                            <td>
                                <span class="level proficient">Proficient</span>
                                <div class="proficiency-bar"><div class="proficiency-fill" style="width: 70%"></div></div>
                            </td>
                            <td>Clear README and design rationale with referenced sources.</td>
                            <td>Standardise diagram styles, apply Cite-Them-Right, and expand trade-off exposition.</td>
                        </tr>
                        <tr>
                            <td><strong>Collaboration &amp; reflective practice</strong></td>
                            <td>
                                <span class="level proficient">Proficient</span>
                                <div class="proficiency-bar"><div class="proficiency-fill" style="width: 75%"></div></div>
                            </td>
                            <td>Reflection linked theory to practice with actionable responses to feedback.</td>
                            <td>Include specific outcome metrics, cite impacts on delivery quality, and broaden perspectives.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

        <!-- Reflection Highlights -->
        <section id="reflection">
            <div class="section-header">
                <h2>Reflection Highlights</h2>
                <div class="divider"></div>
                <p>Key takeaways from the module</p>
            </div>

            <div class="reflection-panel">
                <p>
                    The module underscored the importance of connecting architectural artefacts with quantifiable
                    risk arguments. Tutor feedback highlighted the need for better diagram polish and clearer ABCDE
                    traceability, which now drive specific improvements in modelling collateral.
                </p>
                <p>
                    Implementing authenticated encryption with measurable chaos testing reinforced the value of
                    automation and telemetry in CPS/IoT environments. The next iteration will emphasise forward
                    secrecy, evidence-backed trade-off narratives, and showcasing the measurable impact of
                    collaborative changes.
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
                <p style="color: var(--text-secondary); line-height: 1.7; font-size: 0.92rem; padding: 0.8rem 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); margin: 0;">Council of the European Union (2016) <em style="color: var(--text);">Regulation (EU) 2016/679 of the European Parliament and of the Council on the protection of natural persons with regard to the processing of personal data (General Data Protection Regulation)</em>. Brussels.</p>
                <p style="color: var(--text-secondary); line-height: 1.7; font-size: 0.92rem; padding: 0.8rem 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); margin: 0;">Shostack, A. (2014) <em style="color: var(--text);">Threat Modeling: Designing for Security</em>. Indianapolis: Wiley.</p>
                <p style="color: var(--text-secondary); line-height: 1.7; font-size: 0.92rem; padding: 0.8rem 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); margin: 0;">National Institute of Standards and Technology (2007) <em style="color: var(--text);">NIST SP 800-38D Recommendation for Block Cipher Modes of Operation: Galois/Counter Mode (GCM) and GMAC</em>. Gaithersburg: NIST.</p>
                <p style="color: var(--text-secondary); line-height: 1.7; font-size: 0.92rem; padding: 0.8rem 0; margin: 0;">Howard, M. and LeBlanc, D. (2003) <em style="color: var(--text);">Writing Secure Code</em>. 2nd edn. Redmond: Microsoft Press.</p>
            </div>
        </section>

    </div>

    <footer style="text-align: center; padding: 3rem 5%; border-top: 1px solid rgba(255,255,255,0.08); color: var(--text-secondary); font-size: 0.9rem;">
        <p>MSc Cyber Security Portfolio &mdash; Diogo Neno</p>
    </footer>

    <script>
        // Mobile nav overlay open
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

        // Sortable tables
        function sortTable(table, columnIndex, direction) {
            const tbody = table.querySelector('tbody');
            const rows = Array.from(tbody.querySelectorAll('tr'));

            rows.sort((a, b) => {
                let aValue = a.cells[columnIndex].textContent.trim();
                let bValue = b.cells[columnIndex].textContent.trim();

                const aData = a.cells[columnIndex].getAttribute('data-date');
                const bData = b.cells[columnIndex].getAttribute('data-date');

                if (aData && bData) {
                    return direction === 'asc'
                        ? parseInt(aData) - parseInt(bData)
                        : parseInt(bData) - parseInt(aData);
                }

                return direction === 'asc'
                    ? aValue.localeCompare(bValue)
                    : bValue.localeCompare(aValue);
            });

            rows.forEach(row => tbody.appendChild(row));
        }

        document.querySelectorAll('th button[data-sort]').forEach(button => {
            let direction = 'asc';
            button.addEventListener('click', () => {
                const table = button.closest('table');
                const th = button.closest('th');
                const columnIndex = Array.from(th.parentElement.children).indexOf(th);
                direction = direction === 'asc' ? 'desc' : 'asc';
                button.setAttribute('aria-label', `Sort by ${button.textContent.trim()} ${direction === 'asc' ? 'ascending' : 'descending'}`);
                sortTable(table, columnIndex, direction);
                const svg = button.querySelector('svg');
                if (svg) svg.style.transform = direction === 'desc' ? 'rotate(180deg)' : 'rotate(0deg)';
            });
        });
    </script>
</body>
</html>
