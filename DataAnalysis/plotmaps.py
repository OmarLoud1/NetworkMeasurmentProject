
import os
import csv
import requests
import folium

api_key = "3a959fa27bdd20690b32ea484886484afc4902e8afe0fbf848ce3fa9"

def get_coordinates(ip_address):
    url = f"https://api.ipdata.co/{ip_address}?api-key={api_key}"
    response = requests.get(url)
    data = response.json()

    latitude = data.get("latitude")
    longitude = data.get("longitude")

    return latitude, longitude

def save_coordinates(input_file_path, output_file_path):
    with open(input_file_path, "r") as csvfile, open(output_file_path, "w") as outfile:
        csv_reader = csv.reader(csvfile)
        csv_writer = csv.writer(outfile)

        for row in csv_reader:
            ip_address = row[0]
            latitude, longitude = get_coordinates(ip_address)
            if latitude and longitude:
                csv_writer.writerow([ip_address, latitude, longitude])

def plot_map(coordinates_file_path, map_file_path):
    coordinates = []

    with open(coordinates_file_path, "r") as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            latitude, longitude = float(row[1]), float(row[2])
            coordinates.append((latitude, longitude))

    if coordinates:
        map = folium.Map(location=[0, 0], zoom_start=2)
        for lat, lon in coordinates:
            folium.Marker(location=[lat, lon]).add_to(map)

        map.save(map_file_path)

main_folders = ['abuseipdb', 'focsec', 'httpbl', 'ipSum']
subfolders = ["Legal", "Illegal"]

for main_folder in main_folders:
    for subfolder in subfolders:
        input_folder_path = f"Results/{main_folder}/{subfolder}"

        for file_name in os.listdir(input_folder_path):
            input_file_path = f"{input_folder_path}/{file_name}"
            file_base_name, _ = os.path.splitext(file_name)

            coordinates_file_path = f"{input_folder_path}/{file_base_name}_coordinates.csv"
            save_coordinates(input_file_path, coordinates_file_path)

            map_file_path = f"{input_folder_path}/{file_base_name}_map.html"
            plot_map(coordinates_file_path, map_file_path)

