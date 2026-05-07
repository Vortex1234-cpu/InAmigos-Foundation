from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sys, os

sys.path.insert(0, os.path.dirname(__file__))
from database.db import init_db, save_contact, save_volunteer, save_newsletter

app = Flask(__name__)
app.secret_key = "inamigos-secret-key-change-in-production"


# ── Pages ─────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name    = request.form.get("name", "").strip()
        email   = request.form.get("email", "").strip()
        phone   = request.form.get("phone", "").strip()
        subject = request.form.get("subject", "").strip()
        message = request.form.get("message", "").strip()

        if not all([name, email, subject, message]):
            flash("Please fill in all required fields.", "error")
            return redirect(url_for("contact"))

        save_contact(name, email, phone, subject, message)
        flash("Thank you! We'll get back to you soon. 🌱", "success")
        return redirect(url_for("contact"))

    return render_template("contact.html")


# ── API endpoints (used by JS forms) ─────────────────────────────────────────

@app.route("/api/volunteer", methods=["POST"])
def api_volunteer():
    data = request.get_json(force=True)
    name     = data.get("name", "").strip()
    email    = data.get("email", "").strip()
    phone    = data.get("phone", "").strip()
    city     = data.get("city", "").strip()
    interest = data.get("interest", "").strip()

    if not all([name, email]):
        return jsonify({"ok": False, "msg": "Name and email are required."}), 400

    save_volunteer(name, email, phone, city, interest)
    return jsonify({"ok": True, "msg": "Welcome aboard, Amigo! 🤝"})


@app.route("/api/newsletter", methods=["POST"])
def api_newsletter():
    data  = request.get_json(force=True)
    email = data.get("email", "").strip()
    if not email:
        return jsonify({"ok": False, "msg": "Email required."}), 400

    added = save_newsletter(email)
    if added:
        return jsonify({"ok": True, "msg": "Subscribed! Thanks for joining. 💛"})
    return jsonify({"ok": False, "msg": "You're already subscribed!"}), 409


# ── Bootstrap ─────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5000)
