
from math import radians, sin, cos, sqrt, atan2

def haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Calculate the differences in coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Calculate the distance
    distance = R * c

    return distance

def main():
    # Input coordinates of the first point
    lat1 = float(input("Enter the latitude of the first point: "))
    lon1 = float(input("Enter the longitude of the first point: "))

    # Input coordinates of the second point
    lat2 = float(input("Enter the latitude of the second point: "))
    lon2 = float(input("Enter the longitude of the second point: "))

    # Calculate and display the distance
    distance = haversine(lat1, lon1, lat2, lon2)
    print(f"The distance between the two points is {distance:.2f} km.")

    # Calculate coordinates with a 100m difference
    lat2_new = lat2 + 0.0009  # 100m is approximately 0.0009 degrees in latitude
    lon2_new = lon2 + 0.0009  # 100m is approximately 0.0009 degrees in longitude

    # Calculate and display the new distance
    new_distance = haversine(lat1, lon1, lat2_new, lon2_new)
    print(f"The new distance with a 100m difference is {new_distance:.2f} km.")

if __name__ == "__main__":
    main()
