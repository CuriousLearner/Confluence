# Confluence
This is Confluence of Conference.

# Setup Guide

### Creating a Virtual Environment
Virtual Environment allows us to have requirements installed specifically to our project instead of complete system. To create a virtual environment goto any directory where you will store your code and run the following command on terminal (linux) or Windows PowerShell (Windows)(For windows, run Windows Powershell as Administrator before running below commands)
```
python -m venv venvconf
```
#### Activating the Virtual Environment
Run the following command to activate your virtual environment:
##### Windows
```
./venvconf/Scripts/activate
```
##### Linux
```
source venvconf/bin/activate
```
**Note:** To deactivate the Virtual Environment, type deactivate in the shell to deactivate.
#### Clone your forked repo
```
git clone https://github.com/<github_username>/Confluence
```
##### Change to develop branch
```
git checkout develop
```
Development does not happen on develop branch. It would happen on a feature branch and PRs would be created from feature branch on their fork to the develop branch of this project.

Understand this, as, if many people are working on develop branch in their fork they have to continually rebase to get latest code and place their code on top of it (and solving merge conflicts).

We prefer solving merge conflicts when a single feature is complete (and also would be squashed to a single commit on develop branch)

#### Installing Project Requirements (First Time Only or on Requirement changes)
Change directory to project directory 
```
cd confluence
```
Use pip to install  missing requirements: (if you don't have pip installed on your system, google how to install) (Windows Users should run this command Adminsitrator Shell or will get error)
```
pip install -r requirements.txt
```
#### Creating Environment Variables File
Change directory to src/confluence to create a ".env" file that will contain your enviroment variables.
**Note:** ".env" does not get included in git. That is the whole point of keeping settings as environment variables (because we want to prevent including confidential information on git tree)
```
cd src\confluence
```
Create file ".env" with following data:
```
EXPLARA_API_KEY=<your_explara_key>
FACEBOOK_PAGE_ACCESS_TOKEN=<your_page_access_token>
TWITTER_CONSUMER_KEY=<your_consumer_key>
TWITTER_CONSUMER_SECRET=<your_consumer_secret>
TWITTER_ACCESS_KEY=<your_access_key>
TWITTER_ACCESS_SECRET=<your_access_secret>
```
**Note:** Create your own apps to retrieve these keys for testing.

#### Create Database Migrations

Navigate to root of /src and run the following commands to make database tables.
```
python manage.py makemigrations
python manage.py migrate
```

#### Run Server 
Once all above setup is done, run the following code to start your development server,
```
python manage.py runserver
```

On successful setup you will a line stating ' Starting Development Server at http://127.0.0.1:8000/ '. Visit http://localhost:8000 url on your web browser to see your project in action.