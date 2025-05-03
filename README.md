# Group_2-headstream-K-12-Mental_Health_Navigator_

This project is designed to combine both the frontend and backend for the K-12 Mental Health Navigator. It helps schools and districts choose and use effective digital tools for student mental health and well-being.

---

## Table of Contents
1. [Features](#features)
2. [Project Structure](#project-structure)
3. [Setup Instructions](#setup-instructions)
4. [Running the Project](#running-the-project)
5. [Making Changes](#making-changes)
6. [Linking Pages](#linking-pages)
7. [Adding Images](#adding-images)
8. [Troubleshooting](#troubleshooting)

---

## Features
- **Survey Modal**: A popup survey form that automatically loads on the homepage.
- **Thank You Modal**: Displays a thank-you message with a countdown timer and redirection logic.
- **Dynamic Navigation**: Links to multiple pages, including "About Us," "Case Studies," and "Explore."
- **Chat Feature**: A floating chat bubble for user interaction.
- **Responsive Design**: Works on both desktop and mobile devices.

---

## Project Structure

survey_project/
├── survey_app/
│   ├── templates/survey_app/       # HTML templates
│   │   ├── index.html              # Main page
│   │   ├── aboutus.html            # About Us page
│   │   ├── assess.html             # Assess page
│   │   ├── casestudies.html        # Case Studies page
│   │   ├── explore.html            # Explore page
│   │   ├── ...                     # Other pages
│   ├── static/survey_app/          # Static files
│   │   ├── css/                    # CSS files
│   │   │   ├── styles.css          # Main stylesheet
│   │   ├── images/                 # Images
│   │   │   ├── logo.png            # Example logo
│   │   │   ├── hero.jpg            # Example hero image
│   │   ├── js/                     # JavaScript files
│   │   │   ├── index.js            # Main JavaScript file
│   ├── views.py                    # Django views
│   ├── urls.py                     # URL routing
├── manage.py                       # Django management script

Setup Instructions
Prerequisites
Python: Ensure Python 3.9 or higher is installed.
Django: Install Django using pip:
django

pip install django

Steps to Set Up the Project
Clone the repository:

git clone <repository-url>
cd survey_project

2. Install dependencies:

pip install -r requirements.txt

3. Apply migrations:

python manage.py makemigrations
python manage.py migrate

4. Run the development server:

python manage.py runserver

5. Open the application in your browser:
http://127.0.0.1:8000/

Running the Project
1. Start the Django development server:

python manage.py runserver

2. Access the application at http://127.0.0.1:8000/.


Making Changes
After Making Changes to Code or Templates

1. Save your changes.
2. Restart the development server:

python manage.py runserver

3. Refresh the browser to see the updates.
After Adding New Static Files (CSS, JS, Images)
1. Collect static files:
python manage.py collectstatic

2. Restart the server:
python manage.py runserver

Linking Pages
Adding Links to Navigation
To add a new page to the navigation menu:

1. Create a view in views.py:
def new_page(request):
    return render(request, 'survey_app/new_page.html')

2. Add a URL pattern in urls.py:
path('new-page/', views.new_page, name='new_page'),

3. Add the link to the navigation in index.html or other templates:
<li><a href="{% url 'new_page' %}">New Page</a></li>

Adding Images
Placing Images

1. Place your images in the static/survey_app/images/ directory. Example:
/survey_project/survey_app/static/survey_app/images/example.png

Referencing Images in Templates
Use the {% static %} template tag to reference images:

<img src="{% static 'survey_app/images/logo.png' %}" alt="Logo">

Troubleshooting
Common Issues

1. Static Files Not Loading

Ensure STATIC_URL and STATICFILES_DIRS are configured in settings.py:
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

Run python manage.py collectstatic.

2. Page Not Found (404)
Ensure the view is defined in views.py and the URL pattern is added in urls.py.

3. CSRF Token Missing
Ensure {% csrf_token %} is included in all forms.

4. JavaScript Not Working

<script src="{% static 'survey_app/js/index.js' %}" defer></script>