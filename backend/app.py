from flask import Flask
from flask_cors import CORS

from code_challenge_backend.sr_api_client.client import TrafikApiClient

app = Flask(__name__)
CORS(app)

@app.route('/healthcheck')
def healthcheck():
    return "Healthy!"

@app.route('/')
def hello():
    return "Hello!"


@app.route('/incidents')
def incidents():
    incident_list = TrafikApiClient().list_incidents()
    # can we just return a top-level list? seems nicer
    # https://stackoverflow.com/questions/13081532/return-json-response-from-flask-view
    return {"incidents": incident_list}
