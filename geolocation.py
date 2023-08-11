import requests

GELOCATION_API_KEY = 'AIzaSyBM_L32LJNZu0nU_emJQ4D391HPBSoc5hM'
PLACES_API_KEY = 'AIzaSyBM_L32LJNZu0nU_emJQ4D391HPBSoc5hM'

# Step 1: Get User's Location using Geolocation API
geolocation_url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={GELOCATION_API_KEY}'
geolocation_response = requests.post(geolocation_url)
geolocation_data = geolocation_response.json()

latitude = geolocation_data['location']['lat']
longitude = geolocation_data['location']['lng']

print(f'Latitude: {latitude}, Longitude: {longitude}')

# Step 2: Use User's Location for Places API Nearby Search
radius = 5000  # 5km in meters
places_url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={PLACES_API_KEY}&location={latitude},{longitude}&radius={radius}&type=restaurant'
places_response = requests.get(places_url)
places_data = places_response.json()

for place in places_data['results']:
    name = place['name']
    address = place['vicinity']
    print(f'Restaurant: {name}, Address: {address}')