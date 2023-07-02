** Python IP Traceroute Visualizer
This project contains three Python scripts that perform the task of tracing internet packet routes, identifying IP addresses in the path, fetching their geographical locations, and visualizing the path on a map.

Project Files
setup.py: This script executes a traceroute command and writes the output into an ip.txt file. It then extracts the IP addresses, formats them into a list of strings, and writes these IP addresses into the map4.py script.

map4.py: This script reads the IP addresses from the traceroute.txt file, fetches their geographical locations using the ipinfo service, and generates a KML file for visualizing the path between routers when visiting websites.

main.py: This is the main script that triggers the execution of setup.py and map4.py.

How to Run
To run the scripts, simply execute the main.py file:


python3 main.py


This will automatically trigger the execution of setup.py and map4.py, generate the ip.txt and KML files, and write the IP addresses into map4.py.

After execution, open the generated KML file in a geographic visualization tool like Google Earth to visualize the path between routers.

Dependencies
This project uses the ipinfo service to fetch geographical locations of IP addresses. Ensure that you have the ipinfo library installed:


pip install ipinfo


License
This project is open-sourced under the MIT license.
