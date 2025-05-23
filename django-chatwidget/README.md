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

To teach your AI assistant custom knowledge:

- Place `.json` files inside `chatwidget/data/`
- Each should be a list or dict with a `title` and `content`
- These are automatically loaded at server start

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

🧠 These become part of the assistant’s context. Ask things like:

- “Who is Matt Raynor?”
- “How do I install this chatbot?”
- “Tell me about Matt’s portfolio.”

---

## 🧪 Example Project Setup

To test:

```bash
python manage.py runserver
```

Then visit:

```txt
http://localhost:8000/test-chatwidget/
```

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
