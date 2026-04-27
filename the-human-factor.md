---
layout: null
title: The Human Factor
description: Human-centred security, behavioural insight, and cultural interventions
data-theme: human-factor
nav-menu: true
nav-order: 6
summary: >-
  Behavioural and cultural interventions that embed privacy, accessibility,
  and ethics into security programmes by design.
topic_tags:
  - Security Awareness
  - Human-Centred Design
---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{{ page.summary | strip_newlines | strip }}">
    <title>The Human Factor | MSc Portfolio</title>
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
            color: var(--primary);
            font-size: 1.05rem;
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
            margin-left: 0.5rem;
            padding: 0.15rem 0.6rem;
            background: rgba(16, 185, 129, 0.15);
            color: var(--success);
            border: 1px solid rgba(16, 185, 129, 0.3);
            border-radius: 50px;
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

        table.skills-matrix td:first-child {
            font-weight: 600;
            color: var(--primary);
        }

        /* Responsive */
        @media (max-width: 768px) {
            .module-hero-content { padding: 2.5rem 1.5rem; }
            .objectives-grid { grid-template-columns: 1fr; }
            .prose-card,
            .action-list { padding: 1.5rem; }
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
                <li><a href="#action-plan">Action Plan</a></li>
                <li><a href="#skills-matrix">Skills</a></li>
            </ul>
            <button class="mobile-menu-btn" aria-label="Open navigation menu">&#9776;</button>
        </div>
    </nav>
    {% include mobile-nav.html %}

    <section class="module-hero">
        <div class="module-hero-content">
            <span class="module-badge">THE HUMAN FACTOR MODULE</span>
            <h1>The Human Factor</h1>
            <p>
                This module explored how people, culture, and usability influence security outcomes in organisations.
                It addressed the dominance of the "human element" in breach causation, the impact of design choices
                on risky behaviour, and the integration of privacy, accessibility, and ethics into effective controls.
                The focus was on transforming behavioural insights into interventions and metrics that enhance outcomes.
            </p>
        </div>
    </section>

    <div class="main-content">

        <!-- Module Overview -->
        <section id="overview">
            <div class="section-header">
                <h2>Module Overview</h2>
                <div class="divider"></div>
                <p>Behavioural insight, human-centred design, and cultural interventions for security</p>
            </div>

            <div class="prose-card">
                <p>
                    The module examined how human abilities, motivations, and constraints shape security outcomes —
                    from the dominance of the human element in breach causation, through design choices that drive
                    risky behaviour, to the integration of privacy, accessibility, and ethics into effective controls.
                    Coursework focused on translating behavioural insight into interventions and metrics that improve
                    outcomes within real organisational contexts, with a particular emphasis on the constraints faced
                    by start-ups.
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
                    <div class="objective-icon"><span aria-hidden="true">🧠</span></div>
                    <h4>Behavioural Insight</h4>
                    <p>Examine how human abilities, constraints, and motivations affect security actions and incident risk.</p>
                </div>

                <div class="objective-card">
                    <div class="objective-icon"><span aria-hidden="true">🎨</span></div>
                    <h4>Human-Centred Design</h4>
                    <p>Apply human-centred and usable-security principles to create safer defaults without hindering legitimate work.</p>
                </div>

                <div class="objective-card">
                    <div class="objective-icon"><span aria-hidden="true">🕵️</span></div>
                    <h4>Insider Risk Assessment</h4>
                    <p>Assess insider-risk scenarios — malicious and unintentional — and propose proportionate detection, access, and cultural interventions.</p>
                </div>

                <div class="objective-card">
                    <div class="objective-icon"><span aria-hidden="true">🧾</span></div>
                    <h4>Governance Integration</h4>
                    <p>Integrate privacy-by-design and continuous improvement into governance processes and control selection.</p>
                </div>

                <div class="objective-card">
                    <div class="objective-icon"><span aria-hidden="true">📢</span></div>
                    <h4>Communicating Assurance</h4>
                    <p>Clearly communicate risks and recommendations to both technical and non-technical audiences.</p>
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
                    <span class="artefact-icon" aria-hidden="true">🧾</span>
                    <div class="artefact-title">
                        <h3>Individual Essay (individualessay.pdf)</h3>
                        <div class="badge-row">
                            <span class="unit-badge">UNIT 3</span>
                        </div>
                    </div>
                </div>
                <div class="artefact-content">
                    <p>
                        Critical analysis of three human factors for a local start-up: employee awareness, organisational
                        culture and security mindset, and insider threats. The work connects start-up constraints to
                        increased human-centred risk and argues for culture, training, and clear role definition.
                    </p>
                    <div class="feedback-box">
                        <p>
                            <strong><span aria-hidden="true">📝</span> Feedback:</strong>
                            Very good knowledge and understanding across awareness, culture, and insider threat;
                            strengthen with current data points (e.g., prevalence) and brief, concrete examples.
                        </p>
                    </div>
                </div>
            </article>

            <article class="artefact">
                <div class="artefact-header">
                    <span class="artefact-icon" aria-hidden="true">🤝</span>
                    <div class="artefact-title">
                        <h3>Peer Review Submission (review.pdf)</h3>
                        <div class="badge-row">
                            <span class="unit-badge">UNIT 4</span>
                        </div>
                    </div>
                </div>
                <div class="artefact-content">
                    <p>
                        Reviewed two essays, identifying strengths and areas for improvement; applied concepts such as
                        compliance budget and cognitive biases, and offered references to support suggestions.
                    </p>
                    <div class="feedback-box">
                        <p>
                            <strong><span aria-hidden="true">📝</span> Feedback:</strong>
                            Strong critical engagement with balanced, evidence-based recommendations. Wide reading
                            demonstrated; prioritise peer-reviewed sources over non-peer-reviewed material.
                        </p>
                    </div>
                </div>
            </article>

            <article class="artefact">
                <div class="artefact-header">
                    <span class="artefact-icon" aria-hidden="true">🎤</span>
                    <div class="artefact-title">
                        <h3>Individual Presentation (final assignment.pdf)</h3>
                        <div class="badge-row">
                            <span class="unit-badge">UNIT 6</span>
                        </div>
                    </div>
                </div>
                <div class="artefact-content">
                    <p>
                        Proposed solutions addressing cognitive limitations and human error, insider threats, and
                        design–behaviour mismatches for start-ups, supported by data and visuals.
                    </p>
                    <div class="feedback-box">
                        <p>
                            <strong><span aria-hidden="true">📝</span> Feedback:</strong>
                            Measures and implications are well articulated; ground solutions in a theoretical lens
                            (e.g., COM-B) and include mechanisms for monitoring and continuous improvement. Good
                            breadth of sources; add in-slide citations and a full references slide. Structure and
                            visuals are effective; improve audio quality and narration clarity.
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
                <p>Concrete next 6–8 week goals derived from tutor feedback</p>
            </div>

            <ol class="action-list">
                <li><strong>Evidence base &amp; currency.</strong> Add recent peer-reviewed studies and current insider statistics to the essay and slides, updating citations and figures as proof of completion. <span class="target">Week 2</span></li>
                <li><strong>Concrete examples.</strong> Embed brief, relevant case studies alongside each factor and recommendation, evidenced by revised essay sections with example call-outs. <span class="target">Week 2</span></li>
                <li><strong>Theoretical grounding.</strong> Map controls to a behavioural framework such as COM-B, linking actions to metrics and documenting the mapping in slides and narrative. <span class="target">Week 3</span></li>
                <li><strong>Monitoring &amp; improvement.</strong> Design a feedback loop covering KPIs, pulse surveys, A/B tests, and incident reviews, evidenced by an appended continuous-improvement plan. <span class="target">Week 4</span></li>
                <li><strong>Peer-review rigour.</strong> Swap non-peer-reviewed sources for academic equivalents and annotate rationale, evidenced by an updated review with quality notes. <span class="target">Week 3</span></li>
                <li><strong>Presentation polish.</strong> Add slide citations, a full references slide, and re-record audio with a script to tighten delivery, evidenced by new slide exports and transcripts. <span class="target">Week 3</span></li>
                <li><strong>Accessibility &amp; usable security.</strong> Introduce plain-language summaries, task-based guidance, readability checks, and alt text — evidenced by improved scores and annotated slides. <span class="target">Week 4</span></li>
            </ol>
        </section>

        <!-- Skills Matrix -->
        <section id="skills-matrix">
            <div class="section-header">
                <h2>Professional Skills Matrix</h2>
                <div class="divider"></div>
                <p>Snapshot of competencies developed across the module</p>
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
                            <td>Human-centred security &amp; usability</td>
                            <td>Operating at a proficient level by identifying cognitive limits, design–behaviour mismatches, and mitigations within the start-up context; next step is to align recommendations with COM-B and embed feedback loops.</td>
                        </tr>
                        <tr>
                            <td>Insider-risk analysis</td>
                            <td>Proficient differentiation of malicious versus unintentional insiders with practical access and monitoring implications; improvement focuses on incorporating current prevalence data and threshold-based controls.</td>
                        </tr>
                        <tr>
                            <td>Evidence-based writing</td>
                            <td>Progressing towards proficiency through appropriate sourcing and peer-review additions; next actions are increasing peer-reviewed material, refreshing statistics, and tightening citation placement.</td>
                        </tr>
                        <tr>
                            <td>Critical review &amp; feedback</td>
                            <td>Maintaining a proficient, balanced critique style with actionable recommendations, while adding source-quality flags and alternative peer-reviewed citations to elevate rigour.</td>
                        </tr>
                        <tr>
                            <td>Presentation &amp; storytelling</td>
                            <td>Delivering clear, data-backed narratives with strong visuals; focus is on enhancing audio, adding on-slide citations, and including a full references slide.</td>
                        </tr>
                        <tr>
                            <td>Academic practice &amp; referencing</td>
                            <td>Currently developing with correct structure but dated sources; improvement entails applying Cite-Them-Right consistently, alphabetising entries, and ensuring references appear both on slides and in full lists.</td>
                        </tr>
                    </tbody>
                </table>
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
