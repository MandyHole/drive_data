## Get Driveing API

This is the accompanying database to go with my frontend website created with React (GetDriveing). GetDriveing pulls the json data from this django rest framework and manipulates it to provide CRUD functionality to the user.

Get Driveing Frontend website screenshot:
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1689448397/Screenshot_2023-07-15_at_20.12.59_w3qytx.png" width = 15% alt="GetDriveing Logo"></a>

Link to deployed site: <a href="https://get-drive-ing-36f2443ac236.herokuapp.com/" target="new" aria-label="Deployed GetDriveing website">https://get-drive-ing-36f2443ac236.herokuapp.com/</a>

Link to deployed database: <a href="https://getdriveing-6933e088a46d.herokuapp.com/" target="new" aria-label="Deployed GetDriveing website">https://getdriveing-6933e088a46d.herokuapp.com/</a> 

GetDriveing Github Repository (see that ReadMe for more details about this project): <a href="https://github.com/MandyHole/getdriveing" target="new" aria-label=" GetDriveing GitHub Repository">https://github.com/MandyHole/getdriveing</a> 


<h2 id="languages">Languages & frameworks Used</h2>
<ul>
<li>Python</li>
<li><strong>Django Rest Framework</strong>to compile json data for the frontend website</li>
</ul>

<h2> Testing </h2>
<p id="python"><strong>Python:</strong> Tested the pages I created/used with Pycode Style (no errors found). See steps below:</p>
<ul><li>In the terminal, check you have pycodestyle installed by running: pip install pycodestyle</li>
<li>In the terminal, run pycodestyle *ADD RELATIVE FILE/FOLDER PATH HERE* for each of the pages you wish to check until no errors are found (see examples below). NB there were issues with line length in the automatically generated migration files and in the default settings (drive_api/settings.py).</li><ul>
<li>pycodestyle authors</li>
<li>pycodestyle comments</li>
<li>pycodestyle drive_api</li>
<li>pycodestyle saved_tips</li>
<li>pycodestyle tips</li>
</ul>
</ul>

<h2 id="deploy"> Deployment & Local Development</h2>

<h3 id="deployment">Deployment</h3>
This project was deployed through Heroku (live link found here: <a href="https://getdriveing-6933e088a46d.herokuapp.com/" target="new" aria-label="Deployed site">https://getdriveing-6933e088a46d.herokuapp.com/)</a> using the following steps:
<ol>
<li>Login / Sign up to Heroku</li>
<li>Click New -- Create New App</li>
<li>Name your app (must be unique), select your nearest region and click “Create app” to confirm.</li>
<li>Go to settings and add the following Key/Data information (which match the information in your env.py file that should be set up to be ignored by git), to the config vars:<ul>
<li>ALLOWED_HOST (for example getdriveing-6933e088a46d.herokuapp.com)
<li>CLIENT_ORIGIN (link to your deployed frontend website, eg: https://get-drive-ing-36f2443ac236.herokuapp.com)
<li>CLIENT_ORIGIN_DEV (link to your frontend website's local development - this may change so you may need to update it if it stops working)</>
<li>DATABASE_URL (from your database, eg elephant sql)</li>
<li>SECRET_KEY</li>
<li>CLOUDINARY_URL (from your Cloudinary account)</li>
<li>DISABLE_COLLECTSTATIC (1) if you haven't added static files yet. NB This can be removed once you deploy your site</li>
</ul></li>
<li>Add your Heroku app and local host to the 'Allowed Hosts' section of the settings.py file (example below)<ul><li>ALLOWED_HOSTS = [
    'localhost',
    os.environ.get('ALLOWED_HOST'),
    ]
</li></ul></li>
<li>Create a Profile in the main directory with the following info:  release: python manage.py makemigrations && python manage.py migrate
 web: gunicorn drive_api.wsgi where 'drive-api' is the name of your project</li>
<li>Add/Commit/Push all changes to Github</li>
<li>Click Deploy in the Heroku App dashboard - then deploy via Github - connect to the repository, scroll down and click on deploy branch</li>
</ol>

<h3 id="fork">How to fork this repo</h3>

Visit the repo (https://github.com/MandyHole/school-clubs) and click the 'Fork' button in the top right part of the screen. You may need to sign in to Github.

<h3 id="clone">How to clone this repo</h3>

Visit the repo (https://github.com/MandyHole/school-clubs) and click the green 'Code' button above the list of files. Click on the 'local' and select from the following options: HTTPS, SSH and GitHub CLI. Copy the link. Open the terminal in your code editor, ensuring the current working directory is where you want the files, and type git clone and paste in the copied URL before clicking enter.