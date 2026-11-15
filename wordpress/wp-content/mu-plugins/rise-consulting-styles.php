<?php
/**
 * Plugin Name: Rise Growth Consulting Theme Enhancement
 * Description: Premium styles, fonts, layout overrides, CORS support, and interactivity for Rise Growth Group.
 * Version: 1.1.0
 * Author: Antigravity
 */

// Enable CORS so Headless React / Next.js can query the WordPress REST API seamlessly
add_action( 'rest_api_init', function() {
    remove_filter( 'rest_pre_serve_request', 'rest_send_cors_headers' );
    add_filter( 'rest_pre_serve_request', function( $value ) {
        header( 'Access-Control-Allow-Origin: *' );
        header( 'Access-Control-Allow-Methods: GET, POST, OPTIONS' );
        header( 'Access-Control-Allow-Headers: Authorization, Content-Type, X-Requested-With' );
        return $value;
    });
}, 15 );

// Disable entry titles on front page and about-contact page for seamless custom layout
add_filter( 'astra_the_title_enabled', function( $enabled ) {
    if ( is_front_page() || is_page( 'about-contact' ) || is_page( 'home' ) ) {
        return false;
    }
    return $enabled;
});

// Set full width layout for custom pages
add_filter( 'astra_page_layout', function( $layout ) {
    if ( is_front_page() || is_page( 'about-contact' ) || is_page( 'home' ) ) {
        return 'no-sidebar';
    }
    return $layout;
});

// Inject global HTML (Scroll progress bar) into header
add_action( 'wp_body_open', function() {
    echo '<div id="r-scroll-progress"></div>';
});

