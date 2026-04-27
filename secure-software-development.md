---
layout: null
title: Secure Software Development
description: Designing resilient products through secure-by-default SDLC practices
nav-menu: true
nav-order: 5
summary: >-
  Architecture-led approach to secure software development, UML-driven design,
  and assurance activities that embed security as a first-class requirement
  across the SDLC.
topic_tags:
  - Application Security
  - DevSecOps
---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{{ page.summary | strip_newlines | strip }}">
    <title>Secure Software Development | MSc Portfolio</title>
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

        .feedback-box p { margin-bottom: 0; color: var(--text-secondary); }

        .feedback-box strong { color: var(--warning); }

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
            margin-left: 0.4rem;
            padding: 0.1rem 0.6rem;
            border-radius: 50px;
            background: rgba(16, 185, 129, 0.15);
            color: var(--success);
            border: 1px solid rgba(16, 185, 129, 0.3);
            font-size: 0.78rem;
            font-weight: 600;
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
            vertical-align: top;
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

        table.skills-matrix td:first-child {
            color: var(--text);
            font-weight: 600;
        }

        table.skills-matrix tr:hover td {
            background: rgba(0, 212, 255, 0.03);
            color: var(--text);
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

        .references a {
            color: var(--primary);
            text-decoration: none;
            word-break: break-all;
        }

        .references a:hover { text-decoration: underline; }

        /* Responsive */
        @media (max-width: 768px) {
            .module-hero-content { padding: 2.5rem 1.5rem; }
            .objectives-grid { grid-template-columns: 1fr; }
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
                <li><a href="/about-me.html">About Me</a></li>
                <li><a href="#overview">Overview</a></li>
                <li><a href="#objectives">Outcomes</a></li>
                <li><a href="#artefacts">Artefacts</a></li>
                <li><a href="#action-plan">Action Plan</a></li>
                <li><a href="#skills-matrix">Skills</a></li>
            </ul>
            <button class="mobile-menu-btn" aria-label="Open navigation menu">&#9776;</button>
        </div>
    </nav>
    {% include mobile-nav.html %}

    <section class="module-hero">
        <div class="module-hero-content">
            <span class="module-badge">SECURE SOFTWARE DEVELOPMENT MODULE</span>
            <h1>Secure Software Development</h1>
            <p>
                This module emphasised incorporating security as a primary requirement throughout the software development lifecycle. Activities included UML modelling (use case, class, sequence), secure coding (authentication, authorisation, hashing, encryption, integrity checks), and supporting practices (testing, static analysis, documentation). The focus was on clear design rationale, modularity, and secure-by-default choices.
            </p>
        </div>
    </section>

    <div class="main-content">

        <!-- Module Overview -->
        <section id="overview">
            <div class="section-header">
                <h2>Module Overview</h2>
                <div class="divider"></div>
                <p>Architecture-led, secure-by-default delivery across the SDLC</p>
            </div>

            <div class="prose-card">
                <p>
                    Architecture-led approach to secure software development, UML-driven design, and assurance activities that embed security as a first-class requirement across the SDLC. The module combined design artefacts, secure coding implementation, and structured reflection to translate threat-modelling intent into working, testable code.
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
                    <h4>Secure UML Design</h4>
                    <p>Design secure systems with UML based on object-oriented principles and clearly articulated architectural rationale.</p>
                </div>

                <div class="objective-card">
                    <div class="objective-icon">🔐</div>
                    <h4>Secure Coding</h4>
                    <p>Use secure coding techniques such as password hashing, encryption, checksums, and RBAC, and justify design choices.</p>
                </div>

                <div class="objective-card">
                    <div class="objective-icon">🧪</div>
                    <h4>Testing &amp; Automation</h4>
                    <p>Integrate testing and automated quality gates to maintain code quality throughout the SDLC.</p>
                </div>

                <div class="objective-card">
                    <div class="objective-icon">⚙️</div>
                    <h4>Process Evaluation</h4>
                    <p>Evaluate development approaches (e.g., agile and waterfall), ensuring security from inception to delivery.</p>
                </div>

                <div class="objective-card">
                    <div class="objective-icon">🗣️</div>
                    <h4>Communication</h4>
                    <p>Communicate design and testing decisions to technical and non-technical audiences with clarity.</p>
                </div>
            </div>
        </section>

        <!-- Key Artefacts -->
        <section id="artefacts">
            <div class="section-header">
                <h2>Key Artefacts</h2>
                <div class="divider"></div>
                <p>Summative submissions with feedback received</p>
            </div>

            <article class="artefact">
                <div class="artefact-header">
                    <span class="artefact-icon">🧾</span>
                    <div class="artefact-title">
                        <h3>Development Team Project: Design Document</h3>
                        <div class="badge-row">
                            <span class="unit-badge">UNIT 3</span>
                        </div>
                    </div>
                </div>
                <div class="artefact-content">
                    <p>
                        Created a structured design using UML diagrams, highlighting security features (RBAC, password hashing in storage, file encryption, checksum, audit logging) guided by the CIA triad and least-privilege principles.
                    </p>
                    <div class="feedback-box">
                        <p>
                            <strong>📝 Feedback:</strong> Clear early emphasis on security with strong depth in diagrams; refine use-case relationships, add a cover page and ToC, include an upfront security features list, and standardise referencing.
                        </p>
                    </div>
                </div>
            </article>

            <article class="artefact">
                <div class="artefact-header">
                    <span class="artefact-icon">💻</span>
                    <div class="artefact-title">
                        <h3>Development Individual Project: Coding Output</h3>
                        <div class="badge-row">
                            <span class="unit-badge">UNIT 6</span>
                        </div>
                    </div>
                </div>
                <div class="artefact-content">
                    <p>
                        Developed a Python CLI implementing password hashing, encryption, checksums, timestamps, and RBAC, with unit tests and static/security analysis supported by README guidance and reports.
                    </p>
                    <div class="feedback-box">
                        <p>
                            <strong>📝 Feedback:</strong> Implementation covered most required mechanisms; future work should increase modularity, harden UX (secure password input, account governance, validation, lockouts), and add demo evidence with clearer documentation.
                        </p>
                    </div>
                </div>
            </article>

            <article class="artefact">
                <div class="artefact-header">
                    <span class="artefact-icon">🪞</span>
                    <div class="artefact-title">
                        <h3>Individual Reflective Submission</h3>
                        <div class="badge-row">
                            <span class="unit-badge">UNIT 6</span>
                        </div>
                    </div>
                </div>
                <div class="artefact-content">
                    <p>
                        Structured reflection using Rolfe's model, connecting methodology comparisons, UML practice, and secure-SDLC integration to actionable improvements.
                    </p>
                    <div class="feedback-box">
                        <p>
                            <strong>📝 Feedback:</strong> Well-structured and appropriately framed; deepen personal reflection, cite frameworks inline, define acronyms on first use, and enhance presentation formatting.
                        </p>
                    </div>
                </div>
            </article>
        </section>

        <!-- Action Plan -->
        <section id="action-plan">
            <div class="section-header">
                <h2>Action Plan</h2>
                <div class="divider"></div>
                <p>Concrete goals for the next 6&ndash;8 weeks</p>
            </div>

            <ol class="action-list">
                <li><strong>Design hygiene.</strong> Add cover page/ToC, introduce an upfront "Security Features" list, refine use-case relationships, define acronyms, and alphabetise references — evidenced by an updated design document and refreshed UML exports. <span class="target">Week 2</span></li>
                <li><strong>Modularity.</strong> Break the CLI into auth, crypto, storage, CLI, and models packages with updated imports and tests — confirmed via the repository tree and passing unit tests. <span class="target">Week 4</span></li>
                <li><strong>Hardening &amp; UX.</strong> Implement secure password input, governed account creation, file validation, retry limits, lockout, and richer audit logging — evidenced through new test cases, README notes, and sample audit logs. <span class="target">Week 5</span></li>
                <li><strong>Evidence &amp; docs.</strong> Record a short demo video, restructure the README for quick starts and task flows, and expand comments/docstrings — evidenced by the published video link, README diff, and improved linter scores. <span class="target">Week 3</span></li>
                <li><strong>Automation.</strong> Introduce pre-commit hooks (Black, Flake8, Bandit, Pylint) and a CI pipeline, tracking trend data — evidenced by pipeline logs, a badge, and committed hook configuration. <span class="target">Week 3</span></li>
                <li><strong>Reflection quality.</strong> Embed specific incidents, emotions, and corrected citations in the reflection, with the final document noting word count — evidenced by the revised submission. <span class="target">Week 2</span></li>
            </ol>
        </section>

        <!-- Skills Matrix -->
        <section id="skills-matrix">
            <div class="section-header">
                <h2>Professional Skills Matrix</h2>
                <div class="divider"></div>
                <p>Snapshot of current competency and growth focus</p>
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
                            <td>Secure design &amp; UML</td>
                            <td>Proficient level evidenced by clear use-case, class, and sequence diagrams with early security requirements; next step is refining relationships and standardising a pre-diagram "Security Features" list.</td>
                        </tr>
                        <tr>
                            <td>Secure coding (Python)</td>
                            <td>Proficient implementation of bcrypt/Fernet, checksums, timestamps, and RBAC; plan to improve via modular packaging and stronger validation plus lockout controls.</td>
                        </tr>
                        <tr>
                            <td>Testing &amp; automation</td>
                            <td>Progressing from developing to proficient with unit tests and static/security analysis in place; focus is on formalising pre-commit and CI to enforce coverage and quality gates.</td>
                        </tr>
                        <tr>
                            <td>Code quality &amp; maintainability</td>
                            <td>Currently developing, with Flake8/Pylint highlighting docstring and complexity gaps; action is to refactor into modules, add documentation, and simplify functions.</td>
                        </tr>
                        <tr>
                            <td>Technical communication &amp; documentation</td>
                            <td>Proficient communication through the design document and README; improvement focuses on scan-readability and producing a short demo video.</td>
                        </tr>
                        <tr>
                            <td>Reflective practice</td>
                            <td>At a developing stage, using Rolfe's model effectively; next step is adding personal challenges, decisions, emotions, and tighter citation placement.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

        <!-- References -->
        <section id="references">
            <div class="section-header">
                <h2>References</h2>
                <div class="divider"></div>
            </div>

            <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 16px; padding: 2rem 2.5rem;">
                <p style="color: var(--text-secondary); line-height: 1.7; font-size: 0.92rem; padding: 0.8rem 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); margin: 0;">ISO/IEC (2011) <em style="color: var(--text);">ISO/IEC 27034-1:2011 Information technology — Security techniques — Application security — Part 1: Overview and concepts</em>. Geneva: International Organization for Standardization.</p>
                <p style="color: var(--text-secondary); line-height: 1.7; font-size: 0.92rem; padding: 0.8rem 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); margin: 0;">McGraw, G. (2006) <em style="color: var(--text);">Software Security: Building Security In</em>. Boston: Addison-Wesley.</p>
                <p style="color: var(--text-secondary); line-height: 1.7; font-size: 0.92rem; padding: 0.8rem 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); margin: 0;">OWASP Foundation (2021) <em style="color: var(--text);">OWASP Application Security Verification Standard (ASVS) v4.0.3</em>. Available at: <a href="https://owasp.org/www-project-application-security-verification-standard/" target="_blank" rel="noopener" style="color: var(--primary); text-decoration: none;">https://owasp.org/www-project-application-security-verification-standard/</a></p>
                <p style="color: var(--text-secondary); line-height: 1.7; font-size: 0.92rem; padding: 0.8rem 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); margin: 0;">Saltzer, J.H. and Schroeder, M.D. (1975) 'The protection of information in computer systems', <em style="color: var(--text);">Proceedings of the IEEE</em>, 63(9), pp. 1278–1308.</p>
                <p style="color: var(--text-secondary); line-height: 1.7; font-size: 0.92rem; padding: 0.8rem 0; margin: 0;">Howard, M. and Lipner, S. (2006) <em style="color: var(--text);">The Security Development Lifecycle</em>. Redmond: Microsoft Press.</p>
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
