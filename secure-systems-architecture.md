---
layout: page
title: Secure Systems Architecture
description: Designing resilient platforms through layered security patterns
nav-menu: true
nav-order: 7
summary: >-
  Architecture-led approach to threat modelling, control selection, and
  verification across complex systems.
---
<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Secure Systems Architecture module: designing resilient platforms through layered security patterns, threat modelling, and authenticated encryption for CPS/IoT systems.">
  <meta name="author" content="MSc Cybersecurity Portfolio">
  <meta name="theme-color" content="#0A1628">
  
  <!-- Open Graph -->
  <meta property="og:title" content="Secure Systems Architecture | MSc Portfolio">
  <meta property="og:description" content="Architecture-led approach to threat modelling, control selection, and verification across complex systems.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://example.github.io/secure-systems-architecture">
  
  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Secure Systems Architecture">
  <meta name="twitter:description" content="Designing resilient platforms through layered security patterns.">
  
  <link rel="canonical" href="https://example.github.io/secure-systems-architecture">
  <title>Secure Systems Architecture | MSc Portfolio</title>
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  
  <style>
    /* ===== CSS VARIABLES ===== */
    :root {
      /* Light Mode Palette */
      --bg-primary: #FFFFFF;
      --bg-secondary: #F8FAFC;
      --bg-tertiary: #F1F5F9;
      --bg-elevated: #FFFFFF;
      --text-primary: #1e293b;
      --text-secondary: #475569;
      --text-tertiary: #64748b;
      --accent-primary: #0891B2;
      --accent-hover: #06B6D4;
      --accent-light: #EFF6FF;
      --border: #E2E8F0;
      --border-strong: #CBD5E1;
      --shadow-sm: 0 2px 8px rgba(15, 23, 42, 0.04);
      --shadow-md: 0 4px 12px rgba(15, 23, 42, 0.08);
      --shadow-lg: 0 8px 24px rgba(15, 23, 42, 0.12);
      --feedback-info-bg: #EFF6FF;
      --feedback-info-border: #0891B2;
      --feedback-info-text: #0A3A5A;
      --feedback-success-bg: #D1FAE5;
      --feedback-success-border: #10B981;
      --feedback-success-text: #065F46;
      --feedback-warning-bg: #FEF3C7;
      --feedback-warning-border: #F59E0B;
      --feedback-warning-text: #92400E;
      --hero-gradient: linear-gradient(135deg, #0E2744 0%, #1e3a5f 100%);
      
      /* Typography */
      --font-display: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      --font-body: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      --font-mono: 'JetBrains Mono', 'Courier New', monospace;
      
      /* Spacing */
      --space-xs: 0.5rem;
      --space-sm: 0.75rem;
      --space-md: 1rem;
      --space-lg: 1.5rem;
      --space-xl: 2rem;
      --space-2xl: 3rem;
      --space-3xl: 4rem;
      
      /* Animation */
      --transition-fast: 150ms ease-out;
      --transition-base: 200ms ease-out;
      --transition-slow: 300ms ease-out;
    }
    
    [data-theme="dark"] {
      --bg-primary: #0A1628;
      --bg-secondary: #0E2744;
      --bg-tertiary: #1e3a5f;
      --bg-elevated: #132844;
      --text-primary: #F1F5F9;
      --text-secondary: #CBD5E1;
      --text-tertiary: #94A3B8;
      --accent-primary: #06B6D4;
      --accent-hover: #22D3EE;
      --accent-light: #1e3a5f;
      --border: #1e3a5f;
      --border-strong: #334155;
      --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.2);
      --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.3);
      --shadow-lg: 0 8px 32px rgba(0, 0, 0, 0.4);
      --feedback-info-bg: #1e3a5f;
      --feedback-info-border: #06B6D4;
      --feedback-info-text: #BAE6FD;
      --feedback-success-bg: #134E3E;
      --feedback-success-border: #10B981;
      --feedback-success-text: #A7F3D0;
      --feedback-warning-bg: #78350F;
      --feedback-warning-border: #F59E0B;
      --feedback-warning-text: #FDE68A;
      --hero-gradient: linear-gradient(135deg, #0A1628 0%, #0E2744 100%);
    }
    
    /* ===== BASE STYLES ===== */
    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    
    html {
      scroll-behavior: smooth;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }
    
    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
      }
    }
    
    body {
      font-family: var(--font-body);
      font-size: 1rem;
      line-height: 1.65;
      color: var(--text-primary);
      background: var(--bg-secondary);
      transition: background var(--transition-base), color var(--transition-base);
    }
    
    /* ===== SKIP LINK ===== */
    .skip-link {
      position: absolute;
      top: -40px;
      left: 0;
      background: var(--accent-primary);
      color: white;
      padding: 0.75rem 1.5rem;
      text-decoration: none;
      font-weight: 600;
      z-index: 100;
      border-radius: 0 0 0.5rem 0;
    }
    
    .skip-link:focus {
      top: 0;
      outline: 3px solid var(--accent-hover);
      outline-offset: 2px;
    }
    
    /* ===== HEADER ===== */
    .header {
      position: sticky;
      top: 0;
      z-index: 50;
      background: var(--bg-elevated);
      border-bottom: 1px solid var(--border);
      box-shadow: var(--shadow-sm);
      backdrop-filter: blur(10px);
    }
    
    .header-inner {
      max-width: 1400px;
      margin: 0 auto;
      padding: 1rem 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
    }
    
    .header-title {
      font-size: 1.125rem;
      font-weight: 700;
      color: var(--text-primary);
      letter-spacing: -0.01em;
    }
    
    .header-controls {
      display: flex;
      align-items: center;
      gap: 1rem;
    }
    
    .btn {
      background: transparent;
      border: 1px solid var(--border);
      border-radius: 0.5rem;
      padding: 0.5rem 1rem;
      font-size: 0.875rem;
      font-weight: 500;
      color: var(--text-primary);
      cursor: pointer;
      transition: all var(--transition-fast);
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
    }
    
    .btn:hover {
      background: var(--bg-tertiary);
      border-color: var(--border-strong);
    }
    
    .btn:focus-visible {
      outline: 3px solid var(--accent-primary);
      outline-offset: 2px;
    }
    
    .btn-primary {
      background: var(--accent-primary);
      border-color: var(--accent-primary);
      color: white;
    }
    
    .btn-primary:hover {
      background: var(--accent-hover);
      border-color: var(--accent-hover);
    }
    
    /* ===== TABLE OF CONTENTS ===== */
    .toc-overlay {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.4);
      backdrop-filter: blur(4px);
      z-index: 60;
      opacity: 0;
      visibility: hidden;
      transition: opacity var(--transition-base), visibility var(--transition-base);
    }
    
    .toc-overlay.active {
      opacity: 1;
      visibility: visible;
    }
    
    .toc {
      position: fixed;
      top: 0;
      right: -320px;
      width: 320px;
      height: 100vh;
      background: var(--bg-elevated);
      border-left: 1px solid var(--border);
      z-index: 70;
      overflow-y: auto;
      transition: right var(--transition-base);
      box-shadow: -4px 0 24px rgba(0, 0, 0, 0.1);
    }
    
    .toc.active {
      right: 0;
    }
    
    .toc-header {
      padding: 1.5rem;
      border-bottom: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      background: var(--bg-elevated);
      z-index: 1;
    }
    
    .toc-title {
      font-size: 1rem;
      font-weight: 600;
      color: var(--text-primary);
    }
    
    .toc-list {
      list-style: none;
      padding: 1.5rem;
    }
    
    .toc-list li {
      margin-bottom: 0.75rem;
    }
    
    .toc-link {
      display: block;
      padding: 0.5rem 0.75rem;
      color: var(--text-secondary);
      text-decoration: none;
      border-radius: 0.375rem;
      transition: all var(--transition-fast);
      font-size: 0.9375rem;
    }
    
    .toc-link:hover,
    .toc-link.active {
      background: var(--accent-light);
      color: var(--accent-primary);
      padding-left: 1rem;
    }
    
    .toc-link:focus-visible {
      outline: 2px solid var(--accent-primary);
      outline-offset: 2px;
    }
    
    /* ===== MAIN CONTENT ===== */
    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 1.5rem;
    }
    
    .section {
      padding: var(--space-3xl) 0;
      opacity: 0;
      transform: translateY(20px);
      transition: opacity 0.6s ease-out, transform 0.6s ease-out;
    }
    
    .section.visible {
      opacity: 1;
      transform: translateY(0);
    }
    
    /* ===== HERO ===== */
    .hero {
      background: var(--hero-gradient);
      color: white;
      border-radius: 1rem;
      padding: var(--space-3xl) var(--space-xl);
      margin: var(--space-xl) 0;
      box-shadow: var(--shadow-lg);
    }
    
    .badge {
      display: inline-block;
      background: rgba(255, 255, 255, 0.15);
      backdrop-filter: blur(10px);
      padding: 0.4rem 1rem;
      border-radius: 999px;
      font-size: 0.8125rem;
      font-weight: 600;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      margin-bottom: 1.5rem;
      border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .hero h1 {
      font-size: clamp(2rem, 5vw, 3rem);
      font-weight: 700;
      margin-bottom: 1rem;
      letter-spacing: -0.02em;
      line-height: 1.15;
    }
    
    .hero-lead {
      font-size: 1.125rem;
      line-height: 1.75;
      opacity: 0.95;
      margin-bottom: 1.5rem;
      max-width: 900px;
    }
    
    .hero-subtext {
      font-size: 1rem;
      line-height: 1.7;
      opacity: 0.85;
      max-width: 900px;
    }
    
    .chip-group {
      display: flex;
      flex-wrap: wrap;
      gap: 0.75rem;
      margin-top: 2rem;
    }
    
    .chip {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: rgba(255, 255, 255, 0.1);
      backdrop-filter: blur(10px);
      border: 1px solid rgba(255, 255, 255, 0.2);
      padding: 0.5rem 1rem;
      border-radius: 999px;
      font-size: 0.875rem;
      font-weight: 500;
      color: white;
    }
    
    .chip svg {
      width: 16px;
      height: 16px;
      opacity: 0.9;
    }
    
    /* ===== SECTION HEADERS ===== */
    .section-header {
      text-align: center;
      margin-bottom: var(--space-2xl);
    }
    
    .section-header h2 {
      font-size: clamp(1.75rem, 4vw, 2.25rem);
      font-weight: 700;
      color: var(--text-primary);
      margin-bottom: 0.75rem;
      letter-spacing: -0.015em;
    }
    
    .section-header .underline {
      width: 60px;
      height: 3px;
      background: linear-gradient(90deg, var(--accent-primary), var(--accent-hover));
      margin: 0 auto 1rem;
      border-radius: 999px;
    }
    
    .section-header p {
      color: var(--text-secondary);
      font-size: 1rem;
      max-width: 600px;
      margin: 0 auto;
    }
    
    /* ===== CARDS ===== */
    .card-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.5rem;
    }
    
    .card {
      background: var(--bg-primary);
      border: 1px solid var(--border);
      border-radius: 0.75rem;
      padding: 1.75rem;
      box-shadow: var(--shadow-md);
      transition: all var(--transition-base);
      height: 100%;
    }
    
    .card:hover {
      transform: translateY(-4px);
      box-shadow: var(--shadow-lg);
      border-color: var(--accent-primary);
    }
    
    .card-icon {
      width: 48px;
      height: 48px;
      background: var(--accent-light);
      border-radius: 0.75rem;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 1rem;
    }
    
    .card-icon svg {
      width: 24px;
      height: 24px;
      color: var(--accent-primary);
    }
    
    .card h4 {
      font-size: 1.125rem;
      font-weight: 600;
      color: var(--text-primary);
      margin-bottom: 0.75rem;
    }
    
    .card p {
      font-size: 0.9375rem;
      color: var(--text-secondary);
      line-height: 1.65;
    }
    
    /* ===== ARTEFACTS ===== */
    .artefact {
      background: var(--bg-primary);
      border-left: 4px solid var(--accent-primary);
      border-radius: 0.75rem;
      padding: var(--space-xl);
      margin-bottom: var(--space-xl);
      box-shadow: var(--shadow-md);
    }
    
    .artefact h3 {
      font-size: 1.375rem;
      font-weight: 600;
      color: var(--text-primary);
      margin-bottom: 1rem;
      line-height: 1.4;
    }
    
    .artefact-content {
      color: var(--text-secondary);
      line-height: 1.75;
      margin-bottom: 1.5rem;
    }
    
    .feedback {
      border-left: 4px solid;
      border-radius: 0.5rem;
      padding: 1.25rem 1.5rem;
      margin-top: 1.5rem;
    }
    
    .feedback-info {
      background: var(--feedback-info-bg);
      border-color: var(--feedback-info-border);
      color: var(--feedback-info-text);
    }
    
    .feedback-success {
      background: var(--feedback-success-bg);
      border-color: var(--feedback-success-border);
      color: var(--feedback-success-text);
    }
    
    .feedback-warning {
      background: var(--feedback-warning-bg);
      border-color: var(--feedback-warning-border);
      color: var(--feedback-warning-text);
    }
    
    .feedback strong {
      font-weight: 600;
      display: block;
      margin-bottom: 0.5rem;
    }
    
    /* ===== TABLES ===== */
    .table-container {
      overflow-x: auto;
      border-radius: 0.75rem;
      box-shadow: var(--shadow-md);
      margin: var(--space-xl) 0;
    }
    
    table {
      width: 100%;
      border-collapse: collapse;
      background: var(--bg-primary);
      min-width: 720px;
    }
    
    thead {
      background: var(--bg-secondary);
    }
    
    th {
      padding: 1rem 1.25rem;
      text-align: left;
      font-weight: 600;
      font-size: 0.875rem;
      color: var(--text-primary);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      border-bottom: 2px solid var(--border);
      white-space: nowrap;
    }
    
    th button {
      background: none;
      border: none;
      font: inherit;
      color: inherit;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0;
      width: 100%;
    }
    
    th button:hover {
      color: var(--accent-primary);
    }
    
    th button:focus-visible {
      outline: 2px solid var(--accent-primary);
      outline-offset: 2px;
      border-radius: 0.25rem;
    }
    
    td {
      padding: 1.25rem;
      border-bottom: 1px solid var(--border);
      color: var(--text-secondary);
      font-size: 0.9375rem;
      line-height: 1.6;
    }
    
    tbody tr {
      transition: background var(--transition-fast);
    }
    
    tbody tr:hover {
      background: var(--bg-secondary);
    }
    
    tbody tr:last-child td {
      border-bottom: none;
    }
    
    .status-badge {
      display: inline-block;
      padding: 0.35rem 0.875rem;
      border-radius: 999px;
      font-size: 0.8125rem;
      font-weight: 500;
      white-space: nowrap;
    }
    
    .status-proficient {
      background: #DBEAFE;
      color: #1E40AF;
    }
    
    [data-theme="dark"] .status-proficient {
      background: #1e3a5f;
      color: #93C5FD;
    }
    
    .proficiency-bar {
      width: 100%;
      height: 6px;
      background: var(--bg-tertiary);
      border-radius: 999px;
      overflow: hidden;
      margin-top: 0.5rem;
    }
    
    .proficiency-fill {
      height: 100%;
      background: linear-gradient(90deg, var(--accent-primary), var(--accent-hover));
      border-radius: 999px;
      transition: width 0.6s ease-out;
    }
    
    /* ===== REFLECTION PANEL ===== */
    .reflection-panel {
      background: var(--hero-gradient);
      color: white;
      border-radius: 1rem;
      padding: var(--space-2xl);
      box-shadow: var(--shadow-lg);
      margin: var(--space-3xl) 0;
    }
    
    .reflection-panel h2 {
      font-size: 1.875rem;
      font-weight: 700;
      margin-bottom: 1.25rem;
    }
    
    .reflection-panel p {
      font-size: 1.0625rem;
      line-height: 1.8;
      opacity: 0.95;
      margin-bottom: 1.25rem;
    }
    
    .reflection-panel p:last-child {
      margin-bottom: 0;
    }
    
    /* ===== FOOTER ===== */
    .footer {
      background: var(--bg-primary);
      border-top: 1px solid var(--border);
      padding: var(--space-xl) 0;
      margin-top: var(--space-3xl);
      text-align: center;
      color: var(--text-tertiary);
      font-size: 0.875rem;
    }
    
    /* ===== PRINT STYLES ===== */
    @media print {
      @page {
        margin: 2cm;
      }
      
      .header,
      .toc,
      .toc-overlay,
      .btn,
      .chip-group,
      .skip-link {
        display: none !important;
      }
      
      body {
        background: white;
        color: black;
        font-size: 11pt;
      }
      
      .section {
        page-break-inside: avoid;
        opacity: 1 !important;
        transform: none !important;
      }
      
      .hero {
        background: #f0f4f8;
        color: black;
        border: 2px solid #0891B2;
      }
      
      .card,
      .artefact {
        page-break-inside: avoid;
        box-shadow: none;
        border: 1px solid #ccc;
      }
      
      a::after {
        content: " (" attr(href) ")";
        font-size: 0.875em;
        color: #666;
      }
      
      table {
        page-break-inside: avoid;
      }
    }
    
    /* ===== RESPONSIVE ===== */
    @media (max-width: 768px) {
      .header-inner {
        padding: 0.875rem 1rem;
      }
      
      .header-title {
        font-size: 1rem;
      }
      
      .hero {
        padding: var(--space-xl) var(--space-lg);
      }
      
      .section {
        padding: var(--space-xl) 0;
      }
      
      .card-grid {
        grid-template-columns: 1fr;
      }
      
      .table-container {
        margin: var(--space-lg) -1rem;
        border-radius: 0;
      }
      
      th, td {
        padding: 0.875rem;
        font-size: 0.875rem;
      }
    }
  </style>
