from flask import Flask, request
from flask_cors import CORS
from flask_caching import Cache

from code_challenge_backend.distance_filterer.distance_filterer import filter_locations_by_distance
from code_challenge_backend.sr_api_client.client import TrafikApiClient

app = Flask(__name__)
CORS(app)

cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
cache.init_app(app)

@app.route('/healthcheck')
def healthcheck():
    return "Healthy!"

@app.route('/')
def hello():
    return "Hello!"


@app.route('/incidents')
@cache.cached(timeout=900)
def incidents():
    incident_list = TrafikApiClient().list_incidents()

    if 'lat' in request.args and 'long' in request.args:
        user_lat = request.args.get('lat')
        user_long = request.args.get('long')
        incident_list = filter_locations_by_distance(locations=incident_list, lat=user_lat, long=user_long, max_distance=30)

    # can we just return a top-level list? seems nicer
    # https://stackoverflow.com/questions/13081532/return-json-response-from-flask-view
    return {"incidents": incident_list}
