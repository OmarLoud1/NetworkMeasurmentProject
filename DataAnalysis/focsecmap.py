import csv
import requests
import os

api_key = '3a959fa27bdd20690b32ea484886484afc4902e8afe0fbf848ce3fa9'
url_template = "https://api.ipdata.co/{ip}?api-key={api_key}&fields=ip,latitude,longitude"

input_file = "focsec-illegal.csv"
output_file = "focsec-illegal-coordinates.csv"

flags = set()

with open(input_file, "r") as infile, open(output_file, "w", newline='') as outfile:
    csv_reader = csv.reader(infile)
    csv_writer = csv.writer(outfile)
    
    for row in csv_reader:
        ip = row[0]
        url = url_template.format(ip=ip, api_key=api_key)
        response = requests.get(url)
        data = response.json()
        latitude, longitude = data["latitude"], data["longitude"]
        coordinates_row = [ip, latitude, longitude] + row[1:]
        csv_writer.writerow(coordinates_row)
        flags.update(row[1:])

print("Coordinates saved to", output_file)