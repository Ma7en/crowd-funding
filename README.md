<h1 align="center" id="title">Crowd Funding Web App - ITI</h1>

<h2 id="description">Description</h2>

<p>
This project aims to create a comprehensive online crowdfunding platform specifically designed for the Egyptian market. The platform will enable individuals and organizations to launch fundraising campaigns for various projects, while allowing users to contribute to these initiatives. Key features include a user-friendly interface, secure authentication, robust project management tools, and a variety of options for users to engage with and support campaigns. By providing a centralized platform for crowdfunding in Egypt, this project seeks to foster community engagement, support innovative ideas, and facilitate economic development. 
</p>

## 🔧 Github Commands :-

`Step 1` : SSH Configuration.

```
ssh-keygen -t ed25519 -C "ex@gmail.com"
```

```
cat ~/.ssh/id_ed25519.pub
```

```
git config --global user.email "ex@gmail.com"
```

```
git config --global user.name "ex"
```

`Step 2` : Starting Git.

```
git init
```

```
git add .
```

```
git commit -m "first commit"
```

```
git branch -M main
```

```
git remote add origin git@github.com:Ma7en/crowd-funding.git
```

```
git push -u origin main
```

`Step 3` : Clone.

```
git clone git@github.com:Ma7en/crowd-funding.git
```

`Step 4` : Pull.

```
git pull -r origin main
```

```
Accept Both Changes
```

```
git rebase --continue
```

```
git config --global pull.rebase true
```

`Step 5` : Tag.

```
git checkout main
```

```
git tag
```

```
git tag -a v1.0 -m "Version 1.0"
```

```
git push origin v1.0
```

---

## 🛠️ Installation Steps :-

<h3 align="center"> Ubuntu </h3>

`Step 1` : Install and activate VirtualEnvironment.

```
pip install virtualenv
```

```
virtualenv venv
```

```
source venv/bin/activate
```

`Step 2` : Install Packages.

```
pip install django
```

```
pip install --upgrade pip
```

```
pip install psycopg2-binary
```

```
pip install pillow
```

```
pip install django-crispy-forms
```

```
pip install crispy-bootstrap5
```

```
pip install djangorestframework
```

```
pip install fontawesomefree
```

```
pip install django-jquery
```

```
pip install django-cleanup
```

```
pip install django-utils-six
```

```
pip install social-auth-app-django
```

```
pip install django-allauth
```

```
pip install python-dotenv
```

```
pip install django-countries
```

`Step 3` : Install requiremental Packages.

```
pip freeze > requirements.txt
```

```
pip install -r requirements.txt
```

`Step 4` : Create Project.

```
django-admin startproject crowdfunding
```

```
cd crowdfunding
```

`Step 5` : Create Apps.

```
python3 manage.py startapp account
```

```
python3 manage.py startapp projects
```

```
python3 manage.py startapp home
```

```
python3 manage.py startapp Feedback
```

`Step 6` : Create Database.

```
su - postgres
```

```
psql
```

```
CREATE USER django_proj WITH PASSWORD 'django@@1';
```

```
create database crowd_funding;
```

```
\c crowd_funding;
```

```
GRANT ALL PRIVILEGES ON DATABASE crowd_funding TO django_proj;
```

```
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO django_proj;
```

```
GRANT ALL PRIVILEGES ON SCHEMA public TO django_proj;
```

```
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO django_proj;
```

`Step 7` : Create Migrate.

```
python3 manage.py makemigrations
```

```
python3 manage.py migrate
```

```
python3 manage.py createsuperuser
```

`Step 8` : Run Server.

```
python3 manage.py runserver
```

<h3 align="center"> Windows </h3>

`Step 1` : Install and activate VirtualEnvironment.

```
pip install virtualenv
```

```
virtualenv wvenv
```

```
wvenv\Scripts\activate
```

`Step 2` : Install Packages.

```
pip install django
```

```
pip install --upgrade pip
```

```
pip install psycopg2-binary
```

