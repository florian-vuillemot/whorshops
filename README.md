# Quick Docker workshop

This workshop is for people that already have theorical knowledge of Docker and docker-compose and want to practice with someone that already know Docker and docker compose.
Best practices are *out of the scope* !

## Install Docker and docker compose

Go on `docker.com` and install Docker and docker-compose
- Docker: https://docs.docker.com/desktop/
- Docker-Compose: https://docs.docker.com/compose/install/


## The Tags App

This application is a really simple example of a small tag application for Azure. 
The goal of this application is just to show with a intern app the capabilities of Docker. 

## Step 0: Write, build and run a Docker

First we will build and run a simple Docker container.

1. In the terminal, run `docker pull ubuntu`. This will pull the `ubuntu` image on your laptop.
2. You can see all your images with `docker images`
3. Now you can use Docker to generate your container from the image with `docker run -it ubuntu`
4. Enjoy your Ubuntu shell ! You can now run commands like `ls`, `cd` or `apt`

Now you know how to pull an image and run a container. Running an Ubuntu shell is good but it's not enought, we want to run the application !

Go in the `step0` folder and read the `Dockerfile`.
You can build it with: `docker build -t step0 .`.
This file allows you to create Docker image as you need for your application.
You can now run it with the command: `docker run step0`

## Step 1: Docker-compose

In the `step1` folder you will see a Dockerfile with more fonctionalities.
It creates a Docker image with the `tags` application able to run.

Directly launching the Docker command line could be difficult and time consuming. 
So we added the file `docker-compose` beside the Dockerfile. Open it and try to understand its goal.
You will see some interesting elements like `ports` that allows communication between the computer and the containers.

You can run it with: `docker-compose up --build` and see the result in your browser with `localhost:8000`.


## Step 2: Multi stages

In this folder you will see the multi stages composition in Docker. This allows you to obtain small and dedicated images.
You can see the `test` stage. This will allow you to run your application tests before creating the image.
It's a really powerfull feature that allows you to separate your build, test and running components of your application.

## Step 3: Env variable

This step shows you how to provide Env variable to your application with Docker compose. 
This is really important because thanks to this feature you don't have to change your code between env.
The env file is `.env`.

## Step 4: Volumes

Actually, when you stop your container you will lose all your data. This comes from the fact that container are by default stateless.
You can bypass this behaviour thanks to volumes that allow you to persist data (files and directories).

In this example, you can also show how to make a migration in a container environment without manually accessing the container. 


## Step 5: Multiple Containers 

This step updates the application to use a PostgreSQL database and not SQLite.
This allows you to show the networking configuration that allows to segregate applications and limit access.
