import numpy as np

def haversine_distance(lat1, lon1, lat2, lon2, R=6371):
    """
    Calculates the Haversine distance between two sets of geographic coordinates
    using NumPy for vectorized operations.

    Args:
        lat1 (np.array or scalar): Latitude(s) of the first point(s) in degrees.
        lon1 (np.array or scalar): Longitude(s) of the first point(s) in degrees.
        lat2 (np.array or scalar): Latitude(s) of the second point(s) in degrees.
        lon2 (np.array or scalar): Longitude(s) of the second point(s) in degrees.
        R (float): Radius of the Earth in kilometers (default is 6371 km).

    Returns:
        np.array or scalar: The Haversine distance(s) in kilometers.
    """
    # Convert latitude and longitude from degrees to radians
    lat1_rad, lon1_rad, lat2_rad, lon2_rad = map(np.radians, [lat1, lon1, lat2, lon2])

    # Calculate the difference in latitude and longitude
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Apply the Haversine formula
    a = np.sin(dlat / 2.0)**2 + np.cos(lat1_rad) * np.cos(lat2_rad) * np.sin(dlon / 2.0)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    distance = R * c

    return distance
