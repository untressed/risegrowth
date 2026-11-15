import subprocess
import os
import sys

wp_bin = r"C:\Users\visha\AppData\Local\Microsoft\WinGet\Packages\PHP.PHP.8.3_Microsoft.Winget.Source_8wekyb3d8bbwe\php.exe"
wp_cli = r"C:\Users\visha\.gemini\antigravity-ide\scratch\wordpress-site\wp-cli.phar"
wp_dir = r"C:\Users\visha\.gemini\antigravity-ide\scratch\wordpress-site\wordpress"

def run_wp(*args):
    cmd = [wp_bin, wp_cli, f"--path={wp_dir}"] + list(args)
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0 and res.stderr:
        print(f"Error running {' '.join(args)}: {res.stderr}")
    return res.stdout.strip()

print("Updating site title and tagline...")
run_wp("option", "update", "blogname", "Rise Growth Group")
run_wp("option", "update", "blogdescription", "Strategic Advisory & Enterprise Scaling")

# ==========================================
# 1. LANDING PAGE CONTENT (HOME)
# ==========================================
home_html = """
<!-- HERO SECTION -->
<section class="r-section" style="padding-top: 110px; padding-bottom: 75px; background: radial-gradient(circle at 50% -20%, rgba(37,99,235,0.25) 0%, rgba(9,13,22,1) 75%);">
  <div class="r-glow-orb" style="top: 50px; left: 10%;"></div>
  <div class="r-glow-orb" style="top: 150px; right: 5%; width: 450px; height: 450px; animation-delay: -5s;"></div>

  <div class="r-container">
    <div style="max-width: 880px; margin: 0 auto; text-align: center;">
      <div class="r-tag">
        <span class="r-tag-dot"></span>
        STRATEGIC ADVISORY & REVENUE SCALING
      </div>
      <h1 class="r-heading-xl">
        Scaling Visionary Enterprises Into <span class="r-gradient-text">Market Leaders</span>
      </h1>
      <p class="r-lead" style="margin: 0 auto 38px auto;">
        Rise Growth Group partners with high-growth companies and corporate leadership to engineer scalable revenue engines, streamline core operations, and achieve multi-million dollar valuation exits.
      </p>
      <div class="r-btn-group" style="justify-content: center;">
        <a href="/about-contact/#contact" class="r-btn r-btn-primary">
          Schedule Strategy Call →
        </a>
        <a href="#services" class="r-btn r-btn-secondary">
          Explore Practice Areas
        </a>
      </div>
    </div>

    <!-- METRICS GRID -->
    <div class="r-stats-grid">
      <div class="r-stat-card">
        <div class="r-stat-num">$450M+</div>
        <div class="r-stat-label">Client Revenue &amp; Capital Unlocked</div>
      </div>
      <div class="r-stat-card">
        <div class="r-stat-num">3.4x</div>
        <div class="r-stat-label">Average 18-Month Client ROI Multiple</div>
      </div>
      <div class="r-stat-card">
        <div class="r-stat-num">98%</div>
        <div class="r-stat-label">Client Retention &amp; Executive Satisfaction</div>
      </div>
      <div class="r-stat-card">
        <div class="r-stat-num">140+</div>
        <div class="r-stat-label">Enterprise Scaling Engagements Delivered</div>
      </div>
    </div>

    <!-- TRUSTED CLIENT BADGES -->
    <div style="margin-top: 60px; text-align: center; border-top: 1px solid var(--r-border); padding-top: 40px;">
      <div style="font-size: 0.85rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; color: #64748b; margin-bottom: 24px;">
        TRUSTED BY LEADERS ACROSS ENTERPRISE SAAS, FINTECH &amp; HEALTHCARE
      </div>
      <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 40px; align-items: center; opacity: 0.75;">
        <span style="font-family: Outfit, sans-serif; font-size: 1.25rem; font-weight: 700; color: #cbd5e1; letter-spacing: -0.01em;">▲ NEXUS CAPITAL</span>
        <span style="font-family: Outfit, sans-serif; font-size: 1.25rem; font-weight: 700; color: #cbd5e1; letter-spacing: -0.01em;">● APEX CLOUD</span>
        <span style="font-family: Outfit, sans-serif; font-size: 1.25rem; font-weight: 700; color: #cbd5e1; letter-spacing: -0.01em;">◆ VANGUARD SYSTEMS</span>
        <span style="font-family: Outfit, sans-serif; font-size: 1.25rem; font-weight: 700; color: #cbd5e1; letter-spacing: -0.01em;">■ HORIZON GLOBAL</span>
        <span style="font-family: Outfit, sans-serif; font-size: 1.25rem; font-weight: 700; color: #cbd5e1; letter-spacing: -0.01em;">✦ ELEVATE FINTECH</span>
      </div>
    </div>
  </div>
</section>

<!-- WHY US / VALUE PROPOSITION -->
<section class="r-section" style="background-color: #0b0f1a; border-top: 1px solid var(--r-border);">
  <div class="r-container">
    <div style="text-align: center; max-width: 760px; margin: 0 auto 50px auto;">
      <div class="r-tag">
        <span class="r-tag-dot"></span>
        THE RISE ADVANTAGE
      </div>
      <h2 class="r-heading-lg">Consulting Reimagined for Concrete Results</h2>
      <p class="r-lead" style="margin: 0 auto;">
        Traditional consultants deliver 100-page slide presentations and walk away. We embed directly with your executive team to design the strategy, execute the playbooks, and guarantee measurable business outcomes.
      </p>
    </div>

    <div class="r-grid-3">
      <div class="r-card">
        <div class="r-card-icon">⚡</div>
        <h3 class="r-card-title">Empirical Diagnostic</h3>
        <p class="r-card-desc">
          We perform an exhaustive audit of your pipeline mechanics, unit economics, and operational drag in the first 14 days, revealing high-leverage growth opportunities.
        </p>
        <ul class="r-card-features">
          <li><span class="r-check">✓</span> 14-day rapid financial audit</li>
          <li><span class="r-check">✓</span> CAC &amp; LTV cohort decomposition</li>
          <li><span class="r-check">✓</span> Bottleneck prioritization matrix</li>
        </ul>
      </div>

      <div class="r-card">
        <div class="r-card-icon">🎯</div>
        <h3 class="r-card-title">Embedded Execution</h3>
        <p class="r-card-desc">
          Our senior partners don't just advise—we participate in executive reviews, restructure sales motions, and manage cross-functional accountability until target metrics hit.
        </p>
        <ul class="r-card-features">
          <li><span class="r-check">✓</span> Fractional executive leadership</li>
          <li><span class="r-check">✓</span> Weekly OKR &amp; sprint tracking</li>
          <li><span class="r-check">✓</span> Hands-on team mentorship</li>
        </ul>
      </div>

      <div class="r-card">
        <div class="r-card-icon">📈</div>
        <h3 class="r-card-title">Valuation Acceleration</h3>
        <p class="r-card-desc">
          Every growth sprint is directly mapped to enterprise valuation multiples, EBITDA margin expansion, and capital market readiness for Series B through pre-IPO stages.
        </p>
        <ul class="r-card-features">
          <li><span class="r-check">✓</span> Strategic M&amp;A &amp; capital readiness</li>
          <li><span class="r-check">✓</span> Sustainable gross margin expansion</li>
          <li><span class="r-check">✓</span> Investor-grade reporting hygiene</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- SERVICES SECTION WITH INTERACTIVE FILTER TABS -->
<section id="services" class="r-section" style="background-color: #090d16; border-top: 1px solid var(--r-border);">
  <div class="r-container">
    <div style="text-align: center; max-width: 720px; margin: 0 auto 40px auto;">
      <div class="r-tag">
        <span class="r-tag-dot"></span>
        OUR PRACTICE AREAS
      </div>
      <h2 class="r-heading-lg" style="margin-bottom: 12px;">Specialized Strategic Advisory</h2>
      <p class="r-lead" style="margin: 0 auto;">
        Click below to filter our advisory practices based on your enterprise's core growth focus.
      </p>
    </div>

    <!-- Interactive Filter Buttons -->
    <div class="r-filter-bar">
      <button class="r-filter-btn active" onclick="filterServices('all', this)">All Practice Areas</button>
      <button class="r-filter-btn" onclick="filterServices('strategy', this)">Executive Strategy</button>
      <button class="r-filter-btn" onclick="filterServices('gtm', this)">Revenue &amp; GTM</button>
      <button class="r-filter-btn" onclick="filterServices('ops', this)">Operations &amp; Scale</button>
      <button class="r-filter-btn" onclick="filterServices('ai', this)">Digital &amp; AI</button>
    </div>

    <div class="r-grid-2" id="services-grid">
      <!-- Service 1 -->
      <div class="r-card service-item" data-category="strategy">
        <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 18px;">
          <div class="r-card-icon" style="margin-bottom: 0;">🏛️</div>
          <h3 class="r-card-title" style="margin-bottom: 0;">Executive Strategy &amp; Board Advisory</h3>
        </div>
        <p class="r-card-desc">
          Guiding CEOs, founders, and boards of directors through pivotal corporate milestones, competitive repositioning, and strategic capital allocation.
        </p>
        <ul class="r-card-features">
          <li><span class="r-check">✓</span> Corporate positioning and market defense strategy</li>
          <li><span class="r-check">✓</span> Board governance and investor communication synthesis</li>
          <li><span class="r-check">✓</span> M&amp;A target evaluation and post-merger integration</li>
          <li><span class="r-check">✓</span> Strategic turnaround and pivot roadmaps</li>
        </ul>
      </div>

      <!-- Service 2 -->
      <div class="r-card service-item" data-category="gtm">
        <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 18px;">
          <div class="r-card-icon" style="margin-bottom: 0;">🚀</div>
          <h3 class="r-card-title" style="margin-bottom: 0;">Revenue Architecture &amp; Go-To-Market</h3>
        </div>
        <p class="r-card-desc">
          Building resilient, predictable revenue engines that dramatically increase sales velocity, win rates, and customer lifetime value.
        </p>
        <ul class="r-card-features">
          <li><span class="r-check">✓</span> Enterprise sales org design and quota optimization</li>
          <li><span class="r-check">✓</span> Value-based pricing model overhaul and margin lifting</li>
          <li><span class="r-check">✓</span> Account-Based Marketing (ABM) pipeline deployment</li>
          <li><span class="r-check">✓</span> Sales enablement, pitch collateral, and playbooks</li>
        </ul>
      </div>

      <!-- Service 3 -->
      <div class="r-card service-item" data-category="ops">
        <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 18px;">
          <div class="r-card-icon" style="margin-bottom: 0;">⚙️</div>
          <h3 class="r-card-title" style="margin-bottom: 0;">Operational Excellence &amp; Scale</h3>
        </div>
        <p class="r-card-desc">
          Streamlining cross-functional workflows, reducing operational bloat, and installing institutional rhythms that support 10x headcount expansion.
        </p>
        <ul class="r-card-features">
          <li><span class="r-check">✓</span> Executive OKR orchestration and transparency dashboards</li>
          <li><span class="r-check">✓</span> End-to-end automated workflow integration</li>
          <li><span class="r-check">✓</span> Cost discipline and non-dilutive efficiency measures</li>
          <li><span class="r-check">✓</span> Senior executive recruiting and organizational charting</li>
        </ul>
      </div>

      <!-- Service 4 -->
      <div class="r-card service-item" data-category="ai">
        <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 18px;">
          <div class="r-card-icon" style="margin-bottom: 0;">🤖</div>
          <h3 class="r-card-title" style="margin-bottom: 0;">Digital &amp; AI Transformation</h3>
        </div>
        <p class="r-card-desc">
          Harnessing modern artificial intelligence and data infrastructure to automate repetitive processes, forecast market demands, and protect market share.
        </p>
        <ul class="r-card-features">
          <li><span class="r-check">✓</span> Enterprise LLM and AI workflow deployment</li>
          <li><span class="r-check">✓</span> Real-time executive decision intelligence dashboards</li>
          <li><span class="r-check">✓</span> Cloud migration and legacy system modernization</li>
          <li><span class="r-check">✓</span> Data security and regulatory compliance protocols</li>
        </ul>
      </div>
    </div>
  </div>

  <script>
  function filterServices(category, btn) {
    var buttons = document.querySelectorAll('.r-filter-btn');
    buttons.forEach(function(b) { b.classList.remove('active'); });
    btn.classList.add('active');

    var items = document.querySelectorAll('.service-item');
    items.forEach(function(item) {
      if (category === 'all' || item.getAttribute('data-category') === category) {
        item.style.display = 'flex';
        item.style.opacity = '1';
        item.style.transform = 'translateY(0)';
      } else {
        item.style.display = 'none';
      }
    });
  }
  </script>
</section>

<!-- INTERACTIVE ROI / VALUATION CALCULATOR WIDGET -->
<section class="r-section" style="background-color: #0b0f1a; border-top: 1px solid var(--r-border);">
  <div class="r-container">
    <div style="text-align: center; max-width: 760px; margin: 0 auto 30px auto;">
      <div class="r-tag">
        <span class="r-tag-dot"></span>
        INTERACTIVE VALUATION MODEL
      </div>
      <h2 class="r-heading-lg">Estimate Your Enterprise Growth Potential</h2>
      <p class="r-lead" style="margin: 0 auto;">
        Adjust the sliders below to model potential enterprise value expansion with Rise Growth Group's strategic revenue acceleration.
      </p>
    </div>

    <div class="r-calc-container">
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 40px; align-items: center;">
        <div>
          <!-- Slider 1 -->
          <div style="margin-bottom: 24px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="font-family: Outfit, sans-serif; font-weight: 700; color: #ffffff; font-size: 1.05rem;">Current Annual Recurring Revenue (ARR):</span>
              <span id="arr-display" style="font-family: Outfit, sans-serif; font-weight: 800; color: #38bdf8; font-size: 1.3rem;">$10M</span>
            </div>
            <input type="range" id="arr-slider" class="r-slider" min="2" max="50" step="1" value="10" oninput="updateCalculator()" />
            <div style="display: flex; justify-content: space-between; color: #64748b; font-size: 0.85rem;">
              <span>$2M</span>
              <span>$25M</span>
              <span>$50M+</span>
            </div>
          </div>

          <!-- Slider 2 -->
          <div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="font-family: Outfit, sans-serif; font-weight: 700; color: #ffffff; font-size: 1.05rem;">Target 24-Month Growth Multiple:</span>
              <span id="growth-display" style="font-family: Outfit, sans-serif; font-weight: 800; color: #10b981; font-size: 1.3rem;">2.5x</span>
            </div>
            <input type="range" id="growth-slider" class="r-slider" min="1.5" max="4.0" step="0.1" value="2.5" oninput="updateCalculator()" />
            <div style="display: flex; justify-content: space-between; color: #64748b; font-size: 0.85rem;">
              <span>1.5x (Steady)</span>
              <span>2.5x (Accelerated)</span>
              <span>4.0x (Hyper-Growth)</span>
            </div>
          </div>
        </div>

        <!-- Real-time Output Cards -->
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px;">
          <div class="r-calc-output-card">
            <div style="font-size: 0.85rem; color: #94a3b8; font-weight: 600; text-transform: uppercase; margin-bottom: 6px;">Target Scaled ARR</div>
            <div id="scaled-arr-val" style="font-family: Outfit, sans-serif; font-size: 2.2rem; font-weight: 800; color: #ffffff;">$25M</div>
            <div style="font-size: 0.8rem; color: #38bdf8; margin-top: 4px;">+$15M ARR Lift</div>
          </div>

          <div class="r-calc-output-card" style="background: rgba(37,99,235,0.12); border-color: rgba(56,189,248,0.4);">
            <div style="font-size: 0.85rem; color: #94a3b8; font-weight: 600; text-transform: uppercase; margin-bottom: 6px;">Projected Enterprise Value</div>
            <div id="ev-val" style="font-family: Outfit, sans-serif; font-size: 2.2rem; font-weight: 800; color: #38bdf8;">$200M</div>
            <div style="font-size: 0.8rem; color: #10b981; margin-top: 4px;">Based on 8x EV multiple</div>
          </div>

          <div class="r-calc-output-card" style="grid-column: span 2; background: rgba(16,185,129,0.08); border-color: rgba(16,185,129,0.3);">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <div style="text-align: left;">
                <div style="font-size: 0.85rem; color: #94a3b8; font-weight: 600; text-transform: uppercase;">Estimated Shareholder Value Created</div>
                <div id="lift-val" style="font-family: Outfit, sans-serif; font-size: 1.8rem; font-weight: 800; color: #10b981;">+$120,000,000</div>
              </div>
              <a href="/about-contact/#contact" class="r-btn r-btn-primary" style="padding: 10px 22px; font-size: 0.95rem;">
                Audit Your Numbers →
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <script>
  function updateCalculator() {
    var arr = parseFloat(document.getElementById('arr-slider').value);
    var growth = parseFloat(document.getElementById('growth-slider').value);
    
    document.getElementById('arr-display').innerText = '$' + arr + 'M';
    document.getElementById('growth-display').innerText = growth.toFixed(1) + 'x';

    var scaledArr = arr * growth;
    var currentEv = arr * 8;
    var newEv = scaledArr * 8;
    var lift = newEv - currentEv;

    document.getElementById('scaled-arr-val').innerText = '$' + Math.round(scaledArr) + 'M';
    document.getElementById('ev-val').innerText = '$' + Math.round(newEv) + 'M';
    document.getElementById('lift-val').innerText = '+$' + Math.round(lift).toLocaleString() + ',000,000';
  }
  </script>
</section>

<!-- METHODOLOGY / 4-STEP PROCESS -->
<section class="r-section" style="background-color: #090d16; border-top: 1px solid var(--r-border);">
  <div class="r-container">
    <div style="text-align: center; max-width: 720px; margin: 0 auto 50px auto;">
      <div class="r-tag">
        <span class="r-tag-dot"></span>
        HOW WE ENGAGE
      </div>
      <h2 class="r-heading-lg">Our 4-Phase Growth Framework</h2>
      <p class="r-lead" style="margin: 0 auto;">
        A disciplined, milestone-driven engagement structure that delivers actionable clarity within weeks, not quarters.
      </p>
    </div>

    <div class="r-grid-4">
      <div class="r-card">
        <div class="r-step-num">PHASE 01</div>
        <h4 class="r-card-title" style="font-size: 1.2rem;">Growth Diagnostic</h4>
        <div style="color: #64748b; font-size: 0.82rem; font-weight: 600; margin-bottom: 12px;">WEEKS 1–2</div>
        <p class="r-card-desc" style="font-size: 0.92rem;">
          Deep analysis of revenue streams, unit economics, churn drivers, and team operational bottlenecks.
        </p>
      </div>

      <div class="r-card">
        <div class="r-step-num">PHASE 02</div>
        <h4 class="r-card-title" style="font-size: 1.2rem;">Strategic Blueprint</h4>
        <div style="color: #64748b; font-size: 0.82rem; font-weight: 600; margin-bottom: 12px;">WEEKS 3–4</div>
        <p class="r-card-desc" style="font-size: 0.92rem;">
          Co-creating the 12-month growth playbook, defining definitive KPIs, and designing new market motions.
        </p>
      </div>

      <div class="r-card">
        <div class="r-step-num">PHASE 03</div>
        <h4 class="r-card-title" style="font-size: 1.2rem;">Embedded Sprints</h4>
        <div style="color: #64748b; font-size: 0.82rem; font-weight: 600; margin-bottom: 12px;">MONTHS 2–6</div>
        <p class="r-card-desc" style="font-size: 0.92rem;">
          Active execution alongside your department heads, rolling out new pricing, automations, and sales playbooks.
        </p>
      </div>

      <div class="r-card">
        <div class="r-step-num">PHASE 04</div>
        <h4 class="r-card-title" style="font-size: 1.2rem;">Scale &amp; Handover</h4>
        <div style="color: #64748b; font-size: 0.82rem; font-weight: 600; margin-bottom: 12px;">MONTHS 6+</div>
        <p class="r-card-desc" style="font-size: 0.92rem;">
          Institutionalizing systems, training permanent leadership, and locking in sustained compound growth.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- TESTIMONIALS SECTION -->
<section class="r-section" style="background-color: #0b0f1a; border-top: 1px solid var(--r-border);">
  <div class="r-container">
    <div style="text-align: center; max-width: 720px; margin: 0 auto 50px auto;">
      <div class="r-tag">
        <span class="r-tag-dot"></span>
        CLIENT ENDORSEMENTS
      </div>
      <h2 class="r-heading-lg">Endorsed by Visionary Founders &amp; Boards</h2>
      <p class="r-lead" style="margin: 0 auto;">
        Real results delivered for companies operating in hyper-competitive markets.
      </p>
    </div>

    <div class="r-grid-3">
      <div class="r-quote-card">
        <div>
          <div class="r-stars">★★★★★</div>
          <p class="r-quote-text">
            "Rise Growth Group overhauled our entire enterprise sales motion. Within 12 months, our ARR expanded from $8M to $23M with a 38% increase in gross margins. Their partners are in a league of their own."
          </p>
        </div>
        <div class="r-client-info">
          <div class="r-avatar">MV</div>
          <div>
            <div class="r-client-name">Marcus Vance</div>
            <div class="r-client-role">Founder &amp; CEO, Nexus Cloud</div>
          </div>
        </div>
      </div>

      <div class="r-quote-card">
        <div>
          <div class="r-stars">★★★★★</div>
          <p class="r-quote-text">
            "Their operational precision and strategic clarity are extraordinary. They didn't just point out bottlenecks—they actively sat in the trenches with our leadership team until target KPIs were hit."
          </p>
        </div>
        <div class="r-client-info">
          <div class="r-avatar" style="background: linear-gradient(135deg, #059669, #10b981);">ER</div>
          <div>
            <div class="r-client-name">Elena Rostova</div>
            <div class="r-client-role">Managing Partner, Vanguard Capital</div>
          </div>
        </div>
      </div>

      <div class="r-quote-card">
        <div>
          <div class="r-stars">★★★★★</div>
          <p class="r-quote-text">
            "Working with Rise Growth was the highest-ROI investment of our post-Series B journey. They transformed our customer acquisition economics and paved the way for our successful acquisition."
          </p>
        </div>
        <div class="r-client-info">
          <div class="r-avatar" style="background: linear-gradient(135deg, #d97706, #f59e0b);">DC</div>
          <div>
            <div class="r-client-name">David Chen</div>
            <div class="r-client-role">Chief Operating Officer, Horizon Tech</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- INTERACTIVE FAQ ACCORDION -->
<section class="r-section" style="background-color: #090d16; border-top: 1px solid var(--r-border);">
  <div class="r-container">
    <div style="text-align: center; max-width: 720px; margin: 0 auto 50px auto;">
      <div class="r-tag">
        <span class="r-tag-dot"></span>
        FREQUENTLY ASKED QUESTIONS
      </div>
      <h2 class="r-heading-lg">Advisory Engagement Clarity</h2>
      <p class="r-lead" style="margin: 0 auto;">
        Everything you need to know about partnering with Rise Growth Group.
      </p>
    </div>

    <div class="r-faq-list">
      <div class="r-faq-item open">
        <div class="r-faq-header" onclick="toggleFaq(this)">
          <span>How does an engagement with Rise Growth Group typically work?</span>
          <span class="r-faq-icon">+</span>
        </div>
        <div class="r-faq-body">
          We operate as an embedded advisory team. We start with a 14-day rapid Diagnostic audit, formulate a 12-month blueprint, and then embed senior partners directly alongside your executive committee to execute sprints, restructure operations, and optimize your revenue funnel.
        </div>
      </div>

      <div class="r-faq-item">
        <div class="r-faq-header" onclick="toggleFaq(this)">
          <span>What stage of companies do you typically partner with?</span>
          <span class="r-faq-icon">+</span>
        </div>
        <div class="r-faq-body">
          Our primary clients are post-Series A through Pre-IPO growth scaleups ($2M to $100M+ in ARR) looking to accelerate revenue, achieve operational profitability, or prepare for major institutional funding rounds and M&amp;A exits.
        </div>
      </div>

      <div class="r-faq-item">
        <div class="r-faq-header" onclick="toggleFaq(this)">
          <span>How soon can we expect measurable ROI?</span>
          <span class="r-faq-icon">+</span>
        </div>
        <div class="r-faq-body">
          Our diagnostic identifies immediate low-hanging revenue leakage within the first 14 days. Most enterprise clients experience measurable sales pipeline acceleration and gross margin improvements within 60 to 90 days of active implementation.
        </div>
      </div>

      <div class="r-faq-item">
        <div class="r-faq-header" onclick="toggleFaq(this)">
          <span>What is the fee and compensation structure?</span>
          <span class="r-faq-icon">+</span>
        </div>
        <div class="r-faq-body">
          We offer bespoke retainer models tailored to client scale, with performance-tied incentive alignments for qualified growth partnerships. We discuss transparent engagement options during your initial discovery session.
        </div>
      </div>
    </div>
  </div>

  <script>
  function toggleFaq(header) {
    var item = header.parentElement;
    item.classList.toggle('open');
  }
  </script>
</section>

<!-- CALL TO ACTION BANNER -->
<section class="r-section" style="padding-top: 40px; padding-bottom: 90px; background-color: #090d16;">
  <div class="r-container">
    <div class="r-cta-banner">
      <div class="r-tag">
        <span class="r-tag-dot"></span>
        ELEVATE YOUR BUSINESS
      </div>
      <h2 class="r-heading-lg" style="max-width: 780px; margin: 0 auto 20px auto;">
        Ready to Break Through Your Next Growth Ceiling?
      </h2>
      <p class="r-lead" style="margin: 0 auto 36px auto;">
        Book a confidential 30-minute strategic consultation with our managing partners to evaluate your growth trajectory and identify untapped valuation levers.
      </p>
      <a href="/about-contact/#contact" class="r-btn r-btn-primary" style="font-size: 1.1rem; padding: 16px 36px;">
        Book Strategic Consultation →
      </a>
    </div>
  </div>
</section>
"""

