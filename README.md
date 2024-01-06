<h1>App Tracker Pro</h1>

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


<h2>Deployment</h2>

I facilitated the deployment of this project using the railway.app web application, establishing a seamless connection to our GitHub repository and automating the deployment process by generating a Docker image. Importantly, each new commit made to the main/master branch triggers an automatic update of the Docker image on railway.app. For easy access, the live version of the project can be explored at the following link:

<a>https://deploynextlabproject-production.up.railway.app/</a>. 

To register as an admin user, please use this link:
 
<a> https://deploynextlabproject-production.up.railway.app/home/registeradmin</a>.

<h2>Screen Recording<h2>

Link to the screen recording:
<a>https://screenrec.com/share/uFTfarm9ek</a>
