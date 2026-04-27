---
layout: null
title: Research Methods and Professional Practice
description: Scientific method, research design, ethics, and evidence-based inquiry applied to misinformation detection
nav-menu: true
nav-order: 8
summary: >-
  e-Portfolio for the Research Methods and Professional Practice module — artefacts, unit reflections,
  evaluations, Skills Matrix, SWOT, and Action Plan. The 1,000-word reflective piece is submitted
  separately as a Word document.
topic_tags:
  - Academic Research
  - Professional Practice
---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{{ page.summary | strip_newlines | strip }}">
    <title>Research Methods and Professional Practice | MSc Portfolio</title>
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

        .submission-note {
            display: inline-block;
            margin-top: 1rem;
            padding: 0.6rem 1.2rem;
            background: rgba(124, 58, 237, 0.15);
            border: 1px solid rgba(124, 58, 237, 0.3);
            border-radius: 8px;
            color: var(--text);
            font-size: 0.92rem;
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

        .grade-badge {
            display: inline-block;
            background: rgba(16, 185, 129, 0.15);
            color: var(--success);
            padding: 0.2rem 0.8rem;
            border-radius: 50px;
            font-size: 0.75rem;
            font-weight: 700;
            border: 1px solid rgba(16, 185, 129, 0.3);
        }

        .artefact-content p {
            color: var(--text-secondary);
            line-height: 1.7;
            margin-bottom: 1rem;
        }

        .lo-tag {
            display: inline-block;
            background: rgba(0, 212, 255, 0.1);
            color: var(--primary);
            padding: 0.15rem 0.6rem;
            border-radius: 4px;
            font-size: 0.78rem;
            font-weight: 600;
            margin-right: 0.3rem;
        }

        .evidence-box {
            background: rgba(0, 212, 255, 0.05);
            border: 1px solid rgba(0, 212, 255, 0.2);
            border-radius: 8px;
            padding: 1rem 1.2rem;
            margin-bottom: 0.8rem;
        }

        .evidence-box p { margin-bottom: 0; }

        .evidence-box a {
            color: var(--primary);
            text-decoration: none;
            font-weight: 500;
        }

        .evidence-box a:hover { text-decoration: underline; }

        .feedback-box {
            background: rgba(245, 158, 11, 0.05);
            border: 1px solid rgba(245, 158, 11, 0.2);
            border-radius: 8px;
            padding: 1rem 1.2rem;
        }

        .feedback-box p { margin-bottom: 0; color: var(--text-secondary); }

        .feedback-box strong { color: var(--warning); }

        /* Unit Reflections */
        .units-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
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

        .unit-number {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 40px;
            height: 40px;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            border-radius: 10px;
            font-weight: 800;
            font-size: 0.85rem;
            color: #fff;
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

        /* Evaluation cards */
        .evaluation-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
            gap: 1.5rem;
        }

        .evaluation-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 2rem;
        }

        .evaluation-card h3 {
            font-size: 1.15rem;
            color: #fff;
            margin-bottom: 0.5rem;
        }

        .evaluation-card .grade-badge {
            margin-bottom: 1rem;
        }

        .evaluation-card p {
            color: var(--text-secondary);
            line-height: 1.7;
            font-size: 0.95rem;
        }

        /* Skills Matrix Table */
        .matrix-wrap {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 1.5rem;
            overflow-x: auto;
        }

        .matrix-key {
            background: rgba(124, 58, 237, 0.05);
            border-left: 3px solid var(--accent);
            padding: 1rem 1.5rem;
            border-radius: 8px;
            margin-bottom: 1.5rem;
            color: var(--text-secondary);
            font-size: 0.92rem;
            line-height: 1.7;
        }

        .matrix-key strong { color: var(--primary); }

        table.skills-matrix {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.9rem;
        }

        table.skills-matrix th,
        table.skills-matrix td {
            padding: 0.75rem 1rem;
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

        table.skills-matrix tr:hover td {
            background: rgba(0, 212, 255, 0.03);
            color: var(--text);
        }

        .level {
            display: inline-block;
            padding: 0.15rem 0.6rem;
            border-radius: 50px;
            font-size: 0.78rem;
            font-weight: 600;
        }

        .level.aware { background: rgba(245, 158, 11, 0.15); color: var(--warning); border: 1px solid rgba(245, 158, 11, 0.3); }
        .level.trained { background: rgba(0, 212, 255, 0.15); color: var(--primary); border: 1px solid rgba(0, 212, 255, 0.3); }
        .level.proficient { background: rgba(16, 185, 129, 0.15); color: var(--success); border: 1px solid rgba(16, 185, 129, 0.3); }
        .level.expert { background: rgba(124, 58, 237, 0.2); color: var(--accent); border: 1px solid rgba(124, 58, 237, 0.4); }

        /* SWOT */
        .swot-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.5rem;
        }

        .swot-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 1.8rem;
            transition: all 0.3s ease;
        }

        .swot-card:hover { transform: translateY(-4px); }

        .swot-card.s { border-top: 3px solid var(--success); }
        .swot-card.w { border-top: 3px solid var(--warning); }
        .swot-card.o { border-top: 3px solid var(--primary); }
        .swot-card.t { border-top: 3px solid var(--accent); }

        .swot-card h3 {
            color: #fff;
            font-size: 1.05rem;
            margin-bottom: 0.8rem;
            display: flex;
            align-items: center;
            gap: 0.6rem;
        }

        .swot-card p {
            color: var(--text-secondary);
            line-height: 1.7;
            font-size: 0.93rem;
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
            .objectives-grid,
            .units-grid,
            .evaluation-grid,
            .swot-grid { grid-template-columns: 1fr; }
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
                <li><a href="#artefacts">Artefacts</a></li>
                <li><a href="#units">Units</a></li>
                <li><a href="#evaluation">Evaluation</a></li>
                <li><a href="#skills-matrix">Skills</a></li>
                <li><a href="#swot">SWOT</a></li>
                <li><a href="#action-plan">Action Plan</a></li>
            </ul>
            <button class="mobile-menu-btn" aria-label="Open navigation menu">&#9776;</button>
        </div>
    </nav>
    {% include mobile-nav.html %}

    <section class="module-hero">
        <div class="module-hero-content">
            <span class="module-badge">RESEARCH MODULE</span>
            <h1>Research Methods and Professional Practice</h1>
            <p>
                e-Portfolio branch — module submission. This page covers the artefacts, unit reflections,
                evaluations of the summative submissions, and the Professional Development Plan
                (Skills Matrix, SWOT, Action Plan).
            </p>
            <span class="submission-note">📄 The 1,000-word reflective piece is submitted separately as a Word document.</span>
        </div>
    </section>

    <div class="main-content">

        <!-- Module Overview -->
        <section id="overview">
            <div class="section-header">
                <h2>Module Overview</h2>
                <div class="divider"></div>
                <p>Twelve units, two summative artefacts, and a thread of misinformation research</p>
            </div>

            <div class="prose-card">
                <p>
                    This module enhanced my skills in designing and evaluating research in computing. Through twelve
                    units, I explored the scientific method, research strategies, statistics, validity, and project
                    risk, culminating in a literature review and research proposal on misinformation detection in
                    social media.
                </p>
                <p style="margin-top: 1.5rem; color: var(--text);"><strong>Skills developed.</strong>
                    The module outlines skills including time management, commercial awareness, critical thinking and
                    analysis, decision-making, problem-solving, initiative, entrepreneurial thinking, and various forms
                    of communication and literacy. Each skill is linked to a self-assessment in the Skills Matrix below,
                    with subsequent artefacts and reflections providing supporting evidence.
                </p>
            </div>
        </section>

        <!-- Module Learning Outcomes -->
        <section id="objectives">
            <div class="section-header">
                <h2>Module Learning Outcomes</h2>
                <div class="divider"></div>
                <p>The four outcomes assessed by this module</p>
            </div>

            <div class="objectives-grid">
                <div class="objective-card">
                    <div class="objective-icon">⚖️</div>
                    <p><strong style="color: var(--primary);">LO 1.</strong> Evaluate the professional, legal, social, cultural, and ethical issues impacting computing professionals.</p>
                </div>
                <div class="objective-card">
                    <div class="objective-icon">📚</div>
                    <p><strong style="color: var(--primary);">LO 2.</strong> Evaluate academic investigation principles and apply them to a computing research topic.</p>
                </div>
                <div class="objective-card">
                    <div class="objective-icon">🔍</div>
                    <p><strong style="color: var(--primary);">LO 3.</strong> Critically evaluate existing literature, research design, methodology, and data analysis for the chosen topic.</p>
                </div>
                <div class="objective-card">
                    <div class="objective-icon">📝</div>
                    <p><strong style="color: var(--primary);">LO 4.</strong> Critically produce and evaluate a research proposal for the topic.</p>
                </div>
            </div>
        </section>

        <!-- Key Artefacts -->
        <section id="artefacts">
            <div class="section-header">
                <h2>Key Artefacts</h2>
                <div class="divider"></div>
                <p>Summative submissions, mandatory worksheets, and the reflective piece</p>
            </div>

            <!-- Unit 7 — Literature Review -->
            <article class="artefact">
                <div class="artefact-header">
                    <span class="artefact-icon">📖</span>
                    <div class="artefact-title">
                        <h3>Literature Review — Detecting Misinformation on Social Media</h3>
                        <div class="badge-row">
                            <span class="unit-badge">UNIT 7</span>
                            <span class="grade-badge">62% Merit</span>
                            <span class="lo-tag">LO 2</span>
                            <span class="lo-tag">LO 3</span>
                        </div>
                    </div>
                </div>
                <div class="artefact-content">
                    <p>
                        A literature review on automated misinformation detection, including content, propagation,
                        source-credibility, and hybrid retrieval methods, relating to the EU AI Act and UK Online Safety
                        Act. The search adhered to PRISMA 2020 standards across ACM DL, IEEE Xplore, ACL Anthology, and
                        Scopus.
                    </p>
                    <div class="evidence-box">
                        <p>
                            <strong>📁 Evidence:</strong>
                            <a href="/assets/ResearchModule/Literature%20Review.odt" target="_blank" rel="noopener">Literature Review.odt</a>
                        </p>
                    </div>
                    <div class="feedback-box">
                        <p>
                            <strong>✓ Tutor feedback:</strong> Highlighted good topic understanding but pointed out a fragmented
                            structure, weak PRISMA evidence, over-reliance on books, and templated content affecting originality.
                        </p>
                    </div>
                </div>
            </article>

            <!-- Unit 7 — Summary Measures -->
            <article class="artefact">
                <div class="artefact-header">
                    <span class="artefact-icon">📊</span>
                    <div class="artefact-title">
                        <h3>Summary Measures Worksheet</h3>
                        <div class="badge-row">
                            <span class="unit-badge">UNIT 7</span>
                            <span class="lo-tag">LO 3</span>
                        </div>
                    </div>
                </div>
                <div class="artefact-content">
                    <p>
                        Mandatory worksheet applying descriptive statistics — mean, standard deviation, median, quartiles,
                        IQR — to the Diet A vs Diet B dataset, and frequency analysis on the Brand × Area dataset.
                        Diet A had a higher and more consistent mean weight loss (5.34 kg, SD 2.54) than Diet B
                        (3.71 kg, SD 2.77).
                    </p>
                    <div class="evidence-box">
                        <p>
                            <strong>📁 Evidence:</strong>
                            <a href="/assets/ResearchModule/Summary%20Measures.xlsx" target="_blank" rel="noopener">Summary Measures.xlsx</a>
                        </p>
                    </div>
                </div>
            </article>

            <!-- Unit 8 — Hypothesis Testing -->
            <article class="artefact">
                <div class="artefact-header">
                    <span class="artefact-icon">📈</span>
                    <div class="artefact-title">
                        <h3>Hypothesis Testing Worksheet</h3>
                        <div class="badge-row">
                            <span class="unit-badge">UNIT 8</span>
                            <span class="lo-tag">LO 3</span>
                        </div>
                    </div>
                </div>
                <div class="artefact-content">
                    <p>
                        Mandatory worksheet applying inferential statistics. A paired t-test on filtration agents
                        (t(11) = −3.26, p ≈ 0.0076) rejected the null, identifying Agent 1 as significantly more
                        effective. A Welch t-test on bank cardholder income by sex showed no significant difference,
                        with the small n = 3 highlighting the limits of small-sample inference.
                    </p>
                    <div class="evidence-box">
                        <p>
                            <strong>📁 Evidence:</strong>
                            <a href="/assets/ResearchModule/Hyphothesis%20Testing.xlsx" target="_blank" rel="noopener">Hyphothesis Testing.xlsx</a>
                        </p>
                    </div>
                </div>
            </article>

            <!-- Unit 9 — Charts Worksheet -->
            <article class="artefact">
                <div class="artefact-header">
                    <span class="artefact-icon">📉</span>
                    <div class="artefact-title">
                        <h3>Charts Worksheet</h3>
                        <div class="badge-row">
                            <span class="unit-badge">UNIT 9</span>
                            <span class="lo-tag">LO 3</span>
                        </div>
                    </div>
                </div>
                <div class="artefact-content">
                    <p>
                        Mandatory worksheet on chart selection: percentage frequency bar charts for brand preference in
                        two demographics, interpreting competitive concentration. Emphasised how chart choice impacts
                        the validity of conclusions drawn.
                    </p>
                    <div class="evidence-box">
                        <p>
                            <strong>📁 Evidence:</strong>
                            <a href="/assets/ResearchModule/Charts%20Worksheet.xlsx" target="_blank" rel="noopener">Charts Worksheet.xlsx</a>
                        </p>
                    </div>
                </div>
            </article>

            <!-- Unit 10 — Research Proposal -->
            <article class="artefact">
                <div class="artefact-header">
                    <span class="artefact-icon">🎤</span>
                    <div class="artefact-title">
                        <h3>Research Proposal Presentation — Detecting Misinformation on Social Media</h3>
                        <div class="badge-row">
                            <span class="unit-badge">UNIT 10</span>
                            <span class="grade-badge">68% Merit</span>
                            <span class="lo-tag">LO 4</span>
                        </div>
                    </div>
                </div>
                <div class="artefact-content">
                    <p>
                        A 15-slide research proposal outlining a hybrid detector with calibration and selective
                        abstention, plus a governance mapping on transparency, audit, human oversight, security,
                        and data protection.
                    </p>
                    <div class="evidence-box">
                        <p>
                            <strong>📁 Evidence:</strong>
                            <a href="/assets/ResearchModule/Research%20Proposal.pptx" target="_blank" rel="noopener">Research Proposal.pptx</a>
                        </p>
                    </div>
                    <div class="feedback-box">
                        <p>
                            <strong>✓ Tutor feedback:</strong> Emphasised clear research questions and a strong artefact but pointed
                            out an under-developed methodology and an absent references slide despite citations.
                        </p>
                    </div>
                </div>
            </article>

            <!-- Unit 12 — Reflective Piece -->
            <article class="artefact">
                <div class="artefact-header">
                    <span class="artefact-icon">📝</span>
                    <div class="artefact-title">
                        <h3>Reflective Piece (Submission)</h3>
                        <div class="badge-row">
                            <span class="unit-badge">UNIT 12</span>
                            <span class="lo-tag">LO 1</span>
                        </div>
                    </div>
                </div>
                <div class="artefact-content">
                    <p>
                        A 1,000-word reflection on statistical analysis skills, the research methods process, and
                        personal/professional development, written using Rolfe et al.'s (2001) <em>What, So What, Now What</em>
                        framework. Submitted as a separate Word document.
                    </p>
                    <div class="evidence-box">
                        <p>
                            <strong>📁 Evidence:</strong>
                            <a href="/assets/ResearchModule/ReflectivePiece.docx" target="_blank" rel="noopener">ReflectivePiece.docx</a>
                        </p>
                    </div>
                </div>
            </article>
        </section>

        <!-- Unit Reflections -->
        <section id="units">
            <div class="section-header">
                <h2>Unit Reflections</h2>
                <div class="divider"></div>
                <p>Key takeaways across all twelve units</p>
            </div>

            <div class="units-grid">
                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="unit-number">01</span>
                        <h3>Introduction to Research Methods</h3>
                    </div>
                    <p>Differentiating inductive from deductive reasoning, I see ethical considerations as foundational obligations. This shift affects my empirical work planning.</p>
                </div>

                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="unit-number">02</span>
                        <h3>Research Questions, Literature Review and Proposal</h3>
                    </div>
                    <p>Practised turning broad topics into testable questions. The "RQ first, scope second" discipline showed when I rushed the proposal methodology to fit a slide budget.</p>
                </div>

                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="unit-number">03</span>
                        <h3>Methodology and Research Methods</h3>
                    </div>
                    <p>Compared quantitative, qualitative, and mixed-methods approaches against typical question shapes, revealing that a quantitative design suits my AI-driven misinformation thesis better.</p>
                </div>

                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="unit-number">04</span>
                        <h3>Case Studies, Focus Groups and Observations</h3>
                    </div>
                    <p>Observation methods have biases — like observer effects and sampling — so documenting protocol is as vital as data collection.</p>
                </div>

                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="unit-number">05</span>
                        <h3>Interviews, Surveys and Questionnaire Design</h3>
                    </div>
                    <p>Consider question wording as a tool that affects measurement, not just response rates. Pre- and post-testing should be habitual practices.</p>
                </div>

                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="unit-number">06</span>
                        <h3>Quantitative Methods: Descriptive and Inferential Statistics</h3>
                    </div>
                    <p>Re-grounded summary measures (mean, median, SD, IQR) were applied to the Diet A/B dataset for written interpretations.</p>
                </div>

                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="unit-number">07</span>
                        <h3>Inferential Statistics and Hypothesis Testing</h3>
                    </div>
                    <p>Applied paired t-tests, F-tests for variance, and Welch t-tests on datasets. The n = 3 income data exercise was a lesson in small-sample inference.</p>
                </div>

                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="unit-number">08</span>
                        <h3>Data Analysis and Visualisation</h3>
                    </div>
                    <p>Distinguished between descriptive and misleading visualisations. As an SRE, I read charts daily but seldom check their visual integrity.</p>
                </div>

                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="unit-number">09</span>
                        <h3>Validity and Generalisability in Research</h3>
                    </div>
                    <p>Internal and external validity, reliability, and associated threats are tied to the temporal-shift issue in misinformation detection.</p>
                </div>

                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="unit-number">10</span>
                        <h3>Research Writing</h3>
                    </div>
                    <p>Structured writing for a dissertation includes signposting, theoretical framing, and defended scope. The tutor's feedback on the literature review described it as "fragmented, itemised", impacting this unit's framing.</p>
                </div>

                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="unit-number">11</span>
                        <h3>Professional Development and e-Portfolio</h3>
                    </div>
                    <p>Completed the Skills Matrix, SWOT, and Action Plan; treated the portfolio as a continuous record.</p>
                </div>

                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="unit-number">12</span>
                        <h3>Project Management and Managing Risk</h3>
                    </div>
                    <p>Mapped a risk register to my proposal, including data licensing, compute, integration, and schedule with mitigations, influencing my dissertation scope.</p>
                </div>
            </div>
        </section>

        <!-- Evaluation of Submissions -->
        <section id="evaluation">
            <div class="section-header">
                <h2>Evaluation of Submissions</h2>
                <div class="divider"></div>
                <p>Critical self-assessment of the two summative artefacts</p>
            </div>

            <div class="evaluation-grid">
                <div class="evaluation-card">
                    <h3>Literature Review</h3>
                    <span class="grade-badge">62% Merit</span>
                    <p>
                        The review highlighted major task families and included current governance frameworks. However,
                        three weaknesses emerged. First, the PRISMA search lacked a flow diagram, reducing methodological
                        traceability. Second, I relied on books and industry guidance instead of the expected
                        peer-reviewed journals. Third, some sections became generic and list-like, compressing depth into
                        surface coverage. In future work, I would focus on a clear research question with a theoretical
                        framework, conduct a documented PRISMA search with clear criteria, and write in my voice from the
                        first draft.
                    </p>
                </div>

                <div class="evaluation-card">
                    <h3>Research Proposal Presentation</h3>
                    <span class="grade-badge">68% Merit</span>
                    <p>
                        The proposal presented clear aims, objectives, and research questions, with the hybrid
                        architecture diagram and governance mapping as key strengths. Two issues impacted the grade: the
                        methodology lacked detail, describing the evaluation without procedural steps for reproducibility,
                        and I missed a references slide, a presentation-level oversight. Both can be resolved with a
                        methodology slide and a formatted references slide in Harvard style.
                    </p>
                </div>
            </div>
        </section>

        <!-- Skills Matrix -->
        <section id="skills-matrix">
            <div class="section-header">
                <h2>Professional Skills Matrix</h2>
                <div class="divider"></div>
                <p>Self-assessment against the module competency framework</p>
            </div>

            <div class="matrix-wrap">
                <div class="matrix-key">
                    <strong>Level key:</strong>
                    <span class="level aware">Aware</span> general understanding ·
                    <span class="level trained">Trained</span> applies independently in some contexts ·
                    <span class="level proficient">Proficient</span> broad in-depth knowledge, minimal supervision ·
                    <span class="level expert">Expert</span> leads and trains others
                </div>

                <table class="skills-matrix">
                    <thead>
                        <tr>
                            <th>Competency Area</th>
                            <th>Skill</th>
                            <th>Level</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr><td>Communication &amp; Literacy</td><td>Express information to technical and non-technical audiences</td><td><span class="level proficient">Proficient</span></td></tr>
                        <tr><td>Communication &amp; Literacy</td><td>Create reports, diagrams, plans, manuals</td><td><span class="level proficient">Proficient</span></td></tr>
                        <tr><td>Commercial Awareness</td><td>Keep current with industry tools and emerging technology</td><td><span class="level proficient">Proficient</span></td></tr>
                        <tr><td>Commercial Awareness</td><td>Familiarity with codes of conduct (BCS / industry)</td><td><span class="level trained">Trained</span></td></tr>
                        <tr><td>Critical Thinking &amp; Analysis</td><td>Critically analyse complex ideas in computing</td><td><span class="level trained">Trained</span></td></tr>
                        <tr><td>Critical Thinking &amp; Analysis</td><td>Recognise gaps and seek additional information</td><td><span class="level proficient">Proficient</span></td></tr>
                        <tr><td>Ethical Awareness</td><td>Comply with applicable laws; maintain privacy and confidentiality</td><td><span class="level proficient">Proficient</span></td></tr>
                        <tr><td>Cultural Awareness</td><td>Act in the interest of the wider community</td><td><span class="level proficient">Proficient</span></td></tr>
                        <tr><td>Teamwork &amp; Leadership</td><td>Collaborate effectively in diverse teams</td><td><span class="level proficient">Proficient</span></td></tr>
                        <tr><td>Teamwork &amp; Leadership</td><td>Give and receive constructive feedback</td><td><span class="level trained">Trained</span></td></tr>
                        <tr><td>Decision Making &amp; Initiative</td><td>Decide on complex matters using multiple sources</td><td><span class="level proficient">Proficient</span></td></tr>
                        <tr><td>Numeracy</td><td>Inferential statistics and hypothesis testing</td><td><span class="level trained">Trained</span></td></tr>
                        <tr><td>IT &amp; Digital — SQL</td><td>Database querying</td><td><span class="level proficient">Proficient</span></td></tr>
                        <tr><td>IT &amp; Digital — Python</td><td>Programming and scripting</td><td><span class="level proficient">Proficient</span></td></tr>
                        <tr><td>IT &amp; Digital — Java</td><td>Programming</td><td><span class="level aware">Aware</span></td></tr>
                        <tr><td>IT &amp; Digital — R</td><td>Statistical computing</td><td><span class="level aware">Aware</span></td></tr>
                        <tr><td>IT &amp; Digital — noSQL</td><td>Document and key-value stores</td><td><span class="level trained">Trained</span></td></tr>
                        <tr><td>IT &amp; Digital — Git</td><td>Repository development and maintenance</td><td><span class="level proficient">Proficient</span></td></tr>
                        <tr><td>IT &amp; Digital — VLE / Office</td><td>Moodle, Word, Excel, e-library</td><td><span class="level proficient">Proficient</span></td></tr>
                        <tr><td>Project Management</td><td>Risk register, project life cycle, change management</td><td><span class="level trained">Trained</span></td></tr>
                        <tr><td>Critical Reflection</td><td>Self-assess and adjust</td><td><span class="level trained">Trained</span></td></tr>
                        <tr><td>Research</td><td>Literature search, synthesis, methodology design</td><td><span class="level trained">Trained</span></td></tr>
                    </tbody>
                </table>
            </div>
        </section>

        <!-- SWOT -->
        <section id="swot">
            <div class="section-header">
                <h2>SWOT Analysis</h2>
                <div class="divider"></div>
                <p>Honest assessment of where I stand entering the dissertation</p>
            </div>

            <div class="swot-grid">
                <div class="swot-card s">
                    <h3>💪 Strengths</h3>
                    <p>With a decade of site reliability engineering experience, my work is rooted in production reality. My multilingual skills and cloud certification enhance my commercial awareness. Daily practices include Git, scripting, and incident-driven decisions. Feedback from my MSc cohort and tutors has fostered a habit of embracing critique instead of deflecting it.</p>
                </div>

                <div class="swot-card w">
                    <h3>⚠️ Weaknesses</h3>
                    <p>Inferential statistical reasoning lags my descriptive skills; I read percentile charts daily but seldom conduct paired tests on the differences I assert as real. My academic writing is evolving, but under pressure, I revert to list-oriented drafting, as noted by my tutor. My R and qualitative methods are less developed compared to my quantitative tools.</p>
                </div>

                <div class="swot-card o">
                    <h3>🚀 Opportunities</h3>
                    <p>The MSc dissertation formalises evaluation methods (calibration, time-split, paired tests with confidence intervals) for work. Maintaining the reflection habit compounds module-on-module.</p>
                </div>

                <div class="swot-card t">
                    <h3>🛑 Threats</h3>
                    <p>Time pressure from full-time work and dissertation leads me to templated drafting, the tutor's concern. Without clear structure at the start, originality diminishes.</p>
                </div>
            </div>
        </section>

        <!-- Action Plan -->
        <section id="action-plan">
            <div class="section-header">
                <h2>Action Plan</h2>
                <div class="divider"></div>
                <p>Concrete, time-bound goals derived from the Skills Matrix and SWOT</p>
            </div>

            <ol class="action-list">
                <li><strong>PRISMA discipline.</strong> Before drafting a review chapter for the dissertation, create a search log, inclusion/exclusion criteria, and a PRISMA flow diagram.</li>
                <li><strong>Voice over template.</strong> Write prose in the first draft; use bullets only for genuine lists. Review each chapter draft.</li>
                <li><strong>Statistical formalisation.</strong> For system evaluations in the dissertation or at work: use paired tests against baselines, 95% confidence intervals, calibration metrics (Expected Calibration Error), and time-split evaluation. Review the dissertation evaluation chapter.</li>
                <li><strong>Living portfolio.</strong> Update the Skills Matrix, SWOT, and Action Plan after each module review instead of archiving.</li>
                <li><strong>Targeted skill gaps.</strong> Move R from <em>Aware</em> to <em>Trained</em> with a tutorial cycle; enhance qualitative methods literacy through one text. Review: mid-dissertation checkpoint.</li>
            </ol>
        </section>

        <!-- References -->
        <section id="references">
            <div class="section-header">
                <h2>References</h2>
                <div class="divider"></div>
            </div>

            <div class="references">
                <p>Berenson, M.L., Levine, D.M., Szabat, K.A. and Stephan, D.F. (2019) <em>Basic Business Statistics: Concepts and Applications</em>. 14th edn. Harlow: Pearson.</p>
                <p>Page, M.J., McKenzie, J.E., Bossuyt, P.M., Boutron, I., Hoffmann, T.C., Mulrow, C.D., Shamseer, L., Tetzlaff, J.M., Akl, E.A., Brennan, S.E., Chou, R., Glanville, J., Grimshaw, J.M., Hróbjartsson, A., Lalu, M.M., Li, T., Loder, E.W., Mayo-Wilson, E., McDonald, S., McGuinness, L.A., Stewart, L.A., Thomas, J., Tricco, A.C., Welch, V.A., Whiting, P. and Moher, D. (2021) 'The PRISMA 2020 statement: an updated guideline for reporting systematic reviews', <em>BMJ</em>, 372, n71. Available at: <a href="https://doi.org/10.1136/bmj.n71" target="_blank" rel="noopener">https://doi.org/10.1136/bmj.n71</a></p>
                <p>Rolfe, G., Freshwater, D. and Jasper, M. (2001) <em>Critical Reflection in Nursing and the Helping Professions: A User's Guide</em>. Basingstoke: Palgrave Macmillan.</p>
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
