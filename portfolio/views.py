from django.views.generic import TemplateView
from django.http import Http404


SERVICES = [
    {
        "icon": "fas fa-globe",
        "title": "Websites",
        "headline": "Get your business online. Clean, fast, mobile-friendly sites that show up on Google.",
        "tech": "WordPress, custom builds, SEO, responsive design",
    },
    {
        "icon": "fas fa-cogs",
        "title": "Web Applications",
        "headline": "Replace the chaos. Booking systems, job management, dashboards \u2014 built around how your business actually works.",
        "tech": "Django, React, Next.js, TypeScript, PostgreSQL",
    },
    {
        "icon": "fas fa-shopping-cart",
        "title": "E-Commerce",
        "headline": "Sell online. Products, services, gift cards, subscriptions \u2014 with real payment processing.",
        "tech": "Stripe integration, inventory, order management",
    },
    {
        "icon": "fas fa-robot",
        "title": "AI Integrations",
        "headline": "Add a smart assistant to your site, automate repetitive tasks, or build AI into your workflow.",
        "tech": "Claude, LangChain, LangGraph, OpenAI, vector search, computer vision",
    },
    {
        "icon": "fas fa-wrench",
        "title": "Consulting & Maintenance",
        "headline": "Already have something that\u2019s broken, slow, or outdated? I\u2019ll fix it, upgrade it, or rebuild it.",
        "tech": "Code audits, performance, security, migrations",
    },
]

