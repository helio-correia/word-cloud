# Word Cloud

This project will show you the top words that are surfing the web.
As a client you can see the top 100 words of a website of your choice.
As an admin you can see the top words of every website that clients searched.

## Setup

### Requirements

In this project I use docker and docker-compose because I think it's the fastest way to run the project in every environ.
If don't have this two installed, visit the [official website](https://docs.docker.com/compose/install/)

The following codes can be shorted but we use like this to prevent the error when te server starts before the db service

### Steps

```
docker-compose up --no-start
docker-compose start db
docker-compose run --rm web python manage.py migrate
docker-compose start web
```

## Instructions

### Client

In the client just go to the home page and type a valid url on the input, after hitting submit you will see the top 100 words.


### Admin

#### Create a super user

In the terminal on the root of the project run the command `docker-compose run --rm web python manage.py createsuperuser` and follow the instructions.
After that, access to admin page on the /admin/, login and you will see the words menu with every word and its repetitions.