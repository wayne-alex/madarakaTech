# Wayne Murunga | Portfolio

A simple, fast portfolio site for Wayne Murunga, a software engineer working with Python, Django and PostgreSQL.

**Live site:** https://madarakatech.vercel.app/

## About

This site lists my experience, projects, skills and education, with links to my code and contact details. It is a single static page with no build step and no dependencies.

## Project structure

```
.
├── index.html    # The whole site (HTML and CSS in one file)
└── README.md
```

## Features

- Single page with Experience, Projects, Skills, Education and Contact sections
- Responsive layout that works on phones and desktops
- Automatic light and dark mode based on the device setting
- Keyboard-friendly, with visible focus styles
- Fast to load: one file, plus two Google Fonts (IBM Plex Sans and Source Serif 4)

## Run locally

Open `index.html` in a browser. No install is needed.

To serve it locally instead:

```bash
python -m http.server 8000
```

Then visit http://localhost:8000

## Deploy

The site is hosted on Vercel as a static site. To update it, commit the change to the main branch and Vercel will redeploy automatically.

## Editing the content

All content is in `index.html`. To update it:

- **Intro and links:** edit the `intro` section near the top
- **Experience:** edit the `#experience` section
- **Projects:** copy an existing `<div class="item">` block in `#projects` and change the text and links
- **Colours and fonts:** change the variables at the top of the `<style>` block (`--accent`, `--ink`, `--serif`, `--sans`)

## Contact

- Email: waynealex9914@gmail.com
- GitHub: https://github.com/wayne-alex
- LinkedIn: https://ke.linkedin.com/in/wayne-murunga-107886253

## License

© 2026 Wayne Murunga. All rights reserved.