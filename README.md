# MatthewRaynor.com

![CI](https://github.com/mattyray/matthew_raynor_website/actions/workflows/ci.yml/badge.svg)

A personal full-stack web platform for Matthew Raynor — a quadriplegic self-taught developer, artist, and motivational creator — featuring a blog, portfolio, online store, press hub, and AI chatbot.

## 🧠 Project Purpose

This website showcases:
- Inspirational blog posts and Substack content
- A portfolio of Django and React projects
- An online store for artwork and Matthew's book
- Press/media features
- A motivational AI-powered chatbot
- Accessible UX for users with disabilities

## ⚙️ Tech Stack

**Backend**: Django 5.1.6, PostgreSQL, Docker, Gunicorn  
**Frontend**: Bootstrap 5, SCSS, ScrollReveal  
**Features**: Google SSO, Stripe Checkout, Cloudinary image hosting, Whitenoise, reCAPTCHA  
**Deployment**: Heroku with Docker  
**CI/CD**: GitHub Actions

## 🚀 Installation (Dev)

```bash
# Clone the repo
git clone https://github.com/mattyray/matthew_raynor_website.git
cd matthew_raynor_website

# Copy and edit .env file
cp .env.example .env  # (You’ll need to manually add real keys)

# Run Docker
docker-compose up --build

App will be available at http://localhost:8001

# Enter web container
docker-compose exec web bash

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput

docker-compose exec web python manage.py test

#deploy

heroku container:login
heroku container:push web --app matthew-raynor-site
heroku container:release web --app matthew-raynor-site

Created by Matthew Raynor
GitHub: @mattyray
Email: mnraynor90@gmail.com