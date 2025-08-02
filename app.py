from flask import Flask, render_template, request, redirect, url_for, flash, abort
import os
import markdown
import yaml
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'dev_key')  # Use environment variable in production

# Home route
@app.route('/')
def home():
    return render_template('index.html', page_title="Home")

def load_blogs():
    posts = []
    for filename in os.listdir('blogs'):
        if filename.endswith('.md'):
            with open(os.path.join('blogs', filename), 'r', encoding='utf-8') as f:
                content = f.read()
                # Extract front-matter
                if content.startswith('---'):
                    front_matter, md_body = content.split('---', 2)[1:]
                    meta = yaml.safe_load(front_matter)
                else:
                    meta, md_body = {}, content
                meta['slug'] = filename[:-3]
                meta['body'] = md_body.strip()
                posts.append(meta)
    # Sort by date (descending)
    posts.sort(key=lambda x: x.get('date', ''), reverse=True)
    return posts

@app.route('/blogs')
def blogs():
    posts = load_blogs()
    return render_template('blogs.html', posts=posts, page_title='Blogs')

@app.route('/blog/<slug>')
def blog(slug):
    path = os.path.join('blogs', f'{slug}.md')
    if not os.path.exists(path):
        abort(404)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        if content.startswith('---'):
            front_matter, md_body = content.split('---', 2)[1:]
            meta = yaml.safe_load(front_matter)
        else:
            meta, md_body = {}, content
        html_body = markdown.markdown(md_body, extensions=["fenced_code", "codehilite"])
    return render_template('blog_detail.html', post=meta, body=html_body, page_title=meta.get('title', 'Blog'))

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone', '')
    message = request.form.get('message')

    if not name or not email or not message:
        flash('Please fill in all required fields.', 'danger')
        return redirect(url_for('home', _anchor='contact'))

    # Prepare email content
    email_message = EmailMessage()
    email_message['Subject'] = f'Portfolio Contact from {name}'
    email_message['From'] = os.environ.get('EMAIL_ADDRESS')  # Your email address
    email_message['To'] = os.environ.get('RECEIVER_EMAIL')  # Destination (your) email

    body = f"""
    You have received a new message from your portfolio contact form.

    Name: {name}
    Email: {email}
    Phone: {phone}
    Message:
    {message}
    """

    email_message.set_content(body)

    try:
        # Connect to SMTP server
        smtp_server = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
        smtp_port = int(os.environ.get('SMTP_PORT', 587))
        smtp_user = os.environ.get('EMAIL_ADDRESS')
        smtp_password = os.environ.get('EMAIL_PASSWORD')

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.send_message(email_message)
        flash('Your message has been sent successfully!', 'success')
    except Exception as e:
        print(f"Email send failed: {e}")
        flash('Failed to send your message. Please try again later.', 'danger')

    return redirect(url_for('home', _anchor='contact'))

# 404 handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', page_title="Page Not Found"), 404

if __name__ == '__main__':
    app.run(debug=True)
