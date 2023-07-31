## Get Driveing API

This is the accompanying database to go with my frontend website created with React (GetDriveing). GetDriveing pulls the json data from this django rest framework and manipulates it to provide the necessary CRUD, filter, sort and search functionality to the user.

Get Driveing Frontend website screenshot:
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1689887554/Screenshot_2023-07-20_at_22.12.20_slwv6q.png" width = 95% alt="Sample views of GetDriveing website"></a>

Link to deployed site: <a href="https://get-drive-ing-36f2443ac236.herokuapp.com/" target="new" aria-label="Deployed GetDriveing website">https://get-drive-ing-36f2443ac236.herokuapp.com/</a>

Link to deployed database: <a href="https://getdriveing-6933e088a46d.herokuapp.com/" target="new" aria-label="Deployed GetDriveing website">https://getdriveing-6933e088a46d.herokuapp.com/</a> 

GetDriveing Github Repository (see that ReadMe for more details about this project): <a href="https://github.com/MandyHole/getdriveing" target="new" aria-label=" GetDriveing GitHub Repository">https://github.com/MandyHole/getdriveing</a> 

Link to Agile Planning Project Board for front-end user stories: https://github.com/users/MandyHole/projects/5

## Contents
<a href="#structure" aria-label="Jump to Database Structure">Database Structure</a><br>
<a href="#user" aria-label="Jump to Developer User Stories">Developer User Stories</a><br>
<a href="#endpoint" aria-label="Jump to Endpoint/User Story Testing">Endpoint/User Story Testing</a><br>
<a href="#languages" aria-label="Jump to Languages & Frameworks Used">Languages & Frameworks Used</a><br>
<a href="#code" aria-label="Jump to Code Testing">Code Testing</a><br>
<a href="#bugs" aria-label="Jump to Known Bugs">Known Bugs</a><br>
<a href="#deploy" aria-label="Jump to Deployment & Local Development">Deployment & Local Development</a><br>
<a href="#credits" aria-label="Jump to Credits">Credits</a><br>
<a href="#info" aria-label="Jump to Credits">Further Information</a><br>






<h2 id=structure> Database Structure</h2>
The overall structure of the project was modelled from from the <a href="https://github.com/Code-Institute-Solutions/drf-api" aria-label="Go to drf-api repository; opens in new window" target="new"> drf-api walkthrough</a>. 

<ul>
<li><a href="https://res.cloudinary.com/dd4cchm7g/image/upload/v1689634279/Models_stt0lf.png" aria-label="a mockup of the Database models relationship" target="new">Mockup of database models relationship</a> </li>
<li><a href="https://res.cloudinary.com/dd4cchm7g/image/upload/v1689634288/crud_sfem7l.png" aria-label="a mockup of CRUD functionality" target="new">Mockup of CRUD functionality</a> </li></ul>


<h2 id="user"> Developer User Stories</h2>

Below is the functionality that I wanted for the frontend of the website; these were tested by reviewing the endpoints (see next section).<br>

### Authors
As a developer using this backend database, I want to fetch the data from authors so that I can display it to users.<br>
As a developer using this backend database, I want to protect the author data so it can only be edited by the owner.<br>

### Comments
As a developer using this backend database, I want to fetch all comments made related to a specific tip <br>
As a developer using this backend database, I want to fetch a specific comment<br>
As a developer using this backend database, I want to protect the comment data so it can only be edited/deleted by the owner.<br>
As a developer using this backend database, I want logged in users to be able to add comments to the database.<br>

### Rating
As a developer using this backend database, I want to access a list of ratings.<br>
As a developer using this backend database, I want a unique relationship between a rating and a specific tip so a user can only rate a tip once.<br>
As a developer using this backend database, I want to protect the rating data so it can only be edited/deleted by the owner.<br>
As a developer using this backend database, I want logged in users to be able to rate tips.<br>
As a developer using this backend database, I want to access a specific rating. <br>


### Saved Tips
As a developer using this backend database, I want a unique relationship between a saved tip and a specific tip so a user can only save a tip once.<br>
As a developer using this backend database, I want to protect the saved tip data so it can only be deleted by the owner.<br>
As a developer using this backend database, I want logged in users to be able to save a tip.<br>
As a developer using this backend database, I want a list of all saved tips.<br>
As a developer using this backend database, I want to access a specific saved tip.<br>



### Tips
As a developer using this backend database, I want to fetch the data from tips so that I can display it to users.<br>
As a developer using this backend database, I want logged-in users to add a tip.<br>
As a developer using this backend database, I want to protect the tip data so it can only be edited/deleted by the owner.<br>
As a developer using this backend database, I want an average of the ratings to be calculated to display back to the users.<br>
As a developer using this backend database, I want the sum of times a tip has been saved to be calculated and displayed back to the users.<br>
As a developer using this backend database, I want the tips to be filtered (by ability, category, saved tip ownership and author) as well as ordered (by date created, star rating and number of saves) and searched.<br>


<h2 id=endpoint> Endpoint/User Story Testing</h2>

