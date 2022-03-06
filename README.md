# Pastebin Clone
this is a [Pastebin](https://pastebin.com/) clone where users can store plain text.

## General Requirements
* clone the project and go to the project directory using your terminal / CMD
* [Docker](https://docs.docker.com/get-docker/)

## Project Setup
* Copy the content of `.env.template` file and paste into the new created file `.env`
* In `.env` change all configurations to your desired configurations
* Run : `docker build .`
* Run : `docker-compose build` to build the docker image.
* Run : `docker-compose up`.

## Project Docs
* The documetation should be now running under `http://127.0.0.1:8000/docs` (if port 8000 is available)

## Authentication
* Create account from: `http://127.0.0.1:8000/auth/register/`.
* Go to `http://127.0.0.1:8000/auth/login-with-token/` to get user token.
* Then go to swagger authorize part and type: `Bearer <YOUR_TOKEN>`, now you are logged in:
* HINT: i made the authentication with JWT beacouse i can't understand the point of login with github, i send a following up email but i got no respond.

## Access the endpoints from CLI
* `docker-compose run web sh -c "python manage.py list_pastes"`, will list all pastes in the system.
* `docker-compose run web sh -c "python manage.py access_list"`, will ask you to input the paste slug.
* `docker-compose run web sh -c "python manage.py statistics"`, will shows statistics about the top 5 users (username and pastes count).

## Run Tests
* To Run unit tests : `docker-compose run web sh -c "python manage.py test"`.


## Admin Dashboard
* To access Admin dashboard : `http://127.0.0.1:8000/admin` and the admin credentials are: `admin`, `admin@1234`.