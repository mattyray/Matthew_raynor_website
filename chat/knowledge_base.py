# chat/knowledge_base.py

KNOWLEDGE_BASE = """
About Matthew:
- Matthew Raynor is an AI Engineer & Full-Stack Developer with 3 years of experience building production applications.
- He has four live production apps deployed and six projects in his portfolio.
- He's a freelance developer based in Hampton Bays, NY, actively seeking a full-time remote role.
- Former commercial fisherman from Long Island who rebuilt his life through code and creativity after a spinal cord injury.
- He builds better than most — and his portfolio proves it.

What He Builds:
- Agentic AI systems with LangChain, LangGraph, and Claude
- Computer vision pipelines with TensorFlow.js, MediaPipe, and OpenCV
- Full-stack platforms with React, TypeScript, Next.js, and Django
- Desktop applications with Rust, Tauri, and FFmpeg
- Real-time systems with Django Channels and WebSocket
- Production AI agents with tool use, SSE streaming, and observability via LangSmith

Tech Stack:
- AI/ML: LangChain, LangGraph, Claude API, GPT-4, TensorFlow.js, MediaPipe, OpenCV, MiDaS, pgvector, CLIP embeddings, Ollama, Llama 3.2
- Backend: Python, Django 5.x, Django REST Framework, Django Channels, Celery, PostgreSQL, Redis, Rust
- Frontend: React 19, TypeScript, Next.js 15/16, Vite, Tailwind CSS, TanStack Query, Tauri
- Infrastructure: AWS (S3, SES, SNS), Docker, Fly.io, Railway, Heroku, Netlify, Vercel, Sentry

=== LIVE PRODUCTION PROJECTS ===

ToteTaxi (totetaxi.com):
- Full-stack luxury delivery and mini-moving platform serving Manhattan to Hamptons, South Florida to NYC airports, and the NYC tri-state area.
- Tech: Django 5.2, DRF, Next.js 16, React 19, TypeScript, Stripe, Onfleet, LangGraph, Claude API, Google Places API, AWS SES/S3, Fly.io, Netlify.
- Handles four service types: Mini Moves (tiered packages), Standard Delivery, Specialty Items, and Airport Transfers.
- Sophisticated dynamic pricing engine with geographic surcharges, weekend/peak premiums, same-day restrictions, and promotional discount codes.
- AI-powered customer service assistant built with LangGraph and Claude, streamed via Server-Sent Events. The agent has 6 tools: ZIP code coverage, real-time pricing, date availability, authenticated booking lookups, and hand-off to booking wizard with up to 22 pre-filled parameters.
- Dual authentication (httpOnly cookies for desktop, session fallback for mobile). Separate customer and staff portals with role-based access.
- Onfleet driver dispatch with real-time webhook status tracking. Stripe payment processing with atomic booking creation. Automated email confirmations with calendar invites.
- Backend runs on Fly.io with gevent workers for concurrent SSE streaming alongside standard API traffic.
- 310+ backend tests via pytest, Playwright E2E tests, full security audit covering payment flow hardening, input validation, rate limiting, and LLM-specific attack surface analysis.

Matthew Raynor Photography Store (store.matthewraynor.com):
- Full e-commerce platform for fine art photography targeting the Hamptons luxury art market.
- Tech: Django 5, DRF, Next.js 15, TypeScript, Tailwind CSS, LangChain, Claude API, pgvector, MiDaS, Stripe Checkout, Celery, Redis, AWS S3, Resend, MailerLite, Railway, Netlify, Sentry.
- Sells archival paper prints, dye-sublimated aluminum prints, a photography book, and gift cards with Stripe Checkout, gift card redemption, and promotional codes.
- AI-powered shopping assistant built with LangChain and Claude, streamed via SSE. Agent searches photos semantically using pgvector embeddings, manages carts, filters by color/mood/subject, checks gift card balances, and answers questions about sizing and materials.
- Photo embeddings generated with OpenAI text-embedding-ada-002, stored in PostgreSQL with pgvector for cosine similarity search. Claude Vision auto-generates all photo metadata.
- "See It In Room" feature: MiDaS depth estimation + RANSAC plane-fitting composites prints at correct scale on customer-uploaded wall photos.
- Session-based cart persistence with cross-origin cookie handling, honeypot spam protection, automated order emails via Resend, dark mode support, and optimized S3 image loading.
- Next.js App Router with server-side rendering, separating server components (internal API) from client components (public API).

IDP EasyCapture (built for IDP Americas):
- Enterprise computer vision pipeline for real-time photo validation, background compositing, and auto-capture.
- Tech: TensorFlow.js, MediaPipe, OpenCV, React, TypeScript, Tailwind CSS, Django REST Framework, Celery, Redis, AWS S3/SES, Docker, Fly.io, Netlify.
- Live camera preview with positioning guides. On-device face detection (BlazeFace), lighting analysis, and blur detection — all in-browser with zero server round-trips.
- Dynamic backgrounds: solid colors, professional blur effects, and custom images via OpenCV server-side compositing.
- Role-based multi-tenant architecture for enterprise organizations. Configurable rules per job/use case. Async exports and cleanups via Celery + Redis.
- Transforms traditional photo booth workflows into AI-driven smartphone-based capture for enterprise badge systems.
- ASURE ID compatible exports for enterprise badge printing.

Eric Art Mover (ericartmover.net):
- Operations platform for a fine art logistics business serving NYC and the Hamptons.
- Tech: Django, PostgreSQL, Heroku, Docker, Cloudinary, WeasyPrint.
- Calendar scheduling with FullCalendar, dynamic AJAX invoice creation from work orders, PDF invoice generation, and centralized client/job management.
- Digitized manual scheduling and invoicing workflows for a real business.

=== ADDITIONAL PORTFOLIO PROJECTS ===

SkyClip — AI Video Editor:
- Desktop application for automated drone footage analysis and highlight reel generation.
- Tech: Rust, Tauri, React, TypeScript, OpenCV, CLIP embeddings, Claude API, FFmpeg.
- Analyzes drone video footage using CLIP embeddings for semantic scene understanding and Claude API for intelligent clip selection.
- OpenCV handles frame extraction and video processing; FFmpeg powers the final highlight reel compilation.
- Built as a native desktop app with Tauri (Rust backend) and React/TypeScript frontend for fast, local processing without cloud dependencies.
- Demonstrates Matt's range — from web platforms to native desktop apps, from Python to Rust.

Matty's Crew — Care Team Scheduler:
- Real-time care team scheduling and coordination platform.
- Tech: Django, Django Channels, WebSocket, PostgreSQL, JWT authentication, AWS SES/SNS, multi-view calendar.
- Live WebSocket updates for real-time schedule changes and notifications across the care team.
- Multi-view calendar (day/week/month) for managing shifts and appointments.
- JWT-based authentication for secure access across team members.
- AWS SES for email notifications and SNS for push notifications when schedules change.
- Built to solve a real problem — coordinating care teams efficiently with instant communication.

Drone Photography & Art:
- Matt is a drone and seascape photographer selling fine art aluminum prints at store.matthewraynor.com.
- The store features a live AI shopping assistant — try it out!
- Custom drone photography available for real estate, landscapes, art installations, and events.

How to Connect:
- Hire Matt for freelance AI engineering or web development
- Connect him with full-time remote opportunities
- Check out his portfolio at matthewraynor.com
- Try his AI shopping assistant at store.matthewraynor.com
- Visit the Contact page to get in touch

Using the Website:
- Visit the Portfolio to see his production projects with video walkthroughs
- Visit the Store to browse art and try the AI shopping assistant
- Use the Contact form for questions or project inquiries
- The blog contains reflections, updates, and inspirational writing

AI Assistant:
- This assistant helps answer questions about Matt's work, projects, technical skills, art, and how to hire him.
- Lead with what Matt builds — he's a builder, and the work speaks for itself.
- When asked about projects, give detailed technical answers — Matt's work is impressive and deserves the full picture.
"""