### / 
Expected: message stating "You are accessing the database for GetDriveing"
Pass
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690468158/Screenshot_2023-07-27_at_15.27.48_xfj8jq.png" alt="Screenshot of /">


### /authors (get request)

User story: As a developer using this backend database, I want to fetch the data from authors so that I can display it to users - pass<br>

<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690468365/Screenshot_2023-07-27_at_15.32.34_k7khdj.png" alt="Screenshot of /authors/">

### /authors/id (get request)
User story: As a developer using this backend database, I want to fetch the data from authors so that I can display it to users - pass<br>
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690468713/Screenshot_2023-07-27_at_15.38.22_yoldvl.png" alt="Screenshot of /authors">

### /authors/id (put request)
User story: As a developer using this backend database, I want to protect the author data so it can only be edited by the owner - Pass<br>
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690468614/Screenshot_2023-07-27_at_15.36.02_phejdn.png" alt="Screenshot of /authors/id if owner">
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690468615/Screenshot_2023-07-27_at_15.36.12_rjtrxz.png" alt="Screenshot of /authors/id if not owner">

### /comments (get request)

User story: As a developer using this backend database, I want to fetch all comments made related to a specific tip - Pass<br>
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690468862/Screenshot_2023-07-27_at_15.40.29_ifa4um.png" alt="Screenshot of /comments">

### /comments (post request)
User story: As a developer using this backend database, I want logged in users to be able to add comments to the database. - pass <br>
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690468972/Screenshot_2023-07-27_at_15.42.00_gw3rna.png" alt="Screenshot of add comment form - logged in at /comments">
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690468973/Screenshot_2023-07-27_at_15.42.09_lympc0.png" alt="Screenshot with no add comment form and prompt to login at /comments">

### /comments/id (get request)
User story: As a developer using this backend database, I want to fetch a specific comment - pass<br>
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690469375/Screenshot_2023-07-27_at_15.46.34_tksukv.png" alt="Screenshot of /comments/id">

### /comments/id (put/delete request)
User story: As a developer using this backend database, I want to protect the comment data so it can only be edited/deleted by the owner. pass <br>
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690469375/Screenshot_2023-07-27_at_15.46.34_tksukv.png" alt="Screenshot of /comments/id when logged in">
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690469390/Screenshot_2023-07-27_at_15.49.04_alefkq.png" alt="Screenshot of /comments/id when logged out">

### /rating (get request)

User story: As a developer using this backend database, I want to access a list of ratings. pass <br>
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690469983/Screenshot_2023-07-27_at_15.57.00_vqv0re.png" alt="Screenshot of /rating">

### /rating (post request) 
User story: As a developer using this backend database, I want logged in users to be able to rate tips. pass <br>
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690469983/Screenshot_2023-07-27_at_15.57.10_f3hkl0.png" alt="Screenshot of add rating form - logged in at /rating">
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690469983/Screenshot_2023-07-27_at_15.57.00_vqv0re.png" alt="Screenshot with no add rating form and prompt to login at /rating">

User story: As a developer using this backend database, I want a unique relationship between a rating and a specific tip so a user can only rate a tip once.<br> pass <br>
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690472503/Screenshot_2023-07-27_at_16.38.43_jwfxbz.png" alt="Screenshot with error as already rated that tip /rating">


### /rating/id (get request)

User story: As a developer using this backend database, I want to access a specific rating. pass <br>
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690469984/Screenshot_2023-07-27_at_15.57.34_oy5es6.png" alt="Screenshot of /rating/id">

### /rating/id (put/delete request)

User story: As a developer using this backend database, I want to protect the rating data so it can only be edited/deleted by the owner. pass<br>

<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690469984/Screenshot_2023-07-27_at_15.57.28_z75ury.png" alt="Screenshot of /comments/id when logged in">
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690469984/Screenshot_2023-07-27_at_15.57.34_oy5es6.png" alt="Screenshot of /rating/id when logged out">

### /saved_tips (get request)

User story: As a developer using this backend database, I want a list of all saved tips. pass<br>
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690470512/Screenshot_2023-07-27_at_16.05.02_ethqol.png" alt="Screenshot of /saved_tips">

### /saved_tips (post request)
User story: As a developer using this backend database, I want logged in users to be able to save a tip. pass<br>
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690470512/Screenshot_2023-07-27_at_16.05.10_h8h1yr.png" alt="Screenshot of save tip form - logged in at /saved_tips">
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690470512/Screenshot_2023-07-27_at_16.05.02_ethqol.png" alt="Screenshot with no save tip form and prompt to login at /saved_tips">
User story: As a developer using this backend database, I want a unique relationship between a saved tip and a specific tip so a user can only save a tip once. pass <br>
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690473114/Screenshot_2023-07-27_at_16.51.36_tkbflk.png" alt="Screenshot with an error as already saved that tip">


### /saved_tips/id (get request)

User story: As a developer using this backend database, I want to access a specific saved tip. pass <br>

