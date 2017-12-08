# Word Cloud

This project will show you the top words that are surfing the web.
As a client you can see the top 100 words of a website of your choice.
As an admin you can see the top words of every website that clients searched.

## Setup

### Requirements

In this project I use docker and docker-compose because I think it's the fastest way to run the project in every environ.
If don't have this two installed, visit the [official website](https://docs.docker.com/compose/install/)

The following codes can be shorted but we use like this to prevent the error when te server starts before the db service

```
docker-compose up --no-start
docker-compose start db
docker-compose run --rm web python manage.py migrate
docker-compose start web
```