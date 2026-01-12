def find_extreme_coordinates(coord_list):
    latitudes = [lat for lat, lon in coord_list]
    longitudes = [lon for lat, lon in coord_list]

    min_lat = min(latitudes)
    max_lat = max(latitudes)
    min_lon = min(longitudes)
    max_lon = max(longitudes)
    
    return (min_lat, max_lat, min_lon, max_lon)

gps_data = [
    (34.05, -118.24),
    (40.71, -74.00),
    (51.50, -0.12),
    (35.68, 139.69),
    (28.61, 77.20),
]

print("🌍 GPS Coordinate Tracker 🌍")
print(f"Tracking {len(gps_data)} coordinates.")

min_lat, max_lat, min_lon, max_lon = find_extreme_coordinates(gps_data)

print("\n--- Extreme Boundaries Found ---")
print(f"Minimum Latitude: {min_lat}")
print(f"Maximum Latitude: {max_lat}")
print(f"Minimum Longitude: {min_lon}")
print(f"Maximum Longitude: {max_lon}")
