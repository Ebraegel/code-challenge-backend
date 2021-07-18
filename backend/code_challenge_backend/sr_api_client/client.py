import requests

class TrafikApiClient:
    BASE_URL = "http://api.sr.se/api/v2/traffic"
    DEFAULT_PARAMS = {"pagination": "false", "format": "json"}
    def __init__(self, base_url = BASE_URL, default_params = DEFAULT_PARAMS):
        self._base_url=base_url
        self._default_params = default_params

    def list_incidents(self):
        """Returns a list of all incidents from the SR traffic API"""
        url = self._base_url + "/messages"
        print("getting traffic incidents from SR API")
        response = requests.get(url, params=self._default_params)
        if response.ok:
            return response.json()['messages']
        else:
            return []
