Local Docker Setup
------------------

1. Uvicorn

```bash
docker container stop api-demo
docker container rm api-demo
docker rmi api-demo:v1
docker build -t api-demo:v1 -f server.Dockerfile .
docker run -d -p 8000:5000 --name api-demo api-demo:v1
```

2. Gunicorn

```bash
docker container stop fastapi_gunicorn
docker container rm api-demo
docker rmi api-demo:v1.2
docker build -t api-demo:v1.2 -f gunicorn.Dockerfile .
docker run -d -p 8000:5000 --name fastapi_gunicorn api-demo:v1.2
```