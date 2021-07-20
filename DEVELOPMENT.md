# Doro Backend Code Challenge
Developer documentation for the backend code challenge.

## Prerequisites
* [Docker](https://docs.docker.com/get-docker/)

## Running the app locally
```shell
./bin/run
```
### UI
* http://localhost:5000

### Backend
* http://localhost:5000/healthcheck
* http://localhost:5000/incidents
* http://localhost:5000/incidents?lat=55.60401900135806&long=13.006521052652744
* http://localhost:5000/incidents?lat=55.60401900135806&long=13.006521052652744&distance=200


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
```shell
./bin/backend-tests
```


### UI
```shell
./bin/ui-tests
```