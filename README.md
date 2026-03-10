# MADARAKA TECHNOLOGY

> **Bridging software intelligence with telecommunications engineering.**  
> We design, build, and deploy ICT solutions that transform organisations — online, anywhere, anytime.

---

## 🌐 Live Site

```
https://madarakatech.vercel.app/
```

---

## 📁 Project Structure

```
madaraka/
├── frontend/
│   └── landing.html          # Main website (single-file)
├── backend/
│   ├── manage.py
│   ├── requirements.txt
│   └── contact/
│       ├── views.py           # Contact form + email handler
│       └── urls.py
└── README.md
```

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎮 **Hack Game** | Playable space firewall defender embedded in the hero section |
| 🌍 **Interactive Globe** | Draggable 3D globe showing global reach — Nairobi highlighted |
| 🔐 **Secret Easter Egg** | Konami code `↑↑↓↓←→←→BA` triggers Matrix rain mosaic of the company name |
| ⌨️ **Live Terminal** | Animated typing terminal bar cycling ICT facts and system status |
| ✉️ **Contact Form** | Submits to Django backend — sends branded emails to both team and enquirer |
| 🌌 **Particle Constellation** | Mouse-reactive particle background with connecting lines |

---

## 🛠 Tech Stack

### Frontend
- Vanilla HTML / CSS / JavaScript — zero frameworks, zero dependencies
- **Three.js r128** — 3D globe
- **Canvas API** — particle system, game engine, Matrix rain
- **Google Fonts** — Bebas Neue, Rajdhani, Share Tech Mono

### Backend
- **Django** — REST contact endpoint
- **django-cors-headers** — cross-origin request handling
- **Requests** — HTTP calls to email microservice

---

## 🚀 Getting Started

### Frontend

Just open `frontend/madaraka.html` in a browser — no build step required.

For local development with Live Server (VS Code):
```bash
# Install Live Server extension, then right-click madaraka.html → Open with Live Server
```

---

### Backend

**1. Clone and set up virtual environment**
```bash
git clone https://github.com/wayne-alex/madaraka.git
cd madaraka/backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the dev server**
```bash
python manage.py runserver
```

Backend will be live at `http://localhost:8000`

---

## 📦 Requirements

`backend/requirements.txt`
```
django>=4.2
django-cors-headers>=4.0
requests>=2.31
```

---

## ✉️ Contact Form Flow

```
User submits form
      │
      ▼
Django /contact/ endpoint
      │
      ├──▶ POST → node-mailer (Vercel)
      │         └──▶ 📧 madarakatech@gmail.com
      │                   "New Enquiry from {name}"
      │
      └──▶ POST → node-mailer (Vercel)
                └──▶ 📧 {user email}
                          "Enquiry Received — Madaraka Technology"
                          (branded dark HTML, no-reply)
```

---

## 🔧 Configuration

Update these values before deploying:

**`frontend/madaraka.html`** — line with `DJANGO_URL`:
```js
const DJANGO_URL = 'https://madarakatech.vercel.app/contact/'; // ← your live URL
```

**`backend/contact/views.py`**:

**`backend/settings.py`**:
```python
CORS_ALLOWED_ORIGINS = [
    "https://madarakatech.vercel.app/"
]
# Remove CORS_ALLOW_ALL_ORIGINS = True in production
```

---

## 🎮 Easter Egg

On the live site, type the Konami code on your keyboard:

```
↑  ↑  ↓  ↓  ←  →  ←  →  B  A
```

The screen fills with Matrix rain that resolves into a glowing character-mosaic spelling:

```
MADARAKA
TECHNOLOGY
```

---

## 👥 Founders

| | Role | Expertise |
|---|---|---|
| **WAYNE MURUNGA** | Software & Systems Director | Full-stack dev, AI/ML, databases, cybersecurity |
| **JOB WANDERA** | Telecoms & Infrastructure Director | Networking, VoIP, cloud, system integration |

---

## 📬 Contact

- **Email:** madarakatech@gmail.com
- **Website:** [madaraka.tech](https://madarakatech.vercel.app/)
- **Location:** Nairobi, Kenya 🇰🇪

---

## 📄 License

© 2024 Madaraka Technology. All rights reserved.

---

<div align="center">
  <sub>Built with ⚡ by Madaraka Technology — CS + Telecom Engineering</sub>
</div>
