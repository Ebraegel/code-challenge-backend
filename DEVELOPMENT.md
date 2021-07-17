# Doro Backend Code Challenge
Developer documentation for the backend code challenge.

## Prerequisites
* [Docker](https://docs.docker.com/get-docker/)

## Running the app locally
```shell
./bin/run
```
This will start the backend api server on localhost:5000 and the ui on localhost:3000, and hot-reload after changes.


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

### React
???


