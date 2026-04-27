---
layout: null
title: Network Security
description: Defending communications infrastructure from evolving threats
nav-menu: true
nav-order: 3
summary: >-
  Highlights from audits and executive reporting that strengthened networked backup,
  failover, and encryption across enterprise environments.
topic_tags:
  - Network Defence
  - Threat Response
---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{{ page.summary | strip_newlines | strip }}">
    <title>Network Security &amp; Resilience | MSc Portfolio</title>
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

        /* Tech term inline tag */
        .tech-term {
            font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
            background: rgba(0, 212, 255, 0.1);
            color: var(--primary);
            padding: 0.1rem 0.45rem;
            border-radius: 4px;
            font-size: 0.9em;
            border: 1px solid rgba(0, 212, 255, 0.2);
        }

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
            color: #fff;
            font-size: 1.1rem;
            font-weight: 700;
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

        .evidence-box p { margin-bottom: 0; }

        .feedback-box {
            background: rgba(245, 158, 11, 0.05);
            border: 1px solid rgba(245, 158, 11, 0.2);
            border-radius: 8px;
            padding: 1rem 1.2rem;
        }

        .feedback-box p { margin-bottom: 0; color: var(--text-secondary); font-style: italic; }

        .feedback-box strong { color: var(--warning); font-style: normal; }

        .feedback-box.success {
            background: rgba(16, 185, 129, 0.05);
            border-color: rgba(16, 185, 129, 0.25);
        }

        .feedback-box.success strong { color: var(--success); }

        /* Unit / Reflection cards */
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
            gap: 1rem;
            margin-bottom: 1rem;
        }

        .unit-icon {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 40px;
            height: 40px;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            border-radius: 10px;
            font-size: 1.1rem;
            flex-shrink: 0;
        }

        .unit-card h3 {
            font-size: 1rem;
            font-weight: 600;
            color: #fff;
            line-height: 1.4;
        }

        .unit-card p {
            color: var(--text-secondary);
            font-size: 0.93rem;
            line-height: 1.7;
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
            line-height: 1.6;
        }

        table.skills-matrix tr:hover td {
            background: rgba(0, 212, 255, 0.03);
            color: var(--text);
        }

        table.skills-matrix td.competency {
            color: var(--primary);
            font-weight: 600;
            white-space: nowrap;
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

        .action-list .timeframe {
            display: inline-block;
            background: rgba(124, 58, 237, 0.15);
            color: var(--accent);
            padding: 0.15rem 0.6rem;
            border-radius: 50px;
            font-size: 0.72rem;
            font-weight: 700;
            border: 1px solid rgba(124, 58, 237, 0.3);
            margin-left: 0.5rem;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }

        /* Conclusion */
        .conclusion-card {
            background: linear-gradient(135deg, rgba(0, 212, 255, 0.08), rgba(124, 58, 237, 0.08));
            border: 1px solid rgba(0, 212, 255, 0.2);
            border-left: 4px solid var(--primary);
            border-radius: 16px;
            padding: 2.5rem;
        }

        .conclusion-card h2 {
            color: #fff;
            font-size: 1.6rem;
            margin-bottom: 1rem;
            font-weight: 700;
        }

        .conclusion-card p {
            color: var(--text-secondary);
            line-height: 1.8;
            font-size: 1.05rem;
        }

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
            .objectives-grid,
            .units-grid { grid-template-columns: 1fr; }
            .prose-card,
            .action-list,
            .references { padding: 1.5rem; }
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
                <li><a href="/about">About</a></li>
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
            <span class="module-badge">CYBER SECURITY MODULE</span>
            <h1>Network Security &amp; Resilience</h1>
            <p>
                This module focused on hardening networked backup systems and recovery planes. Key
                deliverables included identifying vulnerabilities in transit encryption, designing access
                controls for administration planes, and proving failover reliability across hybrid enterprise
                environments.
            </p>
        </div>
    </section>

    <div class="main-content">

        <!-- Module Overview -->
        <section id="overview">
            <div class="section-header">
                <h2>Module Overview</h2>
                <div class="divider"></div>
                <p>Hardening backup, failover, and encryption across enterprise networks</p>
            </div>

            <div class="prose-card">
                <p>
                    The module synthesised verifiable encryption and access control practices with dependable
                    backup, failover, and monitoring strategies. Audits and executive reporting were used to
                    convert technical findings into business-language recommendations spanning compliance,
                    risk, and recovery posture.
                </p>
                <p>
                    Tooling decisions were exercised in depth — comparing <span class="tech-term">Veeam</span>,
                    <span class="tech-term">Commvault</span>, <span class="tech-term">Rubrik</span>, and
                    <span class="tech-term">HashiCorp Vault</span> — alongside hands-on traffic and log
                    analysis with <span class="tech-term">Wireshark</span>, <span class="tech-term">Splunk</span>,
                    <span class="tech-term">Kali Linux</span>, <span class="tech-term">Nmap</span>, and
                    <span class="tech-term">Burp Suite</span>.
                </p>
            </div>
        </section>

        <!-- Module Learning Outcomes -->
        <section id="objectives">
            <div class="section-header">
                <h2>Module Learning Outcomes</h2>
                <div class="divider"></div>
                <p>The outcomes assessed by this module</p>
            </div>

            <div class="objectives-grid">
                <div class="objective-card">
                    <div class="objective-icon">🌐</div>
                    <h4>Threat Analysis</h4>
                    <p>Identify and analyse network security threats, selecting specific investigative methods to mitigate risks in data transmission and storage.</p>
                </div>
                <div class="objective-card">
                    <div class="objective-icon">🔐</div>
                    <h4>Control Evaluation</h4>
                    <p>Critically evaluate solutions for managing risks such as encryption, IAM (Identity Access Management), and continuous monitoring.</p>
                </div>
                <div class="objective-card">
                    <div class="objective-icon">⚖️</div>
                    <h4>Standards Alignment</h4>
                    <p>Align recommendations with organisational priorities and frameworks including <span class="tech-term">GDPR</span>, <span class="tech-term">ISO 27001</span>, and <span class="tech-term">NIST SP 800-34</span>.</p>
                </div>
            </div>
        </section>

        <!-- Key Artefacts -->
        <section id="artefacts">
            <div class="section-header">
                <h2>Key Artefacts &amp; Feedback</h2>
                <div class="divider"></div>
                <p>Audits, executive reports, and reflective submissions</p>
            </div>

            <article class="artefact">
                <div class="artefact-header">
                    <span class="artefact-icon">🛡️</span>
                    <div class="artefact-title">
                        <h3>Vulnerability Audit: Baseline Analysis</h3>
                        <div class="badge-row">
                            <span class="unit-badge">AUDIT</span>
                        </div>
                    </div>
                </div>
                <div class="artefact-content">
                    <p>
                        Established an initial risk baseline covering unencrypted data paths, weak access
                        controls, and ransomware exposure. Selected a security stack including
                        <span class="tech-term">Veeam</span>, <span class="tech-term">Commvault</span>,
                        <span class="tech-term">HashiCorp Vault</span>, and <span class="tech-term">Wireshark</span>
                        to deliver a six-week programme of configuration checks and restoration drills.
                    </p>
                    <div class="feedback-box">
                        <p>
                            <strong>🎓 Tutor feedback:</strong> "Demonstrated solid knowledge and application
                            to the case study; the next iteration should deepen supporting research and
                            academic referencing."
                        </p>
                    </div>
                </div>
            </article>

            <article class="artefact">
                <div class="artefact-header">
                    <span class="artefact-icon">📋</span>
                    <div class="artefact-title">
                        <h3>Executive Summary &amp; Recommendations</h3>
                        <div class="badge-row">
                            <span class="unit-badge">REPORT</span>
                        </div>
                    </div>
                </div>
                <div class="artefact-content">
                    <p>
                        Reported on weaknesses across password policies, outdated software, and backup
                        reliability. Recommended strengthening encryption, improving failover coverage, and
                        institutionalising regular testing.
                    </p>
                    <div class="feedback-box success">
                        <p>
                            <strong>✅ Tutor feedback:</strong> "Praised for clear structure and sourcing;
                            highlighted effective discussion of methods and linkage between recommendations
                            and findings."
                        </p>
                    </div>
                </div>
            </article>

            <article class="artefact">
                <div class="artefact-header">
                    <span class="artefact-icon">📝</span>
                    <div class="artefact-title">
                        <h3>Individual Reflective Piece</h3>
                        <div class="badge-row">
                            <span class="unit-badge">REFLECTION</span>
                        </div>
                    </div>
                </div>
                <div class="artefact-content">
                    <p>
                        Reflected on tooling decisions (comparing <span class="tech-term">Rubrik</span> vs
                        <span class="tech-term">Veeam</span>) and the value of peer support using
                        <span class="tech-term">Kali Linux</span>, <span class="tech-term">Nmap</span>, and
                        <span class="tech-term">Burp Suite</span>. Identified opportunities to deepen
                        critical analysis.
                    </p>
                    <div class="feedback-box">
                        <p>
                            <strong>🚀 Growth area:</strong> "Encouraged broader discussion of collaboration
                            and attention to alphabetical referencing in both application and presentation
                            materials."
                        </p>
                    </div>
                </div>
            </article>
        </section>

        <!-- Core Reflections -->
        <section id="reflections">
            <div class="section-header">
                <h2>Core Reflections</h2>
                <div class="divider"></div>
                <p>Themes consolidated across the module</p>
            </div>

            <div class="units-grid">
                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="unit-icon">🛠️</span>
                        <h3>Tool–Risk Linkage</h3>
                    </div>
                    <p>Clarified how <span class="tech-term">Wireshark</span> validated secured transmissions and how <span class="tech-term">Splunk</span> surfaced log anomalies to prove control effectiveness.</p>
                </div>

                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="unit-icon">📚</span>
                        <h3>Standards Alignment</h3>
                    </div>
                    <p>Ensured recommendations were traceable to <span class="tech-term">ISO/IEC 27031</span> and <span class="tech-term">NIST SP 800-34</span> for continuity, recovery, and legal assurance.</p>
                </div>

                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="unit-icon">🗣️</span>
                        <h3>Communication</h3>
                    </div>
                    <p>Executive-facing materials emphasised business impacts — downtime, data loss, and legal exposure — paired with plain-language actions.</p>
                </div>

                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="unit-icon">🤝</span>
                        <h3>Collaboration</h3>
                    </div>
                    <p>Supporting a peer with <span class="tech-term">Kali</span> and <span class="tech-term">Burp Suite</span> walkthroughs sharpened my explanations and reinforced shared understanding.</p>
                </div>
            </div>
        </section>

        <!-- Skills Matrix -->
        <section id="skills-matrix">
            <div class="section-header">
                <h2>Skills Matrix</h2>
                <div class="divider"></div>
                <p>Competencies exercised through module artefacts</p>
            </div>

            <div class="matrix-wrap">
                <table class="skills-matrix">
                    <thead>
                        <tr>
                            <th>Competency</th>
                            <th>Application in Module</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="competency">Risk &amp; Exposure Analysis</td>
                            <td>Enumerated risks including unencrypted data paths, weak access controls, ransomware, and testing gaps.</td>
                        </tr>
                        <tr>
                            <td class="competency">Tooling &amp; Validation</td>
                            <td>Integrated <span class="tech-term">Veeam</span> and <span class="tech-term">Commvault</span> workflows; used <span class="tech-term">Vault</span> for keys; <span class="tech-term">Wireshark</span> for traffic validation.</td>
                        </tr>
                        <tr>
                            <td class="competency">Compliance Strategy</td>
                            <td>Situated recommendations within <span class="tech-term">GDPR</span> and <span class="tech-term">ISO 27001</span> to balance resilience and regulatory expectations.</td>
                        </tr>
                        <tr>
                            <td class="competency">Planning &amp; Testing</td>
                            <td>Developed a six-week roadmap covering integrity verification, monitoring, key management, and restoration drills.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

        <!-- Action Plan -->
        <section id="action-plan">
            <div class="section-header">
                <h2>Development Action Plan</h2>
                <div class="divider"></div>
                <p>Concrete, time-bound goals derived from module feedback</p>
            </div>

            <ol class="action-list">
                <li><strong>Strengthen Research.</strong> Incorporate recent empirical studies and add in-text citations beyond core standards to reinforce recommendations. <span class="timeframe">Dec 2025</span></li>
                <li><strong>Link Findings.</strong> Pair each identified weakness with a specific control, KPI, and enforcement cadence (e.g., password policies vs. audit frequency). <span class="timeframe">Dec 2025</span></li>
                <li><strong>Tooling Analysis.</strong> Produce comparative matrices (e.g., <span class="tech-term">Rubrik</span> vs <span class="tech-term">Veeam</span>) to evidence critical evaluation of vendor capabilities. <span class="timeframe">Jan 2026</span></li>
                <li><strong>Evidence Dashboards.</strong> Track backup test success rates and mean time to recovery (MTTR) via quarterly dashboards. <span class="timeframe">Jan 2026</span></li>
            </ol>
        </section>

        <!-- Conclusion -->
        <section id="conclusion">
            <div class="conclusion-card">
                <h2>Conclusion</h2>
                <p>
                    This module synthesised verifiable encryption and access control practices with
                    dependable backup, failover, and monitoring strategies. By linking technical actions to
                    business risk, compliance posture, and measurable outcomes, I advanced my capability to
                    guide enterprise network resilience.
                </p>
            </div>
        </section>

        <!-- References -->
        <section id="references">
            <div class="section-header">
                <h2>References</h2>
                <div class="divider"></div>
            </div>

            <div class="references">
                <p>International Organization for Standardization (2013) <em>ISO/IEC 27001: Information security management systems — Requirements</em>. Geneva: ISO.</p>
                <p>International Organization for Standardization (2011) <em>ISO/IEC 27031: Guidelines for information and communication technology readiness for business continuity</em>. Geneva: ISO.</p>
                <p>National Institute of Standards and Technology (2010) <em>NIST SP 800-34 Rev. 1: Contingency Planning Guide for Federal Information Systems</em>. Gaithersburg, MD: NIST.</p>
                <p>European Parliament and Council (2016) <em>Regulation (EU) 2016/679 (General Data Protection Regulation)</em>. Brussels: Official Journal of the European Union.</p>
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
