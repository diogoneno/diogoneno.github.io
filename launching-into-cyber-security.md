---
layout: null
title: Launching into Cyber Security
description: Comprehensive overview of cyber security principles and secure system design
nav-menu: true
nav-order: 2
summary: >-
  Foundation module covering cyber security principles, secure system design, and professional
  standards with practical implementation through portfolio artefacts.
topic_tags:
  - Security Foundations
  - Systems Thinking
---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Launching into Cyber Security | MSc Portfolio</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary: #00d4ff;
            --secondary: #0066ff;
            --dark: #0a0e27;
            --darker: #050816;
            --text: #e4e4e7;
            --text-secondary: #a1a1aa;
            --accent: #7c3aed;
            --success: #10b981;
            --warning: #f59e0b;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
            background: var(--darker);
            color: var(--text);
            line-height: 1.6;
            overflow-x: hidden;
        }

        /* Animated Background */
        .animated-bg {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            background: linear-gradient(135deg, var(--darker) 0%, var(--dark) 100%);
        }

        .animated-bg::before {
            content: '';
            position: absolute;
            width: 200%;
            height: 200%;
            background: 
                radial-gradient(circle at 20% 50%, rgba(0, 212, 255, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 80% 80%, rgba(124, 58, 237, 0.1) 0%, transparent 50%);
            animation: gradientShift 20s ease infinite;
        }

        @keyframes gradientShift {
            0%, 100% { transform: translate(0, 0); }
            50% { transform: translate(-50px, -50px); }
        }

        /* Navigation */
        nav {
            position: fixed;
            top: 0;
            width: 100%;
            padding: 1.5rem 5%;
            background: rgba(10, 14, 39, 0.8);
            backdrop-filter: blur(10px);
            z-index: 1000;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }

        nav .container {
            max-width: 1400px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: 700;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-decoration: none;
        }

        .nav-links {
            display: flex;
            gap: 2rem;
            list-style: none;
        }

        .nav-links a {
            color: var(--text);
            text-decoration: none;
            font-weight: 500;
            transition: all 0.3s ease;
        }

        /* Module Hero */
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
            line-height: 1.8;
            max-width: 900px;
        }

        /* Main Content */
        .main-content {
            max-width: 1400px;
            margin: 0 auto;
            padding: 4rem 5%;
        }

        .section-header {
            text-align: center;
            margin-bottom: 4rem;
        }

        .section-header h2 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            color: var(--text);
        }

        .section-header p {
            color: var(--text-secondary);
            font-size: 1.1rem;
        }

        .divider {
            width: 60px;
            height: 4px;
            background: linear-gradient(90deg, var(--primary), var(--accent));
            margin: 1rem auto;
            border-radius: 2px;
        }

        /* Learning Outcomes Grid */
        .outcomes-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
            margin-bottom: 6rem;
        }

        .outcome-card {
            background: rgba(255, 255, 255, 0.03);
            border-radius: 20px;
            padding: 2.5rem;
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: all 0.3s ease;
        }

        .outcome-card:hover {
            background: rgba(255, 255, 255, 0.05);
            border-color: var(--primary);
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0, 212, 255, 0.2);
        }

        .outcome-icon {
            width: 60px;
            height: 60px;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            margin-bottom: 1.5rem;
        }

        .outcome-card h3 {
            color: var(--primary);
            margin-bottom: 1rem;
            font-size: 1.3rem;
        }

        .outcome-card p {
            color: var(--text-secondary);
            line-height: 1.7;
        }

        /* Artefacts Section */
        .artefacts-section {
            margin: 6rem 0;
        }

        .artefact {
            background: rgba(255, 255, 255, 0.03);
            border-radius: 20px;
            padding: 3rem;
            margin-bottom: 2rem;
            border-left: 5px solid var(--primary);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-left: 5px solid var(--primary);
            transition: all 0.3s ease;
        }

        .artefact:hover {
            background: rgba(255, 255, 255, 0.05);
            transform: translateX(10px);
        }

        .artefact-header {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1.5rem;
            flex-wrap: wrap;
        }

        .artefact-icon {
            font-size: 2.5rem;
        }

        .artefact-title {
            flex: 1;
            min-width: 200px;
        }

        .artefact-title h3 {
            color: var(--text);
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
        }

        .unit-badge {
            display: inline-block;
            background: rgba(0, 212, 255, 0.1);
            color: var(--primary);
            padding: 0.3rem 1rem;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
        }

        .artefact-content p {
            color: var(--text-secondary);
            line-height: 1.8;
            margin-bottom: 1rem;
        }

        .evidence-box {
            background: rgba(124, 58, 237, 0.1);
            border-left: 3px solid var(--accent);
            padding: 1.5rem;
            border-radius: 8px;
            margin: 1.5rem 0;
        }

        .evidence-box p {
            color: var(--text);
            margin: 0;
            font-size: 0.95rem;
        }

        .evidence-box a {
            color: var(--primary);
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .evidence-box a:hover {
            color: var(--accent);
        }

        .feedback-box {
            background: rgba(16, 185, 129, 0.1);
            border-left: 3px solid var(--success);
            padding: 1.5rem;
            border-radius: 8px;
            margin: 1.5rem 0;
        }

        .feedback-box strong {
            color: var(--success);
        }

        /* SWOT Analysis */
        .swot-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin: 3rem 0;
        }

        .swot-card {
            background: rgba(255, 255, 255, 0.03);
            border-radius: 16px;
            padding: 2rem;
            border: 2px solid;
            transition: all 0.3s ease;
        }

        .swot-card.strengths {
            border-color: var(--success);
        }

        .swot-card.weaknesses {
            border-color: #ef4444;
        }

        .swot-card.opportunities {
            border-color: var(--warning);
        }

        .swot-card.threats {
            border-color: #8b5cf6;
        }

        .swot-card:hover {
            background: rgba(255, 255, 255, 0.05);
            transform: translateY(-5px);
        }

        .swot-card h3 {
            font-size: 1.5rem;
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            gap: 0.8rem;
        }

        .swot-card ul {
            list-style: none;
            padding: 0;
        }

        .swot-card li {
            padding: 0.8rem 0;
            padding-left: 2rem;
            position: relative;
            color: var(--text-secondary);
            line-height: 1.6;
        }

        .swot-card li::before {
            content: '→';
            position: absolute;
            left: 0;
            font-weight: bold;
        }

        .swot-card.strengths li::before { color: var(--success); }
        .swot-card.weaknesses li::before { color: #ef4444; }
        .swot-card.opportunities li::before { color: var(--warning); }
        .swot-card.threats li::before { color: #8b5cf6; }

        /* Action Plan */
        .action-plan {
            margin: 6rem 0;
        }

        .action-items {
            display: grid;
            gap: 2rem;
            margin-top: 3rem;
        }

        .action-item {
            background: rgba(255, 255, 255, 0.03);
            border-radius: 16px;
            padding: 2.5rem;
            border-top: 4px solid;
            transition: all 0.3s ease;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .action-item:nth-child(1) { border-top-color: var(--success); }
        .action-item:nth-child(2) { border-top-color: var(--primary); }
        .action-item:nth-child(3) { border-top-color: var(--warning); }
        .action-item:nth-child(4) { border-top-color: #ec4899; }
        .action-item:nth-child(5) { border-top-color: var(--accent); }

        .action-item:hover {
            background: rgba(255, 255, 255, 0.05);
            transform: translateY(-5px);
        }

        .action-header {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1.5rem;
        }

        .action-icon {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
        }

        .action-item:nth-child(1) .action-icon { background: rgba(16, 185, 129, 0.2); }
        .action-item:nth-child(2) .action-icon { background: rgba(0, 212, 255, 0.2); }
        .action-item:nth-child(3) .action-icon { background: rgba(245, 158, 11, 0.2); }
        .action-item:nth-child(4) .action-icon { background: rgba(236, 72, 153, 0.2); }
        .action-item:nth-child(5) .action-icon { background: rgba(124, 58, 237, 0.2); }

        .action-content h4 {
            color: var(--text);
            font-size: 1.3rem;
            margin-bottom: 1rem;
        }

        .action-content p {
            color: var(--text-secondary);
            line-height: 1.7;
        }

        .action-footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 1.5rem;
            padding-top: 1.5rem;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }

        .target-date {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.5rem 1.2rem;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 600;
        }

        .action-item:nth-child(1) .target-date { background: rgba(16, 185, 129, 0.2); color: var(--success); }
        .action-item:nth-child(2) .target-date { background: rgba(0, 212, 255, 0.2); color: var(--primary); }
        .action-item:nth-child(3) .target-date { background: rgba(245, 158, 11, 0.2); color: var(--warning); }
        .action-item:nth-child(4) .target-date { background: rgba(236, 72, 153, 0.2); color: #ec4899; }
        .action-item:nth-child(5) .target-date { background: rgba(124, 58, 237, 0.2); color: var(--accent); }

        /* Conclusion */
        .conclusion-section {
            background: linear-gradient(135deg, rgba(0, 212, 255, 0.1), rgba(124, 58, 237, 0.1));
            border-radius: 24px;
            padding: 4rem 3rem;
            margin: 6rem 0;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .conclusion-header {
            display: flex;
            align-items: center;
            gap: 1.5rem;
            margin-bottom: 2rem;
        }

        .conclusion-icon {
            width: 70px;
            height: 70px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2.5rem;
        }

        .conclusion-section h2 {
            font-size: 2.5rem;
            color: var(--text);
        }

        .conclusion-section p {
            color: var(--text);
            line-height: 1.8;
            font-size: 1.1rem;
            margin-bottom: 1.5rem;
        }

        /* Footer */
        footer {
            padding: 3rem 5%;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            text-align: center;
        }

        footer p {
            color: var(--text-secondary);
        }

        footer a {
            color: var(--primary);
            text-decoration: none;
        }

        /* Responsive */
        @media (max-width: 968px) {
            .nav-links {
                display: none;
            }

            .module-hero {
                padding: 6rem 5% 3rem;
            }

            .module-hero-content {
                padding: 3rem 2rem;
            }

            .outcomes-grid,
            .swot-grid {
                grid-template-columns: 1fr;
            }

            .artefact {
                padding: 2rem;
            }

            .artefact-header {
                flex-direction: column;
                align-items: flex-start;
            }
        }

        /* Smooth Scroll */
        html {
            scroll-behavior: smooth;
        }
    </style>
</head>
<body>
    <div class="animated-bg"></div>

    <!-- Navigation -->
    <nav>
        <div class="container">
            <a href="/" class="logo">DIOGO • CYBER SEC</a>
            <ul class="nav-links">
                <li><a href="/">Home</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="#outcomes">Outcomes</a></li>
                <li><a href="#artefacts">Artefacts</a></li>
                <li><a href="#action-plan">Action Plan</a></li>
            </ul>
        </div>
    </nav>

    <!-- Module Hero -->
    <section class="module-hero">
        <div class="module-hero-content">
            <span class="module-badge">FOUNDATION MODULE</span>
            <h1>Launching into Cyber Security</h1>
            <p>
                This module provided a comprehensive overview of cyber security principles, secure system design, and professional standards. I implemented foundational concepts, regulatory frameworks, and ethical considerations in practical scenarios using portfolio artefacts. Throughout the process, I emphasised quantifiable results, effective communication, and systematic evaluation to foster ongoing enhancements.
            </p>
        </div>
    </section>

    <!-- Main Content -->
    <div class="main-content">
        <!-- Learning Outcomes -->
        <section id="outcomes">
            <div class="section-header">
                <h2>Learning Outcomes</h2>
                <div class="divider"></div>
                <p>Core competencies developed throughout this foundational module</p>
            </div>

            <div class="outcomes-grid">
                <div class="outcome-card">
                    <div class="outcome-icon">🛡️</div>
                    <h3>Core Concepts Mastery</h3>
                    <p>
                        Exhibit a comprehensive grasp of essential cyber security concepts (least privilege, defence-in-depth, secure-by-design, Zero Trust) and their foundational role in the development of resilient systems.
                    </p>
                </div>

                <div class="outcome-card">
                    <div class="outcome-icon">🎯</div>
                    <h3>Security Implementation</h3>
                    <p>
                        Implement security techniques (threat modelling, risk assessment, control selection) to guide design and operational decision-making within organisations.
                    </p>
                </div>

                <div class="outcome-card">
                    <div class="outcome-icon">📋</div>
                    <h3>Framework Assessment</h3>
                    <p>
                        Assess the efficacy of control frameworks (e.g., ISO/IEC 27001, NIST CSF 2.0) for aligned recommendations.
                    </p>
                </div>

                <div class="outcome-card">
                    <div class="outcome-icon">💬</div>
                    <h3>Communication Excellence</h3>
                    <p>
                        Appraise and communicate security findings to diverse audiences on risks and assurance.
                    </p>
                </div>
            </div>
        </section>

        <!-- Artefacts Section -->
        <section class="artefacts-section" id="artefacts">
            <div class="section-header">
                <h2>Artefacts and Feedback</h2>
                <div class="divider"></div>
                <p>Practical implementations and peer review throughout the module</p>
            </div>

            <!-- Artefact 1 -->
            <article class="artefact">
                <div class="artefact-header">
                    <span class="artefact-icon">💬</span>
                    <div class="artefact-title">
                        <h3>Collaborative Discussion 1 — Initial Post</h3>
                        <span class="unit-badge">UNIT 1</span>
                    </div>
                </div>
                <div class="artefact-content">
                    <p>
                        Introduced the Log4j case to frame economic, legal (GDPR), and reputational impacts of cyber security; advocated for proactive investment over reactive spending and underlined the relationship between compliance and trust.
                    </p>
                    <div class="evidence-box">
                        <p>
                            <strong>📁 Evidence:</strong>
                            <a href="/assets/LauchingIntoCybersecurity/Initial%20Post.pdf" target="_blank" rel="noopener">Initial Post.pdf</a>
                        </p>
                    </div>
                    <div class="feedback-box">
                        <p>
                            <strong>✓ Feedback:</strong> Formative comments suggested including specific case examples and clearer connections from risk to control to outcome in future posts.
                        </p>
                    </div>
                </div>
            </article>

            <!-- Artefact 2 -->
            <article class="artefact">
                <div class="artefact-header">
                    <span class="artefact-icon">📊</span>
                    <div class="artefact-title">
                        <h3>Unit 3 - Summary Post</h3>
                        <span class="unit-badge">UNIT 3</span>
                    </div>
                </div>
                <div class="artefact-content">
                    <p>
                        Consolidated insights from the Log4j discussion, highlighting economic impacts, regulatory obligations (GDPR Art. 32), and reputational effects, with peer-suggested real-world examples.
                    </p>
                    <div class="evidence-box">
                        <p>
                            <strong>📁 Evidence:</strong>
                            <a href="/assets/LauchingIntoCybersecurity/Summary%20Post.pdf" target="_blank" rel="noopener">Summary Post.pdf</a>
                        </p>
                    </div>
                    <div class="feedback-box">
                        <p>
                            <strong>✓ Feedback:</strong> Involvement of peers enhanced the justification for implementing patching and monitoring, while the precision of the recommendations was improved.
                        </p>
                    </div>
                </div>
            </article>

            <!-- Artefact 3 -->
            <article class="artefact">
                <div class="artefact-header">
                    <span class="artefact-icon">📊</span>
                    <div class="artefact-title">
                        <h3>Unit 3 - Summary Post</h3>
                        <span class="unit-badge">UNIT 3</span>
                    </div>
                </div>
                <div class="artefact-content">
                    <p>
                        Consolidated insights from the Log4j discussion, highlighting economic impacts, regulatory obligations (GDPR Art. 32), and reputational effects, with peer-suggested real-world examples.
                    </p>
                    <div class="evidence-box">
                        <p>
                            <strong>📁 Evidence:</strong>
                            <a href="/assets/LauchingIntoCybersecurity/Summary%20Post.pdf" target="_blank" rel="noopener">Summary Post (PDF)</a>
                        </p>
                    </div>
                    <div class="feedback-box">
                        <p>
                            <strong>✓ Feedback:</strong> Involvement of peers enhanced the justification for implementing patching and monitoring, while the precision of the recommendations was improved.
                        </p>
                    </div>
                </div>
            </article>

            <!-- Artefact 4 -->
            <article class="artefact">
                <div class="artefact-header">
                    <span class="artefact-icon">📝</span>
                    <div class="artefact-title">
                        <h3>Key Considerations for Implementing a Comprehensive Backup and Recovery Plan for an Online Shopping System (OSS)</h3>
                        <span class="unit-badge">UNIT 9</span>
                    </div>
                </div>
                <div class="artefact-content">
                    <p>
                        Key considerations for an e-commerce backup and recovery plan include risk assessment, layered controls, failover, redundancy, RTO/RPO alignment, integrity checks, log monitoring, and routine recovery validation, highlighting governance and testing for resilient service continuity.
                    </p>
                    <div class="evidence-box">
                        <p>
                            <strong>📁 Evidence:</strong>
                            <a href="/assets/LauchingIntoCybersecurity/Essay9.pdf" target="_blank" rel="noopener">Essay9.pdf</a>
                        </p>
                    </div>
                    <div class="feedback-box">
                        <p>
                            <strong>✓ Feedback:</strong> Prioritise risk-to-control traceability and include dashboardable metrics for executives.
                        </p>
                    </div>
                </div>
            </article>

            <!-- Artefact 5 -->
            <article class="artefact">
                <div class="artefact-header">
                    <span class="artefact-icon">🔒</span>
                    <div class="artefact-title">
                        <h3>Unit 12 — Secure Backup Application (Python)</h3>
                        <span class="unit-badge">UNIT 12</span>
                    </div>
                </div>
                <div class="artefact-content">
                    <p>
                        Created a secure backup prototype using secure-by-design and Zero Trust principles: TLS transport, credential authentication, encryption at rest and in transit, and integrity checks. The README covers assumptions, threat model, and testing methods.
                    </p>
                    <div class="evidence-box">
                        <p style="margin-bottom: 0.8rem;">
                            <strong>📁 Evidence folder:</strong> <code style="background: rgba(124, 58, 237, 0.1); padding: 0.3rem 0.6rem; border-radius: 4px;">assets/LauchingIntoCybersecurity/unit12</code>
                        </p>
                        <p>
                            <strong>🗂️ Key files:</strong><br>
                            <a href="/assets/LauchingIntoCybersecurity/unit12/secure_backup.py" target="_blank" rel="noopener">secure_backup.py</a> •
                            <a href="/assets/LauchingIntoCybersecurity/unit12/requirements.txt" target="_blank" rel="noopener">requirements.txt</a> •
                            <a href="/assets/LauchingIntoCybersecurity/unit12/README.md" target="_blank" rel="noopener">README.md</a> •
                            <a href="/assets/LauchingIntoCybersecurity/unit12/TestData/ResultsScreenshots.pdf" target="_blank" rel="noopener">TestData/ResultsScreenshots.pdf</a>
                        </p>
                    </div>
                    <div class="feedback-box">
                        <p>
                            <strong>✓ Feedback:</strong> Test plan and integrity verification received positive feedback. Next steps include secret management, key rotation, and automated restoration tests.
                        </p>
                    </div>
                </div>
            </article>

            <!-- Artefact 6 -->
            <article class="artefact">
                <div class="artefact-header">
                    <span class="artefact-icon">📈</span>
                    <div class="artefact-title">
                        <h3>Risk Analysis — Summary</h3>
                        <span class="unit-badge">SUMMARY</span>
                    </div>
                </div>
                <div class="artefact-content">
                    <p>
                        During the Log4j analysis and backup/recovery efforts, I focused on practical risk management over theoretical catalogues. Decisions were driven by regulatory requirements (notably GDPR Article 32), service-continuity objectives (including Recovery Time Objectives and Recovery Point Objectives), and validated controls such as Transport Layer Security, encryption, credential verification, and integrity checks.
                    </p>
                    <div class="evidence-box">
                        <p>
                            <strong>📁 Evidence:</strong>
                            <a href="/assets/LauchingIntoCybersecurity/Initial%20Post.pdf" target="_blank" rel="noopener">Initial Post.pdf</a> (p.1);
                            <a href="/assets/LauchingIntoCybersecurity/Summary%20Post.pdf" target="_blank" rel="noopener">Summary Post.pdf</a> (p.1);
                            <a href="/assets/LauchingIntoCybersecurity/Essay9.pdf" target="_blank" rel="noopener">Essay9.pdf</a> (pp.1–3);
                            <a href="/assets/LauchingIntoCybersecurity/unit12/README.md" target="_blank" rel="noopener">Unit 12 README</a>
                        </p>
                    </div>
                </div>
            </article>
        </section>

        <!-- SWOT Analysis -->
        <section id="swot">
            <div class="section-header">
                <h2>Personal SWOT Analysis</h2>
                <div class="divider"></div>
                <p>Self-evaluation of capabilities and development areas</p>
            </div>

            <div class="swot-grid">
                <div class="swot-card strengths">
                    <h3><span>💪</span> Strengths</h3>
                    <ul>
                        <li>Systematic approach to frameworks, assessments, and documentation</li>
                        <li>Strong grasp of NIST, ISO/IEC 27001, OWASP</li>
                        <li>Multilingual communication and cross-functional teamwork</li>
                    </ul>
                </div>

                <div class="swot-card weaknesses">
                    <h3><span>⚠️</span> Weaknesses</h3>
                    <ul>
                        <li>Limited experience in quantitative risk modelling</li>
                        <li>Still building governance/policy-writing skills</li>
                        <li>Need deeper hands-on penetration testing exposure</li>
                    </ul>
                </div>

                <div class="swot-card opportunities">
                    <h3><span>🚀</span> Opportunities</h3>
                    <ul>
                        <li>Gain formal certification (CISSP/CISM) to validate expertise</li>
                        <li>Leverage e-portfolio for job applications in UK market</li>
                        <li>Contribute to open-source security projects or publications</li>
                    </ul>
                </div>

                <div class="swot-card threats">
                    <h3><span>⚡</span> Threats</h3>
                    <ul>
                        <li>Rapidly evolving threat landscape outpacing current knowledge</li>
                        <li>High competition for senior security roles</li>
                        <li>Potential burnout from balancing study, work, and upskilling</li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- Action Plan -->
        <section class="action-plan" id="action-plan">
            <div class="section-header">
                <h2>Action Plan</h2>
                <div class="divider"></div>
                <p>Concrete steps to address weaknesses and capitalize on opportunities</p>
            </div>

            <div class="action-items">
                <div class="action-item">
                    <div class="action-header">
                        <div class="action-icon">🔍</div>
                        <div class="action-content">
                            <h4>Monitor Threat Landscape</h4>
                            <p><strong>Steps:</strong> Subscribe to CVE/ENISA/NCSC feeds; weekly review and log one relevant vulnerability/TTP mapped to current controls.</p>
                        </div>
                    </div>
                    <div class="action-footer">
                        <span class="target-date">📅 Target: 2024-12-15</span>
                    </div>
                </div>

                <div class="action-item">
                    <div class="action-header">
                        <div class="action-icon">📊</div>
                        <div class="action-content">
                            <h4>Build Quantitative Risk Scenarios</h4>
                            <p><strong>Steps:</strong> Develop scenario models (ransomware vs insider breach) and dashboards of assumptions/impacts; define action thresholds.</p>
                        </div>
                    </div>
                    <div class="action-footer">
                        <span class="target-date">📅 Target: 2025-02-01</span>
                    </div>
                </div>

                <div class="action-item">
                    <div class="action-header">
                        <div class="action-icon">🏛️</div>
                        <div class="action-content">
                            <h4>Enhance Governance Capability</h4>
                            <p><strong>Steps:</strong> Study for CISSP/CISM; join a study group; apply governance patterns in projects; attempt exams; integrate new controls.</p>
                        </div>
                    </div>
                    <div class="action-footer">
                        <span class="target-date">📅 Target: 2025-08-01</span>
                    </div>
                </div>

                <div class="action-item">
                    <div class="action-header">
                        <div class="action-icon">🗣️</div>
                        <div class="action-content">
                            <h4>Improve Communication Skills</h4>
                            <p><strong>Steps:</strong> Practise narrative slide walkthroughs; collect peer feedback on clarity; present Unit 12 to a non-technical audience.</p>
                        </div>
                    </div>
                    <div class="action-footer">
                        <span class="target-date">📅 Target: 2025-01-15</span>
                    </div>
                </div>

                <div class="action-item">
                    <div class="action-header">
                        <div class="action-icon">✍️</div>
                        <div class="action-content">
                            <h4>Share Knowledge</h4>
                            <p><strong>Steps:</strong> Publish three short posts on threat modelling and backups; track engagement.</p>
                        </div>
                    </div>
                    <div class="action-footer">
                        <span class="target-date">📅 Target: 2025-03-01</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- Conclusion -->
        <section class="conclusion-section">
            <div class="conclusion-header">
                <div class="conclusion-icon">🎯</div>
                <h2>Conclusion</h2>
            </div>
            <p>
                I entered confident in my technical skills and learned that resilience and ethics are central. I improved my ability to express risk in business terms while deepening governance and ethical awareness. I view security as an ongoing process requiring continuous threat assessment, collaboration, and evidence-based decisions.
            </p>
            <p>
                Reflection produced concrete next steps that I'll apply in future projects to ensure security measures positively impact the organisation. I'm committed to lifelong learning, sharing best practice, and addressing emerging cybersecurity challenges.
            </p>
        </section>
    </div>

    <!-- Footer -->
    <footer>
        <p>&copy; 2025 MSc Cyber Security Portfolio • Designed by Diogo</p>
    </footer>

    <script>
        // Smooth scrolling
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            });
        });

        // Intersection Observer for animations
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, observerOptions);

        document.querySelectorAll('.outcome-card, .artefact, .swot-card, .action-item').forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(30px)';
            el.style.transition = 'all 0.6s ease';
            observer.observe(el);
        });
    </script>
</body>
</html>
