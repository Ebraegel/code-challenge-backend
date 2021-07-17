import requests


class TrafikApiClient:
    BASE_URL = "http://api.sr.se/api/v2/traffic"
    DEFAULT_PARAMS = {"pagination": "false", "format": "json"}
    # do I actually want to change this anywhere? maybe these should just all be static members or whatever
    def __init__(self, base_url = BASE_URL, default_params = DEFAULT_PARAMS):
        self._base_url=base_url
        self._default_params = default_params

    # we have no state yet, could be a static method
    def list_incidents(self):
        """Returns a list of all incidents from the SR traffic API"""
        url = self._base_url + "/messages"
        response = requests.get(url, params=self._default_params)
        # import pdb; pdb.set_trace()
        return response.json()['messages']

# todo real error handlng? https://www.nylas.com/blog/use-python-requests-module-rest-apis/
        # response.json() =>
        #
        # {'copyright': 'Copyright Sveriges Radio 2021. All rights reserved.',
        # 'messages':
        # [
        # {'id': 8551656,
        #   'priority': 3,
        #   'createddate': '/Date(1625110852730+0200)/',
        #   'title': 'Lv 1732  Ölsremma–Nyarp',
        #   'exactlocation': '',
        #   'description': 'Asfaltering, vakt och lots reglerar trafiken. Långa väntetider upp till 30 min kan uppstå. Om möjligt välj annan väg.',
        #   'latitude': 57.66111755371094,
        #   'longitude': 13.598100662231445,
        #   'category': 0,
        #   'subcategory': 'Vägarbete'
        #   }, ...]
        # }

    # def get_area(self, latitude: str, longitude: str):
    #     url = self.BASE_URL + "/areas"
    #     params = {"latitude": latitude, "longitude": longitude}.update(self.DEFAULT_PARAMS)
    #
    #     response = requests.get(url, params=params)

    # def get(self, **kwargs):
    #     try:
    #         requests.get(kwargs)
    #     except:
    #         print("Oh no, an exception!")

