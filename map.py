import requests
import simplekml
import os


# Function to get location of an IP address
def get_ip_location(ip_address, token):
    url = f"https://ipinfo.io/{ip_address}?token={token}"
    response = requests.get(url)
    data = response.json()
    if "loc" in data:
        lat, lon = data["loc"].split(',')
        return float(lat), float(lon)
    else:
        # if there's no location data for the IP, return default values
        return 0.0, 0.0

# Traceroute log data: replace with actual data
traceroute_log = ["104.19.245.20", "10.253.156.1", "172.103.80.169", "172.103.80.169", "64.186.0.77", "64.186.0.77", "206.223.118.145", "141.101.74.100", "141.101.74.100", "104.19.245.20", "104.19.245.20"]


# Token for accessing ipinfo.io
token = "9be5108549bfcb"

# Get location of each IP address on the traceroute path
locations = [get_ip_location(ip_address, token) for ip_address in traceroute_log]

# Create a new KML object
kml = simplekml.Kml()

# Add each location to the KML as a placemark
for i, (lat, lon) in enumerate(locations, start=1):
    kml.newpoint(name=f"Hop {i}", coords=[(lon, lat)])  # Note that lon is before lat in coordinates

# Create a linestring (path) connecting all the locations
linestring = kml.newlinestring(name="Path")
linestring.coords = [(lon, lat) for lat, lon in locations]

# Save the KML
kml.save("traceroute.kml")
