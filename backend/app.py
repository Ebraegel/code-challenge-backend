from flask import Flask, request, jsonify
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
    return "Healthy!\n"


@app.route('/')
def hello():
    return "Hello!\n"


@app.route('/incidents')
# 15-minute cache for unique requests
@cache.cached(timeout=900, key_prefix=lambda: request.url)
def incidents():
    incident_list = TrafikApiClient().list_incidents()
    if 'lat' in request.args and 'long' in request.args:
        user_lat = request.args.get('lat')
        user_long = request.args.get('long')
        distance = request.args.get('distance') or 30
        incident_list = filter_locations_by_distance(locations=incident_list,
                                                     lat=user_lat,
                                                     long=user_long,
                                                     max_distance=distance)

    return jsonify(incident_list)
