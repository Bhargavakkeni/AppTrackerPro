<h1>NextLabProject - Problem Set Solutions</h1>

<h2>Problem Set I - Regex</h2>

<h3>Task</h3>

Write a regex to extract all the numbers with an orange color background from the provided JSON text.

<h3>Solution</h3>

The regex to extract numbers with an orange color background is:
```python
re.findall(r':(\d+)',string)
```

<h2>Problem Set II - A Functioning Web App with API</h2>

<h3>Description</h3>

This project consists of a Django web application with API endpoints. It includes an Admin Facing component where an admin user can add Android apps and assign points, and a User Facing component where users can view added apps, points, and complete tasks.

<h3>Features</h3>

REST API with proper permissions and authentication.
Admin Dashboard for adding apps and assigning points.
User Dashboard with signup, login, profile, points earned, tasks completed, and screenshot upload.

<h3>
Installation
<h3>

Clone the repository:
```python
git clone https://github.com/Bhargavakkeni/NextLabProject.git
```
Navigate to the project directory:
```
cd webapp
cd nextlabproject
```

Install dependencies:
```python
pip install -r requirements.txt
```
Run migrations:
```python
python manage.py migrate
```
<h3>Usage</h3>

Run the development server:
```python
python manage.py runserver
```

The application will be accessible at <a>http://localhost:8000/home</a>

<h2>Documentation</h2>
For detailed documentation, please navigate to: <b><i>webapp\nextlabproject\builddir</b></i>


then run <b><i>index.html</i></b> by double clicking it or run it from any text editor tools like VSCode, notepad++

<h2>Problem Set III - Questions</h2>

<h3>System to Schedule Periodic Tasks</h3>

I chose APScheduler for scheduling periodic tasks. It's a lightweight, easy-to-use library for scheduling tasks in Python applications. It supports various types of triggers, including cron-like expressions, and integrates seamlessly with Django.

<h3>Flask vs Django</h3>

Use Flask for lightweight applications or microservices where simplicity and flexibility are crucial. Use Django for larger, feature-rich applications with built-in components like ORM, admin interface, and batteries-included approach.
