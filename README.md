**🚀Swaroop — Full Stack Web Developer Portfolio**

A modern, dynamic personal portfolio built with **Flask, Bootstrap, and dynamic Markdown-based blog engine, showcasing projects, skills, education, certifications**, and more. Responsive, animated, and ready for job seekers or freelancers!✨🌐

<hr/>

**✨ Features**
- 📱 Responsive design (Bootstrap, custom CSS) — looks great on desktop and mobile
- 🌙 Dark/Bright Mode Toggle (with persistence)
- 🎯 Hero section with animated typewriter effect and gradient border CV download button
- 👨💻 About Me section with image and highlights
- 🏗️ Filterable Projects grid (category filter, hover overlay, one-click GitHub open)
- 🧰 Skills panel (Font Awesome icons)
- 🎓 Education & Certifications (tabbed, links to certificate credentials)
- 📝 Dynamic Blogs powered by Markdown files (just drop a .md file in /blogs/ to add a post)
- ✉️ Contact form (with Flask mail backend — auto-emails you new messages)
- 🛑 Custom 404 error page

<hr/>

**🗂️ Project Structure**
```
project/
│
├── app.py                        # Flask application (backend)
├── requirements.txt              # Dependencies
├── Procfile                      # (if deploying to Heroku)
├── .env                          # (ignored) for local secrets/environment
│
├── templates/                    # HTML templates (base, index, blogs, blog_detail, 404, partials)
├── static/
│   ├── styles/main.css           # Custom CSS
│   ├── js/main.js                # Custom JS
│   ├── images/                   # All site images
│   └── assets/Swaroop-CV.pdf     # Downloadable CV for hero section
│
├── blogs/                        # Markdown blog posts (use front-matter)
└── README.md                     # This file
```

<hr/>

**🚀 Getting Started Locally**

**1) Clone the repository**

```
  git clone https://github.com/your-username/your-portfolio-repo.git
  cd your-portfolio-repo
```
**2) Install required packages**

  Create a virtual environment (recommended):
```
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
```
  Install dependencies:
```
  pip install -r requirements.txt
```
**3) Set environment variables**

  Create a .env file (or export via shell) for secrets and email credentials:

```
  FLASK_SECRET_KEY=your-random-key
  EMAIL_ADDRESS=youremail@example.com
  EMAIL_PASSWORD=yourpassword-or-appkey
  RECEIVER_EMAIL=youremail@example.com
  SMTP_SERVER=smtp.gmail.com
  SMTP_PORT=587
```

**4) Run the app**

```
  flask run
```
  or

```
  python app.py
```

**5) Visit your site**
```
Open http://localhost:5000 in your browser.
```

<hr/>

**✍️ Adding Blog Posts**

Create a new Markdown file in /blogs/ with this header:
```
---
  title: "Awesome Demo Post"
  date: "2025-07-29"
  summary: "A summary displayed on the blog card."
  image: "/static/images/blog-image.jpg"
  external_url: "https://your-external-link.com"   # Optional, for Google Docs/Medium etc.
---
Your blog content (Markdown supported)
```

For blogs on Google, just add the external_url field—the "Read More" button will link out.

<hr/>

**🎨 Credits**

- 🚀 Bootstrap
- 🐍 Flask
- ⚡ Font Awesome 
- 👀 AOS Animate on Scroll
- ✍️ Markdown, PyYAML

<hr/>

**🔒 License**

  MIT License, free for all personal use & learning

  © 2025 Swaroop

<hr/>

Feel free to modify this file with your own links, branding, and deployment notes!
