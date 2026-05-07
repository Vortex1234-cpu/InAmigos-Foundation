// ── Volunteer quick-sign-up (home page) ──────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
    const btn = document.getElementById('vf-submit');
    const msg = document.getElementById('vf-msg');
    if (!btn) return;

    btn.addEventListener('click', async () => {
        const name     = document.getElementById('vf-name').value.trim();
        const email    = document.getElementById('vf-email').value.trim();
        const phone    = document.getElementById('vf-phone').value.trim();
        const city     = document.getElementById('vf-city').value.trim();
        const interest = document.getElementById('vf-interest').value.trim();

        if (!name || !email) {
            msg.style.color = '#f87171';
            msg.textContent = 'Please enter your name and email.';
            return;
        }

        btn.disabled = true;
        btn.textContent = 'Submitting…';

        try {
            const res  = await fetch('/api/volunteer', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ name, email, phone, city, interest })
            });
            const data = await res.json();

            if (data.ok) {
                msg.style.color = 'var(--gold-light)';
                msg.textContent = data.msg;
                ['vf-name','vf-email','vf-phone','vf-city'].forEach(id => {
                    document.getElementById(id).value = '';
                });
                document.getElementById('vf-interest').value = '';
            } else {
                msg.style.color = '#f87171';
                msg.textContent = data.msg;
            }
        } catch {
            msg.style.color = '#f87171';
            msg.textContent = 'Something went wrong. Please try again.';
        } finally {
            btn.disabled = false;
            btn.textContent = '🤝 Join as Volunteer';
        }
    });
});
