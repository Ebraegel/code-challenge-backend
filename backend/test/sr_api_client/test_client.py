from unittest.mock import patch

from code_challenge_backend.sr_api_client.client import TrafikApiClient


def test_test():
    assert True

def test_it_compiles():
    assert TrafikApiClient()

@patch('code_challenge_backend.sr_api_client.client.requests.get')
def test_list_incidents(mock_get):
    response = {
        'copyright': 'Copyright Sveriges Radio 2021. All rights reserved.',
        'messages':[
            {
                'id': 8551656,
                'priority': 3,
                'createddate': '/Date(1625110852730+0200)/',
                'title': 'Lv 1732  Ölsremma–Nyarp',
                'exactlocation': '',
                'description': 'Asfaltering, vakt och lots reglerar trafiken. Långa väntetider upp till 30 min kan uppstå. Om möjligt välj annan väg.',
                'latitude': 57.66111755371094,
                'longitude': 13.598100662231445,
                'category': 0,
                'subcategory': 'Vägarbete'
            },
            {
                'id': 8551657,
                'priority': 3,
                'createddate': '/Date(1625110852730+0200)/',
                'title': 'Lv 1732  Ölsremma–Nyarp',
                'exactlocation': '',
                'description': 'Asfaltering, vakt och lots reglerar trafiken. Långa väntetider upp till 30 min kan uppstå. Om möjligt välj annan väg.',
                'latitude': 87.66111755371094,
                'longitude': 93.598100662231445,
                'category': 0,
                'subcategory': 'Vägarbete'
            },
        ]
    }

    mock_get.return_value.ok = True
    mock_get.return_value.json.return_value = response

    incidents = TrafikApiClient().list_incidents()

    assert len(incidents) == 2
    assert response['messages'] == incidents


@patch('code_challenge_backend.sr_api_client.client.requests.get')
def test_list_incidents_returns_empty_list_on_failure(mock_get):
    mock_get.return_value.ok = False

    incidents = TrafikApiClient().list_incidents()

    assert incidents == []
