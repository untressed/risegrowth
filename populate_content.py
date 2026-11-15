#!/usr/bin/env python3
"""
Populate Rise Growth Group WordPress CPTs via WP-CLI.
Run: python populate_content.py
"""
import subprocess, json, sys, os

WP = os.path.join(os.path.dirname(__file__), 'wp.bat')
WP_PATH = os.path.join(os.path.dirname(__file__), 'wordpress')

def wp(*args):
    cmd = [WP, '--path=' + WP_PATH, '--allow-root'] + list(args)
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    if result.returncode != 0:
        print(f"  ⚠  WP-CLI warning: {result.stderr.strip()[:120]}")
    return result.stdout.strip()

def create_post(post_type, title, content, excerpt='', meta=None):
    post_id = wp('post', 'create',
        f'--post_type={post_type}',
        f'--post_title={title}',
        f'--post_content={content}',
        f'--post_excerpt={excerpt}',
        '--post_status=publish',
        '--porcelain'
    )
    if meta and post_id.isdigit():
        for key, val in meta.items():
            wp('post', 'meta', 'update', post_id, key, val)
    print(f"  \u2713 Created [{post_type}] id={post_id}  '{title}'")
    return post_id

print("\n=== Rise Growth: Populating WordPress Content ===\n")

# ── Delete existing CPT posts (fresh seed) ─────────────────────────
for pt in ['rise_service', 'rise_team', 'rise_testimonial', 'rise_faq']:
    ids = wp('post', 'list', f'--post_type={pt}', '--format=ids')
    if ids:
        for pid in ids.split():
            wp('post', 'delete', pid, '--force')
        print(f"  🗑  Cleared old {pt} posts")

print()

# ─────────────────────────────────────────────────────────────────────
# SERVICES
# ─────────────────────────────────────────────────────────────────────
print("▶ Creating Services...")

SERVICES = [
    {
        'title': 'Executive Strategy & Board Advisory',
        'content': 'Guiding CEOs and boards through pivotal corporate milestones, competitive repositioning, and strategic capital allocation.',
        'excerpt': 'strategy',
        'meta': {
            'rise_icon': '🏛️',
            'rise_color': 'rgba(37,99,235,0.15)',
            'rise_border_color': 'rgba(59,130,246,0.3)',
            'rise_filter_id': 'strategy',
            'rise_features': json.dumps([
                'Corporate positioning & market defense',
                'Board governance & investor communication',
                'M&A target evaluation & integration',
                'Strategic turnaround roadmaps'
            ])
        }
    },
    {
        'title': 'Revenue Architecture & Go-To-Market',
        'content': 'Building resilient, predictable revenue engines that dramatically increase sales velocity, win rates, and LTV.',
        'excerpt': 'gtm',
        'meta': {
            'rise_icon': '🚀',
            'rise_color': 'rgba(16,185,129,0.12)',
            'rise_border_color': 'rgba(52,211,153,0.3)',
            'rise_filter_id': 'gtm',
            'rise_features': json.dumps([
                'Enterprise sales org design & quotas',
                'Value-based pricing model overhaul',
                'Account-Based Marketing pipeline',
                'Sales enablement & pitch playbooks'
            ])
        }
    },
    {
        'title': 'Operational Excellence & Scale',
        'content': 'Streamlining workflows, reducing operational drag, and installing rhythms that support 10x headcount expansion.',
        'excerpt': 'ops',
        'meta': {
            'rise_icon': '⚙️',
            'rise_color': 'rgba(139,92,246,0.12)',
            'rise_border_color': 'rgba(167,139,250,0.3)',
            'rise_filter_id': 'ops',
            'rise_features': json.dumps([
                'Executive OKR orchestration & dashboards',
                'End-to-end automated workflow integration',
                'Cost discipline & efficiency programs',
                'Senior executive recruiting & mapping'
            ])
        }
    },
    {
        'title': 'Digital & AI Transformation',
        'content': 'Deploying AI and modern data infrastructure to automate processes, forecast demand, and protect competitive moats.',
        'excerpt': 'ai',
        'meta': {
            'rise_icon': '🤖',
            'rise_color': 'rgba(251,191,36,0.1)',
            'rise_border_color': 'rgba(251,191,36,0.25)',
            'rise_filter_id': 'ai',
            'rise_features': json.dumps([
                'Enterprise LLM & AI workflow deployment',
                'Executive decision intelligence dashboards',
                'Cloud migration & legacy modernisation',
                'Data security & compliance protocols'
            ])
        }
    },
]

for s in SERVICES:
    create_post('rise_service', s['title'], s['content'], s['excerpt'], s['meta'])

# ─────────────────────────────────────────────────────────────────────
# TEAM
# ─────────────────────────────────────────────────────────────────────
print("\n▶ Creating Team Members...")