<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690470600/Screenshot_2023-07-27_at_16.09.49_lg0xjd.png" alt="Screenshot of /saved_tips/id">

### /saved_tips/id (delete request)

User story: As a developer using this backend database, I want to protect the saved tip data so it can only be deleted by the owner. pass <br>
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690470599/Screenshot_2023-07-27_at_16.09.44_j8svsm.png" alt="Screenshot of /saved_tips/id when logged in">
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690470600/Screenshot_2023-07-27_at_16.09.49_lg0xjd.png" alt="Screenshot of /saved_tips/id when logged out">

### /tips (get request)

User story: As a developer using this backend database, I want to fetch the data from tips so that I can display it to users. pass<br>
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690470800/Screenshot_2023-07-27_at_16.12.38_wdx56r.png" alt="Screenshot of /tips">
User story: As a developer using this backend database, I want the tips to be filtered (by ability, category, saved tip ownership and author) as well as ordered (by date created, star rating and number of saves) and searched. pass <br>
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690471141/Screenshot_2023-07-27_at_16.18.03_x9zzp8.png" alt="Screenshot of filter menu available from /tips">


User story: As a developer using this backend database, I want an average of the ratings to be calculated to display back to the users. pass<br>
User story: As a developer using this backend database, I want the sum of times a tip has been saved to be calculated and displayed back to the users. pass <br>
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690473829/Screenshot_2023-07-27_at_17.03.39_fw6nop.png" alt="Screenshot of filter menu available from /tips">

### /tips (post request)
User story: As a developer using this backend database, I want logged-in users to add a tip. pass<br>
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690470801/Screenshot_2023-07-27_at_16.12.46_egsk5g.png" alt="Screenshot of add a tip form - logged in at /tips">
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690470800/Screenshot_2023-07-27_at_16.12.38_wdx56r.png" alt="Screenshot with no add a tip form and prompt to login at /tips">


### /tips/id (get request)

User story: As a developer using this backend database, I want to fetch the data from tips so that I can display it to users. pass<br>
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690470971/Screenshot_2023-07-27_at_16.15.50_pu6jrv.png" alt="Screenshot of /tips/id">

### /tips/id (put/delete requests)
User story: As a developer using this backend database, I want to protect the tip data so it can only be edited/deleted by the owner. pass <br>
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690470972/Screenshot_2023-07-27_at_16.15.41_hhyibd.png" alt="Screenshot of /tips/id when logged in">
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1690470971/Screenshot_2023-07-27_at_16.15.50_pu6jrv.png" alt="Screenshot of /tips/id when logged out">




<h2 id="languages">Languages & Frameworks Used</h2>
<ul>
<li>Python</li>
<li><strong>Django Rest Framework</strong> to compile json data for the frontend website</li>
</ul>

<h2 id="code"> Code Testing </h2>
<p id="python"><strong>Python:</strong> Tested the pages I created/used with Pycode Style (no errors found). See steps below:</p>
<ul><li>In the terminal, check you have pycodestyle installed by running: pip install pycodestyle</li>
<li>In the terminal, run pycodestyle *ADD RELATIVE FILE/FOLDER PATH HERE* for each of the pages you wish to check until no errors are found (see examples below). NB there were issues with line length in the automatically generated migration files.</li><ul>
<li>pycodestyle authors</li>
<li>pycodestyle comments</li>
<li>pycodestyle drive_api</li>
<li>pycodestyle rating</li>
<li>pycodestyle saved_tips</li>
<li>pycodestyle tips</li>
</ul>
</ul>

<h2 id=bugs>Known Bugs</h2>

The Sign In functionality on the front-end website doesn't work on Safari unless the "Prevent Cross-Site tracking" option is turned off (Settings -- Safari -- Privacy and Security) due to the nature of how it was deployed from two repositories.

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

Visit the repo (https://github.com/MandyHole/drive_data) and click the 'Fork' button in the top right part of the screen. You may need to sign in to Github.

<h3 id="clone">How to clone this repo</h3>

Visit the repo (https://github.com/MandyHole/drive_data) and click the green 'Code' button above the list of files. Click on the 'local' and select from the following options: HTTPS, SSH and GitHub CLI. Copy the link. Open the terminal in your code editor, ensuring the current working directory is where you want the files, and type git clone and paste in the copied URL before clicking enter.

<h2 id="credits">Credits</h2>

Stack Overflow: https://stackoverflow.com/questions/59339485/django-rest-framework-ordering-set-the-location-of-none-values/59341084#59341084: to correctly order null values when sorting by average rating / number of saves.

Code Institute: for providing the drf-api walkthrough project and the help the tutor team provided to help troubleshoot the above-mentioned issue. Also, for general inspiration and support from the programme and mentor.

<h2 id="info">Further information</h2>

For further information about how this api was used, please see the ReadMe for my GetDriveing Github Repository: <a href="https://github.com/MandyHole/getdriveing" target="new" aria-label=" GetDriveing GitHub Repository">https://github.com/MandyHole/getdriveing</a> 