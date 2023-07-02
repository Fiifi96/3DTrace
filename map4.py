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
traceroute_log = ["142.250.68.142", "10.253.156.1", "172.103.80.169", "172.103.80.169", "64.186.0.77", "64.186.0.77", "72.14.196.102", "72.14.196.102", "142.251.60.44", "142.251.60.44", "72.14.237.47", "72.14.237.47", "108.170.240.129", "108.170.240.129", "142.250.68.142"]

# Token for accessing ipinfo.io
token = "9be5108549bfcb"

# Get location of each IP address on the traceroute path
locations = [get_ip_location(ip_address, token) for ip_address in traceroute_log]

# Create a new KML object
kml = simplekml.Kml()

# Add each location to the KML as a placemark
for i, (lat, lon) in enumerate(locations, start=1):
    pnt = kml.newpoint(name=f"Hop {i}", coords=[(lon, lat)])  # Note that lon is before lat in coordinates
    if i == 1:
        pnt.style.iconstyle.color = simplekml.Color.blue  # Set the color of the first hop to blue
    if i == len(locations):  # If this is the last hop
        pnt.style.iconstyle.color = simplekml.Color.red  # Set the color of the last hop to red

# Create a linestring (path) connecting all the locations
linestring = kml.newlinestring(name="Path")
linestring.coords = [(lon, lat) for lat, lon in locations]

# Set the line color to red
linestring.style.linestyle.color = simplekml.Color.red

# Save the KML
kml.save("traceroute.kml")
