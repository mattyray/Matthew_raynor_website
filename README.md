# MatthewRaynor.com

![CI](https://github.com/mattyray/matthew_raynor_website/actions/workflows/ci.yml/badge.svg)

Personal website and platform for Matthew Raynor — AI Engineer & Full-Stack Developer. Built with Django, PostgreSQL, and Docker.

**Live site:** [matthewraynor.com](https://matthewraynor.com)

## Features

- **Blog** — Posts and Substack content
- **Portfolio** — Project showcases with detail pages
- **Store** — Stripe-powered checkout for artwork and books
- **Press** — Media features and coverage
- **AI Chatbot** — OpenAI-powered conversational widget
- **Google SSO** — Social login via django-allauth
- **Contact Form** — reCAPTCHA-protected with email notifications

## Tech Stack

| Layer | Tools |
|---|---|
| Backend | Django 5.1, Python 3.10, Gunicorn |
| Database | PostgreSQL 15 |
| Frontend | Bootstrap 5, SCSS, ScrollReveal |
| Media | Cloudinary, Whitenoise (static) |
| Payments | Stripe Checkout |
| Auth | django-allauth (Google SSO) |
| Infrastructure | Docker, Heroku |
| CI/CD | GitHub Actions (pytest) |

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
├── static/            # Static assets (CSS, JS, images)
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Local Development Setup

### Prerequisites

- Docker & Docker Compose
- Git

### 1. Clone and configure

```bash
git clone https://github.com/mattyray/matthew_raynor_website.git
cd matthew_raynor_website
cp .env.example .env
```

Edit `.env` and fill in your API keys (OpenAI, Stripe, Cloudinary, Google OAuth, reCAPTCHA, Gmail SMTP).

### 2. Build and run

```bash
docker-compose up --build
```

The app will be available at **http://localhost:8001**.

### 3. Initialize the database

In a separate terminal:

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --noinput
```

Admin panel: http://localhost:8001/admin/

## Running Tests

```bash
# Inside Docker
docker-compose exec web pytest

# Or locally with dev dependencies
pip install -r requirements-dev.txt
pytest
```

CI runs automatically on push to `main` or `feature/**` branches via GitHub Actions.

## Dev Dependencies

The `requirements-dev.txt` includes:

- **pytest** / **pytest-django** — Test runner
- **flake8** / **flake8-bandit** — Linting & security checks
- **mypy** — Type checking
- **safety** — Dependency vulnerability scanning

## Deployment

Deployed to Heroku via Docker container:

```bash
heroku container:login
heroku container:push web --app matthew-raynor-site
heroku container:release web --app matthew-raynor-site
```

Production uses `django_project.settings.prod` with `DJANGO_SETTINGS_MODULE` set in Heroku config vars.

## Environment Variables

See [.env.example](.env.example) for all required variables. Key services that need configuration:

| Variable | Service | Required |
|---|---|---|
| `OPENAI_API_KEY` | AI Chatbot | Yes |
| `STRIPE_*` | Store checkout | Yes (use test keys for dev) |
| `CLOUDINARY_URL` | Image hosting | Yes |
| `RECAPTCHA_*` | Contact form spam protection | Yes |
| `GOOGLE_CLIENT_*` | Google SSO login | Optional |
| `EMAIL_HOST_*` | Contact form email delivery | Optional (falls back to console) |

## Contributing

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes and add tests
4. Run `pytest` and `flake8` to verify
5. Open a PR against `main`

---

Created by Matthew Raynor
GitHub: [@mattyray](https://github.com/mattyray)
Email: mnraynor90@gmail.com
