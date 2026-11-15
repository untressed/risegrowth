import React, { useState, useEffect, useRef, useCallback } from 'react';

const WP_BASE = 'http://localhost:8080/?rest_route=/wp/v2';

/* ─── API helpers ────────────────────────────────────── */
const fetchCPT = (slug, params = '_fields=id,title,content,excerpt,meta&per_page=20') =>
  fetch(`${WP_BASE}/${slug}&${params}`)
    .then(r => { if (!r.ok) throw new Error(r.status); return r.json(); });

/* ─── Skeleton placeholder ──────────────────────────── */
function Skeleton({ h = 20, w = '100%', r = 8, mb = 0 }) {
  return (
    <div style={{
      height: h, width: w, borderRadius: r, marginBottom: mb,
      background: 'linear-gradient(90deg, #0f172a 25%, #1e293b 50%, #0f172a 75%)',
      backgroundSize: '200% 100%',
      animation: 'shimmer 1.4s infinite linear',
    }} />
  );
}

/* ─── Fallback static data (shown if WP offline) ────── */
const FALLBACK = {
  services: [
    { id: 1, title: { rendered: 'Executive Strategy & Board Advisory' }, content: { rendered: '<p>Guiding CEOs and boards through pivotal corporate milestones, competitive repositioning, and strategic capital allocation.</p>' },
      meta: { rise_icon: '🏛️', rise_color: 'rgba(37,99,235,0.15)', rise_border_color: 'rgba(59,130,246,0.3)', rise_filter_id: 'strategy', rise_features: JSON.stringify(['Corporate positioning & market defense','Board governance & investor communication','M&A target evaluation & integration','Strategic turnaround roadmaps']) }},
    { id: 2, title: { rendered: 'Revenue Architecture & Go-To-Market' }, content: { rendered: '<p>Building resilient, predictable revenue engines that dramatically increase sales velocity, win rates, and LTV.</p>' },
      meta: { rise_icon: '🚀', rise_color: 'rgba(16,185,129,0.12)', rise_border_color: 'rgba(52,211,153,0.3)', rise_filter_id: 'gtm', rise_features: JSON.stringify(['Enterprise sales org design & quotas','Value-based pricing model overhaul','Account-Based Marketing pipeline','Sales enablement & pitch playbooks']) }},
    { id: 3, title: { rendered: 'Operational Excellence & Scale' }, content: { rendered: '<p>Streamlining workflows, reducing operational drag, and installing rhythms that support 10x headcount expansion.</p>' },
      meta: { rise_icon: '⚙️', rise_color: 'rgba(139,92,246,0.12)', rise_border_color: 'rgba(167,139,250,0.3)', rise_filter_id: 'ops', rise_features: JSON.stringify(['Executive OKR orchestration & dashboards','End-to-end automated workflow integration','Cost discipline & efficiency programs','Senior executive recruiting & mapping']) }},
    { id: 4, title: { rendered: 'Digital & AI Transformation' }, content: { rendered: '<p>Deploying AI and modern data infrastructure to automate processes, forecast demand, and protect competitive moats.</p>' },
      meta: { rise_icon: '🤖', rise_color: 'rgba(251,191,36,0.1)', rise_border_color: 'rgba(251,191,36,0.25)', rise_filter_id: 'ai', rise_features: JSON.stringify(['Enterprise LLM & AI workflow deployment','Executive decision intelligence dashboards','Cloud migration & legacy modernisation','Data security & compliance protocols']) }},
  ],
  team: [
    { id: 1, title: { rendered: 'David Vance' }, content: { rendered: '<p>Former Tier-1 strategy partner. 18+ years advising Fortune 500 boards and scaling high-velocity tech firms through public listings.</p>' }, meta: { rise_role: 'Managing Principal', rise_initials: 'DV', rise_bg_gradient: 'linear-gradient(135deg,#2563eb,#38bdf8)' }},
    { id: 2, title: { rendered: 'Sarah Jenkins' }, content: { rendered: '<p>Architect of three unicorn revenue expansions. Specialist in complex B2B sales cycles, outbound motions, and pricing power.</p>' }, meta: { rise_role: 'Head of Go-to-Market', rise_initials: 'SJ', rise_bg_gradient: 'linear-gradient(135deg,#8b5cf6,#ec4899)' }},
    { id: 3, title: { rendered: 'Arjun Mehta' }, content: { rendered: '<p>Former VP Engineering turned transformation advisor. Specializes in AI deployment, automated data infrastructure, and tech org design.</p>' }, meta: { rise_role: 'Partner, AI & Tech', rise_initials: 'AM', rise_bg_gradient: 'linear-gradient(135deg,#059669,#10b981)' }},
    { id: 4, title: { rendered: 'Claire Dubois' }, content: { rendered: '<p>Executive leadership coach and people strategist. Expert in scaling leadership teams, founder transitions, and performance culture.</p>' }, meta: { rise_role: 'Principal, Org Design', rise_initials: 'CD', rise_bg_gradient: 'linear-gradient(135deg,#f59e0b,#ef4444)' }},
  ],
  testimonials: [
    { id: 1, title: { rendered: 'Marcus Vance' }, content: { rendered: '<p>Rise Growth overhauled our entire enterprise sales motion. Within 12 months, ARR expanded from $8M to $23M with 38% gross margin improvement. Their partners are in a league of their own.</p>' }, meta: { rise_role: 'Founder & CEO, Nexus Cloud', rise_initials: 'MV', rise_bg_gradient: 'linear-gradient(135deg,#2563eb,#7c3aed)', rise_rating: '5' }},
    { id: 2, title: { rendered: 'Elena Rostova' }, content: { rendered: "<p>Their operational precision is extraordinary. They didn't just advise — they sat in the trenches with our leadership until KPIs were hit.</p>" }, meta: { rise_role: 'Managing Partner, Vanguard Capital', rise_initials: 'ER', rise_bg_gradient: 'linear-gradient(135deg,#059669,#10b981)', rise_rating: '5' }},
    { id: 3, title: { rendered: 'David Chen' }, content: { rendered: '<p>Working with Rise Growth was the highest-ROI investment of our post-Series B journey. They positioned us for a successful $120M acquisition.</p>' }, meta: { rise_role: 'COO, Horizon Tech', rise_initials: 'DC', rise_bg_gradient: 'linear-gradient(135deg,#d97706,#f59e0b)', rise_rating: '5' }},
  ],
  faqs: [
    { id: 1, title: { rendered: 'How does a Rise Growth engagement work?' }, content: { rendered: '<p>We operate as an embedded advisory team. After a 14-day rapid Diagnostic audit, we co-create a 12-month growth blueprint, then embed senior partners alongside your executive committee to execute sprints and optimise your revenue funnel.</p>' }},
    { id: 2, title: { rendered: 'What stage companies do you partner with?' }, content: { rendered: '<p>Post-Series A through Pre-IPO scaleups ($2M–$100M+ ARR) seeking to accelerate revenue, reach operational profitability, or prepare for institutional capital raises and M&A exits.</p>' }},
    { id: 3, title: { rendered: 'How soon can we expect measurable ROI?' }, content: { rendered: '<p>Our diagnostic surfaces immediate revenue leakage within 14 days. Most clients see pipeline acceleration and gross margin improvements within 60–90 days of active implementation.</p>' }},
    { id: 4, title: { rendered: 'What is your fee structure?' }, content: { rendered: '<p>Bespoke retainer models tailored to client scale, with performance-linked incentive alignments for qualified engagements. Discussed transparently in the first discovery session.</p>' }},
    { id: 5, title: { rendered: 'Do you work internationally?' }, content: { rendered: '<p>Yes. Our partners are distributed across North America, Europe, and APAC. We serve clients globally, embedding both virtually and on-site based on engagement scope.</p>' }},
  ],
};

