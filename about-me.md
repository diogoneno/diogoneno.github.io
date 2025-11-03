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
profile_image: /assets/images/test.jpg
profile_image_alt: Diogo Pereira - Cyber Security Professional
azure_badge_image: /assets/images/microsoft-certified-azure-administrator-associate.2.png
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
            --success: #10b981;
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
                radial-gradient(circle at 20% 50%, rgba(0, 212, 255, 0.15) 0%, transparent 50%),
                radial-gradient(circle at 80% 80%, rgba(124, 58, 237, 0.15) 0%, transparent 50%);
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
            background: rgba(10, 14, 39, 0.9);
            backdrop-filter: blur(20px);
            z-index: 1000;
            border-bottom: 1px solid rgba(0, 212, 255, 0.2);
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

        .nav-links a:hover::after,
        .nav-links a.active::after {
            width: 100%;
        }

        .nav-links a:hover {
            color: var(--primary);
        }

        /* Hero Section with Profile */
        .hero-about {
            min-height: 70vh;
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
            grid-template-columns: 350px 1fr;
            gap: 4rem;
            align-items: center;
        }

        .profile-section {
            position: relative;
        }

        .profile-image-container {
            position: relative;
            width: 350px;
            height: 350px;
        }

        .profile-image {
            width: 100%;
            height: 100%;
            border-radius: 30px;
            overflow: hidden;
            border: 3px solid var(--primary);
            box-shadow: 0 25px 70px rgba(0, 212, 255, 0.4);
            position: relative;
            background: linear-gradient(135deg, #1e293b, #0f172a);
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.4s ease;
        }

        .profile-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
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

        .profile-image:hover {
            transform: translateY(-10px) scale(1.02);
            box-shadow: 0 35px 90px rgba(0, 212, 255, 0.5);
        }

        .profile-image.profile-image--no-photo::after {
            content: 'Add your profile photo';
            position: absolute;
            inset: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 1.5rem;
            color: rgba(255, 255, 255, 0.8);
            font-weight: 600;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            background: rgba(10, 14, 39, 0.75);
            border-radius: 30px;
            border: 1px dashed rgba(0, 212, 255, 0.35);
        }

        .status-badge {
            position: absolute;
            bottom: 20px;
            right: 20px;
            background: rgba(16, 185, 129, 0.9);
            backdrop-filter: blur(10px);
            color: white;
            padding: 0.75rem 1.5rem;
            border-radius: 50px;
            font-size: 0.9rem;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            box-shadow: 0 10px 30px rgba(16, 185, 129, 0.3);
            z-index: 2;
        }

        .status-badge::before {
            content: '';
            width: 8px;
            height: 8px;
            background: white;
            border-radius: 50%;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.5; transform: scale(1.2); }
        }

        .hero-text {
            animation: fadeInUp 1s ease;
        }

        .hero-text h1 {
            font-size: 3.5rem;
            font-weight: 800;
            line-height: 1.2;
            margin-bottom: 1.5rem;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .hero-text .subtitle {
            font-size: 1.5rem;
            color: var(--text-secondary);
            margin-bottom: 2rem;
        }

        .hero-text p {
            font-size: 1.2rem;
            color: var(--text);
            line-height: 1.8;
            margin-bottom: 2rem;
        }

        /* Glass Card Effect */
        .glass-card {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            border-radius: 24px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 3rem;
            transition: all 0.4s ease;
            position: relative;
            overflow: hidden;
        }

        .glass-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, rgba(0, 212, 255, 0.1), rgba(124, 58, 237, 0.1));
            opacity: 0;
            transition: opacity 0.4s ease;
            pointer-events: none;
        }

        .glass-card:hover::before {
            opacity: 1;
        }

        .glass-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 25px 50px rgba(0, 212, 255, 0.2);
            border-color: rgba(0, 212, 255, 0.3);
        }

        /* Content Sections */
        .content-section {
            max-width: 1400px;
            margin: 0 auto 4rem;
            padding: 0 5%;
            animation: fadeInUp 0.8s ease;
        }

        .content-section h2 {
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 2rem;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .content-section p {
            font-size: 1.1rem;
            color: var(--text);
            line-height: 1.8;
            margin-bottom: 1.5rem;
        }

        .content-section ul {
            list-style: none;
            padding-left: 0;
        }

        .content-section ul li {
            font-size: 1.1rem;
            color: var(--text);
            line-height: 1.8;
            margin-bottom: 1rem;
            padding-left: 2rem;
            position: relative;
        }

        .content-section ul li::before {
            content: '→';
            position: absolute;
            left: 0;
            color: var(--primary);
            font-weight: bold;
        }

        /* Focus Areas Grid */
        .focus-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }

        .focus-card {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 2rem;
            transition: all 0.3s ease;
        }

        .focus-card:hover {
            background: rgba(255, 255, 255, 0.08);
            border-color: var(--primary);
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(0, 212, 255, 0.2);
        }

        .focus-card h4 {
            color: var(--primary);
            font-size: 1.3rem;
            margin-bottom: 1rem;
        }

        .focus-card p {
            color: var(--text-secondary);
            font-size: 1rem;
            line-height: 1.7;
        }

        /* Certifications */
        .certifications-section {
            max-width: 1400px;
            margin: 0 auto 4rem;
            padding: 0 5%;
        }

        .certifications-section h2 {
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 3rem;
            text-align: center;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .cert-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }

        .cert-badge {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 270px;
            transition: transform 0.3s ease;
        }

        .cert-badge:hover {
            transform: translateY(-10px);
        }

        .microsoft-badge {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 2rem;
            text-align: center;
            transition: all 0.3s ease;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 1rem;
        }

        .microsoft-badge:hover {
            background: rgba(255, 255, 255, 0.08);
            border-color: var(--primary);
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0, 212, 255, 0.2);
        }

        .microsoft-badge img {
            max-width: 150px;
            height: auto;
        }

        .microsoft-badge .cert-name {
            color: var(--primary);
            font-weight: 600;
            margin: 0 0 0.5rem;
        }

        .microsoft-badge .cert-issuer {
            color: var(--text-secondary);
            font-size: 0.9rem;
            margin-bottom: 0.5rem;
        }

        .microsoft-badge a {
            color: var(--primary);
            text-decoration: none;
            font-size: 0.9rem;
            transition: all 0.3s ease;
        }

        .microsoft-badge a:hover {
            color: var(--accent);
        }

        .badge-placeholder {
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 150px;
            width: 100%;
            border-radius: 14px;
            background: rgba(0, 212, 255, 0.05);
            color: rgba(255, 255, 255, 0.7);
            font-weight: 600;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            padding: 1.5rem;
            text-align: center;
            border: 1px dashed rgba(0, 212, 255, 0.35);
        }

        .badge-placeholder--hidden {
            display: none;
        }

        .microsoft-badge.microsoft-badge--no-logo {
            gap: 0.5rem;
        }

        /* Enhanced What I'm Looking For Section */
        .looking-for-section {
            max-width: 1400px;
            margin: 6rem auto;
            padding: 0 5%;
        }

        .section-header {
            text-align: center;
            margin-bottom: 4rem;
        }

        .section-header h2 {
            font-size: 3rem;
            font-weight: 700;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 1rem;
        }

        .section-header p {
            color: var(--text-secondary);
            font-size: 1.2rem;
            max-width: 700px;
            margin: 0 auto;
        }

        .objective-card {
            display: grid;
            grid-template-columns: 100px 1fr;
            gap: 2.5rem;
            padding: 3rem;
            margin-bottom: 2rem;
            align-items: start;
        }

        .objective-icon {
            width: 100px;
            height: 100px;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            border-radius: 25px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 3rem;
            box-shadow: 0 15px 40px rgba(0, 212, 255, 0.4);
            transition: all 0.3s ease;
        }

        .objective-card:hover .objective-icon {
            transform: scale(1.1) rotate(5deg);
            box-shadow: 0 20px 50px rgba(0, 212, 255, 0.6);
        }

        .objective-content h3 {
            color: var(--primary);
            font-size: 1.8rem;
            margin-bottom: 1.5rem;
        }

        .objective-content p {
            color: var(--text);
            font-size: 1.15rem;
            line-height: 1.9;
        }

        /* Stats Section */
        .stats-section {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }

        .stat-card {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 2.5rem;
            text-align: center;
            transition: all 0.3s ease;
        }

        .stat-card:hover {
            background: rgba(255, 255, 255, 0.08);
            transform: translateY(-10px);
            border-color: var(--primary);
            box-shadow: 0 20px 50px rgba(0, 212, 255, 0.3);
        }

        .stat-number {
            font-size: 3.5rem;
            font-weight: 700;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 0.5rem;
        }

        .stat-label {
            color: var(--text-secondary);
            font-size: 1.1rem;
        }

        /* Developer Tools Section */
        .devtools-section {
            max-width: 1400px;
            margin: 6rem auto;
            padding: 0 5%;
        }

        .tools-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }

        .tool-category {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 2rem;
            transition: all 0.3s ease;
        }

        .tool-category:hover {
            background: rgba(255, 255, 255, 0.06);
            border-color: var(--primary);
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0, 212, 255, 0.2);
        }

        .tool-category-header {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1.5rem;
        }

        .tool-icon {
            width: 55px;
            height: 55px;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.8rem;
            box-shadow: 0 8px 20px rgba(0, 212, 255, 0.3);
        }

        .tool-category h4 {
            color: var(--primary);
            font-size: 1.3rem;
        }

        .tool-list {
            display: flex;
            flex-wrap: wrap;
            gap: 0.75rem;
        }

        .tool-badge {
            background: rgba(0, 212, 255, 0.1);
            border: 1px solid rgba(0, 212, 255, 0.3);
            color: var(--primary);
            padding: 0.6rem 1.2rem;
            border-radius: 10px;
            font-size: 0.95rem;
            font-weight: 500;
            transition: all 0.3s ease;
            cursor: default;
        }

        .tool-badge:hover {
            background: rgba(0, 212, 255, 0.2);
            border-color: var(--primary);
            transform: scale(1.05) translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 212, 255, 0.3);
        }

        /* Connect Section */
        .connect-section {
            max-width: 1400px;
            margin: 6rem auto 4rem;
            padding: 0 5%;
        }

        .connect-card {
            text-align: center;
            padding: 4rem 3rem;
            background: linear-gradient(135deg, rgba(0, 212, 255, 0.1), rgba(124, 58, 237, 0.1));
        }

        .connect-card h2 {
            font-size: 3rem;
            margin-bottom: 1.5rem;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .connect-card p {
            font-size: 1.2rem;
            color: var(--text-secondary);
            max-width: 700px;
            margin: 0 auto 2.5rem;
            line-height: 1.8;
        }

        .connect-buttons {
            display: flex;
            gap: 1.5rem;
            justify-content: center;
            flex-wrap: wrap;
        }

        .btn {
            padding: 1.2rem 2.5rem;
            border-radius: 14px;
            font-size: 1.1rem;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.3s ease;
            display: inline-flex;
            align-items: center;
            gap: 0.75rem;
            border: none;
            cursor: pointer;
        }

        .btn-primary {
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: var(--darker);
            box-shadow: 0 10px 30px rgba(0, 212, 255, 0.4);
        }

        .btn-primary:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 40px rgba(0, 212, 255, 0.6);
        }

        .btn-secondary {
            background: rgba(255, 255, 255, 0.1);
            color: var(--text);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .btn-secondary:hover {
            background: rgba(255, 255, 255, 0.15);
            border-color: var(--primary);
            transform: translateY(-3px);
        }

        /* Footer */
        footer {
            text-align: center;
            padding: 3rem 5%;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            color: var(--text-secondary);
        }

        footer p {
            font-size: 1rem;
        }

        /* Animations */
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .fade-in-up {
            animation: fadeInUp 0.8s ease forwards;
        }

        /* Responsive */
        @media (max-width: 1024px) {
            .hero-content {
                grid-template-columns: 300px 1fr;
                gap: 3rem;
            }

            .profile-image-container {
                width: 300px;
                height: 300px;
            }

            .hero-text h1 {
                font-size: 2.5rem;
            }
        }

        @media (max-width: 768px) {
            .hero-content {
                grid-template-columns: 1fr;
                gap: 2rem;
                text-align: center;
            }

            .profile-image-container {
                width: 250px;
                height: 250px;
                margin: 0 auto;
            }

            .profile-image.profile-image--no-photo::after {
                border-radius: 20px;
            }

            .hero-text h1 {
                font-size: 2rem;
            }

            .hero-text .subtitle {
                font-size: 1.2rem;
            }

            .section-header h2 {
                font-size: 2rem;
            }

            .objective-card {
                grid-template-columns: 1fr;
                gap: 1.5rem;
                padding: 2rem;
            }

            .objective-icon {
                width: 80px;
                height: 80px;
                font-size: 2.5rem;
                margin: 0 auto;
            }

            .tools-grid {
                grid-template-columns: 1fr;
            }

            .connect-buttons {
                flex-direction: column;
                align-items: stretch;
            }

            .btn {
                width: 100%;
                justify-content: center;
            }

            .nav-links {
                display: none;
            }

            .stats-section {
                grid-template-columns: repeat(2, 1fr);
            }
        }
    </style>
</head>
<body>
    <div class="animated-bg"></div>

    <!-- Navigation -->
    <nav>
        <div class="container">
            <a href="/" class="logo">Diogo Pereira</a>
            <ul class="nav-links">
                <li><a href="/" class="active">About</a></li>
                <li><a href="#certifications">Certifications</a></li>
                <li><a href="#devtools">Tools</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero-about">
        <div class="hero-content">
            <div class="profile-section">
                <div class="profile-image-container">
                    {% assign profile_src = page.profile_image | default: '' %}
                    {% assign profile_alt = page.profile_image_alt | default: 'Profile photo' %}
                    <div class="profile-image{% if profile_src == '' %} profile-image--no-photo{% endif %}">
                        {% if profile_src != '' %}
                            {% if profile_src contains '://' %}
                                <img src="{{ profile_src }}" alt="{{ profile_alt }}" loading="eager" onerror="this.closest('.profile-image').classList.add('profile-image--no-photo'); this.remove();">
                            {% else %}
                                <img src="{{ profile_src | relative_url }}" alt="{{ profile_alt }}" loading="eager" onerror="this.closest('.profile-image').classList.add('profile-image--no-photo'); this.remove();">
                            {% endif %}
                        {% endif %}
                    </div>
                    <div class="status-badge">Open to Opportunities</div>
                </div>
            </div>
            <div class="hero-text">
                <h1>Cyber Security Professional</h1>
                <p class="subtitle">Building Secure, Resilient Systems</p>
                <p>
                    I'm a cyber security professional with over a decade of experience in security engineering, 
                    data protection, and cloud infrastructure. I specialize in building secure-by-default platforms 
                    and bridging the gap between technology and governance.
                </p>
            </div>
        </div>
    </section>

    <div class="container">
        <!-- Who I Am -->
        <section class="content-section">
            <h2>Who I Am</h2>
            <p>
                I'm Diogo, a Cyber Security professional with 10+ years of IT, 15+ certifications, and an MSc in Cyber Security 
                (University of Essex Online, UK). I have worked in enterprise support roles across multi-national environments 
                where secure technology meets reliability, customer outcomes, and business goals.
            </p>
            <p>
                My specialisation is <strong>data protection</strong> and <strong>enterprise backup management</strong> 
                (NetBackup, appliances, Azure, AWS, GCP), with advanced skills in diagnosing complex issues across UNIX, Linux, 
                Windows Server, storage, networking, and virtualisation. My core approach is <strong>SRE-style reliability</strong> 
                at scale, focusing on automation, measurable outcomes, and systematic improvement.
            </p>
        </section>

        <!-- Journey -->
        <section class="content-section">
            <h2>Journey</h2>
            <ul>
                <li>
                    I started in IT support and advanced to enterprise technical roles at Veritas Technologies, 
                    working with high-value customers globally, leading escalations, and mentoring junior engineers.
                </li>
                <li>
                    I've championed process improvements, built knowledge bases, and co-ordinated multilingual queues 
                    (EN, PT, ES, FR, DE), treating operations as a measurable engineering challenge.
                </li>
                <li>
                    I'm pursuing an MSc in Cyber Security to formalise my practical experience into evidence-based, 
                    research-supported practice. This extends my enterprise support foundation with risk governance, 
                    secure systems design, and human factors.
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
                {% assign azure_badge_src = page.azure_badge_image | default: '' %}
                <div class="microsoft-badge{% if azure_badge_src == '' %} microsoft-badge--no-logo{% endif %}">
                    {% if azure_badge_src != '' %}
                        {% if azure_badge_src contains '://' %}
                            <img src="{{ azure_badge_src }}" alt="Microsoft Certified: Azure Administrator Associate badge" loading="lazy" onerror="const badge = this.closest('.microsoft-badge'); badge.classList.add('microsoft-badge--no-logo'); const placeholder = badge.querySelector('.badge-placeholder'); if (placeholder) { placeholder.classList.remove('badge-placeholder--hidden'); } this.remove();">
                        {% else %}
                            <img src="{{ azure_badge_src | relative_url }}" alt="Microsoft Certified: Azure Administrator Associate badge" loading="lazy" onerror="const badge = this.closest('.microsoft-badge'); badge.classList.add('microsoft-badge--no-logo'); const placeholder = badge.querySelector('.badge-placeholder'); if (placeholder) { placeholder.classList.remove('badge-placeholder--hidden'); } this.remove();">
                        {% endif %}
                    {% endif %}
                    <div class="badge-placeholder{% if azure_badge_src != '' %} badge-placeholder--hidden{% endif %}">Azure Administrator Associate</div>
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
    </div>

    <!-- What I'm Looking For Section -->
    <section class="looking-for-section">
        <div class="section-header fade-in-up">
            <h2>What I'm Looking For</h2>
            <p>Building secure systems that balance innovation with protection</p>
        </div>

        <div class="glass-card objective-card fade-in-up">
            <div class="objective-icon">🔐</div>
            <div class="objective-content">
                <h3>Security Engineering &amp; Architecture</h3>
                <p>
                    I collaborate on security engineering and architecture initiatives—building secure-by-default platforms, 
                    bridging technology and governance, and delivering measurable outcomes. I contribute through hands-on 
                    projects, mentoring, and knowledge-sharing with teams that value evidence-based practice, clear 
                    communication, and shared ownership of risk.
                </p>
            </div>
        </div>

        <div class="stats-section">
            <div class="stat-card fade-in-up">
                <div class="stat-number">10+</div>
                <div class="stat-label">Years in Security</div>
            </div>
            <div class="stat-card fade-in-up">
                <div class="stat-number">15+</div>
                <div class="stat-label">Certifications</div>
            </div>
            <div class="stat-card fade-in-up">
                <div class="stat-number">5+</div>
                <div class="stat-label">Cloud Platforms</div>
            </div>
            <div class="stat-card fade-in-up">
                <div class="stat-number">∞</div>
                <div class="stat-label">Learning Mindset</div>
            </div>
        </div>
    </section>

    <!-- Developer Tools Section -->
    <section class="devtools-section" id="devtools">
        <div class="section-header fade-in-up">
            <h2>Developer Tools &amp; Stack</h2>
            <p>Technologies and tools I work with to build secure, scalable systems</p>
        </div>

        <div class="tools-grid">
            <div class="tool-category fade-in-up">
                <div class="tool-category-header">
                    <div class="tool-icon">☁️</div>
                    <h4>Cloud Platforms</h4>
                </div>
                <div class="tool-list">
                    <span class="tool-badge">Azure</span>
                    <span class="tool-badge">AWS</span>
                    <span class="tool-badge">GCP</span>
                    <span class="tool-badge">Azure DevOps</span>
                    <span class="tool-badge">Terraform</span>
                </div>
            </div>

            <div class="tool-category fade-in-up">
                <div class="tool-category-header">
                    <div class="tool-icon">🔒</div>
                    <h4>Security Tools</h4>
                </div>
                <div class="tool-list">
                    <span class="tool-badge">Nmap</span>
                    <span class="tool-badge">Wireshark</span>
                    <span class="tool-badge">Metasploit</span>
                    <span class="tool-badge">Burp Suite</span>
                    <span class="tool-badge">OWASP ZAP</span>
                    <span class="tool-badge">Snort</span>
                </div>
            </div>

            <div class="tool-category fade-in-up">
                <div class="tool-category-header">
                    <div class="tool-icon">💻</div>
                    <h4>Programming</h4>
                </div>
                <div class="tool-list">
                    <span class="tool-badge">Python</span>
                    <span class="tool-badge">Bash</span>
                    <span class="tool-badge">PowerShell</span>
                    <span class="tool-badge">JavaScript</span>
                    <span class="tool-badge">SQL</span>
                </div>
            </div>

            <div class="tool-category fade-in-up">
                <div class="tool-category-header">
                    <div class="tool-icon">🐳</div>
                    <h4>DevOps &amp; Containers</h4>
                </div>
                <div class="tool-list">
                    <span class="tool-badge">Docker</span>
                    <span class="tool-badge">Kubernetes</span>
                    <span class="tool-badge">Git</span>
                    <span class="tool-badge">Jenkins</span>
                    <span class="tool-badge">Ansible</span>
                </div>
            </div>

            <div class="tool-category fade-in-up">
                <div class="tool-category-header">
                    <div class="tool-icon">💾</div>
                    <h4>Data Protection</h4>
                </div>
                <div class="tool-list">
                    <span class="tool-badge">NetBackup</span>
                    <span class="tool-badge">Veeam</span>
                    <span class="tool-badge">Azure Backup</span>
                    <span class="tool-badge">Commvault</span>
                </div>
            </div>

            <div class="tool-category fade-in-up">
                <div class="tool-category-header">
                    <div class="tool-icon">🖥️</div>
                    <h4>Operating Systems</h4>
                </div>
                <div class="tool-list">
                    <span class="tool-badge">Linux</span>
                    <span class="tool-badge">Windows Server</span>
                    <span class="tool-badge">UNIX</span>
                    <span class="tool-badge">Ubuntu</span>
                    <span class="tool-badge">CentOS</span>
                </div>
            </div>

            <div class="tool-category fade-in-up">
                <div class="tool-category-header">
                    <div class="tool-icon">📊</div>
                    <h4>Monitoring &amp; Analysis</h4>
                </div>
                <div class="tool-list">
                    <span class="tool-badge">Splunk</span>
                    <span class="tool-badge">ELK Stack</span>
                    <span class="tool-badge">Grafana</span>
                    <span class="tool-badge">Prometheus</span>
                    <span class="tool-badge">Nagios</span>
                </div>
            </div>

            <div class="tool-category fade-in-up">
                <div class="tool-category-header">
                    <div class="tool-icon">🌐</div>
                    <h4>Virtualization</h4>
                </div>
                <div class="tool-list">
                    <span class="tool-badge">VMware</span>
                    <span class="tool-badge">Hyper-V</span>
                    <span class="tool-badge">VirtualBox</span>
                    <span class="tool-badge">Proxmox</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Let's Connect Section -->
    <section class="connect-section" id="contact">
        <div class="glass-card connect-card fade-in-up">
            <h2>Let's Connect</h2>
            <p>
                Interested in collaborating or discussing cyber security challenges? 
                I'm always open to connecting with like-minded professionals who are passionate 
                about building secure, resilient systems.
            </p>
            <div class="connect-buttons">
                <a href="mailto:diogoneno@proton.me" class="btn btn-primary">
                    📧 Get in Touch
                </a>
                <a href="{{ site.linkedin_url | default: 'https://www.linkedin.com/in/diogoamarantes/' }}" target="_blank" rel="noopener" class="btn btn-secondary">
                    💼 LinkedIn Profile
                </a>
                <a href="{{ site.github_url | default: 'https://github.com/diogoneno' }}" target="_blank" rel="noopener" class="btn btn-secondary">
                    📄 Download CV
                </a>
            </div>
        </div>
    </section>

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

        // Observe all animated elements
        document.querySelectorAll('.fade-in-up, .content-section, .cert-badge, .focus-card, .microsoft-badge, .tool-category, .stat-card').forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(30px)';
            el.style.transition = 'all 0.8s ease';
            observer.observe(el);
        });

        // Add hover effect to tool badges
        document.querySelectorAll('.tool-badge').forEach(badge => {
            badge.addEventListener('mouseenter', function() {
                this.style.transform = 'scale(1.05) translateY(-2px)';
            });
            badge.addEventListener('mouseleave', function() {
                this.style.transform = 'scale(1) translateY(0)';
            });
        });

        // Highlight active navigation
        const sections = document.querySelectorAll('section[id]');
        const navLinks = document.querySelectorAll('.nav-links a');

        window.addEventListener('scroll', () => {
            let current = '';
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                const sectionHeight = section.clientHeight;
                if (scrollY >= (sectionTop - 200)) {
                    current = section.getAttribute('id');
                }
            });

            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href').includes(current)) {
                    link.classList.add('active');
                }
            });
        });
    </script>
</body>
</html>
