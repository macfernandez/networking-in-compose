# Timestamp Converter

## About this repo

Repo with an API for converting UNIX timestamps to date and time, and vice versa.
The aim of is repo has to practice the networking between containers.


```
root
 |__ images                 # containers images
 |    |__ base              # base image for back and front
 |    |    |__ Dockerfile
 |    |
 |    |__ app               # backend container  
 |    |    |__ Dockerfile
 |    |
 |    |__ web               # frontend container
 |         |__ Dockerfile
 |
 |__ src                    # source code
      |__ app               # backend
      |    |__ app
      |    |__ setup.py
      |
      |__ web               # frontend
           |__ web
           |__ setup.py
```

## Run

For building the containers:

```
make build-web
```

For running:
```
make run-web
```

## Useful links

- [Docker: Networking in Compose](https://docs.docker.com/compose/networking/)
- [FastAPI: FastAPI in Containers - Docker](https://fastapi.tiangolo.com/deployment/docker/)
- [Medium: Docker Compose Network](https://medium.com/@caysever/docker-compose-network-b86e424fad82)
