from geopy import distance

def filter_locations_by_distance(locations=[], lat=0.0, long=0.0, max_distance=30):
    client_location = (lat, long)
    return list(
        filter(
            lambda x: distance.distance(client_location, (x['latitude'], x['longitude'])).km < max_distance,
            locations
        )
    )