Python Setup
------------

```bash
docker container stop api-demo
docker container rm api-demo
docker rmi api-demo:v1
docker build -t api-demo:v1 -f server.Dockerfile .
docker run -d -p 8000:5000 --name api-demo api-demo:v1
```