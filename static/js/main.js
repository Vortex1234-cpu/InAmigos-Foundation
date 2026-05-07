// ── Scroll reveal ────────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
    const els = document.querySelectorAll('.reveal');
    const observer = new IntersectionObserver(
        (entries) => entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); }),
        { threshold: 0.12 }
    );
    els.forEach(el => observer.observe(el));

    // Auto-dismiss flash messages after 4 s
    document.querySelectorAll('.flash').forEach(el => {
        setTimeout(() => { el.style.opacity = '0'; setTimeout(() => el.remove(), 400); }, 4000);
    });
});
