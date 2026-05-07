# InAmigos Foundation — Web App

## Project Structure

```
inamigos/
├── app.py                  ← Flask app & routes
├── database/
│   ├── __init__.py
│   └── db.py               ← SQLite helpers (init, CRUD)
├── templates/
│   ├── base.html           ← Shared nav, footer, flash messages
│   ├── index.html          ← Home page
│   └── contact.html        ← Contact page
└── static/
    ├── css/
    │   ├── main.css        ← Shared styles (nav, hero, sections)
    │   └── contact.css     ← Contact page styles
    └── js/
        ├── main.js         ← Scroll reveal + flash auto-dismiss
        ├── volunteer.js    ← Volunteer form (home page)
        └── contact.js      ← Newsletter subscribe (contact page)
```

## Setup & Run

```bash
pip install flask
python app.py
```

Open http://localhost:5000

## Database

SQLite file is created automatically at `database/inamigos.db` on first run.

### Tables
| Table        | Fields |
|---|---|
| `contacts`   | id, name, email, phone, subject, message, created_at |
| `volunteers` | id, name, email, phone, city, interest, created_at |
| `newsletter` | id, email, subscribed_at |

## API Endpoints

| Method | Route             | Description              |
|--------|-------------------|--------------------------|
| GET    | /                 | Home page                |
| GET    | /contact          | Contact page             |
| POST   | /contact          | Submit contact form      |
| POST   | /api/volunteer    | Register volunteer (JSON)|
| POST   | /api/newsletter   | Subscribe to newsletter  |
