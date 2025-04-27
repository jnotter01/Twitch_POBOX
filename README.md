# Twitch_POBOX Fan Mail Application

## Project Overview
Welcome to the **Fan Mail App** — a web application built for streamers to let fans submit digital fan mail and notify the streamer when physical packages have been sent. The app provides a fun and easy way to create, manage, and showcase fan interactions securely and efficiently.

## Core Features
- **User Authentication**
  - Register, Login, Logout functionality
- **Fan Mail Submission**
  - Fans can submit messages and optionally attach an image
- **Fan Mail Editing and Deletion**
  - Users can edit their fan mail submissions via AJAX without duplication issues
- **Gallery View**
  - Displays a grid of fan mail submissions that include images
- **Package Notification**
  - Fans can notify the streamer that they sent a package
- **Package Submission History**
  - Users can view a personal history of their package notifications
- **Responsive and Polished UI**
  - Uniform styling across the app, including a polished Logout button

## Technologies Used
- **Python 3.13**
- **Django 5.2**
- **SQLite** (default Django database)
- **HTML5** / **CSS3**
- **JavaScript (AJAX)** for asynchronous form handling
- **Git** and **GitHub** for version control

## Setup Instructions

1. Clone the Repository:

https://github.com/jnotter01/Twitch_POBOX.git


2. Set up Virtual Environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


3. Install Dependencies:

pip install -r requirements.txt


4. Apply Migrations:

python manage.py migrate


    4B. (Optional) Create a Superuser: If you want access to the Django admin panel:
    python manage.py createsuperuser

5. Run Server:

python manage.py runserver


6. Open your browser and visit:

http://127.0.0.1:8000/


## How to Use
- Register a new user account.
- Log in.
- Submit fan mail messages and optionally attach an image.
- Edit or delete your fan mail from the home page.
- Browse submitted fan mail in the Gallery.
- Notify the streamer when you've sent a physical package.
- View your past package submissions.

## Final Status
  **Project completed successfully as of April 2025.**

All major functionality works as intended. The project has been polished, tested, and is ready for demonstration.

---

**Thank you for checking out the Fan Mail App!**
