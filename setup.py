import requests
import simplekml
import os

import re

#*************************************************************************
            #get-ip.py

# The destination for the traceroute command
destination = "youtube.com"

# Run traceroute command
traceroute_result = os.popen(f"traceroute {destination}").read()

# Save the output to a file
with open("ip.txt", "w") as file:
    file.write(traceroute_result)

print ('Got route IP!')
#*************************************************************************
            # extract.py

def extract_ip_addresses(file_path):
    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Define a regex pattern for IP address (This pattern does not validate IP, it just search for 4 groups of numbers separated by dots)
    ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

    # Find all IP addresses in the file
    ip_addresses = re.findall(ip_pattern, content)
    
    return ip_addresses

# Path of the traceroute log file
traceroute_file_path = 'ip.txt'

# Extract the IP addresses
ip_addresses = extract_ip_addresses(traceroute_file_path)


# Print the extracted IP addresses
with open('traceroute.txt', 'w') as f:
    for ip in ip_addresses:
        print(ip)
        f.write(str(ip) + '\n')


#*************************************************************************
            # getdatafromip.py


# Define the filename of the data file
data_file = 'traceroute.txt'  # File containing the IP addresses

# Read the file
with open(data_file, 'r') as f:
    ip_addresses = [line.strip() for line in f]

# Convert the list of IP addresses to a string, with quotes and commas
ip_addresses_str = '[' + ', '.join(f'"{ip}"' for ip in ip_addresses) + ']'

# Define the filename of the Python file to modify
python_file = 'map4.py'  # File containing the MAP code

# Read the Python file
with open(python_file, 'r') as f:
    python_script = f.read()

# Substitute the traceroute_log definition
python_script = re.sub(r'traceroute_log = \[.*?\]', f'traceroute_log = {ip_addresses_str}', python_script, flags=re.DOTALL)

# Write the modified Python script back to the file
with open(python_file, 'w') as f:
    f.write(python_script)

print ('Put desired IP from traceroute into map4.py')

#*************************************************************************