PROJECTS = [
    {
        "title": "ToteTaxi",
        "slug": "totetaxi",
        "featured": True,
        "hero_video": "https://youtu.be/PXJ540ZxxuY",
        "case_problem": "Customers had to call for quotes and couldn't book online.",
        "case_built": "Full booking platform with AI-powered customer service, online payments, and driver dispatch.",
        "case_result": "Live at totetaxi.com — processing real bookings across Long Island and NYC.",
        "description": (
            "Booking and logistics platform for a luxury transport company on Long Island. "
            "Customers book through a step-by-step wizard, pay online, and get automated confirmations. "
            "Staff manage bookings, dispatch drivers, and track revenue from a dashboard. "
            "An AI chat assistant answers customer questions about services and pricing in real time."
        ),
        "tech_line": "Django REST Framework \u00b7 Next.js \u00b7 React \u00b7 TypeScript \u00b7 Stripe \u00b7 Onfleet \u00b7 LangGraph + Claude \u00b7 Celery \u00b7 PostgreSQL \u00b7 Redis \u00b7 Sentry \u00b7 LangSmith \u00b7 Fly.io \u00b7 Netlify",
        "live_url": "https://totetaxi.com",
        "github_url": "https://github.com/mattyray/totetaxi",
        "overview": (
            "ToteTaxi is a production logistics platform serving Manhattan to Hamptons, South Florida to NYC airports, and the NYC tri-state area. "
            "It handles four service types \u2014 Mini Moves (tiered packages), Standard Delivery, Specialty Items, and Airport Transfers \u2014 with a sophisticated "
            "dynamic pricing engine that accounts for geographic surcharges, weekend/peak premiums, same-day restrictions, and promotional discount codes."
        ),
        "tech_stack": {
            "backend": ["Django 5.2", "Django REST Framework", "PostgreSQL", "Redis", "Celery"],
            "frontend": ["Next.js 16", "React 19", "TypeScript"],
            "ai": ["LangGraph", "Claude API", "LangSmith"],
            "integrations": ["Stripe", "Onfleet", "Google Places API", "AWS SES/S3"],
            "deployment": ["Fly.io (gevent workers)", "Netlify"],
        },
        "problem": (
            "A luxury delivery business needed a complete platform \u2014 booking, pricing, payment, dispatch, customer service \u2014 "
            "that could handle complex logistics across multiple service areas and service types."
        ),
        "solution": (
            "Built a full-stack platform with an AI customer service agent (LangGraph + Claude, 6 tools, SSE streaming), "
            "dynamic pricing engine, Stripe payment processing with atomic booking creation, Onfleet driver dispatch with "
            "real-time webhook tracking, and separate customer/staff portals with role-based access."
        ),
        "special_features": [
            "AI agent with 6 tools: ZIP coverage, real-time pricing, date availability, booking lookups, hand-off to booking wizard with up to 22 pre-filled parameters",
            "Dynamic pricing engine with geographic surcharges, weekend premiums, same-day restrictions, and promo codes",
            "Dual authentication \u2014 httpOnly cookies for desktop, session fallback for mobile",
            "Onfleet driver dispatch with real-time webhook status tracking",
            "Stripe payment processing with atomic booking creation",
            "Automated email confirmations with calendar invites",
            "310+ backend tests via pytest, Playwright E2E tests",
        ],
        "problems_solved": [
            "Complex multi-zone pricing with dynamic surcharges and restrictions",
            "AI agent that accurately routes services, validates dates, and pre-fills booking forms",
            "Concurrent SSE streaming alongside standard API traffic via gevent workers",
            "Auth-scoped tool binding preventing LLM data access violations",
        ],
        "proud_of": [
            "Production LangGraph agent with adversarial-tested system prompt",
            "Full security audit covering payment hardening, rate limiting, and LLM attack surface",
            "310+ tests and Playwright E2E coverage",
            "Gevent worker architecture for concurrent SSE + API traffic",
        ],
        "build_notes": (
            "<p>Built with Django 5.2 and Next.js 16. The AI agent uses LangGraph's ReAct pattern with Claude, streamed via SSE. "
            "The system prompt was iteratively refined through adversarial testing. Auth-scoped tool binding enforces data access "
            "boundaries at the code level. LangSmith provides full observability into agent behavior in production. "
            "Backend runs on Fly.io with gevent workers for concurrent streaming.</p>"
        ),
    },
    {
        "title": "RepoRadar",
        "slug": "reporadar",
        "featured": True,
        "case_problem": "Job searching on LinkedIn is broken — ghost jobs, black-hole applications, no signal.",
        "case_built": "A tool that scans GitHub to find companies using your tech stack, scores them, and finds open roles.",
        "case_result": "Live tool used by developers to find companies that actually build with their tools.",
        "description": (
            "Job search tool that scans GitHub to find companies building with specific tech stacks. "
            "Instead of applying to LinkedIn ghost jobs, search for companies that use the same tools you do "
            "by reading their dependency files, then reach out directly. Scores prospects 0\u2013100 based on "
            "stack match, AI tool signals, and activity. Automatically checks Greenhouse, Lever, Ashby, and Workable for open roles."
        ),
        "tech_line": "Django REST Framework \u00b7 React \u00b7 TypeScript \u00b7 Celery \u00b7 Redis \u00b7 PostgreSQL \u00b7 Claude API \u00b7 GitHub API \u00b7 Hunter.io \u00b7 Apollo.io \u00b7 Railway \u00b7 Netlify",
        "live_url": "https://reporadar-app.netlify.app",
        "github_url": None,
        "overview": (
            "RepoRadar flips job searching on its head. Instead of 'find jobs, then figure out if the company matches,' "
            "it's 'find companies that build like you build, then reach out directly.' It scans GitHub for requirements.txt, "
            "package.json, CLAUDE.md and other dependency files, detects tech stacks across 200+ known packages, scores prospects, "
            "probes ATS job boards, and generates AI-powered personalized outreach."
        ),
        "tech_stack": {
            "backend": ["Django 5", "Django REST Framework", "PostgreSQL 16", "Redis", "Celery"],
            "frontend": ["React 19", "TypeScript", "Vite", "Tailwind CSS", "TanStack Query"],
            "ai": ["Claude API (resume parsing, outreach generation)"],
            "integrations": ["GitHub REST API v3", "Hunter.io", "Apollo.io", "Greenhouse", "Lever", "Ashby", "Workable"],
            "deployment": ["Railway", "Netlify"],
        },
        "problem": (
            "Job searching on LinkedIn is broken. Posts are stale, ghost jobs are everywhere, and applications "
            "disappear into a black hole. But there's a signal nobody's using: GitHub."
        ),
        "solution": (
            "Built a tool that scans GitHub to find companies using the same tech stack you do, scores them 0-100, "
            "checks their ATS job boards for open roles, and generates personalized outreach using Claude AI."
        ),
        "special_features": [
            "GitHub code search scanning requirements.txt, package.json, CLAUDE.md, and more",
            "Stack detection across 200+ known packages in Python and JavaScript ecosystems",
            "Prospect scoring 0-100 based on stack match, AI tool signals, production readiness, and activity",
            "ATS job probing across Greenhouse, Lever, Ashby, and Workable \u2014 no API keys needed",
            "Contact enrichment via Hunter.io and Apollo.io (BYOK model)",
            "AI-powered outreach generation using resume + prospect data via Claude",
            "Provider adapter pattern \u2014 external APIs abstracted behind mockable interfaces",
            "132 tests passing across 13 test files",
        ],
        "problems_solved": [
            "Finds companies building with your exact tech stack using public GitHub data",
            "Eliminates ghost job applications by connecting directly to real engineering teams",
            "Caches all external API responses (24hr-30day TTLs) to minimize rate limit consumption",
            "BYOK model means free tier costs nothing to run",
        ],
        "proud_of": [
            "Provider adapter architecture that makes the system provider-agnostic",
            "Auth design separating identity (Google OAuth) from data access (GitHub OAuth) from paid services (BYOK)",
            "Caching layer that makes the database grow organically as users scan",
            "132 tests with TDD as the standard",
        ],
        "build_notes": (
            "<p>7 Django apps with clean separation of concerns. External APIs abstracted behind provider adapters \u2014 "
            "views and tasks receive provider instances; tests inject mocks. Identity separated from data access: "
            "Google OAuth for login, GitHub OAuth for API access, Hunter/Apollo as BYOK. "
            "All multi-step workflows run as Celery tasks with frontend polling via TanStack Query.</p>"
        ),
    },
    {
        "title": "IDP EasyCapture",
        "slug": "idp-easycapture",
        "featured": True,
        "hero_video": "https://youtu.be/4g5zsY9exVw",
        "case_problem": "Organizations needed consistent ID photos at scale without hauling photo booth setups on-site.",
        "case_built": "Enterprise SaaS with AI-powered photo capture from any smartphone — face detection, background replacement, badge-ready exports.",
        "case_result": "Live enterprise platform built under contract for IDP Americas (2024–2025).",
        "description": (
            "Enterprise ID photo management platform that replaces traditional photo booth setups. "
            "Organizations collecting employee or student photos at scale use it to capture, validate, and process photos "
            "entirely from a smartphone. TensorFlow.js runs real-time face detection in the browser to ensure quality before "
            "the shot is taken. A server-side ML pipeline handles background compositing \u2014 blur, solid colors, or custom images \u2014 "
            "using MediaPipe segmentation and OpenCV. Exports in ASURE ID-compatible formats for enterprise badge printing."
        ),
        "tech_line": "Django REST Framework \u00b7 React \u00b7 TypeScript \u00b7 TensorFlow.js \u00b7 BlazeFace \u00b7 MediaPipe \u00b7 OpenCV \u00b7 AWS S3 \u00b7 Celery \u00b7 Multi-tenant SaaS \u00b7 Fly.io \u00b7 Netlify",
        "live_url": "https://idpeasycapture.com",
        "login_only": True,
        "github_url": None,
        "overview": (
            "EasyCapture is an enterprise ID photo management SaaS platform built for IDP Americas (contract, 2024\u20132025). "
            "It replaces traditional photo booth setups with an AI-driven, smartphone-based capture workflow. "
            "Organizations collecting employee or student photos at scale \u2014 for badges, credentials, access cards \u2014 "
            "use it to handle everything from capture to ASURE ID-compatible export."
        ),
        "tech_stack": {
            "backend": ["Django 5.1.6", "Django REST Framework", "PostgreSQL", "Celery", "Redis"],
            "frontend": ["React 19", "TypeScript", "Vite", "Tailwind CSS", "TanStack Query"],
            "ai_ml": ["TensorFlow.js (BlazeFace)", "MediaPipe 0.10.18", "OpenCV 4.10", "NumPy", "Pillow"],
            "cloud": ["AWS S3", "AWS SES"],
            "deployment": ["Docker", "Fly.io", "Netlify"],
        },
        "problem": (
            "Organizations need consistent, high-quality ID photos captured quickly with instant feedback \u2014 "
            "without manual review bottlenecks or hauling photo booth setups on-site."
        ),
        "solution": (
            "Built a browser-first pipeline: TensorFlow.js runs real-time face detection with configurable quality thresholds "
            "(blur tolerance, lighting, face confidence). A server-side MediaPipe + OpenCV pipeline handles background compositing "
            "with dual-model segmentation for fine hair detail. Multi-tenant SaaS with role-based access and dynamic form systems."
        ),
        "special_features": [
            "Client-side ML: TensorFlow.js BlazeFace for real-time face detection with auto-capture countdown",
            "Configurable quality thresholds: blur tolerance, lighting brightness, face detection confidence",
            "Server-side dual-model MediaPipe segmentation \u2014 portrait model for hair detail, general model for structure",
            "Background compositing: blur, solid colors (8 options), or custom uploaded images with LANCZOS resampling",
            "Multi-tenant SaaS with role-based access (super_admin vs regular users)",
            "Dynamic form system with 90+ field templates across 9 categories",
            "ASURE ID-compatible exports (CSV + ZIP) with presigned S3 download URLs",
            "Admin review workflow with batch approve/reject and automated rejection emails",
        ],
        "problems_solved": [
            "Instant in-browser quality feedback eliminates bad photos before they're taken",
            "Dual-model segmentation with bilateral filtering prevents halo artifacts on hair edges",
            "Mask quality validation with fragmentation detection triggers retake instead of outputting bad composites",
            "Dynamic form system means admins configure exactly the metadata they need per job",
        ],
        "proud_of": [
            "TensorFlow.js pipeline that feels instant on a smartphone",
            "Dual-model segmentation approach for production-quality background replacement",
            "Sole engineer \u2014 built the full stack from ML pipelines to multi-tenant architecture",
            "Enterprise-grade export system plugging into existing badge printing workflows",
        ],
        "build_notes": (
            "<p>Sole engineer, full stack from architecture to deployment. Client-side ML uses a custom useQualityAnalysis "
            "React hook that continuously validates against configurable global thresholds pulled from a singleton SystemSettings model. "
            "Server-side compositing uses bilateral filtering for hair edge cleanup and edge detection to prevent halo artifacts, "
            "with Gaussian blur anti-aliasing for smooth transitions. Backend uses modular ViewSet architecture split into four "
            "specialized files backed by dedicated service layers.</p>"
        ),
    },
    {
        "title": "Photography Store",
        "slug": "photography-store",
        "featured": True,
        "case_problem": "Selling fine art photography online requires more than a product grid — customers need to discover art by mood, visualize it in their space, and feel confident before buying.",
        "case_built": "E-commerce platform with an AI shopping assistant that searches photos by meaning, manages carts through conversation, and previews prints on your actual wall using ML depth estimation.",
        "case_result": "Live at store.matthewraynor.com — try the AI assistant yourself.",
        "description": (
            "E-commerce platform for fine art photography prints. Three collections of Hamptons landscape photography, "
            "museum-quality printing in multiple formats, gift cards, and promo codes. An AI shopping assistant "
            "understands what's in each photo \u2014 ask for 'sunset over the ocean' and it finds matches using vector search. "
            "A 'See in Room' tool lets customers preview prints on their own wall using ML-powered wall detection. "
            "Includes a self-hosted newsletter platform."
        ),
        "tech_line": "Django REST Framework \u00b7 Next.js \u00b7 TypeScript \u00b7 Stripe Checkout \u00b7 Claude + LangChain \u00b7 pgvector \u00b7 OpenAI embeddings \u00b7 AWS S3 \u00b7 Listmonk \u00b7 Custom analytics \u00b7 Railway \u00b7 Netlify",
        "live_url": "https://store.matthewraynor.com",
        "github_url": None,
        "overview": (
            "A complete e-commerce platform for fine art drone and seascape photography targeting the Hamptons luxury art market. "
            "Features an AI shopping assistant built with LangChain and Claude that can search photos semantically, manage carts, "
            "visualize prints on customer walls using depth estimation, and handle checkout through conversation."
        ),
        "tech_stack": {
            "backend": ["Django 5", "Django REST Framework", "PostgreSQL", "pgvector", "Celery", "Redis"],
            "frontend": ["Next.js 15", "TypeScript", "Tailwind CSS"],
            "ai": ["LangChain", "Claude API", "Claude Vision", "OpenAI Embeddings", "MiDaS Depth Estimation"],
            "integrations": ["Stripe Checkout", "AWS S3", "Resend", "Listmonk", "Sentry"],
            "deployment": ["Railway", "Netlify"],
        },
        "problem": (
            "Selling fine art photography online requires more than a product grid \u2014 customers need to discover art by mood and meaning, "
            "visualize how pieces look in their space, and feel confident about size and materials before purchasing."
        ),
        "solution": (
            "Built an AI shopping assistant with 14 tools that searches photos semantically using pgvector embeddings, manages carts, "
            "filters by color/mood/subject, checks gift card balances, and answers sizing questions. The 'See It In Room' feature uses "
            "MiDaS depth estimation + RANSAC plane-fitting to composite prints at correct scale on customer-uploaded wall photos."
        ),
        "special_features": [
            "AI shopping assistant with 14 tools \u2014 search, cart, checkout, wall visualization all through conversation",
            "pgvector semantic search using OpenAI text-embedding-ada-002 for meaning-based photo discovery",
            "Claude Vision auto-generates all photo metadata (descriptions, moods, colors, subjects)",
            "'See It In Room': MiDaS depth estimation + RANSAC plane-fitting composites prints at correct scale",
            "Stripe Checkout with gift card redemption and promotional codes",
            "Self-hosted Listmonk newsletter with Amazon SES delivery",
            "Custom privacy-friendly analytics \u2014 no cookies, no third-party tracking",
        ],
        "problems_solved": [
            "Semantic photo discovery \u2014 customers find art by meaning, not just keywords",
            "Realistic wall visualization reduces purchase hesitation for expensive prints",
            "Conversational commerce handles the entire shopping experience through the AI assistant",
            "Automated metadata generation eliminates manual photo tagging",
        ],
        "proud_of": [
            "MiDaS + RANSAC pipeline that accurately places prints on real walls",
            "Semantic search that understands 'moody ocean sunset' or 'bright aerial beach'",
            "Full conversational commerce \u2014 browse, add to cart, and check out without leaving the chat",
            "Self-hosted newsletter replacing paid services like MailerLite",
        ],
        "build_notes": (
            "<p>Photo embeddings generated with OpenAI text-embedding-ada-002, stored in PostgreSQL with pgvector for cosine similarity search. "
            "The AI assistant uses LangChain with Claude and 14 tools for a complete shopping experience. The 'See It In Room' feature uses "
            "MiDaS depth estimation to find walls in uploaded photos, then RANSAC plane-fitting to composite prints at physically accurate scale. "
            "Self-hosted Listmonk newsletter on Railway with Amazon SES for delivery and SNS for bounce/complaint handling.</p>"
        ),
        "blog_url": "/blog/i-built-an-ai-shopping-assistant-that-sees-your-wa/",
    },
    {
        "title": "EJ Art Mover",
        "slug": "art-mover",
        "featured": True,
        "hero_video": "https://youtu.be/xWtrO4F0In4",
        "hero_image": "https://res.cloudinary.com/dddye9wli/image/upload/w_400,h_300,c_fill,q_auto,f_auto/v1752173585/art-mover_tlvsny.jpg",
        "case_problem": "An art moving company was managing scheduling, invoicing, and job tracking through spreadsheets and email.",
        "case_built": "A job management app with drag-and-drop scheduling, PDF invoicing, photo documentation, and mobile-first field use.",
        "case_result": "In daily production use — the business runs on it.",
        "login_only": True,
        "description": (
            "Job management app built for a professional art moving company. "
            "Handles the full workflow \u2014 clients, work orders, scheduling, photo documentation, invoicing, and printable PDFs. "
            "A drag-and-drop calendar plans daily routes. Built for the field \u2014 works on a phone as well as a desktop. "
            "Rebuilt from a Django monolith into a decoupled architecture."
        ),
        "tech_line": "Django REST Framework \u00b7 Next.js \u00b7 React \u00b7 TypeScript \u00b7 shadcn/ui \u00b7 FullCalendar \u00b7 WeasyPrint \u00b7 Cloudinary \u00b7 JWT \u00b7 TanStack Query \u00b7 Railway \u00b7 Netlify",
        "live_url": "https://app.ejartmover.net",
        "github_url": "https://github.com/mattyray/ej-art-mover-v2",
        "overview": (
            "A production-grade job management application for an art moving business. It manages the entire workflow from "
            "client intake through job scheduling, execution, and invoicing. Originally built as a Django monolith with Bootstrap "
            "templates, it was rebuilt as a decoupled system \u2014 Django REST Framework API backend with a Next.js/React/TypeScript frontend."
        ),
        "tech_stack": {
            "backend": ["Django 5", "Django REST Framework", "PostgreSQL", "WeasyPrint"],
            "frontend": ["Next.js", "React", "TypeScript", "Tailwind CSS", "shadcn/ui", "FullCalendar"],
            "auth": ["JWT with automatic token refresh via Axios interceptors"],
            "deployment": ["Railway", "Netlify", "Cloudinary"],
        },
        "problem": "The client was managing logistics, invoicing, and scheduling manually via email and spreadsheets, which caused delays and errors.",
        "solution": (
            "Built a centralized system that tracks jobs, clients, and invoices with a drag-and-drop calendar for daily route planning, "
            "PDF generation for work orders and invoices, and a mobile-first responsive design for field use."
        ),
        "special_features": [
            "Drag-and-drop calendar with month, week, and day views \u2014 reorder stops to plan daily routes",
            "PDF generation for work orders and invoices via WeasyPrint",
            "Invoicing with three-stage status flow (unpaid, in QuickBooks, paid)",
            "Mobile-first: card layouts on phones, table layouts on desktop",
            "Work orders track jobs through pending, in progress, completed, invoiced",
            "File attachments with Cloudinary storage for photos and documents",
            "Google Places address autocomplete for service and billing addresses",
        ],
        "problems_solved": [
            "Digitized manual scheduling and invoicing",
            "Visual overview of work orders via FullCalendar with drag-and-drop",
            "Mobile-responsive design means the app works in the field on a phone",
            "Rebuilt from monolith to decoupled architecture for maintainability",
        ],
        "proud_of": [
            "Full monolith-to-decoupled rebuild with direct data migration via pg_dump",
            "Mobile-first UX with bottom sheet drawers on phones, dropdown menus on desktop",
            "Drag-and-drop calendar for daily route planning",
            "Production app used daily by a real business",
        ],
        "build_notes": (
            "<p>Originally a Django monolith with Bootstrap templates and jQuery deployed on Heroku. Rebuilt as a decoupled "
            "system with a DRF API backend and Next.js frontend. Authentication uses JWT with automatic token refresh via "
            "Axios interceptors. Server state managed with TanStack Query. Forms use React Hook Form with Zod validation. "
            "Same PostgreSQL schema allowed direct data migration via pg_dump.</p>"
        ),
    },
    {
        "title": "Chef Bawss",
        "slug": "chef-bawss",
        "featured": True,
        "case_problem": "Private chef businesses juggle clients, chefs, events, and finances across spreadsheets and texts.",
        "case_built": "Multi-tenant SaaS with role-based access, event scheduling, financial tracking, and automated reminders.",
        "case_result": "Live platform — any private chef business can sign up and run their operation from one place.",
        "login_only": True,
        "description": (
            "Operations platform for private chef businesses. Owners manage clients, invite contract chefs, "
            "schedule events, and track financials \u2014 what the client pays, what the chef earns, and the profit. "
            "Chefs see only their own assignments. Automated email reminders before events. "
            "Built as multi-tenant SaaS so any private chef business can sign up."
        ),
        "tech_line": "Django REST Framework \u00b7 Next.js \u00b7 TypeScript \u00b7 Celery \u00b7 Amazon SES \u00b7 FullCalendar \u00b7 PostgreSQL \u00b7 Redis \u00b7 JWT \u00b7 Multi-tenant architecture \u00b7 Fly.io \u00b7 Netlify",
        "live_url": "https://chef-bawss.netlify.app",
        "github_url": None,
        "overview": (
            "Chef Bawss is a multi-tenant SaaS platform built for private chefs and small catering business owners who hire "
            "freelance chefs to work events. It's the back-office tool for managing the whole operation \u2014 clients, chefs, events, "
            "and finances \u2014 all in one place."
        ),
        "tech_stack": {
            "backend": ["Django 5", "Django REST Framework", "PostgreSQL", "Redis", "Celery"],
            "frontend": ["Next.js 16", "TypeScript", "Tailwind CSS", "FullCalendar"],
            "integrations": ["Amazon SES", "JWT auth (httpOnly cookies)"],
            "deployment": ["Fly.io", "Netlify", "Docker Compose"],
        },
        "problem": (
            "Private chef businesses juggle clients, freelance chefs, event scheduling, and financial tracking "
            "across spreadsheets, texts, and email. There's no tool built for how they actually work."
        ),
        "solution": (
            "Built a multi-tenant SaaS with two roles: admins see everything (clients, chefs, events, profit margins), "
            "chefs see only their own assignments and pay. Automated email reminders via Celery + Amazon SES. "
            "Google Calendar-style interface with chef color-coding and drag-to-reschedule."
        ),
        "special_features": [
            "Multi-tenant architecture \u2014 every organization's data is fully isolated",
            "Two-role system: Admin (full control, financials) vs Chef (own assignments only)",
            "Chef invitation flow \u2014 admin enters details, system sends email invite, chef sets password",
            "FullCalendar with auto-assigned chef colors, filtering, drag-to-reschedule, resize-to-change-duration",
            "Automated email notifications: assignment, changes, cancellations, 3-day and 1-day reminders",
            "Event financial tracking: client pay, chef pay, deposits, profit calculation",
        ],
        "problems_solved": [
            "Centralized operations for businesses that were running on spreadsheets and texts",
            "Role-based access so chefs see their pay but not client revenue or profit",
            "Automated reminders eliminate missed events and last-minute confusion",
            "Multi-tenancy means any private chef business can sign up and be isolated",
        ],
        "proud_of": [
            "Multi-tenant architecture with tenant-scoped querysets and middleware",
            "Chef invitation flow that handles the full onboarding lifecycle",
            "Automated Celery task scheduling for event reminders",
            "Built as a real SaaS product, not just a one-off client project",
        ],
        "build_notes": (
            "<p>Multi-tenant SaaS with full data isolation via tenant-scoped querysets and middleware. "
            "JWT auth stored in httpOnly cookies. Celery Beat schedules automated reminder emails (3-day and 1-day) "
            "via Amazon SES with SNS bounce/complaint handling. FullCalendar integration with chef color assignment, "
            "event filtering, and drag-and-drop rescheduling.</p>"
        ),
    },
    {
        "title": "HistoryFace AI",
        "slug": "historyface-ai",
        "hero_video": "https://youtu.be/rpkIL5FZbpA",
        "hero_image": "https://res.cloudinary.com/dddye9wli/image/upload/w_400,h_300,c_fill,q_auto,f_auto/v1752173587/motivational-chatbot_b2e8qv.jpg",
        "description": (
            "Upload a selfie, get transformed into your historical twin. The app extracts a 128-dimension "
            "facial encoding from your photo, matches it against a database of historical figures using cosine similarity, "
            "then runs a face swap through a self-hosted FaceFusion model on HuggingFace Spaces. "
            "Includes concurrency throttling, auto-expiring images with Cloudinary cleanup, and a freemium usage gate."
        ),
        "tech_line": "Django REST Framework \u00b7 React \u00b7 TypeScript \u00b7 face-recognition (dlib) \u00b7 HuggingFace Spaces \u00b7 FaceFusion \u00b7 Cloudinary \u00b7 Redis \u00b7 PostgreSQL \u00b7 Fly.io \u00b7 Netlify",
        "live_url": None,
        "github_url": "https://github.com/mattyray/ai-convert",
        "overview": (
            "HistoryFace is a full-stack AI web app where users upload a selfie and get transformed into a historical figure. "
            "It's a multi-step AI processing pipeline: face detection using dlib, cosine similarity matching against "
            "pre-computed historical figure embeddings, then face swapping via a self-hosted FaceFusion model on HuggingFace Spaces."
        ),
        "tech_stack": {
            "backend": ["Django 5", "Django REST Framework", "PostgreSQL", "Redis", "Celery"],
            "frontend": ["React 19", "TypeScript", "Tailwind CSS"],
            "ai_ml": ["face-recognition (dlib)", "HuggingFace Spaces", "FaceFusion", "OpenCV"],
            "integrations": ["Cloudinary", "Stripe", "Google OAuth"],
            "deployment": ["Docker", "Fly.io", "Netlify"],
        },
        "problem": (
            "Creating a viral AI face-swapping app requires complex facial recognition, expensive GPU processing, "
            "smart cost management, and a sustainable monetization strategy."
        ),
        "solution": (
            "Built a complete SaaS integrating HuggingFace AI models with custom facial recognition. "
            "Freemium model with session-based usage tracking, Redis-based concurrency throttling (max 2 simultaneous jobs), "
            "and automated Cloudinary cleanup that expires generated images after 48 hours."
        ),
        "special_features": [
            "128-dimension facial encoding with cosine similarity matching against ~65 historical figures",
            "Self-hosted FaceFusion model on HuggingFace Spaces with Gradio API",
            "Redis concurrency control \u2014 max 2 simultaneous face-swap jobs, 503 with retry-after if overloaded",
            "Auto-expiring images: 48-hour TTL with background Cloudinary cleanup daemon",
            "Freemium gate: 1 match + 1 randomize per anonymous session, unlimited for logged-in users",
            "Client-side image compression (800x800 max, LANCZOS, JPEG quality 75) before upload",
        ],
        "problems_solved": [
            "Cost-effective AI model integration without running own GPU infrastructure",
            "Concurrency control prevents HuggingFace endpoint from being overwhelmed",
            "Automated asset cleanup prevents runaway Cloudinary storage costs",
            "Freemium model balances free trials with paid conversion",
        ],
        "proud_of": [
            "Multiple AI integrations in one project: facial recognition, face swapping, and conversational AI",
            "Smart cost management with concurrency limits and auto-expiring assets",
            "Full SaaS architecture with auth, usage tracking, and payment integration",
            "Production concerns handled: compression, throttling, cleanup, rate limiting",
        ],
        "build_notes": (
            "<p>Four Django apps: accounts, imagegen, faceswap, chat. The face matching pipeline uses dlib's CNN-based "
            "face detector to extract 128-dimensional encodings, then cosine similarity against pre-computed embeddings. "
            "The HuggingFace client authenticates with a private Space, calls /setup_facefusion then /process_images "
            "with retry logic and exponential backoff. A daemon thread runs every 6 hours to clean up expired Cloudinary assets. "
            "Redis cache counters enforce concurrent job limits.</p>"
        ),
        "video_url": "https://youtu.be/rpkIL5FZbpA",
    },
    {
        "title": "Matt's Freedom Fundraiser",
        "slug": "freedom-fundraiser",
        "hero_video": "https://youtu.be/ZumlW-noN6E",
        "hero_image": "https://res.cloudinary.com/dddye9wli/image/upload/w_400,h_300,c_fill,q_auto,f_auto/v1752173586/fundraiser_gsbo4o.jpg",
        "description": (
            "A fundraising platform I built for myself. After a spinal cord injury left me tetraplegic, "
            "I was living in a long-term care facility and needed a way out. I built this app to collect donations "
            "and sell event tickets through Stripe, connected it to a legal trust to stay compliant with Medicaid, "
            "and raised enough to fund my transition to independent living. Automated thank-you emails, real-time "
            "campaign tracking, and a live progress bar. It worked \u2014 I moved home to Hampton Bays."
        ),
        "tech_line": "Django REST Framework \u00b7 React \u00b7 TypeScript \u00b7 Stripe Checkout \u00b7 Celery \u00b7 Redis \u00b7 SendGrid \u00b7 PostgreSQL \u00b7 Google OAuth \u00b7 Fly.io \u00b7 Netlify",
        "live_url": "https://mattsfreedomfundraiser.com",
        "github_url": "https://github.com/mattyray/mff-v2",
        "overview": (
            "When I needed to raise funds for my transition to independent living, I built my own platform. "
            "Direct Stripe integration with zero platform fees, automated donor communications via Celery + SendGrid, "
            "and real-time campaign tracking. Connected to a legal trust to stay compliant with Medicaid. "
            "Rebuilt from a Django monolith to a decoupled React + DRF architecture."
        ),
        "tech_stack": {
            "backend": ["Django 5", "Django REST Framework", "PostgreSQL", "Redis", "Celery"],
            "frontend": ["React 19", "TypeScript", "Vite", "Tailwind CSS"],
            "payments": ["Stripe Checkout", "Webhook processing"],
            "deployment": ["Fly.io", "Netlify", "Docker Compose"],
        },
        "problem": (
            "Needed to raise funds for my transition out of a long-term care facility to independent living, "
            "with full legal compliance and zero platform fees eating into donations."
        ),
        "solution": (
            "Built an independent donation platform with direct Stripe integration, automated thank-you emails "
            "via Celery + SendGrid, real-time campaign tracking with atomic updates using Django F() expressions, "
            "and event ticket sales with multi-line-item checkout."
        ),
        "special_features": [
            "Direct Stripe integration \u2014 100% of donations reach recipient",
            "Multi-line-item Stripe Checkout \u2014 event tickets and donations in a single session",
            "Automated Celery email system for donor thank-yous and ticket confirmations",
            "Real-time campaign tracking \u2014 progress bar, dollars raised, tickets sold updated live",
            "Atomic donation updates using Django F() expressions",
            "Google OAuth and email-based authentication via Django Allauth",
        ],
        "problems_solved": [
            "Eliminated platform fees that siphon money from donations",
            "Provided immediate access to funds without arbitrary hold periods",
            "Legal compliance through trust integration with Medicaid",
            "Reliable donor communication without platform censorship",
        ],
        "proud_of": [
            "Built under extreme constraints and it worked \u2014 moved home to Hampton Bays",
            "Enterprise-grade donation platform from scratch",
            "Atomic F() updates for concurrent donation tracking",
            "Rebuilt from Django monolith to decoupled architecture",
        ],
        "build_notes": (
            "<p>Stripe webhook processes completed payments \u2014 verifies signature, updates donation status and campaign "
            "totals atomically using Django F() expressions, and queues a Celery task for the thank-you email. "
            "Frontend is a single-page React app with smooth-scroll navigation. Rebuilt from a Django monolith "
            "to a decoupled React + DRF architecture.</p>"
        ),
        "video_url": "https://youtu.be/ZumlW-noN6E",
    },
]


class PortfolioView(TemplateView):
    template_name = "portfolio/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = SERVICES
        context["featured_projects"] = [p for p in PROJECTS if p.get("featured")]
        context["more_projects"] = [p for p in PROJECTS if not p.get("featured")]
        return context


class ProjectDetailView(TemplateView):
    template_name = "portfolio/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get("slug")
        project = next((p for p in PROJECTS if p["slug"] == slug), None)
        if not project:
            raise Http404("Project not found")
        context["project"] = project
        return context