// Enqueue Google Fonts and Custom Modern Design System
add_action( 'wp_enqueue_scripts', function() {
    wp_enqueue_style( 'rise-google-fonts', 'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@500;600;700;800&display=swap', array(), null );
    
    // Custom Interactive Consulting CSS
    $custom_css = '
    :root {
        --r-bg-dark: #090d16;
        --r-bg-surface: #0f172a;
        --r-bg-card: rgba(15, 23, 42, 0.75);
        --r-primary: #2563eb;
        --r-primary-hover: #1d4ed8;
        --r-primary-glow: rgba(37, 99, 235, 0.4);
        --r-accent: #06b6d4;
        --r-emerald: #10b981;
        --r-text: #f8fafc;
        --r-text-dim: #94a3b8;
        --r-border: rgba(255, 255, 255, 0.08);
        --r-border-hover: rgba(56, 189, 248, 0.45);
        --r-radius: 16px;
    }

    html {
        scroll-behavior: smooth;
    }

    body {
        font-family: "Inter", -apple-system, BlinkMacSystemFont, sans-serif !important;
        background-color: var(--r-bg-dark) !important;
        color: var(--r-text) !important;
        line-height: 1.6;
        -webkit-font-smoothing: antialiased;
        overflow-x: hidden;
    }

    /* Fixed Scroll Progress Bar */
    #r-scroll-progress {
        position: fixed;
        top: 0;
        left: 0;
        height: 3px;
        background: linear-gradient(90deg, #2563eb, #38bdf8, #10b981);
        width: 0%;
        z-index: 999999;
        transition: width 0.05s ease-out;
    }

    /* Modern Dark Header for Astra */
    .ast-primary-header-bar, .main-header-bar, .ast-theme-transparent-header #masthead {
        background-color: rgba(8, 12, 20, 0.92) !important;
        backdrop-filter: blur(12px) !important;
        border-bottom: 1px solid var(--r-border) !important;
        position: sticky !important;
        top: 0 !important;
        z-index: 1000 !important;
    }
    .ast-primary-header-bar a, .main-header-menu a, .site-title a {
        color: #f1f5f9 !important;
        font-family: "Outfit", sans-serif !important;
        font-weight: 600;
        transition: color 0.2s ease;
    }
    .main-header-menu a:hover, .main-header-menu .current-menu-item > a {
        color: #38bdf8 !important;
    }

    /* Container Full Width Stretch */
    .site-content .ast-container {
        max-width: 100% !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
    }
    .ast-plain-container.ast-no-sidebar #primary {
        margin: 0 !important;
        padding: 0 !important;
    }
    .entry-content {
        margin: 0 !important;
    }

    /* Ambient Floating Glow Orb */
    .r-glow-orb {
        position: absolute;
        width: 600px;
        height: 600px;
        background: radial-gradient(circle, rgba(37, 99, 235, 0.22) 0%, rgba(6, 182, 212, 0.04) 50%, transparent 70%);
        filter: blur(80px);
        border-radius: 50%;
        pointer-events: none;
        z-index: 0;
        animation: orbFloat 14s ease-in-out infinite alternate;
    }
    @keyframes orbFloat {
        0% { transform: translate(-40px, -20px) scale(0.95); }
        100% { transform: translate(50px, 40px) scale(1.1); }
    }

    /* Rise Consulting Structure */
    .r-section {
        padding: 100px 24px;
        position: relative;
        overflow: hidden;
    }
    .r-container {
        max-width: 1200px;
        margin: 0 auto;
        width: 100%;
        position: relative;
        z-index: 1;
    }
    .r-tag {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 7px 18px;
        background: rgba(37, 99, 235, 0.12);
        border: 1px solid rgba(56, 189, 248, 0.3);
        border-radius: 9999px;
        color: #38bdf8;
        font-size: 0.82rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 24px;
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.15);
    }
    .r-tag-dot {
        width: 8px;
        height: 8px;
        background: #38bdf8;
        border-radius: 50%;
        position: relative;
    }
    .r-tag-dot::after {
        content: "";
        position: absolute;
        inset: -4px;
        border-radius: 50%;
        border: 1px solid #38bdf8;
        animation: pulseRing 2s cubic-bezier(0.215, 0.61, 0.355, 1) infinite;
    }
    @keyframes pulseRing {
        0% { transform: scale(0.5); opacity: 1; }
        100% { transform: scale(2.2); opacity: 0; }
    }

    .r-heading-xl {
        font-family: "Outfit", sans-serif;
        font-size: clamp(2.5rem, 5.5vw, 4.4rem);
        font-weight: 800;
        line-height: 1.12;
        letter-spacing: -0.02em;
        color: #ffffff;
        margin-bottom: 24px;
    }
    .r-heading-lg {
        font-family: "Outfit", sans-serif;
        font-size: clamp(2.1rem, 3.8vw, 3.2rem);
        font-weight: 700;
        line-height: 1.18;
        letter-spacing: -0.01em;
        color: #ffffff;
        margin-bottom: 20px;
    }
    .r-gradient-text {
        background: linear-gradient(135deg, #60a5fa 0%, #38bdf8 45%, #c084fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-size: 200% auto;
        animation: textShimmer 6s linear infinite;
    }
    @keyframes textShimmer {
        0% { background-position: 0% center; }
        100% { background-position: 200% center; }
    }

    .r-lead {
        font-size: 1.2rem;
        color: var(--r-text-dim);
        max-width: 700px;
        margin-bottom: 38px;
        font-weight: 400;
        line-height: 1.75;
    }

    /* Interactive Buttons with Shimmer Sweep */
    .r-btn-group {
        display: flex;
        flex-wrap: wrap;
        gap: 16px;
        align-items: center;
        margin-bottom: 50px;
    }
    .r-btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        padding: 15px 32px;
        border-radius: 12px;
        font-family: "Outfit", sans-serif;
        font-weight: 600;
        font-size: 1.02rem;
        text-decoration: none !important;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }
    .r-btn-primary {
        background: linear-gradient(135deg, #2563eb, #1d4ed8);
        color: #ffffff !important;
        box-shadow: 0 4px 25px var(--r-primary-glow);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    .r-btn-primary::after {
        content: "";
        position: absolute;
        top: -50%;
        left: -80%;
        width: 50%;
        height: 200%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.35), transparent);
        transform: rotate(25deg);
        transition: none;
    }
    .r-btn-primary:hover::after {
        left: 140%;
        transition: left 0.8s ease-in-out;
    }
    .r-btn-primary:hover {
        background: linear-gradient(135deg, #1d4ed8, #1e40af);
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 10px 30px rgba(37, 99, 235, 0.55);
    }
    .r-btn-secondary {
        background: rgba(255, 255, 255, 0.05);
        color: #ffffff !important;
        border: 1px solid var(--r-border);
        backdrop-filter: blur(8px);
    }
    .r-btn-secondary:hover {
        background: rgba(255, 255, 255, 0.12);
        border-color: rgba(56, 189, 248, 0.5);
        transform: translateY(-3px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
    }

    /* Interactive Stats Grid */
    .r-stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 24px;
        margin-top: 40px;
    }
    .r-stat-card {
        background: rgba(15, 23, 42, 0.65);
        border: 1px solid var(--r-border);
        border-radius: var(--r-radius);
        padding: 30px 24px;
        backdrop-filter: blur(14px);
        transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
        position: relative;
    }
    .r-stat-card:hover {
        border-color: #38bdf8;
        transform: translateY(-6px);
        box-shadow: 0 16px 36px -10px rgba(37, 99, 235, 0.35);
    }
    .r-stat-num {
        font-family: "Outfit", sans-serif;
        font-size: 3rem;
        font-weight: 800;
        color: #ffffff;
        line-height: 1;
        margin-bottom: 8px;
        background: linear-gradient(135deg, #ffffff 30%, #94a3b8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .r-stat-label {
        font-size: 0.94rem;
        color: var(--r-text-dim);
        font-weight: 500;
    }

    /* Cards & Grids */
    .r-grid-3 {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 28px;
    }
    .r-grid-2 {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
        gap: 36px;
    }
    .r-grid-4 {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
        gap: 24px;
    }

    /* Interactive Tilt & Hover Lift Card */
    .r-card {
        background: var(--r-bg-card);
        border: 1px solid var(--r-border);
        border-radius: var(--r-radius);
        padding: 38px 32px;
        backdrop-filter: blur(12px);
        transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
        display: flex;
        flex-direction: column;
        position: relative;
    }
    .r-card:hover {
        border-color: var(--r-border-hover);
        transform: translateY(-8px);
        box-shadow: 0 20px 45px -10px rgba(0, 0, 0, 0.5), 0 0 25px rgba(56, 189, 248, 0.15);
    }
    .r-card-icon {
        width: 58px;
        height: 58px;
        border-radius: 14px;
        background: rgba(37, 99, 235, 0.15);
        border: 1px solid rgba(56, 189, 248, 0.3);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.6rem;
        margin-bottom: 24px;
        color: #38bdf8;
        transition: transform 0.3s ease, background 0.3s ease;
    }
    .r-card:hover .r-card-icon {
        transform: scale(1.12) rotate(4deg);
        background: rgba(37, 99, 235, 0.3);
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.3);
    }
    .r-card-title {
        font-family: "Outfit", sans-serif;
        font-size: 1.48rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 14px;
    }
    .r-card-desc {
        color: var(--r-text-dim);
        font-size: 0.98rem;
        line-height: 1.68;
        margin-bottom: 22px;
        flex-grow: 1;
    }
    .r-card-features {
        list-style: none;
        padding: 0;
        margin: 0;
        border-top: 1px solid var(--r-border);
        padding-top: 20px;
    }
    .r-card-features li {
        font-size: 0.92rem;
        color: #cbd5e1;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 10px;
        transition: transform 0.2s ease;
    }
    .r-card:hover .r-card-features li {
        transform: translateX(4px);
    }
    .r-check {
        color: var(--r-emerald);
        font-weight: bold;
    }

    /* Filter Tabs for Services */
    .r-filter-bar {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        margin-bottom: 40px;
        justify-content: center;
    }
    .r-filter-btn {
        padding: 10px 22px;
        border-radius: 999px;
        background: rgba(15, 23, 42, 0.85);
        border: 1px solid var(--r-border);
        color: #94a3b8;
        font-family: "Outfit", sans-serif;
        font-size: 0.92rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.25s ease;
    }
    .r-filter-btn:hover, .r-filter-btn.active {
        background: rgba(37, 99, 235, 0.25);
        border-color: #38bdf8;
        color: #ffffff;
        box-shadow: 0 0 16px rgba(56, 189, 248, 0.25);
        transform: translateY(-2px);
    }

    /* Interactive ROI Calculator Widget */
    .r-calc-container {
        background: linear-gradient(145deg, rgba(15, 23, 42, 0.95), rgba(10, 15, 29, 0.9));
        border: 1px solid rgba(56, 189, 248, 0.35);
        border-radius: 24px;
        padding: 48px;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
        backdrop-filter: blur(16px);
        margin-top: 30px;
    }
    .r-slider {
        -webkit-appearance: none;
        width: 100%;
        height: 10px;
        border-radius: 5px;
        background: #1e293b;
        outline: none;
        margin: 14px 0 26px 0;
        cursor: pointer;
    }
    .r-slider::-webkit-slider-thumb {
        -webkit-appearance: none;
        width: 26px;
        height: 26px;
        border-radius: 50%;
        background: #38bdf8;
        cursor: pointer;
        box-shadow: 0 0 15px #38bdf8;
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    .r-slider::-webkit-slider-thumb:hover {
        transform: scale(1.25);
        box-shadow: 0 0 25px #38bdf8;
    }
    .r-calc-output-card {
        background: rgba(2, 6, 23, 0.75);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 14px;
        padding: 24px;
        text-align: center;
        transition: border-color 0.3s ease;
    }
    .r-calc-output-card:hover {
        border-color: #38bdf8;
    }

    /* Interactive FAQ Accordion */
    .r-faq-list {
        max-width: 840px;
        margin: 0 auto;
    }
    .r-faq-item {
        background: var(--r-bg-card);
        border: 1px solid var(--r-border);
        border-radius: 14px;
        margin-bottom: 16px;
        overflow: hidden;
        transition: all 0.3s ease;
    }
    .r-faq-item:hover {
        border-color: var(--r-border-hover);
    }
    .r-faq-header {
        padding: 22px 26px;
        cursor: pointer;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-family: "Outfit", sans-serif;
        font-weight: 700;
        font-size: 1.15rem;
        color: #ffffff;
        user-select: none;
        transition: color 0.2s ease;
    }
    .r-faq-header:hover {
        color: #38bdf8;
    }
    .r-faq-icon {
        font-size: 1.3rem;
        transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
        color: #38bdf8;
    }
    .r-faq-item.open .r-faq-icon {
        transform: rotate(45deg);
    }
    .r-faq-body {
        max-height: 0;
        overflow: hidden;
        transition: max-height 0.4s cubic-bezier(0.16, 1, 0.3, 1), padding 0.3s ease;
        padding: 0 26px;
        color: var(--r-text-dim);
        font-size: 0.98rem;
        line-height: 1.7;
    }
    .r-faq-item.open .r-faq-body {
        max-height: 350px;
        padding-bottom: 24px;
    }

    /* Interactive Testimonial Cards */
    .r-quote-card {
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid var(--r-border);
        border-radius: var(--r-radius);
        padding: 36px 32px;
        position: relative;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .r-quote-card:hover {
        transform: translateY(-6px);
        border-color: rgba(56, 189, 248, 0.5);
        box-shadow: 0 16px 36px rgba(0, 0, 0, 0.4);
    }
    .r-stars {
        color: #f59e0b;
        font-size: 1.15rem;
        margin-bottom: 16px;
        letter-spacing: 2px;
    }
    .r-quote-text {
        font-size: 1.05rem;
        font-style: italic;
        color: #e2e8f0;
        line-height: 1.7;
        margin-bottom: 24px;
    }
    .r-client-info {
        display: flex;
        align-items: center;
        gap: 14px;
    }
    .r-avatar {
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: linear-gradient(135deg, #2563eb, #7c3aed);
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        color: #ffffff;
        font-size: 1.1rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    }
    .r-client-name {
        font-family: "Outfit", sans-serif;
        font-weight: 700;
        color: #ffffff;
        font-size: 1rem;
    }
    .r-client-role {
        font-size: 0.85rem;
        color: var(--r-text-dim);
    }

    /* Team Member Card */
    .r-team-card {
        background: var(--r-bg-card);
        border: 1px solid var(--r-border);
        border-radius: var(--r-radius);
        overflow: hidden;
        transition: transform 0.35s ease, border-color 0.35s ease;
    }
    .r-team-card:hover {
        transform: translateY(-8px);
        border-color: var(--r-border-hover);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.45);
    }
    .r-team-header {
        height: 140px;
        background: linear-gradient(135deg, #1e293b, #0f172a);
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .r-team-avatar-lg {
        width: 82px;
        height: 82px;
        border-radius: 50%;
        background: linear-gradient(135deg, #2563eb, #38bdf8);
        border: 3px solid #0f172a;
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: "Outfit", sans-serif;
        font-size: 1.65rem;
        font-weight: 800;
        color: #ffffff;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
        transition: transform 0.3s ease;
    }
    .r-team-card:hover .r-team-avatar-lg {
        transform: scale(1.1);
    }
    .r-team-body {
        padding: 26px;
        text-align: center;
    }
    .r-team-name {
        font-family: "Outfit", sans-serif;
        font-size: 1.28rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 4px;
    }
    .r-team-role {
        color: #38bdf8;
        font-size: 0.88rem;
        font-weight: 600;
        margin-bottom: 14px;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .r-team-bio {
        color: var(--r-text-dim);
        font-size: 0.92rem;
        line-height: 1.62;
    }

    /* Contact Box & Form Inputs */
    .r-contact-card {
        background: linear-gradient(180deg, rgba(15, 23, 42, 0.9) 0%, rgba(10, 15, 29, 0.95) 100%);
        border: 1px solid var(--r-border);
        border-radius: 20px;
        padding: 44px;
        box-shadow: 0 20px 45px rgba(0, 0, 0, 0.4);
    }
    .r-form-group {
        margin-bottom: 20px;
    }
    .r-form-group label {
        display: block;
        font-family: "Outfit", sans-serif;
        font-size: 0.92rem;
        font-weight: 600;
        color: #e2e8f0;
        margin-bottom: 8px;
    }
    .r-input, .r-textarea, .r-select {
        width: 100%;
        padding: 14px 16px;
        background: rgba(10, 15, 29, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 10px;
        color: #ffffff;
        font-family: "Inter", sans-serif;
        font-size: 0.98rem;
        transition: border-color 0.25s ease, box-shadow 0.25s ease, background 0.25s ease;
    }
    .r-input:focus, .r-textarea:focus, .r-select:focus {
        outline: none;
        border-color: #38bdf8;
        background: rgba(15, 23, 42, 0.95);
        box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.25);
    }
    .r-textarea {
        resize: vertical;
        min-height: 120px;
    }

    /* Footer styling */
    .site-footer, .ast-footer-copyright {
        background: #060911 !important;
        border-top: 1px solid var(--r-border) !important;
        color: var(--r-text-dim) !important;
        text-align: center;
        padding: 30px 20px !important;
        font-size: 0.9rem;
    }
    .site-footer a {
        color: #94a3b8 !important;
    }
    .site-footer a:hover {
        color: #ffffff !important;
    }

    /* CTA Banner */
    .r-cta-banner {
        background: radial-gradient(circle at 50% 0%, rgba(37, 99, 235, 0.22) 0%, transparent 70%), #0f172a;
        border: 1px solid rgba(56, 189, 248, 0.35);
        border-radius: 24px;
        padding: 64px 40px;
        text-align: center;
        position: relative;
        overflow: hidden;
        box-shadow: 0 20px 45px rgba(0, 0, 0, 0.5);
    }
    ';

    wp_add_inline_style( 'rise-google-fonts', $custom_css );

    // Inject small inline script for scroll progress
    $scroll_js = '
    document.addEventListener("DOMContentLoaded", function() {
        var prog = document.getElementById("r-scroll-progress");
        if (prog) {
            window.addEventListener("scroll", function() {
                var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
                var docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
                var pct = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
                prog.style.width = pct + "%";
            });
        }
    });
    ';
    wp_add_inline_script( 'rise-google-fonts', $scroll_js );
});
