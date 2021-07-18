from code_challenge_backend.distance_filterer.distance_filterer import filter_locations_by_distance


client_lat = 45.02134810452489
client_long = -93.22932153664509
test_incidents = [
    {
        'id': 54321,
        'description': 'a few km away',
        'latitude': 44.95545065195005,
        'longitude': -93.27579171045899,
    },
    {
        'id': 12345,
        'description': 'pretty close',
        'latitude':	44.98866738892112,
        'longitude': -93.2648300477159,
    },
    {
        'id': 98765,
        'description': 'a few hundred km away',
        'latitude': 46.741167856989826,
        'longitude': -94.7343002069181,
    }
]


def test_filter_locations_by_distance():
    filtered = filter_locations_by_distance(locations=test_incidents, lat=client_lat, long=client_long, max_distance=30)
    filtered_ids = list(
        map(lambda x: x['id'], filtered)
    )

    assert len(filtered) == 2
    assert 54321 in filtered_ids
    assert 12345 in filtered_ids


def test_filter_locations_by_longer_distance():
    filtered = filter_locations_by_distance(locations=test_incidents, lat=client_lat, long=client_long, max_distance=3000)

    assert len(filtered) == 3

def test_filter_out_all_locations():
    filtered = filter_locations_by_distance(locations=test_incidents, lat=client_lat, long=client_long, max_distance=0.1)

    assert len(filtered) == 0
