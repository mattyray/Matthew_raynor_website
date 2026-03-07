# MatthewRaynor.com

![CI](https://github.com/mattyray/matthew_raynor_website/actions/workflows/ci.yml/badge.svg)

Personal website and platform for Matthew Raynor — AI Engineer & Full-Stack Developer. Built with Django, PostgreSQL, and Docker. Deployed on Heroku.

**Live site:** [matthewraynor.com](https://matthewraynor.com)

## What It Does

- **Blog** — Original posts and Substack content
- **Portfolio** — Project showcases with detail pages
- **Store** — Stripe-powered checkout for artwork and books
- **Press** — Media features and coverage
- **AI Chatbot** — OpenAI-powered conversational widget
- **Contact Form** — reCAPTCHA-protected with email notifications
- **Google SSO** — Social login via django-allauth

## Tech Stack

| Layer | Tools |
|---|---|
| Backend | Django 5.1, Python 3.10, Gunicorn |
| Database | PostgreSQL 15 |
| Frontend | Bootstrap 5, SCSS, ScrollReveal |
| Media | Cloudinary, Whitenoise (static files) |
| Payments | Stripe Checkout |
| Auth | django-allauth (Google SSO) |
| Infrastructure | Docker, Heroku |
| CI/CD | GitHub Actions (pytest, flake8, mypy) |

## Project Structure

```
matthew_raynor_website/
├── accounts/          # User auth & profiles
├── blog/              # Blog app
├── chat/              # AI chatbot backend
├── django-chatwidget/ # Chat widget package
├── pages/             # Static pages (home, story, contact, press)
├── portfolio/         # Portfolio app
├── search/            # Site search
├── store/             # E-commerce / Stripe
├── django_project/
│   └── settings/
│       ├── base.py    # Shared settings
│       ├── dev.py     # Local development
│       ├── prod.py    # Production (Heroku)
│       └── test.py    # CI test settings
├── templates/         # Global templates
├── static/            # Static assets
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

Created by Matthew Raynor
GitHub: [@mattyray](https://github.com/mattyray)
Email: mnraynor90@gmail.com