</head>
<body>
  <!-- Skip Link -->
  <a href="#main" class="skip-link">Skip to main content</a>
  
  <!-- Header -->
  <header class="header" role="banner">
    <div class="header-inner">
      <h1 class="header-title">Secure Systems Architecture</h1>
      <div class="header-controls">
        <button id="theme-toggle" class="btn" aria-label="Toggle dark mode">
          <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="10" cy="10" r="4"/>
            <path d="M10 1v2m0 14v2M3.93 3.93l1.41 1.41m11.32 11.32l1.41 1.41M1 10h2m14 0h2M3.93 16.07l1.41-1.41m11.32-11.32l1.41-1.41"/>
          </svg>
          <span id="theme-label">Dark mode</span>
        </button>
        <button id="toc-toggle" class="btn btn-primary" aria-label="Open table of contents" aria-expanded="false">
          <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="3" y1="6" x2="21" y2="6"/>
            <line x1="3" y1="12" x2="21" y2="12"/>
            <line x1="3" y1="18" x2="21" y2="18"/>
          </svg>
          <span>Contents</span>
        </button>
      </div>
    </div>
  </header>
  
  <!-- Table of Contents -->
  <div id="toc-overlay" class="toc-overlay" aria-hidden="true"></div>
  <nav id="toc" class="toc" role="navigation" aria-label="Table of contents">
    <div class="toc-header">
      <h2 class="toc-title">Contents</h2>
      <button id="toc-close" class="btn" aria-label="Close table of contents">
        <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <line x1="18" y1="6" x2="6" y2="18"/>
          <line x1="6" y1="6" x2="18" y2="18"/>
        </svg>
      </button>
    </div>
    <ul id="toc-list" class="toc-list" role="list">
      <!-- Generated by JS -->
    </ul>
  </nav>
  
  <!-- Main Content -->
  <main id="main" role="main">
    <div class="container">
      
      <!-- Hero Section -->
      <section class="hero section visible" id="overview" aria-labelledby="overview-heading">
        <div class="badge">Secure Systems Architecture Module</div>
        <h1 id="overview-heading">Secure Systems Architecture</h1>
        <p class="hero-lead">
          This module concentrated on designing and evaluating secure systems-of-systems (SoS) in CPS/IoT contexts. It integrated architectural thinking (CIA triad with ABCDE characteristics), threat modelling (AD-Trees with quantitative scoring), and a secure IoT messaging prototype, emphasising defensible trade-offs, layered controls, and evidence-driven evaluation under real-world constraints (latency, loss, scale).
        </p>
        <p class="hero-subtext">
          Work spanned strategic design reviews, quantitative risk analysis, and hands-on development of authenticated encryption pipelines. Feedback drove refinements in diagram quality, risk traceability, and the presentation of cost-benefit considerations for blockchain-enabled IoT platforms.
        </p>
        <div class="chip-group" role="list" aria-label="Standards and frameworks">
          <span class="chip" role="listitem">
            <svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
            ISO 27001
          </span>
          <span class="chip" role="listitem">
            <svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            NIST CSF
          </span>
          <span class="chip" role="listitem">
            <svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>
            GDPR
          </span>
          <span class="chip" role="listitem">
            <svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="m16 12-4-4-4 4m8 0-4 4-4-4"/></svg>
            CIA Triad
          </span>
        </div>
      </section>
      
      <!-- Learning Outcomes -->
      <section class="section" id="learning-outcomes" aria-labelledby="outcomes-heading">
        <div class="section-header">
          <h2 id="outcomes-heading">Learning Outcomes</h2>
          <div class="underline"></div>
          <p>Core competencies developed through the module.</p>
        </div>
        <div class="card-grid">
          <article class="card">
            <div class="card-icon">
              <svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>
            </div>
            <h4>Architectural Alignment</h4>
            <p>Design secure CPS/IoT architectures by aligning CIA priorities with ABCDE characteristics and SoS constraints.</p>
          </article>
          <article class="card">
            <div class="card-icon">
              <svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
            </div>
            <h4>Quantitative Threat Modelling</h4>
            <p>Prioritise threats through AD-Trees and quantitative scoring (DREAD/DSS) to justify the sequencing of mitigations.</p>
          </article>
          <article class="card">
            <div class="card-icon">
              <svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
            </div>
            <h4>Secure Communications Engineering</h4>
            <p>Implement authenticated encryption with sound object-oriented design, integrating replay protection and resilience to loss.</p>
          </article>
          <article class="card">
            <div class="card-icon">
              <svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
            </div>
            <h4>Testing &amp; Quality Gates</h4>
            <p>Integrate automated testing, coverage targets, and security tooling to assure reliability under adverse conditions.</p>
          </article>
          <article class="card">
            <div class="card-icon">
              <svg fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
            </div>
            <h4>Evidence-led Communication</h4>
            <p>Communicate architectural decisions, trade-offs, and testing results to technical and non-technical audiences with supporting evidence.</p>
          </article>
        </div>
      </section>
      
      <!-- Artefacts and Feedback -->
      <section class="section" id="artefacts-feedback" aria-labelledby="artefacts-heading">
        <div class="section-header">
          <h2 id="artefacts-heading">Artefacts and Feedback</h2>
          <div class="underline"></div>
          <p>Key deliverables with tutor commentary and growth actions.</p>
        </div>
        
        <article class="artefact">
          <h3>Unit 3 – Development Team Project: Design Document</h3>
          <div class="artefact-content">
            <p>
              Architecture for a blockchain-integrated CPS/IoT system-of-systems identified key vulnerabilities and mapped mitigations via AD-Trees (client node, controller/hub, overall SoS). Controls included multi-factor authentication, Zero Trust patterns, and layered detection aligned to quantified DREAD/DSS scores.
            </p>
          </div>
          <div class="feedback feedback-info">
            <strong>Feedback</strong>
            Strong understanding of SoS security challenges and CIA/ABCDE framing; improve by explicitly linking each vulnerability to ABCDE traits and replacing placeholder diagrams with polished figures.
          </div>
        </article>
        
        <article class="artefact">
          <h3>Unit 6 – Development Individual Project: Code Development</h3>
          <div class="artefact-content">
            <p>
              Built a modular Python simulation of secure IoT communication focused on confidentiality within the ABCDE model. Async components (controller, device, network, packet) used AES-GCM with unique nonces, injected loss and delay, and surfaced metrics. Bandit, Flake8, and Pytest underpinned quality assurance, with documentation detailing experiments and results.
            </p>
          </div>
          <div class="feedback feedback-success">
            <strong>Feedback</strong>
            Commended for clear structure, realistic mitigation rationale, and effective automation; next steps include adding replay detection, key rotation, and deeper chaos testing scenarios.
          </div>
        </article>
        
        <article class="artefact">
          <h3>Unit 6 – Individual Reflective Submission</h3>
          <div class="artefact-content">
            <p>
              Captured lessons on secure architecture for blockchain-enabled CPS/IoT deployments, translating tutor feedback into an action plan for automated testing, AD-Tree enhancements, and tighter ABCDE linkage. Reflections examined team collaboration, delegation, and growth areas.
            </p>
          </div>
          <div class="feedback feedback-warning">
            <strong>Feedback</strong>
            Analytical tone and theory integration were strong; add concrete outcome examples, quantify improvements, and reference recent sources with consistent citation formatting.
          </div>
        </article>
      </section>
      
      <!-- Action Plan -->
      <section class="section" id="action-plan" aria-labelledby="action-heading">
        <div class="section-header">
          <h2 id="action-heading">Action Plan (next 6–8 weeks)</h2>
          <div class="underline"></div>
          <p>Prioritised improvements driven by feedback and observed gaps.</p>
        </div>
        
        <div class="table-container">
          <table id="action-table">
            <thead>
              <tr>
                <th scope="col">
                  <button type="button" data-sort="area" aria-label="Sort by action area">
                    Action area
                    <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                      <polyline points="6 9 12 15 18 9"/>
                    </svg>
                  </button>
                </th>
                <th scope="col">What will be done</th>
                <th scope="col">Evidence of completion</th>
                <th scope="col">
                  <button type="button" data-sort="date" aria-label="Sort by target date">
                    Target date
                    <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                      <polyline points="6 9 12 15 18 9"/>
                    </svg>
                  </button>
                </th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td data-label="Action area"><strong>ABCDE linkage &amp; visuals</strong></td>
                <td data-label="What will be done">Map each vulnerability to ABCDE attributes, regenerate AD-Trees via Graphviz or diagram tooling, remove placeholder artefacts, and standardise figure styling.</td>
                <td data-label="Evidence">Appendix table (vulnerability → ABCDE) and refreshed diagram set in the design document.</td>
                <td data-label="Target date" data-date="2">Week 2</td>
              </tr>
              <tr>
                <td data-label="Action area"><strong>Trade-off analysis</strong></td>
                <td data-label="What will be done">Add quantified discussion on blockchain scalability, latency, and mitigation costs, including sensitivity analysis of DREAD/DSS inputs.</td>
                <td data-label="Evidence">New trade-off subsection plus revised scores with sensitivity commentary.</td>
                <td data-label="Target date" data-date="3">Week 3</td>
              </tr>
              <tr>
                <td data-label="Action area"><strong>Comms hardening</strong></td>
                <td data-label="What will be done">Introduce replay detection (sequence numbers), periodic key rotation, and X25519-based session key agreement layered on AES-GCM.</td>
                <td data-label="Evidence">Passing automated tests, code diffs, and updated README crypto notes.</td>
                <td data-label="Target date" data-date="4">Week 4</td>
              </tr>
              <tr>
                <td data-label="Action area"><strong>Reliability testing</strong></td>
                <td data-label="What will be done">Extend chaos scenarios (duplication, reordering, burst loss) and add Hypothesis property tests plus coverage targets.</td>
                <td data-label="Evidence">CI badge, ≥85% coverage reports, and chaos test execution logs or screenshots.</td>
                <td data-label="Target date" data-date="4">Week 4</td>
              </tr>
              <tr>
                <td data-label="Action area"><strong>CI &amp; quality gates</strong></td>
                <td data-label="What will be done">Implement pre-commit hooks (Black, Flake8, Bandit, Pytest) and GitHub Actions with artefact capture and metric trending.</td>
                <td data-label="Evidence">Committed pre-commit config, CI pipeline history, and trend chart exports.</td>
                <td data-label="Target date" data-date="3">Week 3</td>
              </tr>
              <tr>
                <td data-label="Action area"><strong>Documentation polish</strong></td>
                <td data-label="What will be done">Produce updated architecture and sequence diagrams, operating runbook, and Cite-Them-Right references with consistent styling.</td>
                <td data-label="Evidence">Updated README/design document and alphabetised reference list.</td>
                <td data-label="Target date" data-date="3">Week 3</td>
              </tr>
              <tr>
                <td data-label="Action area"><strong>Reflection updates</strong></td>
                <td data-label="What will be done">Add concrete collaboration examples, measurable impacts, and broadened perspectives backed by recent citations.</td>
                <td data-label="Evidence">Revised reflective submission with in-text citations and word count noted.</td>
                <td data-label="Target date" data-date="2">Week 2</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>
      
      <!-- Professional Skills Matrix -->
      <section class="section" id="skills-matrix" aria-labelledby="skills-heading">
        <div class="section-header">
          <h2 id="skills-heading">Professional Skills Matrix (snapshot)</h2>
          <div class="underline"></div>
          <p>Current strengths with planned improvements aligned to feedback.</p>
        </div>
        
        <div class="table-container">
          <table id="skills-table">
            <thead>
              <tr>
                <th scope="col">
                  <button type="button" data-sort="competency" aria-label="Sort by competency">
                    Competency
                    <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                      <polyline points="6 9 12 15 18 9"/>
                    </svg>
                  </button>
                </th>
                <th scope="col">Current level</th>
                <th scope="col">Evidence</th>
                <th scope="col">Planned improvement</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td data-label="Competency"><strong>Systems architecture (CPS/IoT, SoS)</strong></td>
                <td data-label="Current level">
                  <span class="status-badge status-proficient">Proficient</span>
                  <div class="proficiency-bar"><div class="proficiency-fill" style="width: 75%"></div></div>
                </td>
                <td data-label="Evidence">Coherent SoS design with CIA + ABCDE framing and comprehensive vulnerability analysis.</td>
                <td data-label="Planned improvement">Explicit vulnerability-to-ABCDE mapping, polished diagrams, and deeper scalability trade-offs.</td>
              </tr>
              <tr>
                <td data-label="Competency"><strong>Threat modelling &amp; quantification</strong></td>
                <td data-label="Current level">
                  <span class="status-badge status-proficient">Proficient</span>
                  <div class="proficiency-bar"><div class="proficiency-fill" style="width: 75%"></div></div>
                </td>
                <td data-label="Evidence">AD-Trees for client, hub, and SoS layers with DREAD/DSS prioritisation.</td>
                <td data-label="Planned improvement">Regenerate original figures, add sensitivity analysis, and clarify risk acceptance criteria.</td>
              </tr>
              <tr>
                <td data-label="Competency"><strong>Secure comms engineering (Python)</strong></td>
                <td data-label="Current level">
                  <span class="status-badge status-proficient">Proficient</span>
                  <div class="proficiency-bar"><div class="proficiency-fill" style="width: 80%"></div></div>
                </td>
                <td data-label="Evidence">Modular asyncio/websockets simulation with AES-GCM and resilient packet abstraction.</td>
                <td data-label="Planned improvement">Add replay protection, key rotation with forward secrecy, and extended chaos scenarios.</td>
              </tr>
              <tr>
                <td data-label="Competency"><strong>Testing &amp; assurance</strong></td>
                <td data-label="Current level">
                  <span class="status-badge status-proficient">Proficient</span>
                  <div class="proficiency-bar"><div class="proficiency-fill" style="width: 75%"></div></div>
                </td>
                <td data-label="Evidence">Bandit, Flake8, Pytest, and scenario testing under packet loss and latency.</td>
                <td data-label="Planned improvement">CI with quality gates, property-based tests, and ≥85% coverage tracking.</td>
              </tr>
              <tr>
                <td data-label="Competency"><strong>Documentation &amp; academic practice</strong></td>
                <td data-label="Current level">
                  <span class="status-badge status-proficient">Proficient</span>
                  <div class="proficiency-bar"><div class="proficiency-fill" style="width: 70%"></div></div>
                </td>
                <td data-label="Evidence">Clear README and design rationale with referenced sources.</td>
                <td data-label="Planned improvement">Standardise diagram styles, apply Cite-Them-Right, and expand trade-off exposition.</td>
              </tr>
              <tr>
                <td data-label="Competency"><strong>Collaboration &amp; reflective practice</strong></td>
                <td data-label="Current level">
                  <span class="status-badge status-proficient">Proficient</span>
                  <div class="proficiency-bar"><div class="proficiency-fill" style="width: 75%"></div></div>
                </td>
                <td data-label="Evidence">Reflection linked theory to practice with actionable responses to feedback.</td>
                <td data-label="Planned improvement">Include specific outcome metrics, cite impacts on delivery quality, and broaden perspectives.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>
      
      <!-- Reflection Highlights -->
      <section class="section" id="reflection" aria-labelledby="reflection-heading">
        <div class="reflection-panel">
          <h2 id="reflection-heading">Reflection Highlights</h2>
          <p>
            The module underscored the importance of connecting architectural artefacts with quantifiable risk arguments. Tutor feedback highlighted the need for better diagram polish and clearer ABCDE traceability, which now drive specific improvements in modelling collateral.
          </p>
          <p>
            Implementing authenticated encryption with measurable chaos testing reinforced the value of automation and telemetry in CPS/IoT environments. The next iteration will emphasise forward secrecy, evidence-backed trade-off narratives, and showcasing the measurable impact of collaborative changes.
          </p>
        </div>
      </section>
      
    </div>
  </main>
  
  <!-- Footer -->
  <footer class="footer" role="contentinfo">
    <div class="container">
      <p>&copy; 2025 MSc Cybersecurity Portfolio. Last updated: October 2025.</p>
      <p style="margin-top: 0.5rem; font-size: 0.8125rem;">Optimised for print — all URLs will be visible when printed.</p>
    </div>
  </footer>
  
  <!-- JSON-LD Structured Data -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "Secure Systems Architecture",
    "description": "Architecture-led approach to threat modelling, control selection, and verification across complex CPS/IoT systems.",
    "author": {
      "@type": "Person",
      "name": "MSc Cybersecurity Student"
    },
    "datePublished": "2025-10-27",
    "inLanguage": "en-GB"
  }
  </script>
  
  <!-- JavaScript -->
  <script>
    // ===== THEME TOGGLE =====
    const themeToggle = document.getElementById('theme-toggle');
    const themeLabel = document.getElementById('theme-label');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)');
    
    // Initialize theme
    const currentTheme = localStorage.getItem('theme') || (prefersDark.matches ? 'dark' : 'light');
    document.documentElement.setAttribute('data-theme', currentTheme);
    updateThemeLabel(currentTheme);
    
    themeToggle.addEventListener('click', () => {
      const newTheme = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('theme', newTheme);
      updateThemeLabel(newTheme);
    });
    
    function updateThemeLabel(theme) {
      themeLabel.textContent = theme === 'dark' ? 'Light mode' : 'Dark mode';
      themeToggle.setAttribute('aria-label', `Switch to ${theme === 'dark' ? 'light' : 'dark'} mode`);
    }
    
    // ===== TABLE OF CONTENTS =====
    const toc = document.getElementById('toc');
    const tocToggle = document.getElementById('toc-toggle');
    const tocClose = document.getElementById('toc-close');
    const tocOverlay = document.getElementById('toc-overlay');
    const tocList = document.getElementById('toc-list');
    
    // Generate TOC from sections
    const sections = document.querySelectorAll('.section[id]');
    sections.forEach((section, index) => {
      const heading = section.querySelector('h2');
      if (heading) {
        const li = document.createElement('li');
        const a = document.createElement('a');
        a.href = `#${section.id}`;
        a.className = 'toc-link';
        a.textContent = heading.textContent;
        a.addEventListener('click', (e) => {
          e.preventDefault();
          closeTOC();
          section.scrollIntoView({ behavior: 'smooth' });
          section.setAttribute('tabindex', '-1');
          section.focus();
          setTimeout(() => section.removeAttribute('tabindex'), 1000);
        });
        li.appendChild(a);
        tocList.appendChild(li);
      }
    });
    
    function openTOC() {
      toc.classList.add('active');
      tocOverlay.classList.add('active');
      tocToggle.setAttribute('aria-expanded', 'true');
      tocOverlay.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
    }
    
    function closeTOC() {
      toc.classList.remove('active');
      tocOverlay.classList.remove('active');
      tocToggle.setAttribute('aria-expanded', 'false');
      tocOverlay.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    }
    
    tocToggle.addEventListener('click', openTOC);
    tocClose.addEventListener('click', closeTOC);
    tocOverlay.addEventListener('click', closeTOC);
    
    // Close TOC on Escape
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && toc.classList.contains('active')) {
        closeTOC();
        tocToggle.focus();
      }
    });
    
    // ===== SCROLL REVEAL =====
    const observerOptions = {
      root: null,
      rootMargin: '0px',
      threshold: 0.1
    };
    
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
        }
      });
    }, observerOptions);
    
    document.querySelectorAll('.section:not(.visible)').forEach(section => {
      observer.observe(section);
    });
    
    // ===== ACTIVE TOC LINK =====
    const tocLinks = document.querySelectorAll('.toc-link');
    
    const linkObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const id = entry.target.id;
          tocLinks.forEach(link => {
            link.classList.toggle('active', link.getAttribute('href') === `#${id}`);
          });
        }
      });
    }, { rootMargin: '-20% 0px -35% 0px' });
    
    sections.forEach(section => linkObserver.observe(section));
    
    // ===== TABLE SORTING =====
    function sortTable(table, columnIndex, direction = 'asc') {
      const tbody = table.querySelector('tbody');
      const rows = Array.from(tbody.querySelectorAll('tr'));
      
      rows.sort((a, b) => {
        let aValue = a.cells[columnIndex].textContent.trim();
        let bValue = b.cells[columnIndex].textContent.trim();
        
        // Check for data attributes (e.g., data-date for numeric sorting)
        const aData = a.cells[columnIndex].getAttribute('data-date');
        const bData = b.cells[columnIndex].getAttribute('data-date');
        
        if (aData && bData) {
          aValue = parseInt(aData);
          bValue = parseInt(bData);
          return direction === 'asc' ? aValue - bValue : bValue - aValue;
        }
        
        // String comparison
        return direction === 'asc' 
          ? aValue.localeCompare(bValue) 
          : bValue.localeCompare(aValue);
      });
      
      rows.forEach(row => tbody.appendChild(row));
    }
    
    // Add sort handlers to all sortable table headers
    document.querySelectorAll('th button[data-sort]').forEach(button => {
      let direction = 'asc';
      button.addEventListener('click', () => {
        const table = button.closest('table');
        const th = button.closest('th');
        const columnIndex = Array.from(th.parentElement.children).indexOf(th);
        
        // Toggle direction
        direction = direction === 'asc' ? 'desc' : 'asc';
        
        // Update ARIA
        button.setAttribute('aria-label', `Sort by ${button.textContent.trim()} ${direction === 'asc' ? 'ascending' : 'descending'}`);
        
        // Sort
        sortTable(table, columnIndex, direction);
        
        // Visual feedback - rotate arrow
        const svg = button.querySelector('svg');
        svg.style.transform = direction === 'desc' ? 'rotate(180deg)' : 'rotate(0deg)';
      });
    });
    
    // ===== PROFICIENCY BARS ANIMATION =====
    const proficiencyObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const fills = entry.target.querySelectorAll('.proficiency-fill');
          fills.forEach(fill => {
            fill.style.width = fill.style.width; // Trigger reflow for animation
          });
          proficiencyObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });
    
    document.querySelectorAll('#skills-table').forEach(table => {
      proficiencyObserver.observe(table);
    });
    
    // ===== SMOOTH SCROLL FOR HASH LINKS =====
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        const targetId = this.getAttribute('href').substring(1);
        const target = document.getElementById(targetId);
        if (target && targetId) {
          e.preventDefault();
          target.scrollIntoView({ behavior: 'smooth' });
          target.setAttribute('tabindex', '-1');
          target.focus();
          setTimeout(() => target.removeAttribute('tabindex'), 1000);
        }
      });
    });
  </script>
</body>
</html>