# ==========================================
# 2. ABOUT & CONTACT PAGE CONTENT
# ==========================================
about_html = """
<!-- ABOUT HERO SECTION -->
<section class="r-section" style="padding-top: 110px; padding-bottom: 75px; background: radial-gradient(circle at 50% -20%, rgba(37,99,235,0.25) 0%, rgba(9,13,22,1) 75%);">
  <div class="r-glow-orb" style="top: 50px; left: 10%;"></div>
  <div class="r-glow-orb" style="top: 150px; right: 5%; width: 450px; height: 450px; animation-delay: -5s;"></div>

  <div class="r-container">
    <div style="max-width: 860px; margin: 0 auto; text-align: center;">
      <div class="r-tag">
        <span class="r-tag-dot"></span>
        WHO WE ARE &amp; OUR PURPOSE
      </div>
      <h1 class="r-heading-xl">
        Architects of Sustainable <span class="r-gradient-text">Enterprise Value</span>
      </h1>
      <p class="r-lead" style="margin: 0 auto 30px auto;">
        Rise Growth Group was founded to bridge the critical gap between high-level management strategy and granular execution. We help ambitious leaders build enduring businesses that dominate their industries.
      </p>
    </div>
  </div>
</section>

<!-- CORE VALUES & PHILOSOPHY -->
<section class="r-section" style="background-color: #0b0f1a; border-top: 1px solid var(--r-border);">
  <div class="r-container">
    <div style="text-align: center; max-width: 720px; margin: 0 auto 50px auto;">
      <div class="r-tag">
        <span class="r-tag-dot"></span>
        OUR PRINCIPLES
      </div>
      <h2 class="r-heading-lg">The Values That Guide Every Engagement</h2>
    </div>

    <div class="r-grid-4">
      <div class="r-card">
        <div class="r-card-icon" style="font-size: 1.3rem; width: 50px; height: 50px;">🛡️</div>
        <h4 class="r-card-title" style="font-size: 1.15rem;">Radical Accountability</h4>
        <p class="r-card-desc" style="font-size: 0.9rem;">
          We tie our pride and reputation directly to client outcomes. If a strategy doesn't yield measurable revenue or margin lift, we adapt until it does.
        </p>
      </div>

      <div class="r-card">
        <div class="r-card-icon" style="font-size: 1.3rem; width: 50px; height: 50px;">📊</div>
        <h4 class="r-card-title" style="font-size: 1.15rem;">Data Over Dogma</h4>
        <p class="r-card-desc" style="font-size: 0.9rem;">
          No cookie-cutter templates. Every insight is rigorously backed by granular unit economics, market testing, and real cohort behavioral data.
        </p>
      </div>

      <div class="r-card">
        <div class="r-card-icon" style="font-size: 1.3rem; width: 50px; height: 50px;">⚡</div>
        <h4 class="r-card-title" style="font-size: 1.15rem;">Velocity With Rigor</h4>
        <p class="r-card-desc" style="font-size: 0.9rem;">
          Speed is an unfair advantage, but only when paired with sound operational hygiene. We accelerate progress without creating technical or managerial debt.
        </p>
      </div>

      <div class="r-card">
        <div class="r-card-icon" style="font-size: 1.3rem; width: 50px; height: 50px;">🤝</div>
        <h4 class="r-card-title" style="font-size: 1.15rem;">True Partnership</h4>
        <p class="r-card-desc" style="font-size: 0.9rem;">
          We are not detached vendors. We operate as trusted thought partners and strategic confidantes to chief executives navigating high-stakes inflection points.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- LEADERSHIP TEAM SECTION -->
<section class="r-section" style="background-color: #090d16; border-top: 1px solid var(--r-border);">
  <div class="r-container">
    <div style="text-align: center; max-width: 720px; margin: 0 auto 50px auto;">
      <div class="r-tag">
        <span class="r-tag-dot"></span>
        LEADERSHIP &amp; EXPERTISE
      </div>
      <h2 class="r-heading-lg">Meet Our Senior Advisory Partners</h2>
      <p class="r-lead" style="margin: 0 auto;">
        Seasoned operators, former founders, and executive leaders with a collective track record of over $1.5B in enterprise value creation.
      </p>
    </div>

    <div class="r-grid-4">
      <!-- Member 1 -->
      <div class="r-team-card">
        <div class="r-team-header">
          <div class="r-team-avatar-lg">DV</div>
        </div>
        <div class="r-team-body">
          <h4 class="r-team-name">David Vance</h4>
          <div class="r-team-role">Managing Principal</div>
          <p class="r-team-bio">
            Former partner at Tier-1 strategy consultancy. 18+ years advising Fortune 500 boards and scaling high-velocity tech scaleups through public listings.
          </p>
        </div>
      </div>

      <!-- Member 2 -->
      <div class="r-team-card">
        <div class="r-team-header">
          <div class="r-team-avatar-lg" style="background: linear-gradient(135deg, #8b5cf6, #ec4899);">SJ</div>
        </div>
        <div class="r-team-body">
          <h4 class="r-team-name">Sarah Jenkins</h4>
          <div class="r-team-role">Head of Go-to-Market</div>
          <p class="r-team-bio">
            Architect of three unicorn enterprise revenue expansions. Renowned specialist in complex B2B sales cycles, outbound motions, and pricing power.
          </p>
        </div>
      </div>

      <!-- Member 3 -->
      <div class="r-team-card">
        <div class="r-team-header">
          <div class="r-team-avatar-lg" style="background: linear-gradient(135deg, #059669, #10b981);">AM</div>
        </div>
        <div class="r-team-body">
          <h4 class="r-team-name">Arjun Mehta</h4>
          <div class="r-team-role">Partner, AI &amp; Tech</div>
          <p class="r-team-bio">
            Former VP of Engineering and technology architect. Specializes in enterprise AI deployment, automated data infrastructure, and scalable operations.
          </p>
        </div>
      </div>

      <!-- Member 4 -->
      <div class="r-team-card">
        <div class="r-team-header">
          <div class="r-team-avatar-lg" style="background: linear-gradient(135deg, #f59e0b, #ef4444);">CD</div>
        </div>
        <div class="r-team-body">
          <h4 class="r-team-name">Claire Dubois</h4>
          <div class="r-team-role">Principal, Org Design</div>
          <p class="r-team-bio">
            Chief People Strategist and executive leadership coach. Expert in scaling executive teams, founder transitions, and performance-driven culture.
          </p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- CONTACT SECTION -->
<section id="contact" class="r-section" style="background-color: #0b0f1a; border-top: 1px solid var(--r-border);">
  <div class="r-container">
    <div class="r-grid-2" style="align-items: start; gap: 50px;">
      <!-- Contact Info Left Column -->
      <div>
        <div class="r-tag">
          <span class="r-tag-dot"></span>
          GET IN TOUCH
        </div>
        <h2 class="r-heading-lg" style="margin-bottom: 24px;">Start the Conversation</h2>
        <p class="r-lead" style="margin-bottom: 36px;">
          Whether you are preparing for a funding round, seeking to double enterprise sales velocity, or navigating operational complexity, our partners are ready to assist.
        </p>

        <div style="display: flex; flex-direction: column; gap: 20px;">
          <div style="display: flex; align-items: flex-start; gap: 16px; padding: 22px; background: rgba(15,23,42,0.6); border: 1px solid var(--r-border); border-radius: 12px; transition: border-color 0.25s ease;">
            <div style="font-size: 1.5rem;">📍</div>
            <div>
              <div style="font-family: Outfit, sans-serif; font-weight: 700; color: #ffffff; font-size: 1rem; margin-bottom: 4px;">Global Headquarters</div>
              <div style="color: var(--r-text-dim); font-size: 0.92rem;">100 Financial Center Blvd, Suite 2400, New York, NY 10005</div>
            </div>
          </div>

          <div style="display: flex; align-items: flex-start; gap: 16px; padding: 22px; background: rgba(15,23,42,0.6); border: 1px solid var(--r-border); border-radius: 12px; transition: border-color 0.25s ease;">
            <div style="font-size: 1.5rem;">✉️</div>
            <div>
              <div style="font-family: Outfit, sans-serif; font-weight: 700; color: #ffffff; font-size: 1rem; margin-bottom: 4px;">Executive Inquiries</div>
              <div style="color: #38bdf8; font-size: 0.92rem; font-weight: 500;">advisory@risegrowthgroup.com</div>
            </div>
          </div>

          <div style="display: flex; align-items: flex-start; gap: 16px; padding: 22px; background: rgba(15,23,42,0.6); border: 1px solid var(--r-border); border-radius: 12px; transition: border-color 0.25s ease;">
            <div style="font-size: 1.5rem;">📞</div>
            <div>
              <div style="font-family: Outfit, sans-serif; font-weight: 700; color: #ffffff; font-size: 1rem; margin-bottom: 4px;">Direct Desk</div>
              <div style="color: var(--r-text-dim); font-size: 0.92rem;">+1 (800) 482-9150 (Mon–Fri, 8am–6pm EST)</div>
            </div>
          </div>

          <div style="padding: 18px 22px; background: rgba(16,185,129,0.1); border: 1px solid rgba(16,185,129,0.3); border-radius: 12px; color: #6ee7b7; font-size: 0.92rem; font-weight: 500; display: flex; align-items: center; gap: 12px;">
            <span style="font-size: 1.2rem;">⏱️</span>
            <span><strong>Guaranteed SLA:</strong> Inquiries are reviewed and answered within 4 business hours.</span>
          </div>
        </div>
      </div>

      <!-- Contact Form Right Column -->
      <div class="r-contact-card">
        <h3 style="font-family: Outfit, sans-serif; font-size: 1.5rem; font-weight: 700; color: #ffffff; margin-bottom: 8px;">
          Request Strategic Consultation
        </h3>
        <p style="color: var(--r-text-dim); font-size: 0.92rem; margin-bottom: 24px;">
          Complete the form below to connect directly with a Managing Principal.
        </p>

        <form id="rise-contact-form" onsubmit="handleFormSubmit(event)">
          <div class="r-form-group">
            <label for="contact-name">Full Name *</label>
            <input type="text" id="contact-name" class="r-input" placeholder="e.g. Alexander Wright" required />
          </div>

          <div class="r-form-group">
            <label for="contact-email">Corporate Email *</label>
            <input type="email" id="contact-email" class="r-input" placeholder="alexander@company.com" required />
          </div>

          <div class="r-form-group">
            <label for="contact-company">Company Name &amp; Revenue Stage</label>
            <select id="contact-company" class="r-select">
              <option value="Under $5M ARR">Growth Stage: Under $5M ARR</option>
              <option value="$5M - $20M ARR" selected>Scale Stage: $5M - $20M ARR</option>
              <option value="$20M - $100M ARR">Expansion Stage: $20M - $100M ARR</option>
              <option value="$100M+ Enterprise">Enterprise: $100M+ Revenue</option>
            </select>
          </div>

          <div class="r-form-group">
            <label for="contact-practice">Primary Advisory Focus</label>
            <select id="contact-practice" class="r-select">
              <option value="Executive Strategy & Board Advisory">Executive Strategy &amp; Board Advisory</option>
              <option value="Revenue Architecture & GTM">Revenue Architecture &amp; Go-To-Market</option>
              <option value="Operational Excellence & Scaling">Operational Excellence &amp; Scaling</option>
              <option value="AI & Digital Transformation">AI &amp; Digital Transformation</option>
            </select>
          </div>

          <div class="r-form-group">
            <label for="contact-message">Key Strategic Challenge / Objective</label>
            <textarea id="contact-message" class="r-textarea" placeholder="Briefly describe your current growth bottleneck or upcoming milestone..." required></textarea>
          </div>

          <button type="submit" id="submit-btn" class="r-btn r-btn-primary" style="width: 100%; font-size: 1.05rem; padding: 15px;">
            Submit Consultation Request →
          </button>
        </form>

        <div id="form-success-message" style="display: none; padding: 28px; background: rgba(16,185,129,0.15); border: 1px solid rgba(16,185,129,0.4); border-radius: 12px; margin-top: 20px; text-align: center;">
          <div style="font-size: 2.2rem; margin-bottom: 8px;">🎉</div>
          <h4 style="font-family: Outfit, sans-serif; font-size: 1.3rem; font-weight: 700; color: #6ee7b7; margin-bottom: 6px;">Request Received</h4>
          <p style="color: #cbd5e1; font-size: 0.95rem; margin: 0;">
            Thank you! A Senior Partner will review your briefing and reach out within 4 business hours to schedule your strategy session.
          </p>
        </div>

        <script>
        function handleFormSubmit(e) {
          e.preventDefault();
          var btn = document.getElementById('submit-btn');
          btn.disabled = true;
          btn.innerText = 'Transmitting Request...';
          setTimeout(function() {
            document.getElementById('rise-contact-form').style.display = 'none';
            document.getElementById('form-success-message').style.display = 'block';
          }, 600);
        }
        </script>
      </div>
    </div>
  </div>
</section>
"""

# ==========================================
# 3. UPDATE PAGES VIA WP-CLI
# ==========================================
# Update Home Page
home_id = run_wp("post", "list", "--post_type=page", "--name=home", "--field=ID")
if not home_id:
    out = run_wp("post", "list", "--post_type=page", "--title=Home", "--field=ID")
    if out:
        home_id = out.split()[0]

print(f"Updating Home page (ID: {home_id})...")
with open("temp_home.html", "w", encoding="utf-8") as f:
    f.write(home_html)
run_wp("post", "update", home_id, "temp_home.html")
if os.path.exists("temp_home.html"):
    os.remove("temp_home.html")

# Update About & Contact Page
about_id = run_wp("post", "list", "--post_type=page", "--name=about-contact", "--field=ID")
if not about_id:
    out = run_wp("post", "list", "--post_type=page", "--title=About & Contact", "--field=ID")
    if out:
        about_id = out.split()[0]

print(f"Updating About & Contact page (ID: {about_id})...")
with open("temp_about.html", "w", encoding="utf-8") as f:
    f.write(about_html)
run_wp("post", "update", about_id, "temp_about.html")
if os.path.exists("temp_about.html"):
    os.remove("temp_about.html")

print("\nSUCCESS! Highly interactive consulting pages deployed!")
