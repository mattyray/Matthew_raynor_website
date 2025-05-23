# Django ChatWidget

**Django ChatWidget** is a reusable, pip-installable AI-powered chat widget for Django projects. It allows you to drop an OpenAI-powered assistant into any Django site, trained on your custom `.json` knowledge base files.

---

## 🚀 Features

* Floating chat UI that integrates with your site
* Powered by OpenAI's GPT models (configurable)
* Loads context from `.json` files you provide
* No external database dependencies required
* Works with any Django app via `{% include %}`
* MIT licensed

---

## 📦 Installation

```bash
pip install django-chatwidget
```

Add `chatwidget` to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'chatwidget',
]
```

Include the widget in your `base.html`:

```django
{% load static %}
{% include "chatwidget/widget.html" %}
```

Include the URLs in your root `urls.py`:

```python
from django.urls import include, path

urlpatterns = [
    ...
    path("chatwidget/", include("chatwidget.urls")),
]
```

---

## 🔑 Set Your OpenAI API Key

Add to your `.env` file or `settings.py`:

```bash
export OPENAI_API_KEY=your-openai-key
```

Or in `settings.py`:

```python
import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
```

---

## 🧠 How to Train the Chatbot

Add `.json` files inside `chatwidget/data/`. Each should have:

```json
[
  {
    "title": "About Us",
    "content": "We are a nonprofit organization providing support..."
  },
  {
    "title": "Contact",
    "content": "Email us at support@example.com."
  }
]
```

These files will be automatically loaded into the system prompt and used by the assistant.

---

## 🎨 Required CSS Framework

This widget uses Bootstrap 5 classes such as `form-control` and `btn`. You must include Bootstrap 5 in your base template for correct styling:

```html
<!-- Add to your base.html <head> -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
```

---

## 🧪 Example Project Setup

To test:

```bash
python manage.py runserver
```

Visit `http://localhost:8000/chatwidget/` or wherever you embed the widget.

---

## 📁 File Structure

```
chatwidget/
├── data/                  # Your custom knowledge base files
├── static/chatwidget/    # CSS & JS for chat
├── templates/chatwidget/ # Contains widget.html
├── views.py              # Handles OpenAI requests
├── urls.py               # Exposes POST endpoint
├── openai_utils.py       # Loads knowledge + handles API
```

---

## 📃 License

MIT License © 2025 Matthew Raynor

---

## 🧠 Attribution / Shout Out

Built by [Matthew Raynor](https://www.matthewraynor.com), a quadriplegic full-stack developer turning his creativity into independence — follow for more tools that empower and inspire.