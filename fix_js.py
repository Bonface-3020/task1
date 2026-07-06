import os

html_files = ['index.html', 'what-we-do.html', 'solutions.html', 'portfolio.html', 'accountability.html', 'mission.html']

for file in html_files:
    if not os.path.exists(file):
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace JS hero buttons scroll with simple navigation
    # Or just wrap in if checks
    js_to_replace = """    /* ─── HERO BUTTON SCROLL ─── */
    document.getElementById('heroExploreBrn').addEventListener('click', () => {
      document.getElementById('solutions').scrollIntoView({ behavior: 'smooth' });
    });
    document.getElementById('heroPortfolioBtn').addEventListener('click', () => {
      document.getElementById('portfolio').scrollIntoView({ behavior: 'smooth' });
    });"""
    
    replacement = """    /* ─── HERO BUTTON SCROLL ─── */
    const heroExploreBtn = document.getElementById('heroExploreBrn');
    const heroPortfolioBtn = document.getElementById('heroPortfolioBtn');
    if (heroExploreBtn) heroExploreBtn.addEventListener('click', () => window.location.href = 'solutions.html');
    if (heroPortfolioBtn) heroPortfolioBtn.addEventListener('click', () => window.location.href = 'portfolio.html');
"""
    
    # Also link the CTA buttons (Partner with us)
    # The nav has: <button class="nav-cta" id="navCtaBtn">Partner With Us</button>
    # The mobile menu has: <button class="mobile-menu-cta" onclick="closeMobileMenu()">Partner With Us</button>
    # CTA section has: <button class="btn-white" id="ctaPartnerBtn">Partner With Us</button>
    # We should add JS to scroll to CTA if it's on the same page, or go to index.html#contact if not. But CTA is on ALL pages!
    # Let's add JS for navCtaBtn to scroll to contact.
    
    nav_cta_js = """    /* ─── CTA SCROLL ─── */
    const navCtaBtn = document.getElementById('navCtaBtn');
    if (navCtaBtn) navCtaBtn.addEventListener('click', () => {
      const contactSec = document.getElementById('contact');
      if (contactSec) contactSec.scrollIntoView({ behavior: 'smooth' });
      else window.location.href = 'index.html#contact';
    });"""
    
    replacement = replacement + "\n" + nav_cta_js
    
    content = content.replace(js_to_replace, replacement)
    
    # The mobile menu CTA button
    content = content.replace('<button class="mobile-menu-cta" onclick="closeMobileMenu()">Partner With Us</button>', '<button class="mobile-menu-cta" onclick="closeMobileMenu(); document.getElementById(\'contact\').scrollIntoView({ behavior: \'smooth\' });">Partner With Us</button>')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("JS updated successfully in all files.")