/* ─── useCMSData hook ────────────────────────────────── */
function useCMSData() {
  const [data, setData] = useState({ services: [], team: [], testimonials: [], faqs: [] });
  const [loading, setLoading] = useState(true);
  const [source, setSource] = useState('loading'); // 'wp' | 'fallback' | 'loading'

  useEffect(() => {
    const endpoints = [
      fetchCPT('services'),
      fetchCPT('team'),
      fetchCPT('testimonials'),
      fetchCPT('faqs'),
    ];

    Promise.allSettled(endpoints).then(([svc, team, test, faq]) => {
      const ok = r => r.status === 'fulfilled' && Array.isArray(r.value) && r.value.length > 0;
      if (ok(svc) || ok(team)) {
        setData({
          services:     ok(svc)  ? svc.value  : FALLBACK.services,
          team:         ok(team) ? team.value : FALLBACK.team,
          testimonials: ok(test) ? test.value : FALLBACK.testimonials,
          faqs:         ok(faq)  ? faq.value  : FALLBACK.faqs,
        });
        setSource('wp');
      } else {
        setData(FALLBACK);
        setSource('fallback');
      }
      setLoading(false);
    });
  }, []);

  return { data, loading, source };
}

/* ─── Strip HTML from WP rendered content ───────────── */
const stripHtml = (html = '') => html.replace(/<[^>]*>/g, '').trim();

/* ─── Hooks ─────────────────────────────────────────── */
function useScrollProgress() {
  const [p, setP] = useState(0);
  useEffect(() => {
    const h = () => {
      const el = document.documentElement;
      setP((el.scrollTop / (el.scrollHeight - el.clientHeight)) * 100);
    };
    window.addEventListener('scroll', h, { passive: true });
    return () => window.removeEventListener('scroll', h);
  }, []);
  return p;
}

function useInView(threshold = 0.15) {
  const ref = useRef(null);
  const [v, setV] = useState(false);
  useEffect(() => {
    const obs = new IntersectionObserver(
      ([e]) => { if (e.isIntersecting) { setV(true); obs.disconnect(); } },
      { threshold }
    );
    if (ref.current) obs.observe(ref.current);
    return () => obs.disconnect();
  }, [threshold]);
  return [ref, v];
}

/* ─── Sub-components ────────────────────────────────── */
function SectionBadge({ children, variant = 'blue' }) {
  const dotColors = { blue: '#22d3ee', green: '#34d399', violet: '#a78bfa' };
  return (
    <div className={`badge badge-${variant}`} style={{ marginBottom: 20 }}>
      <span className="pulse-dot" style={{ background: dotColors[variant], boxShadow: `0 0 8px ${dotColors[variant]}` }} />
      {children}
    </div>
  );
}

function StatCard({ num, label, delay = 0 }) {
  const [ref, visible] = useInView(0.2);
  return (
    <div ref={ref} className="card stat-card card-glow" style={{
      opacity: visible ? 1 : 0, transform: visible ? 'translateY(0)' : 'translateY(20px)',
      transition: `opacity 0.5s ease ${delay}ms, transform 0.5s ease ${delay}ms`
    }}>
      <div className="stat-num gradient-text">{num}</div>
      <div className="stat-label">{label}</div>
    </div>
  );
}

