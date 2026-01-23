# Shop API - Dockerized

A minimal Flask API sample as a Docker image.


## Prerequisites

- [Docker Desktop](https://docs.docker.com/get-started/introduction/get-docker-desktop/) installed and running


## Build the image

From the project root run:

```bash
docker build -t shop-api .
```


## Run the container

```bash
docker run -p 5000:5000 --name shop-api shop-api
```


## Access the application

Once running, open your browser and go to:

http://localhost:5000