```
pip install pillow
```

```
pip install django-crispy-forms
```

```
pip install crispy-bootstrap5
```

```
pip install djangorestframework
```

```
pip install fontawesomefree
```

```
pip install django-jquery
```

```
pip install django-cleanup
```

```
pip install django-utils-six
```

```
pip install social-auth-app-django
```

```
pip install django-allauth
```

```
pip install python-dotenv
```

```
pip install django-countries
```

`Step 3` : Install requiremental Packages.

```
pip freeze > wrequirements.txt

```

```
pip install -r wrequirements.txt
```

`Step 4` : Create Project.

```
django-admin startproject crowdfunding
```

```
cd crowdfunding
```

`Step 5` : Create Apps.

```
python manage.py startapp account
```

```
python manage.py startapp projects
```

```
python manage.py startapp home
```

```
python manage.py startapp Feedback
```

`Step 6` : Create Database.

```
su - postgres
```

```
psql
```

```
CREATE USER django_proj WITH PASSWORD 'django@@1';
```

```
create database crowd_funding;
```

```
\c crowd_funding
```

```
GRANT ALL PRIVILEGES ON DATABASE crowd_funding TO django_proj;
```

```
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO django_proj;
```

```
GRANT ALL PRIVILEGES ON SCHEMA public TO django_proj;
```

```
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO django_proj;
```

`Step 7` : Create Migrate.

```
python manage.py makemigrations
```

```
python manage.py migrate
```

```
python manage.py createsuperuser
```

`Step 8` : Run Server.

```
python manage.py runserver
```

---

## 🧐 Features :

<ul>
<li>
    <b>User Authentication:</b> Secure registration, login, and password recovery.
</li>

<li>
    <b>Project Creation:</b> Users can launch fundraising campaigns with detailed information.
</li>
<li>
    <b>Project Management:</b> Features for viewing, commenting, rating, and reporting projects.
</li>
<li>
    <b>Donations:</b> Users can contribute to project targets. 
</li>
<li>
    <b>Homepage:</b> Displays featured, latest, and categorized projects. 
</li>
<li>
    <b>Search:</b> Allows users to find projects by title or tag. 
</li>
<li>
    <b>Additional Features:</b> Social login, user profiles, and notifications.
</li>
</ul>

---

## 💻 Built with :-

Technologies used in the project:

-   Django Framework
-   Postgres Database
-   HTML
-   CSS
-   JS
-   Bootstrap
-   Fontawesome

---

<table>
    <tr>
        <td>
            <img src="https://avatars.githubusercontent.com/u/15892077?v=4"></img>
        </td>
    </tr>
    <tr>
        <td>
            <a href="https://github.com/josspheenboles">josspheenboles</a>
        </td>
    </tr>
</table>

---

## Contributors

<table>
    <tr>
        <td>
            <img src="https://avatars.githubusercontent.com/u/91129862?v=4"></img>
        </td>
        <td>
            <img src="https://avatars.githubusercontent.com/u/91077855?v=4"></img>
        </td>
        <td>
            <img src="https://avatars.githubusercontent.com/u/171288314?v=4"></img>
        </td>
    </tr>
    <tr>
        <td>
            <a href="https://github.com/Ma7en">Mazen Saad</a>
        </td>
        <td>
            <a href="https://github.com/MichaelAwadEissa">Michael Awad</a>
        </td>
        <td>
            <a href="https://github.com/safasuli01">Safa Abdullah</a>
        </td>
    </tr>
    <tr>
        <td>
            <img src="https://avatars.githubusercontent.com/u/167586570?v=4"></img>
        </td>
        <td>
            <img src="https://avatars.githubusercontent.com/u/144252185?v=4"></img>
        </td>
    </tr>
    <tr>
        <td>
            <a href="https://github.com/gihannazmy">Gihan Atef</a>
        </td>
        <td>
            <a href="https://github.com/Helana-99">Helana Nabil</a>
        </td>
    </tr>
</table>
