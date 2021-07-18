# Doro Backend Code Challenge
Developer documentation for the backend code challenge.

## Prerequisites
* [Docker](https://docs.docker.com/get-docker/)

## Running the app locally
```shell
./bin/run
```
### UI
http://localhost:5000
### Backend
```shell
curl localhost:5000/healthcheck
curl localhost:5000/incidents
```

## Debugging
### Watching Container Logs
```shell
docker-compose logs -f
```
### Python
Set a breakpoint in your python code with `import pdb; pdb.set_trace()`
Then, attach to the running container:
```shell
docker attach backend
```
To detach without killing the process, use `Ctrl`+`P` then `Ctrl`+`Q`, instead of `Ctrl`+`C`.


## Testing
### Backend
In Docker
```shell
./bin/test
```

Locally
```shell
cd backend
pip3 install -r requirements.txt
pytest
```
