---
layout: null
title: Research Methods and Professional Practice
description: Scientific method, research design, ethics, and evidence-based inquiry applied to computing
nav-menu: true
nav-order: 8
summary: >-
  Developed research competencies through literature review, proposal writing, and reflective practice
  across quantitative, qualitative, and mixed methods in computing contexts.
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
            font-size: 1.2rem;
            color: var(--text-secondary);
            max-width: 800px;
            line-height: 1.8;
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
            counter-increment: obj-counter;
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
        .artefacts-section { }

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
        }

        .artefact-icon {
            font-size: 2rem;
            flex-shrink: 0;
        }

        .artefact-title h3 {
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 0.4rem;
            color: #fff;
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

        .evidence-box a {
            color: var(--primary);
            text-decoration: none;
            font-weight: 500;
        }

        .evidence-box a:hover { text-decoration: underline; }

        .feedback-box {
            background: rgba(16, 185, 129, 0.05);
            border: 1px solid rgba(16, 185, 129, 0.2);
            border-radius: 8px;
            padding: 1rem 1.2rem;
        }

        .feedback-box p { margin-bottom: 0; }

        .feedback-box strong { color: var(--success); }

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

        /* Responsive */
        @media (max-width: 768px) {
            .module-hero-content { padding: 2.5rem 1.5rem; }
            .objectives-grid,
            .units-grid { grid-template-columns: 1fr; }
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
                <li><a href="#objectives">Objectives</a></li>
                <li><a href="#artefacts">Artefacts</a></li>
                <li><a href="#units">Units</a></li>
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
                This module developed my ability to design and critically evaluate research in computing contexts.
                I explored the scientific method, research strategies, statistical analysis, and ethical considerations
                — producing a literature review and research proposal that applied these methods to real-world problems.
            </p>
        </div>
    </section>

    <div class="main-content">

        <!-- Learning Objectives -->
        <section id="objectives">
            <div class="section-header">
                <h2>Learning Objectives</h2>
                <div class="divider"></div>
                <p>Core competencies developed throughout this research module</p>
            </div>

            <div class="objectives-grid">
                <div class="objective-card">
                    <div class="objective-icon">🔬</div>
                    <p>Acquire the ability to study and reflect on key principles and methods in research based on the scientific method and relevant to various disciplines.</p>
                </div>
                <div class="objective-card">
                    <div class="objective-icon">🗺️</div>
                    <p>Acquire the ability to examine various research strategies and designs as applicable to projects at hand.</p>
                </div>
                <div class="objective-card">
                    <div class="objective-icon">📊</div>
                    <p>Acquire the ability to develop research competencies, in particular those relating to the collection and analysis of data types to enable a critical design and evaluation of independent research.</p>
                </div>
                <div class="objective-card">
                    <div class="objective-icon">🧠</div>
                    <p>Have the opportunity to take a reflective and independent approach to the learning process.</p>
                </div>
                <div class="objective-card">
                    <div class="objective-icon">⚖️</div>
                    <p>Appraise the professional, legal, social, cultural and ethical issues that affect computing professionals.</p>
                </div>
                <div class="objective-card">
                    <div class="objective-icon">📚</div>
                    <p>Appraise the principles of academic investigation, applying them to a research topic in the applicable computing field.</p>
                </div>
                <div class="objective-card">
                    <div class="objective-icon">🔍</div>
                    <p>Evaluate critically existing literature, research design and methodology for the chosen topic, including data analysis processes.</p>
                </div>
                <div class="objective-card">
                    <div class="objective-icon">📝</div>
                    <p>Produce and evaluate critically a research proposal for the chosen topic.</p>
                </div>
            </div>
        </section>

        <!-- Artefacts -->
        <section class="artefacts-section" id="artefacts">
            <div class="section-header">
                <h2>Key Artefacts</h2>
                <div class="divider"></div>
                <p>Practical outputs demonstrating research competency across the module</p>
            </div>

            <article class="artefact">
                <div class="artefact-header">
                    <span class="artefact-icon">📖</span>
                    <div class="artefact-title">
                        <h3>Literature Review — Deep Learning and Machine Learning in Football Predictions</h3>
                        <span class="unit-badge">UNIT 7</span>
                    </div>
                </div>
                <div class="artefact-content">
                    <p>
                        A critical literature review examining the application of deep learning and machine learning techniques to football match prediction. Evaluated existing research designs, methodologies, and data analysis approaches, identifying strengths, limitations, and gaps in the current body of work.
                    </p>
                    <div class="evidence-box">
                        <p>
                            <strong>📁 Evidence:</strong>
                            <a href="[LINK]" target="_blank" rel="noopener">Literature Review (PDF)</a>
                        </p>
                    </div>
                    <div class="feedback-box">
                        <p>
                            <strong>✓ Feedback:</strong> [Add tutor/peer feedback here]
                        </p>
                    </div>
                </div>
            </article>

            <article class="artefact">
                <div class="artefact-header">
                    <span class="artefact-icon">🎤</span>
                    <div class="artefact-title">
                        <h3>Research Proposal Presentation — Crime Analysis</h3>
                        <span class="unit-badge">UNIT 10</span>
                    </div>
                </div>
                <div class="artefact-content">
                    <p>
                        A research proposal presentation investigating crime analysis through computing methods. Defined the research question, justified the chosen methodology, outlined the data collection strategy, and addressed ethical considerations relevant to the domain.
                    </p>
                    <div class="evidence-box">
                        <p>
                            <strong>📁 Evidence:</strong>
                            <a href="[LINK]" target="_blank" rel="noopener">Research Proposal Presentation</a>
                        </p>
                    </div>
                    <div class="feedback-box">
                        <p>
                            <strong>✓ Feedback:</strong> [Add tutor/peer feedback here]
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
                <p>Learning outcomes and key takeaways across all twelve units</p>
            </div>

            <div class="units-grid">
                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="unit-number">01</span>
                        <h3>Introduction to Research Methods</h3>
                    </div>
                    <p>Introduced to the elements within the scientific method and explored ethical issues in research and their relevance to professional practice. By the end, I could differentiate between inductive and deductive reasoning and understood why ethics matter in my area of research.</p>
                </div>

                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="unit-number">02</span>
                        <h3>Research Questions, Literature Review, and Proposal</h3>
                    </div>
                    <p>Learned how to formulate and revise research questions, examined all parts of a research proposal, and how to present ideas effectively. By the end, I could identify suitable research topics and transform them into well-crafted questions and proposals.</p>
                </div>

                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="unit-number">03</span>
                        <h3>Methodology and Research Methods</h3>
                    </div>
                    <p>Learned about the three research methods — quantitative, qualitative, and mixed methods — and the data collection methods for each. I now understand which methods are suitable for my research area.</p>
                </div>

                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="unit-number">04</span>
                        <h3>Case Studies, Focus Groups, and Observations</h3>
                    </div>
                    <p>Introduced to case studies, focus groups, and observation methods. By the end, I understood how to apply these methods to an investigation and what data each approach yields.</p>
                </div>

                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="unit-number">05</span>
                        <h3>Interviews, Surveys, and Questionnaire Design</h3>
                    </div>
                    <p>Learned about interviews, surveys, and pre- and post-testing. Explored methods for improving response quality and how to analyse data from different types of questions.</p>
                </div>

                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="unit-number">06</span>
                        <h3>Quantitative Methods — Descriptive and Inferential Statistics</h3>
                    </div>
                    <p>Focused on quantitative methods, descriptive statistics, and measures of location and spread. By the end, I could apply these techniques effectively to research data.</p>
                </div>

                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="unit-number">07</span>
                        <h3>Inferential Statistics and Hypothesis Testing</h3>
                    </div>
                    <p>Gained a solid understanding of inferential statistics, probability, and hypothesis testing. By the end, I could apply these to data analysis and form and test hypotheses rigorously.</p>
                </div>

                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="unit-number">08</span>
                        <h3>Data Analysis and Visualisation</h3>
                    </div>
                    <p>Learned how to analyse qualitative and quantitative data, and by the end I was able to use various charts and visualisation techniques to present findings effectively and accessibly.</p>
                </div>

                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="unit-number">09</span>
                        <h3>Validity and Generalisability in Research</h3>
                    </div>
                    <p>Explored validity, generalisability, and reliability and how they impact research design. Applied this understanding to analyse and present research findings with appropriate rigour.</p>
                </div>

                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="unit-number">10</span>
                        <h3>Research Writing</h3>
                    </div>
                    <p>Focused on how to structure a dissertation effectively. By the end, I felt confident in my ability to organise and present research in a clear, academically appropriate format.</p>
                </div>

                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="unit-number">11</span>
                        <h3>Professional Development and e-Portfolio</h3>
                    </div>
                    <p>Reviewed my learning approach and completed the Professional Skills matrix, which helped clarify my future professional goals and identify areas for continued development.</p>
                </div>

                <div class="unit-card">
                    <div class="unit-card-header">
                        <span class="unit-number">12</span>
                        <h3>Project Management and Managing Risk</h3>
                    </div>
                    <p>Learned about project management, risk management, and project life cycles. Developed a risk management plan and understood how to manage project changes and uncertainty effectively.</p>
                </div>
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