TEAM = [
    { 'name': 'David Vance',   'role': 'Managing Principal',     'initials': 'DV', 'bg': 'linear-gradient(135deg,#2563eb,#38bdf8)', 'bio': 'Former Tier-1 strategy partner. 18+ years advising Fortune 500 boards and scaling high-velocity tech firms through public listings.' },
    { 'name': 'Sarah Jenkins', 'role': 'Head of Go-to-Market',   'initials': 'SJ', 'bg': 'linear-gradient(135deg,#8b5cf6,#ec4899)', 'bio': 'Architect of three unicorn revenue expansions. Specialist in complex B2B sales cycles, outbound motions, and pricing power.' },
    { 'name': 'Arjun Mehta',   'role': 'Partner, AI & Tech',     'initials': 'AM', 'bg': 'linear-gradient(135deg,#059669,#10b981)', 'bio': 'Former VP Engineering turned transformation advisor. Specializes in AI deployment, automated data infrastructure, and tech org design.' },
    { 'name': 'Claire Dubois', 'role': 'Principal, Org Design',  'initials': 'CD', 'bg': 'linear-gradient(135deg,#f59e0b,#ef4444)', 'bio': 'Executive leadership coach and people strategist. Expert in scaling leadership teams, founder transitions, and performance culture.' },
]

for m in TEAM:
    create_post('rise_team', m['name'], m['bio'], '', {
        'rise_role': m['role'],
        'rise_initials': m['initials'],
        'rise_bg_gradient': m['bg'],
    })

# ─────────────────────────────────────────────────────────────────────
# TESTIMONIALS
# ─────────────────────────────────────────────────────────────────────
print("\n▶ Creating Testimonials...")

TESTIMONIALS = [
    { 'name': 'Marcus Vance',   'role': 'Founder & CEO, Nexus Cloud',         'initials': 'MV', 'bg': 'linear-gradient(135deg,#2563eb,#7c3aed)', 'quote': 'Rise Growth overhauled our entire enterprise sales motion. Within 12 months, ARR expanded from $8M to $23M with 38% gross margin improvement. Their partners are in a league of their own.' },
    { 'name': 'Elena Rostova',  'role': 'Managing Partner, Vanguard Capital',  'initials': 'ER', 'bg': 'linear-gradient(135deg,#059669,#10b981)', 'quote': "Their operational precision is extraordinary. They didn't just advise — they sat in the trenches with our leadership until KPIs were hit. Highest confidence we've had in any advisory team." },
    { 'name': 'David Chen',     'role': 'Chief Operating Officer, Horizon Tech','initials': 'DC', 'bg': 'linear-gradient(135deg,#d97706,#f59e0b)', 'quote': 'Working with Rise Growth was the highest-ROI investment of our post-Series B journey. They reshaped our customer acquisition economics and positioned us for a successful $120M acquisition.' },
]

for t in TESTIMONIALS:
    create_post('rise_testimonial', t['name'], t['quote'], '', {
        'rise_role': t['role'],
        'rise_initials': t['initials'],
        'rise_bg_gradient': t['bg'],
        'rise_rating': '5',
    })

# ─────────────────────────────────────────────────────────────────────
# FAQS
# ─────────────────────────────────────────────────────────────────────
print("\n▶ Creating FAQs...")

FAQS = [
    { 'q': 'How does a Rise Growth engagement work?',       'a': 'We operate as an embedded advisory team. After a 14-day rapid Diagnostic audit, we co-create a 12-month growth blueprint, then embed senior partners directly alongside your executive committee to execute sprints, restructure operations, and optimise your revenue funnel.' },
    { 'q': 'What stage companies do you partner with?',      'a': 'Post-Series A through Pre-IPO scaleups ($2M–$100M+ ARR) seeking to accelerate revenue, reach operational profitability, or prepare for institutional capital raises and M&A exits.' },
    { 'q': 'How soon can we expect measurable ROI?',         'a': 'Our diagnostic surfaces immediate revenue leakage within 14 days. Most clients see pipeline acceleration and gross margin improvements within 60–90 days of active implementation.' },
    { 'q': 'What is your fee structure?',                    'a': 'Bespoke retainer models tailored to client scale, with performance-linked incentive alignments for qualified engagements. Discussed transparently in the first discovery session.' },
    { 'q': 'Do you work internationally?',                   'a': 'Yes. Our partners are distributed across North America, Europe, and APAC. We serve clients globally and embed both virtually and on-site based on engagement scope.' },
]

for faq in FAQS:
    create_post('rise_faq', faq['q'], faq['a'])

# ─────────────────────────────────────────────────────────────────────
print("\n✅ All content seeded to WordPress!\n")
print("REST API endpoints now available:")
print("  http://localhost:8080/?rest_route=/wp/v2/services")
print("  http://localhost:8080/?rest_route=/wp/v2/team")
print("  http://localhost:8080/?rest_route=/wp/v2/testimonials")
print("  http://localhost:8080/?rest_route=/wp/v2/faqs\n")