function ServiceCard({ svc, visible, delay }) {
  const cardRef = useRef(null);
  const onMouseMove = useCallback((e) => {
    if (!cardRef.current) return;
    const rect = cardRef.current.getBoundingClientRect();
    cardRef.current.style.setProperty('--mouse-x', `${((e.clientX - rect.left) / rect.width) * 100}%`);
    cardRef.current.style.setProperty('--mouse-y', `${((e.clientY - rect.top) / rect.height) * 100}%`);
  }, []);

  const meta = svc.meta || {};
  const features = (() => { try { return JSON.parse(meta.rise_features || '[]'); } catch { return []; } })();

  return (
    <div ref={cardRef} className="card service-card" onMouseMove={onMouseMove}
      style={{
        opacity: visible ? 1 : 0, transform: visible ? 'translateY(0)' : 'translateY(24px)',
        transition: `opacity 0.5s ease ${delay}ms, transform 0.5s ease ${delay}ms, border-color 0.25s, box-shadow 0.25s`,
      }}>
      <div className="service-icon-wrap" style={{ background: meta.rise_color || 'rgba(37,99,235,0.15)', border: `1px solid ${meta.rise_border_color || 'rgba(59,130,246,0.3)'}` }}>
        {meta.rise_icon || '📌'}
      </div>
      <h3 style={{ fontFamily: 'var(--font-display)', fontSize: '1.3rem', fontWeight: 700, color: '#fff', marginBottom: 12 }}>
        {svc.title?.rendered || ''}
      </h3>
      <p style={{ color: 'var(--text-secondary)', fontSize: '0.93rem', lineHeight: 1.65, marginBottom: 22, flexGrow: 1 }}>
        {stripHtml(svc.content?.rendered)}
      </p>
      {features.length > 0 && (
        <ul style={{ listStyle: 'none', borderTop: '1px solid var(--border-subtle)', paddingTop: 18 }}>
          {features.map((f, i) => (
            <li key={i} style={{ display: 'flex', alignItems: 'flex-start', gap: 10, fontSize: '0.88rem', color: '#cbd5e1', marginBottom: 10 }}>
              <span style={{ color: '#34d399', fontWeight: 700, flexShrink: 0 }}>✓</span> {f}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

function TestimonialCard({ t, delay, visible }) {
  const meta = t.meta || {};
  return (
    <div className="card testimonial-card" style={{
      opacity: visible ? 1 : 0, transform: visible ? 'translateY(0)' : 'translateY(24px)',
      transition: `opacity 0.5s ease ${delay}ms, transform 0.5s ease ${delay}ms`
    }}>
      <div className="testimonial-stars">{'★'.repeat(parseInt(meta.rise_rating || '5'))}</div>
      <p className="testimonial-quote">"{stripHtml(t.content?.rendered)}"</p>
      <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
        <div className="avatar-circle" style={{ background: meta.rise_bg_gradient || '#2563eb', boxShadow: '0 4px 12px rgba(0,0,0,0.3)' }}>
          {meta.rise_initials || '??'}
        </div>
        <div>
          <div style={{ fontFamily: 'var(--font-display)', fontWeight: 700, color: '#fff', fontSize: '0.95rem' }}>{t.title?.rendered}</div>
          <div style={{ color: 'var(--text-secondary)', fontSize: '0.82rem' }}>{meta.rise_role}</div>
        </div>
      </div>
    </div>
  );
}

function FaqItem({ faq, index, open, onToggle }) {
  return (
    <div className={`faq-item card ${open ? 'open' : ''}`} style={{ marginBottom: 12 }}>
      <button className="faq-trigger" onClick={() => onToggle(index)}>
        <span style={{ color: open ? '#93c5fd' : undefined, transition: 'color 0.2s' }}>{faq.title?.rendered}</span>
        <div className="faq-icon">+</div>
      </button>
      <div className="faq-body">{stripHtml(faq.content?.rendered)}</div>
    </div>
  );
}

function CMSBadge({ source }) {
  if (source === 'loading') return null;
  const isWP = source === 'wp';
  return (
    <div style={{
      position: 'fixed', bottom: 20, right: 20, zIndex: 9999,
      padding: '8px 14px', borderRadius: 8,
      background: isWP ? 'rgba(16,185,129,0.12)' : 'rgba(251,191,36,0.1)',
      border: `1px solid ${isWP ? 'rgba(52,211,153,0.35)' : 'rgba(251,191,36,0.3)'}`,
      fontSize: '0.75rem', fontWeight: 700, color: isWP ? '#34d399' : '#fbbf24',
      backdropFilter: 'blur(8px)', display: 'flex', alignItems: 'center', gap: 6
    }}>
      <span style={{ width: 6, height: 6, borderRadius: '50%', background: isWP ? '#34d399' : '#fbbf24', boxShadow: `0 0 6px ${isWP ? '#34d399' : '#fbbf24'}`, display: 'inline-block' }} />
      {isWP ? 'Live WordPress CMS' : 'Static Fallback Mode'}
    </div>
  );
}

const LOGOS = ['▲ NEXUS CAPITAL','◆ VANGUARD SYS','■ HORIZON GLOBAL','✦ ELEVATE FINTECH','● APEX CLOUD','▲ NEXUS CAPITAL','◆ VANGUARD SYS','■ HORIZON GLOBAL','✦ ELEVATE FINTECH','● APEX CLOUD'];

/* ─── Home Page ──────────────────────────────────────── */
function HomePage({ onContact, data, loading }) {
  const [filter, setFilter] = useState('all');
  const [arr, setArr] = useState(10);
  const [growth, setGrowth] = useState(2.5);
  const [openFaq, setOpenFaq] = useState(0);

  const [heroRef, heroVisible] = useInView(0.1);
  const [statsRef, statsVisible] = useInView(0.2);
  const [svcRef, svcVisible] = useInView(0.1);
  const [roiRef, roiVisible] = useInView(0.2);
  const [testRef, testVisible] = useInView(0.1);
  const [faqRef, faqVisible] = useInView(0.1);

  const scaledArr = Math.round(arr * growth);
  const evLift = Math.round(scaledArr * 8 - arr * 8);

  const filteredServices = filter === 'all'
    ? data.services
    : data.services.filter(s => (s.meta?.rise_filter_id || s.excerpt?.rendered || '').includes(filter));

  return (
    <div>
      {/* ── HERO ── */}
      <section className="section" style={{ paddingTop: 120, paddingBottom: 80, position: 'relative', overflow: 'hidden' }}>
        <div className="orb" style={{ top: -100, left: '10%', width: 700, height: 700, background: 'radial-gradient(circle, rgba(37,99,235,0.2) 0%, transparent 65%)', filter: 'blur(80px)', animation: 'floatOrb 18s ease-in-out infinite' }} />
        <div className="orb" style={{ top: 200, right: '-5%', width: 500, height: 500, background: 'radial-gradient(circle, rgba(139,92,246,0.15) 0%, transparent 65%)', filter: 'blur(80px)', animation: 'floatOrb 22s ease-in-out infinite reverse' }} />

        <div className="container" style={{ position: 'relative', zIndex: 1 }}>
          <div ref={heroRef} style={{ maxWidth: 860, margin: '0 auto', textAlign: 'center', opacity: heroVisible ? 1 : 0, transform: heroVisible ? 'none' : 'translateY(30px)', transition: 'all 0.7s ease' }}>
            <SectionBadge>Headless React · WordPress CMS · Strategic Advisory</SectionBadge>
            <h1 className="text-display-xl" style={{ marginBottom: 28 }}>
              Scaling Visionary<br />
              Enterprises Into{' '}
              <span className="gradient-text">Market Leaders</span>
            </h1>
            <p style={{ fontSize: '1.18rem', color: 'var(--text-secondary)', maxWidth: 680, margin: '0 auto 40px', lineHeight: 1.75 }}>
              Rise Growth Group partners with high-growth companies to engineer scalable revenue engines,
              streamline core operations, and achieve multi-million dollar valuation exits.
            </p>
            <div style={{ display: 'flex', gap: 14, justifyContent: 'center', flexWrap: 'wrap', marginBottom: 18 }}>
              <button className="btn btn-primary btn-lg" onClick={onContact}>
                Schedule Strategy Call
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="white" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/></svg>
              </button>
              <button className="btn btn-ghost btn-lg" onClick={() => document.getElementById('services-section')?.scrollIntoView({ behavior: 'smooth' })}>
                Explore Practice Areas
              </button>
            </div>
            <p style={{ fontSize: '0.82rem', color: 'var(--text-muted)' }}>No obligation · 30-minute confidential session</p>
          </div>

          {/* Stats */}
          <div ref={statsRef} className="grid-4" style={{ marginTop: 64, gap: 16 }}>
            {[
              { num: '$450M+', label: 'Client Revenue & Capital Unlocked' },
              { num: '3.4×', label: 'Average 18-Month ROI Multiple' },
              { num: '98%', label: 'Executive Retention Rate' },
              { num: '140+', label: 'Enterprise Engagements Delivered' },
            ].map((s, i) => <StatCard key={i} {...s} delay={i * 80} />)}
          </div>
        </div>

        {/* Marquee */}
        <div style={{ borderTop: '1px solid var(--border-subtle)', borderBottom: '1px solid var(--border-subtle)', marginTop: 72, padding: '28px 0', overflow: 'hidden' }}>
          <div style={{ fontSize: '0.72rem', fontWeight: 700, letterSpacing: '0.12em', color: 'var(--text-muted)', textAlign: 'center', marginBottom: 20, textTransform: 'uppercase' }}>
            Trusted by High-Growth Enterprises Across SaaS, Fintech & Healthcare
          </div>
          <div style={{ overflow: 'hidden' }}>
            <div className="marquee-track">
              {LOGOS.map((logo, i) => (
                <div key={i} style={{ padding: '0 44px', color: '#475569', fontSize: '1.05rem', fontFamily: 'var(--font-display)', fontWeight: 700, whiteSpace: 'nowrap', flexShrink: 0 }}>
                  {logo}
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* ── SERVICES (Live from WP) ── */}
      <section id="services-section" className="section" style={{ background: 'var(--bg-deep)' }}>
        <div className="container">
          <div style={{ textAlign: 'center', maxWidth: 640, margin: '0 auto 48px' }}>
            <SectionBadge>Our Practice Areas</SectionBadge>
            <h2 className="text-display-lg" style={{ marginBottom: 14 }}>Specialized Strategic Advisory</h2>
            <p style={{ color: 'var(--text-secondary)', fontSize: '1.05rem' }}>Filter by your company's immediate transformation priority.</p>
          </div>

          <div style={{ marginBottom: 40 }}>
            <div className="filter-tabs">
              {[{ id: 'all', label: 'All Areas' }, { id: 'strategy', label: 'Strategy' }, { id: 'gtm', label: 'Revenue & GTM' }, { id: 'ops', label: 'Operations' }, { id: 'ai', label: 'AI & Digital' }].map(tab => (
                <button key={tab.id} className={`filter-tab ${filter === tab.id ? 'active' : ''}`} onClick={() => setFilter(tab.id)}>{tab.label}</button>
              ))}
            </div>
          </div>

          <div ref={svcRef} className="grid-2">
            {loading
              ? Array(4).fill(0).map((_, i) => (
                <div key={i} className="card service-card">
                  <Skeleton h={52} w={52} r={12} mb={20} />
                  <Skeleton h={24} w="80%" mb={12} />
                  <Skeleton h={16} mb={6} />
                  <Skeleton h={16} w="90%" mb={6} />
                  <Skeleton h={16} w="70%" />
                </div>
              ))
              : filteredServices.map((svc, i) => <ServiceCard key={svc.id} svc={svc} visible={svcVisible} delay={i * 100} />)
            }
          </div>
        </div>
      </section>

      {/* ── ROI CALCULATOR ── */}
      <section className="section">
        <div className="container">
          <div style={{ textAlign: 'center', maxWidth: 640, margin: '0 auto 40px' }}>
            <SectionBadge variant="green">Interactive Valuation Model</SectionBadge>
            <h2 className="text-display-lg" style={{ marginBottom: 14 }}>Model Your Enterprise Growth</h2>
            <p style={{ color: 'var(--text-secondary)', fontSize: '1.05rem' }}>Drag the sliders to simulate ARR expansion and projected enterprise valuation lift.</p>
          </div>
          <div ref={roiRef} style={{ background: 'rgba(12,17,32,0.9)', border: '1px solid rgba(56,189,248,0.2)', borderRadius: 24, padding: 44, boxShadow: '0 30px 60px -20px rgba(0,0,0,0.6)', backdropFilter: 'blur(16px)', opacity: roiVisible ? 1 : 0, transform: roiVisible ? 'none' : 'translateY(24px)', transition: 'opacity 0.6s ease, transform 0.6s ease' }}>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: 48, alignItems: 'center' }}>
              <div>
                {[
                  { label: 'Current ARR', val: arr, setVal: setArr, min: 2, max: 50, step: 1, unit: '$', suffix: 'M', color: '#2563eb', accent: '#38bdf8' },
                  { label: 'Growth Multiple', val: growth, setVal: setGrowth, min: 1.5, max: 4.0, step: 0.1, unit: '', suffix: '×', color: '#059669', accent: '#10b981' },
                ].map(({ label, val, setVal, min, max, step, unit, suffix, color, accent }) => (
                  <div key={label} style={{ marginBottom: 36 }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 14 }}>
                      <span style={{ fontFamily: 'var(--font-display)', fontWeight: 700, color: '#fff' }}>{label}</span>
                      <span style={{ fontFamily: 'var(--font-display)', fontWeight: 900, color: accent, fontSize: '1.4rem' }}>{unit}{typeof val === 'number' && step < 1 ? val.toFixed(1) : val}{suffix}</span>
                    </div>
                    <input type="range" className="roi-slider" min={min} max={max} step={step} value={val} onChange={e => setVal(+e.target.value)}
                      style={{ background: `linear-gradient(to right, ${color} ${(val - min) / (max - min) * 100}%, rgba(30,41,59,0.8) ${(val - min) / (max - min) * 100}%)` }} />
                  </div>
                ))}
              </div>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: 16 }}>
                <div style={{ padding: '20px 22px', borderRadius: 12, textAlign: 'center', background: 'rgba(7,11,24,0.8)', border: '1px solid var(--border-subtle)' }}>
                  <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', textTransform: 'uppercase', fontWeight: 600, letterSpacing: '0.08em', marginBottom: 6 }}>Target ARR</div>
                  <div style={{ fontFamily: 'var(--font-display)', fontSize: '2rem', fontWeight: 900, color: '#fff' }}>${scaledArr}M</div>
                  <div style={{ fontSize: '0.78rem', color: '#38bdf8', marginTop: 4 }}>+${scaledArr - arr}M lift</div>
                </div>
                <div style={{ padding: '20px 22px', borderRadius: 12, textAlign: 'center', background: 'rgba(37,99,235,0.1)', border: '1px solid rgba(56,189,248,0.3)' }}>
                  <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', textTransform: 'uppercase', fontWeight: 600, letterSpacing: '0.08em', marginBottom: 6 }}>Enterprise Value</div>
                  <div style={{ fontFamily: 'var(--font-display)', fontSize: '2rem', fontWeight: 900, color: '#38bdf8' }}>${Math.round(scaledArr * 8)}M</div>
                  <div style={{ fontSize: '0.78rem', color: '#64748b', marginTop: 4 }}>At 8× ARR multiple</div>
                </div>
                <div style={{ gridColumn: 'span 2', padding: '20px 22px', borderRadius: 12, background: 'rgba(16,185,129,0.07)', border: '1px solid rgba(52,211,153,0.3)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', gap: 16 }}>
                  <div>
                    <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', textTransform: 'uppercase', fontWeight: 600, letterSpacing: '0.08em', marginBottom: 4 }}>Shareholder Value Created</div>
                    <div style={{ fontFamily: 'var(--font-display)', fontSize: '1.7rem', fontWeight: 900, color: '#34d399' }}>+${evLift.toLocaleString()}M</div>
                  </div>
                  <button className="btn btn-primary btn-sm" onClick={onContact} style={{ flexShrink: 0 }}>Get Your Audit →</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ── TESTIMONIALS (Live from WP) ── */}
      <section className="section" style={{ background: 'var(--bg-deep)' }}>
        <div className="container">
          <div style={{ textAlign: 'center', maxWidth: 600, margin: '0 auto 48px' }}>
            <SectionBadge>Client Endorsements</SectionBadge>
            <h2 className="text-display-lg">Words From Our Partners</h2>
          </div>
          <div ref={testRef} className="grid-3">
            {loading
              ? Array(3).fill(0).map((_, i) => (
                <div key={i} className="card" style={{ padding: 32 }}>
                  <Skeleton h={16} w={80} mb={16} />
                  <Skeleton h={14} mb={6} />
                  <Skeleton h={14} w="90%" mb={6} />
                  <Skeleton h={14} w="80%" mb={24} />
                  <div style={{ display: 'flex', gap: 12, alignItems: 'center' }}>
                    <Skeleton h={46} w={46} r={23} />
                    <div style={{ flex: 1 }}><Skeleton h={14} w="60%" mb={6} /><Skeleton h={12} w="80%" /></div>
                  </div>
                </div>
              ))
              : data.testimonials.map((t, i) => <TestimonialCard key={t.id} t={t} delay={i * 100} visible={testVisible} />)
            }
          </div>
        </div>
      </section>

      {/* ── FAQ (Live from WP) ── */}
      <section className="section">
        <div className="container">
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(340px, 1fr))', gap: 60, alignItems: 'start' }}>
            <div style={{ position: 'sticky', top: 100 }}>
              <SectionBadge>Common Questions</SectionBadge>
              <h2 className="text-display-lg" style={{ marginBottom: 20 }}>Everything You Need to Know</h2>
              <p style={{ color: 'var(--text-secondary)', lineHeight: 1.7, marginBottom: 32 }}>Have more questions? Our team responds within 4 business hours.</p>
              <button className="btn btn-ghost" onClick={onContact}>Talk to a Partner →</button>
            </div>
            <div ref={faqRef} style={{ opacity: faqVisible ? 1 : 0, transition: 'opacity 0.5s ease' }}>
              {loading
                ? Array(4).fill(0).map((_, i) => <div key={i} className="card" style={{ padding: '20px 24px', marginBottom: 12 }}><Skeleton h={18} w="80%" /></div>)
                : data.faqs.map((faq, i) => <FaqItem key={faq.id} faq={faq} index={i} open={openFaq === i} onToggle={setOpenFaq} />)
              }
            </div>
          </div>
        </div>
      </section>

      {/* ── CTA ── */}
      <section className="section" style={{ paddingTop: 60 }}>
        <div className="container">
          <div className="cta-banner">
            <SectionBadge>Ready to Scale?</SectionBadge>
            <h2 className="text-display-lg" style={{ maxWidth: 720, margin: '0 auto 20px' }}>
              Break Through Your Next <br /><span className="gradient-text">Growth Ceiling</span>
            </h2>
            <p style={{ color: 'var(--text-secondary)', fontSize: '1.1rem', maxWidth: 560, margin: '0 auto 40px', lineHeight: 1.7 }}>
              Book a confidential 30-minute strategy session with a Managing Partner.
            </p>
            <button className="btn btn-primary btn-lg" onClick={onContact}>
              Book Your Strategy Session
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="white" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/></svg>
            </button>
            <div style={{ marginTop: 20, fontSize: '0.82rem', color: 'var(--text-muted)' }}>Confidential · No commitment · 4-hour response SLA</div>
          </div>
        </div>
      </section>
    </div>
  );
}

/* ─── About Page ─────────────────────────────────────── */
function AboutPage({ onContact, data, loading }) {
  const [formData, setFormData] = useState({ name: '', email: '', stage: '$5M–$20M ARR', message: '' });
  const [submitted, setSubmitted] = useState(false);
  const [submitting, setSubmitting] = useState(false);
  const [teamRef, teamVisible] = useInView(0.1);
  const [formRef, formVisible] = useInView(0.1);

  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmitting(true);
    setTimeout(() => { setSubmitting(false); setSubmitted(true); }, 800);
  };

  return (
    <div>
      {/* About Hero */}
      <section className="section" style={{ paddingTop: 120, paddingBottom: 80, position: 'relative', overflow: 'hidden', textAlign: 'center' }}>
        <div className="orb" style={{ top: -80, left: '20%', width: 600, height: 600, background: 'radial-gradient(circle, rgba(139,92,246,0.2) 0%, transparent 65%)', filter: 'blur(80px)', animation: 'floatOrb 20s ease-in-out infinite' }} />
        <div className="container" style={{ position: 'relative', zIndex: 1 }}>
          <SectionBadge variant="violet">Who We Are</SectionBadge>
          <h1 className="text-display-xl" style={{ marginBottom: 24 }}>
            Architects of Sustainable<br /><span className="gradient-text">Enterprise Value</span>
          </h1>
          <p style={{ fontSize: '1.18rem', color: 'var(--text-secondary)', maxWidth: 700, margin: '0 auto', lineHeight: 1.75 }}>
            Rise Growth Group was founded to bridge the critical gap between high-level management strategy and granular execution. We help ambitious leaders build enduring businesses that dominate their industries.
          </p>
        </div>
      </section>

      {/* Team (Live from WP) */}
      <section className="section" style={{ background: 'var(--bg-deep)', paddingTop: 60 }}>
        <div className="container">
          <div style={{ textAlign: 'center', maxWidth: 620, margin: '0 auto 48px' }}>
            <SectionBadge variant="green">Leadership & Expertise</SectionBadge>
            <h2 className="text-display-lg" style={{ marginBottom: 14 }}>Senior Advisory Partners</h2>
            <p style={{ color: 'var(--text-secondary)', fontSize: '1.05rem' }}>$1.5B+ in collective enterprise value creation across SaaS, FinTech, and Enterprise Software.</p>
          </div>
          <div ref={teamRef} className="grid-4">
            {loading
              ? Array(4).fill(0).map((_, i) => (
                <div key={i} className="card team-card">
                  <div style={{ height: 110, background: '#0f172a' }} />
                  <div style={{ padding: 24, textAlign: 'center' }}>
                    <Skeleton h={18} w="70%" mb={8} />
                    <Skeleton h={12} w="50%" mb={12} />
                    <Skeleton h={13} mb={5} />
                    <Skeleton h={13} w="85%" />
                  </div>
                </div>
              ))
              : data.team.map((m, i) => {
                const meta = m.meta || {};
                return (
                  <div key={m.id} className="card team-card" style={{ opacity: teamVisible ? 1 : 0, transform: teamVisible ? 'none' : 'translateY(24px)', transition: `all 0.5s ease ${i * 100}ms` }}>
                    <div className="team-card-header">
                      <div className="team-avatar" style={{ background: meta.rise_bg_gradient || '#2563eb' }}>{meta.rise_initials || '??'}</div>
                    </div>
                    <div style={{ padding: 24, textAlign: 'center' }}>
                      <h4 style={{ fontFamily: 'var(--font-display)', fontSize: '1.15rem', fontWeight: 700, color: '#fff', marginBottom: 4 }}>{m.title?.rendered}</h4>
                      <div style={{ color: '#38bdf8', fontSize: '0.8rem', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.07em', marginBottom: 12 }}>{meta.rise_role}</div>
                      <p style={{ color: 'var(--text-secondary)', fontSize: '0.87rem', lineHeight: 1.6 }}>{stripHtml(m.content?.rendered)}</p>
                    </div>
                  </div>
                );
              })
            }
          </div>
        </div>
      </section>

      {/* Contact Form */}
      <section id="contact" className="section">
        <div className="container">
          <div ref={formRef} style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(360px, 1fr))', gap: 48, opacity: formVisible ? 1 : 0, transform: formVisible ? 'none' : 'translateY(24px)', transition: 'all 0.6s ease' }}>
            <div>
              <SectionBadge>Direct Advisory Channel</SectionBadge>
              <h2 className="text-display-md" style={{ marginBottom: 18 }}>Start the Conversation</h2>
              <p style={{ color: 'var(--text-secondary)', lineHeight: 1.75, marginBottom: 36, fontSize: '1.02rem' }}>
                Whether you are preparing for a funding round, seeking to double enterprise sales velocity, or navigating operational complexity — our partners are ready.
              </p>
              {[
                { icon: '📍', label: 'Headquarters', value: '100 Financial Center Blvd, Suite 2400, New York, NY' },
                { icon: '✉️', label: 'Executive Inquiries', value: 'advisory@risegrowthgroup.com', accent: true },
                { icon: '📞', label: 'Direct Desk', value: '+1 (800) 482-9150  ·  Mon–Fri, 8am–6pm EST' },
                { icon: '⏱️', label: 'Response SLA', value: 'Guaranteed reply within 4 business hours', green: true },
              ].map((r, i) => (
                <div key={i} className="contact-row" style={{ marginBottom: 12 }}>
                  <div className="contact-icon">{r.icon}</div>
                  <div>
                    <div style={{ fontFamily: 'var(--font-display)', fontWeight: 700, fontSize: '0.9rem', color: '#fff', marginBottom: 2 }}>{r.label}</div>
                    <div style={{ fontSize: '0.85rem', color: r.accent ? '#38bdf8' : r.green ? '#34d399' : 'var(--text-secondary)' }}>{r.value}</div>
                  </div>
                </div>
              ))}
            </div>

            <div style={{ background: 'var(--bg-card)', border: '1px solid var(--border-subtle)', borderRadius: 20, padding: 40, backdropFilter: 'blur(16px)' }}>
              {submitted ? (
                <div style={{ textAlign: 'center', padding: '30px 0' }}>
                  <div style={{ fontSize: '3rem', marginBottom: 16 }}>✅</div>
                  <h3 style={{ fontFamily: 'var(--font-display)', fontSize: '1.5rem', fontWeight: 700, color: '#34d399', marginBottom: 12 }}>Request Sent</h3>
                  <p style={{ color: 'var(--text-secondary)', lineHeight: 1.7, marginBottom: 28 }}>
                    Thank you, <strong style={{ color: '#fff' }}>{formData.name || 'partner'}</strong>. A Managing Principal will reach out to <strong style={{ color: '#38bdf8' }}>{formData.email}</strong> within 4 business hours.
                  </p>
                  <button className="btn btn-ghost btn-sm" onClick={() => setSubmitted(false)}>Submit Another →</button>
                </div>
              ) : (
                <>
                  <h3 style={{ fontFamily: 'var(--font-display)', fontSize: '1.35rem', fontWeight: 700, marginBottom: 6 }}>Request Strategy Session</h3>
                  <p style={{ color: 'var(--text-secondary)', fontSize: '0.88rem', marginBottom: 28 }}>Connect directly with a Managing Principal.</p>
                  <form onSubmit={handleSubmit}>
                    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 14, marginBottom: 14 }}>
                      <div><label className="form-label">Full Name *</label><input className="form-input" required placeholder="e.g. Alex Wright" value={formData.name} onChange={e => setFormData({ ...formData, name: e.target.value })} /></div>
                      <div><label className="form-label">Corporate Email *</label><input className="form-input" type="email" required placeholder="alex@company.com" value={formData.email} onChange={e => setFormData({ ...formData, email: e.target.value })} /></div>
                    </div>
                    <div style={{ marginBottom: 14 }}>
                      <label className="form-label">Revenue Stage</label>
                      <select className="form-select" value={formData.stage} onChange={e => setFormData({ ...formData, stage: e.target.value })}>
                        <option>Under $5M ARR</option><option>$5M–$20M ARR</option><option>$20M–$100M ARR</option><option>$100M+ Enterprise</option>
                      </select>
                    </div>
                    <div style={{ marginBottom: 22 }}>
                      <label className="form-label">Strategic Challenge / Goal</label>
                      <textarea className="form-textarea" required placeholder="Describe your growth bottleneck or objective..." value={formData.message} onChange={e => setFormData({ ...formData, message: e.target.value })} />
                    </div>
                    <button type="submit" className="btn btn-primary" disabled={submitting} style={{ width: '100%', fontSize: '1rem', padding: 14, borderRadius: 10, justifyContent: 'center', opacity: submitting ? 0.7 : 1 }}>
                      {submitting ? 'Sending…' : 'Submit Strategy Inquiry →'}
                    </button>
                  </form>
                </>
              )}
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}

/* ─── Main App ───────────────────────────────────────── */
export default function App() {
  const [page, setPage] = useState('home');
  const [showApi, setShowApi] = useState(false);
  const scrollProgress = useScrollProgress();
  const { data, loading, source } = useCMSData();

  const goTo = (tab) => { setPage(tab); window.scrollTo({ top: 0, behavior: 'smooth' }); };
  const goContact = () => goTo('about');

  return (
    <div style={{ minHeight: '100vh', backgroundColor: 'var(--bg-void)' }}>
      <div className="scroll-bar" style={{ width: `${scrollProgress}%` }} />

      {/* Header */}
      <header style={{ position: 'sticky', top: 0, zIndex: 1000, backgroundColor: 'rgba(4,6,14,0.85)', backdropFilter: 'blur(20px)', borderBottom: '1px solid var(--border-subtle)', padding: '0 24px' }}>
        <div style={{ maxWidth: 1200, margin: '0 auto', height: 64, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <button onClick={() => goTo('home')} style={{ background: 'none', border: 'none', cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 12 }}>
            <div style={{ width: 32, height: 32, borderRadius: 8, background: 'linear-gradient(135deg,#2563eb,#38bdf8)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
              <span style={{ color: '#fff', fontFamily: 'var(--font-display)', fontWeight: 900, fontSize: '0.85rem' }}>RG</span>
            </div>
            <span style={{ fontFamily: 'var(--font-display)', fontWeight: 800, fontSize: '1.1rem', letterSpacing: '-0.02em', color: '#fff' }}>
              RISE <span style={{ color: '#38bdf8' }}>GROWTH</span>
            </span>
          </button>

          <nav style={{ display: 'flex', alignItems: 'center', gap: 28 }}>
            <button className={`nav-tab ${page === 'home' ? 'active' : ''}`} onClick={() => goTo('home')}>Home</button>
            <button className={`nav-tab ${page === 'about' ? 'active' : ''}`} onClick={() => goTo('about')}>About & Contact</button>
            <button className="btn btn-ghost btn-sm" onClick={() => setShowApi(!showApi)} style={{ fontSize: '0.78rem', fontWeight: 600, padding: '6px 12px', opacity: 0.7 }}>
              {showApi ? '✕ API' : '{ } WP API'}
            </button>
            <button className="btn btn-primary btn-sm" onClick={goContact}>Book Strategy Call</button>
          </nav>
        </div>
      </header>

      {/* API Inspector */}
      {showApi && (
        <div className="api-panel" style={{ padding: '16px 24px' }}>
          <div style={{ maxWidth: 1200, margin: '0 auto' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 10, fontSize: '0.78rem', flexWrap: 'wrap', gap: 8 }}>
              <span style={{ color: source === 'wp' ? '#34d399' : '#fbbf24' }}>
                {source === 'wp' ? '✓ Live WordPress CPT REST API' : '⚠ Using fallback data (WordPress offline)'}
              </span>
              <span style={{ color: '#475569' }}>Services: {data.services.length} · Team: {data.team.length} · Testimonials: {data.testimonials.length} · FAQs: {data.faqs.length}</span>
            </div>
            <div style={{ fontSize: '0.75rem', color: '#475569', display: 'flex', flexWrap: 'wrap', gap: 16, fontFamily: 'monospace' }}>
              {['services','team','testimonials','faqs'].map(ep => (
                <span key={ep}>GET <span style={{ color: '#38bdf8' }}>{WP_BASE}/{ep}</span></span>
              ))}
            </div>
          </div>
        </div>
      )}

      <main>
        {page === 'home'
          ? <HomePage onContact={goContact} data={data} loading={loading} />
          : <AboutPage onContact={goContact} data={data} loading={loading} />
        }
      </main>

      <footer style={{ background: '#020510', borderTop: '1px solid var(--border-subtle)', padding: '40px 24px' }}>
        <div style={{ maxWidth: 1200, margin: '0 auto', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: 20 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
            <div style={{ width: 28, height: 28, borderRadius: 6, background: 'linear-gradient(135deg,#2563eb,#38bdf8)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
              <span style={{ color: '#fff', fontFamily: 'var(--font-display)', fontWeight: 900, fontSize: '0.75rem' }}>RG</span>
            </div>
            <span style={{ fontFamily: 'var(--font-display)', fontWeight: 700, fontSize: '0.95rem', color: '#fff' }}>Rise Growth Group</span>
          </div>
          <div style={{ color: 'var(--text-muted)', fontSize: '0.8rem', textAlign: 'center' }}>
            © 2026 Rise Growth Group · Headless WordPress CMS + Vite React
          </div>
          <div style={{ display: 'flex', gap: 24 }}>
            {['Privacy', 'Terms', 'Contact'].map(l => (
              <button key={l} className="nav-tab" style={{ fontSize: '0.82rem' }} onClick={l === 'Contact' ? goContact : undefined}>{l}</button>
            ))}
          </div>
        </div>
      </footer>

      {/* Live CMS status badge */}
      <CMSBadge source={source} />
    </div>
  );
}
