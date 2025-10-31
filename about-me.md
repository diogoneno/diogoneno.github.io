---
layout: none
title: About Me
description: Cyber security professional profile and goals
nav-menu: true
nav-order: 1
summary: >-
  Overview of my journey into cyber security, professional focus areas, and the
  values that guide my work with teams and organisations.
topic_tags:
  - Professional Profile
  - Career Journey
profile_image:
profile_image_alt: Diogo Pereira - Cyber Security Professional
azure_badge_image: https://learn.microsoft.com/training/achievements/azure-administrator.svg
---
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Me | Diogo - Cyber Security Portfolio</title>
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
            position: relative;
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 2px;
            background: var(--primary);
            transition: width 0.3s ease;
        }

        .nav-links a:hover::after {
            width: 100%;
        }

        /* Hero Section */
        .hero-about {
            min-height: 60vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 8rem 5% 4rem;
            position: relative;
        }

        .hero-content {
            max-width: 1400px;
            width: 100%;
            display: grid;
            grid-template-columns: 300px 1fr;
            gap: 4rem;
            align-items: center;
        }

        .profile-image-container {
            position: relative;
        }

        .profile-image {
            width: 300px;
            height: 300px;
            border-radius: 20px;
            overflow: hidden;
            border: 3px solid var(--primary);
            box-shadow: 0 20px 60px rgba(0, 212, 255, 0.3);
            position: relative;
            background: linear-gradient(135deg, #1e293b, #0f172a);
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .profile-image::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, rgba(0, 212, 255, 0.2), rgba(124, 58, 237, 0.2));
            opacity: 0;
            transition: opacity 0.4s ease;
            z-index: 1;
        }

        .profile-image:hover::before {
            opacity: 1;
        }

        .profile-image.profile-image--no-photo::after {
            content: 'Add your photo';
            position: absolute;
            inset: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--text-secondary);
            font-weight: 600;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            text-align: center;
            padding: 1.5rem;
            font-size: 0.85rem;
            background: rgba(15, 23, 42, 0.7);
            border-radius: 20px;
            border: 1px dashed rgba(0, 212, 255, 0.35);
        }

        .profile-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .hero-text h1 {
            font-size: clamp(2.5rem, 5vw, 4rem);
            font-weight: 800;
            margin-bottom: 1rem;
            background: linear-gradient(135deg, #fff 0%, var(--primary) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            line-height: 1.2;
        }

        .hero-text .role {
            font-size: 1.5rem;
            color: var(--primary);
            margin-bottom: 1rem;
            font-weight: 600;
        }

        .hero-text .intro {
            font-size: 1.2rem;
            color: var(--text-secondary);
            line-height: 1.8;
            margin-bottom: 2rem;
        }

        .hero-tags {
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
        }

        .tag {
            padding: 0.5rem 1.2rem;
            background: rgba(0, 212, 255, 0.1);
            border-radius: 20px;
            font-size: 0.9rem;
            color: var(--primary);
            border: 1px solid rgba(0, 212, 255, 0.3);
        }

        /* Main Content */
        .main-content {
            max-width: 1400px;
            margin: 0 auto;
            padding: 4rem 5%;
        }

        .content-section {
            background: rgba(255, 255, 255, 0.03);
            border-radius: 24px;
            padding: 3rem;
            margin-bottom: 2rem;
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: all 0.3s ease;
        }

        .content-section:hover {
            background: rgba(255, 255, 255, 0.05);
            border-color: rgba(0, 212, 255, 0.3);
        }

        .content-section h2 {
            font-size: 2rem;
            margin-bottom: 1.5rem;
            color: var(--primary);
            font-weight: 700;
        }

        .content-section h3 {
            font-size: 1.5rem;
            margin-top: 2rem;
            margin-bottom: 1rem;
            color: var(--text);
            font-weight: 600;
        }

        .content-section p {
            color: var(--text);
            line-height: 1.8;
            margin-bottom: 1.5rem;
        }

        .content-section ul {
            list-style: none;
            padding: 0;
            margin: 1.5rem 0;
        }

        .content-section li {
            padding: 1rem 0;
            padding-left: 2rem;
            position: relative;
            color: var(--text);
            line-height: 1.8;
        }

        .content-section li::before {
            content: '→';
            position: absolute;
            left: 0;
            color: var(--primary);
            font-weight: bold;
        }

        .content-section strong {
            color: var(--primary);
            font-weight: 600;
        }

        /* Certifications Section */
        .certifications-section {
            background: linear-gradient(135deg, rgba(0, 212, 255, 0.05), rgba(124, 58, 237, 0.05));
            border-radius: 24px;
            padding: 4rem 3rem;
            margin: 4rem 0;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .certifications-section h2 {
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 3rem;
            color: var(--text);
        }

        .cert-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }

        .cert-badge {
            background: rgba(255, 255, 255, 0.03);
            border-radius: 16px;
            padding: 1.5rem;
            border: 2px solid rgba(255, 255, 255, 0.1);
            text-align: center;
            transition: all 0.3s ease;
            min-height: 300px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }

        .cert-badge:hover {
            transform: translateY(-10px);
            border-color: var(--primary);
            box-shadow: 0 20px 40px rgba(0, 212, 255, 0.2);
            background: rgba(255, 255, 255, 0.05);
        }

        .cert-badge iframe {
            border: none;
            margin: 0 auto;
        }

        /* Microsoft Badge Styling */
        .microsoft-badge {
            background: rgba(255, 255, 255, 0.03);
            border-radius: 16px;
            padding: 2rem;
            border: 2px solid rgba(255, 255, 255, 0.1);
            text-align: center;
            transition: all 0.3s ease;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }

        .microsoft-badge:hover {
            transform: translateY(-10px);
            border-color: var(--primary);
            box-shadow: 0 20px 40px rgba(0, 212, 255, 0.2);
            background: rgba(255, 255, 255, 0.05);
        }

        .microsoft-badge img {
            width: 150px;
            height: 150px;
            object-fit: contain;
            margin-bottom: 1rem;
        }

        .microsoft-badge .cert-name {
            font-weight: 600;
            color: var(--text);
            margin-top: 1rem;
            font-size: 1rem;
        }

        .microsoft-badge .cert-issuer {
            color: var(--text-secondary);
            font-size: 0.9rem;
            margin-top: 0.5rem;
        }

        .microsoft-badge-fallback {
            color: var(--text-secondary);
            font-weight: 600;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            text-align: center;
        }

        .microsoft-badge a {
            color: var(--primary);
            text-decoration: none;
            font-size: 0.85rem;
            margin-top: 0.5rem;
            transition: all 0.3s ease;
        }

        .microsoft-badge a:hover {
            color: var(--accent);
        }

        /* Focus Areas Grid */
        .focus-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin: 2rem 0;
        }

        .focus-card {
            background: rgba(255, 255, 255, 0.03);
            padding: 2rem;
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: all 0.3s ease;
        }

        .focus-card:hover {
            background: rgba(255, 255, 255, 0.05);
            border-color: var(--primary);
            transform: translateY(-5px);
        }

        .focus-card h4 {
            color: var(--primary);
            margin-bottom: 1rem;
            font-size: 1.2rem;
        }

        .focus-card p {
            color: var(--text-secondary);
            line-height: 1.6;
        }

        /* CTA Section */
        .cta-section {
            background: linear-gradient(135deg, rgba(0, 212, 255, 0.1), rgba(124, 58, 237, 0.1));
            padding: 4rem 3rem;
            border-radius: 24px;
            text-align: center;
            margin: 4rem 0;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .cta-section h2 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            color: var(--text);
        }

        .cta-section p {
            color: var(--text-secondary);
            font-size: 1.2rem;
            margin-bottom: 2rem;
            max-width: 700px;
            margin-left: auto;
            margin-right: auto;
        }

        .btn {
            padding: 1rem 2.5rem;
            border-radius: 50px;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.3s ease;
            display: inline-block;
        }

        .btn-primary {
            background: linear-gradient(135deg, var(--primary), var(--accent));
            color: white;
            box-shadow: 0 10px 30px rgba(0, 212, 255, 0.3);
        }

        .btn-primary:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 40px rgba(0, 212, 255, 0.4);
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

        /* Mobile Responsive */
        @media (max-width: 968px) {
            .hero-content {
                grid-template-columns: 1fr;
                text-align: center;
            }

            .profile-image {
                margin: 0 auto;
            }

            .hero-tags {
                justify-content: center;
            }

            .nav-links {
                display: none;
            }

            .content-section {
                padding: 2rem;
            }

            .certifications-section {
                padding: 3rem 2rem;
            }

            .cert-grid {
                grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            }

            .focus-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="animated-bg"></div>

    <!-- Navigation -->
    <nav>
        <div class="container">
            <a href="{{ '/' | relative_url }}" class="logo">DIOGO • CYBER SEC</a>
            <ul class="nav-links">
                <li><a href="{{ '/' | relative_url }}">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#certifications">Certifications</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero-about">
        <div class="hero-content">
            <div class="profile-image-container">
                {% assign profile_image_src = page.profile_image | default: '' %}
                {% assign profile_image_alt = page.profile_image_alt | default: 'Diogo Pereira - Cyber Security Professional' %}
                <div class="profile-image{% if profile_image_src == '' %} profile-image--no-photo{% endif %}">
                    {% if profile_image_src != '' %}
                        {% if profile_image_src contains '://' %}
                            <img src="{{ profile_image_src }}" alt="{{ profile_image_alt }}" loading="lazy" onerror="this.closest('.profile-image').classList.add('profile-image--no-photo'); this.remove();">
                        {% else %}
                            <img src="{{ profile_image_src | relative_url }}" alt="{{ profile_image_alt }}" loading="lazy" onerror="this.closest('.profile-image').classList.add('profile-image--no-photo'); this.remove();">
                        {% endif %}
                    {% endif %}
                </div>
            </div>
            <div class="hero-text">
                <h1>Hello, I'm Diogo</h1>
                <p class="role">Cyber Security SRE • MSc Candidate</p>
                <p class="intro">
                    I design and operate secure systems to improve team efficiency and productivity. 
                    My work blends practical engineering with critical evaluation and research, 
                    emphasising awareness and self-directed problem-solving.
                </p>
                <div class="hero-tags">
                    <span class="tag">Site Reliability Engineering</span>
                    <span class="tag">Data Protection</span>
                    <span class="tag">Security Operations</span>
                    <span class="tag">Multilingual: EN • PT • ES • FR</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Main Content -->
    <div class="main-content">
        <!-- Professional Snapshot -->
        <section class="content-section" id="about">
            <h2>Professional Snapshot</h2>
            <p>
                As a <strong>Site Reliability Engineer III</strong> specialising in backup and data protection, 
                I provide advanced technical support, replicate complex customer environments, mentor peers, 
                and collaborate with sales, engineering, and product teams. I am multilingual (EN, PT, ES, FR) 
                and have a proven track record of enhancing knowledge base development and team enablement.
            </p>
        </section>

        <!-- How I Work -->
        <section class="content-section">
            <h2>How I Work</h2>
            <ul>
                <li>
                    <strong>Evidence-based decisions:</strong> I rely on threat intelligence, telemetry, 
                    and feedback loops to ensure security decisions are data-driven.
                </li>
                <li>
                    I collaborate with engineers and leadership to co-design controls that strike a balance 
                    between risk and delivery, and I prioritise continuous learning through research, 
                    experimentation, and reflection to maintain current and practical skills.
                </li>
            </ul>
        </section>

        <!-- Focus Areas -->
        <section class="content-section">
            <h2>Focus Areas &amp; Strengths</h2>
            <div class="focus-grid">
                <div class="focus-card">
                    <h4>🔐 Data Protection &amp; Backup</h4>
                    <p>
                        Enterprise backup management (NetBackup, related appliances), customer case ownership, 
                        and lab replication. Skilled in diagnostics across UNIX, Linux, Windows Server, storage, 
                        networking, and virtualization (VMware, Hyper-V). Experience with Azure, AWS, and GCP.
                    </p>
                </div>
                <div class="focus-card">
                    <h4>👥 Customer-Facing Engineering</h4>
                    <p>
                        High-touch support for key customers, clear written analysis, and cross-team collaboration 
                        with sales, engineering, and product teams to secure renewals and resolve deployment challenges.
                    </p>
                </div>
                <div class="focus-card">
                    <h4>⚙️ SRE-style Reliability Practice</h4>
                    <p>
                        Operations as an engineering challenge, focusing on automation, measurable outcomes, 
                        and continuous improvement of products and processes.
                    </p>
                </div>
                <div class="focus-card">
                    <h4>📚 Leadership &amp; Mentorship</h4>
                    <p>
                        Lead and coordinate escalations, supervise multilingual queues (EN, PT, ES, FR, DE), 
                        coach engineers, mentor juniors, and contribute to robust knowledge base development.
                    </p>
                </div>
                <div class="focus-card">
                    <h4>🔄 Process &amp; Product Improvement</h4>
                    <p>
                        Document challenges, refine internal processes, and channel field feedback to enhance 
                        features, service quality, and team efficiency.
                    </p>
                </div>
            </div>
            <p style="margin-top: 2rem;">
                These focus areas map to <strong>CyBOK knowledge domains</strong> such as Secure Software Lifecycle, 
                Security Operations &amp; Incident Management, Risk Management &amp; Governance, and Privacy &amp; Online Rights.
            </p>
        </section>

        <!-- Certifications Section -->
        <section class="certifications-section" id="certifications">
            <h2>Certifications &amp; Credentials</h2>
            <div class="cert-grid">
                <!-- Credly Badges -->
                <div class="cert-badge">
                    <div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="e78dbfed-6ecf-4e63-a9a0-8b538264074a" data-share-badge-host="https://www.credly.com"></div>
                </div>
                <div class="cert-badge">
                    <div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="2e1428be-fe45-4cb3-89ff-fef92049eabb" data-share-badge-host="https://www.credly.com"></div>
                </div>
                <div class="cert-badge">
                    <div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="151746a2-8936-4c92-ae05-27fdded866cd" data-share-badge-host="https://www.credly.com"></div>
                </div>
                <div class="cert-badge">
                    <div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="5dd0f7fb-6f46-464a-9869-19cca942bc8f" data-share-badge-host="https://www.credly.com"></div>
                </div>
                <div class="cert-badge">
                    <div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="6b1c6031-8522-46be-bd7c-0d79adbe6005" data-share-badge-host="https://www.credly.com"></div>
                </div>
                <div class="cert-badge">
                    <div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="ce2641df-01bc-4410-a8b1-a1aeca430724" data-share-badge-host="https://www.credly.com"></div>
                </div>
                <div class="cert-badge">
                    <div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="6378c944-aece-4331-8d35-dbbfaedbaf84" data-share-badge-host="https://www.credly.com"></div>
                </div>
                <div class="cert-badge">
                    <div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="d008a3c7-17ac-47b7-b14d-98df48390dd7" data-share-badge-host="https://www.credly.com"></div>
                </div>
                <div class="cert-badge">
                    <div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="b119fcf3-e68f-4f17-be56-b18d5b3e0569" data-share-badge-host="https://www.credly.com"></div>
                </div>
                <div class="cert-badge">
                    <div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="208ac0ef-3a1f-4525-9d7f-0202730a10bc" data-share-badge-host="https://www.credly.com"></div>
                </div>
                
                <!-- Microsoft Badge -->
                <div class="microsoft-badge">
                    {% assign azure_badge_src = page.azure_badge_image | default: '' %}
                    {% if azure_badge_src != '' %}
                        {% if azure_badge_src contains '://' %}
                            <img src="{{ azure_badge_src }}" alt="Microsoft Certified: Azure Administrator Associate badge" loading="lazy">
                        {% else %}
                            <img src="{{ azure_badge_src | relative_url }}" alt="Microsoft Certified: Azure Administrator Associate badge" loading="lazy">
                        {% endif %}
                    {% else %}
                        <span class="microsoft-badge-fallback">Azure Administrator Associate</span>
                    {% endif %}
                    <p class="cert-name">Azure Administrator Associate</p>
                    <p class="cert-issuer">Microsoft</p>
                    <a href="https://learn.microsoft.com/api/credentials/share/en-us/DiogoNeno/2C20F3038C358900?sharingId=48C04B1899FEF4BE" target="_blank" rel="noopener">Verify Credential →</a>
                </div>
            </div>
        </section>

        <!-- What I'm Doing Now -->
        <section class="content-section">
            <h2>What I'm Doing Now</h2>
            <ul>
                <li>
                    I am advancing my <strong>MSc at the University of Essex Online</strong> by building 
                    an e-portfolio that demonstrates research, secure systems, and human factors with direct 
                    professional application. The programme's focus aligns with my experience.
                </li>
                <li>
                    I continue to develop my skills in line with UK professional standards to ensure 
                    ongoing relevance and measurable growth.
                </li>
            </ul>
        </section>

        <!-- What I'm Looking For -->
        <section class="content-section">
            <h2>What I'm Looking For</h2>
            <p>
               I collaborate on security engineering and architecture initiatives—building secure-by-default platforms, bridging technology and governance, and delivering measurable outcomes. 
               I contribute through hands-on projects, mentoring, and knowledge-sharing with teams that value evidence-based practice, clear communication, and shared ownership of risk.
            </p>
        </section>

        <!-- CTA Section -->
        <section class="cta-section" id="contact">
            <h2>Let's Connect</h2>
            <p>
                Interested in collaborating or discussing cyber security challenges? 
                I'm always open to connecting with like-minded professionals.
            </p>
            <a href="mailto:diogoneno@proton.me" class="btn btn-primary">Get in Touch</a>
        </section>
    </div>

    <!-- Footer -->
    <footer>
        <p>&copy; 2025 MSc Cyber Security Portfolio • Designed by Diogo</p>
    </footer>

    <!-- Credly Badge Script -->
    <script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>

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

        document.querySelectorAll('.content-section, .cert-badge, .focus-card, .microsoft-badge').forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(30px)';
            el.style.transition = 'all 0.6s ease';
            observer.observe(el);
        });
    </script>
</body>
</html>
