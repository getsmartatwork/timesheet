# timesheet Project


## Follow the commands to setup the project in local environment

### create virtual environment outside the project
`python3 -m venv timesheet`

### activate environment
`timesheet\Scripts\activate`

### navigate to project root directory
`cd timesheet`

### install requirements
`pip install -r requirements.txt`

### do migrations
`python manage.py migrate`

### runing the server
`python manage.py runserver`


CREATE DATABASE timesheetdb;

CREATE USER timesheetdbuser WITH PASSWORD 'admin12345';

ALTER ROLE timesheetdbuser SET client_encoding TO 'utf8';
ALTER ROLE timesheetdbuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE timesheetdbuser SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE timesheetdb TO timesheetdbuser;

\q

