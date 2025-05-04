# Group_2-headstream-K-12-Mental_Health_Navigator_

This project is designed to combine both the frontend and backend for the K-12 Mental Health Navigator. It helps schools and districts choose and use effective digital tools for student mental health and well-being.

## Navigating to Pages

Here are the links to access different pages of the application:

- **[Home/Index](http://127.0.0.1:8000/):** The main landing page of the application.
- **[About Us](http://127.0.0.1:8000/aboutus/):** Learn more about the purpose and mission of the project.
- **[Explore](http://127.0.0.1:8000/explore/):** Discover tools and resources for mental health support.
- **[Contact](http://127.0.0.1:8000/#contact):** Reach out to us via the contact section on the homepage.

### Additional Pages

- **[Assess](http://127.0.0.1:8000/assess/):** Evaluate student needs for mental health solutions.
- **[Stakeholder Engagement](http://127.0.0.1:8000/stakeholder/):** Plan for stakeholder involvement.
- **[Select Solutions](http://127.0.0.1:8000/selectSolution/):** Choose relevant mental health solutions.
- **[Funding Strategy](http://127.0.0.1:8000/fundingStrategy/):** Develop a funding strategy for implementation.
- **[Implement Solution](http://127.0.0.1:8000/implementSolution/):** Steps to implement chosen solutions.

### Case Studies

- **[Methuen](http://127.0.0.1:8000/methuen/):** Case study on Methuen's mental health initiatives.
- **[Case 2](http://127.0.0.1:8000/case2/):** Rim of the World Unified School District case study.
- **[Case 3](http://127.0.0.1:8000/case3/):** Uplift Education case study.
- **[Case 4](http://127.0.0.1:8000/case4/):** Judson ISD case study.
- **[Case 5](http://127.0.0.1:8000/case5/):** Cherry Creek case study.

### Quick Access

- **[Index Contact](http://127.0.0.1:8000/#contact):** Direct link to the contact section on the homepage.
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

All the html files are in survey_project/survey_app/templates/survey_app  directory

CSS files are in survey_project/survey_app/static/survey_app/css directory

Js files are in survey_project/survey_app/static/survey_app/js  directory

All images need to be placed in survey_project/survey_app/static/survey_app/images  directory

---

## Setup Instructions
Prerequisites
Python: Ensure Python 3.9 or higher is installed.
Django: Install Django using pip:
django

```bash
pip install django
```

Steps to Set Up the Project
Clone the repository:

```bash
git clone https://github.com/syfurrahman/Group_2-headstream-K-12-Mental_Health_Navigator_.git
```

```bash
cd survey_project
```

2. Install dependencies that are prompted SQLlite

3. Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Run the development server:

```bash
python manage.py runserver
```

5. Open the application in your browser:

```bash
http://127.0.0.1:8000/.
```

---

## Running the Project

1. Start the Django development server:

Run this command:
```bash
python manage.py makemigrations
python manage.py migrate
```

Run the server 

```bash
python manage.py runserver
```
2. Access the application at 

```bash
http://127.0.0.1:8000/.
```
---
## Making Changes
After Making Changes to Code or Templates

1. Save your changes.
2. Restart the development server:

```bash
python manage.py runserver
```

3. Refresh the browser to see the updates.

After Adding New Static Files (CSS, JS, Images)

1. Collect static files:

```bash
python manage.py collectstatic
```

2. Restart the server:

```bash
python manage.py runserver
```

---
## Linking Pages
Adding Links to Navigation
To add a new page to the navigation menu:

1. Create a view in views.py:

```python
def new_page(request):
    return render(request, 'survey_app/new_page.html')
```

2. Add a URL pattern in urls.py:

```python
path('new-page/', views.new_page, name='new_page'),
```

3. Add the link to the navigation in index.html or other templates:

```html
<li><a href="{% url 'new_page' %}">New Page</a></li>
```
---
## Adding Images
Placing Images

To see example in use go to:

1. [Example](#example)

1. To add an image to your project, follow these steps:

    1. Place your images in the static/survey_app/images/ directory. 

Example:

/survey_project/survey_app/static/survey_app/images/example.png

    2. Ensure the image file is named appropriately (e.g., logo.png, banner.jpg) and avoid spaces or special characters in the filename.

2. Run the following command to make static work without it images won't show up:

```bash
python manage.py collectstatic
```

3. Restart the Django Development Server

1. Run this command:
```bash
python manage.py makemigrations
python manage.py migrate
```

2. Run the server 

```bash
python manage.py runserver
```

4. Referencing Images in Templates
Use the {% static %} template tag to reference images:

```html
<img src="{% static 'survey_app/images/example.png' %}" alt="Example Image">
```

## Example
Here is a example used in **[Case 3](http://127.0.0.1:8000/case3/):**  

Lines 139 - 142: 

```html
<div class="image-container">

<!-- Example in use for dis.png -->
    <img src="{% static 'survey_app/images/dis.png' %}" alt="School implementation workshop">

    <p class="image-caption">Uplift provides comprehensive training to ensure successful implementation in school environments.</p>
</div>
```

---
## Troubleshooting
Common Issues


1. Page Not Found (404)

First ensure that the CSS styles page is linked correctly:

```html
<link rel="stylesheet" href="{% static 'survey_app/css/styles.css' %}">
```

Ensure the view is defined in views.py and the URL pattern is added in urls.py.

2. load static Token Missing

Ensure {% load static %} is included in all forms.

3. JavaScript Not Working
Make sure your script is referenced properly:

```html
<script src="{% static 'survey_app/js/index.js' %}" defer></script>
```