// ── Newsletter subscription (contact page) ───────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
    const btn = document.getElementById('nl-btn');
    const msg = document.getElementById('nl-msg');
    if (!btn) return;

    btn.addEventListener('click', async () => {
        const email = document.getElementById('nl-email').value.trim();
        if (!email) {
            msg.style.color = '#f87171';
            msg.textContent = 'Please enter your email address.';
            return;
        }

        btn.disabled = true;
        btn.textContent = '…';

        try {
            const res  = await fetch('/api/newsletter', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email })
            });
            const data = await res.json();

            msg.style.color = data.ok ? 'var(--gold-light)' : '#f87171';
            msg.textContent = data.msg;
            if (data.ok) document.getElementById('nl-email').value = '';
        } catch {
            msg.style.color = '#f87171';
            msg.textContent = 'Something went wrong. Please try again.';
        } finally {
            btn.disabled = false;
            btn.textContent = 'Subscribe';
        }
    });
});
