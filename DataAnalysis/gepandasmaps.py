# plot_map.py
import os
import csv
import geopandas as gpd
import matplotlib.pyplot as plt

main_folders = ['abuseipdb', 'focsec', 'httpbl', 'ipSum']
subfolders = ["Legal", "Illegal"]

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

for main_folder in main_folders:
    for subfolder in subfolders:
        input_folder_path = f"Results/{main_folder}/{subfolder}"

        for file_name in os.listdir(input_folder_path):
            if not file_name.endswith("_coordinates.csv"):
                continue
            
            input_file_path = f"{input_folder_path}/{file_name}"
            file_base_name, _ = os.path.splitext(file_name)

            coordinates = []
            with open(input_file_path, "r") as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    latitude, longitude = float(row[1]), float(row[2])
                    coordinates.append((latitude, longitude))

            fig, ax = plt.subplots(figsize=(15, 20))
            world.boundary.plot(ax=ax, linewidth=1)  # Modified line

            for lat, lon in coordinates:
                plt.scatter(lon, lat, c='blue', marker='o', s=30)

            label = f"{file_base_name[:-12]} from {main_folder}/{subfolder}"
            plt.title(label, fontsize=14)

            ax.set_aspect('equal', 'box')

            output_file_path = f"{input_folder_path}/{file_base_name[:-12]}_map.jpeg"
            plt.savefig(output_file_path, dpi=300, bbox_inches='tight')
            plt.close()
