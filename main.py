import openpyxl
import gmaps
gmaps.configure(api_key="AIzaSyCJf2H1WJbzUz9EZV3tGxNqs409ZH8bjCI")
from geocoder import geocode_address

# Loading address values in the Excel files and appending these to Python list
file_path = r'./동탄 라이브오피스_사업환경-2.xlsx'
wb = openpyxl.load_workbook(file_path)
sheet = wb['화성시공급현황raw']
addresses = []
weights = []
latitudes = []
longitudes = []

for i in range(5,245):
    addresses.append(sheet['A' + str(i)].value)
    weights.append(sheet['D' + str(i)].value)

api_key = "XXXXXXXX"

# Convert each address into a latitude and longitude
for address in addresses:
    latitude, longitude = geocode_address(address, api_key)
    latitudes.append(latitude)
    longitudes.append(longitude)
    
heyon_data = list(zip(latitudes, longitudes))

# Define the latitude and longitude of the center of the locations
center_lat = sum(latitudes) / len(latitudes)
center_lng = sum(longitudes) / len(longitudes)
fig = gmaps.figure(map_type='HYBRID', zoom_level=11, center=(center_lat, center_lng))
heatmap_layer = gmaps.heatmap_layer(heyon_data, weights=weights, point_radius=40)
fig.add_layer(heatmap_layer)
fig
