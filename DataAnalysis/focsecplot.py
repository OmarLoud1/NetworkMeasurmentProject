import csv
import geopandas as gpd
import matplotlib.pyplot as plt

input_file = "focsec-illegal-coordinates.csv"

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

flags= ["is_vpn", "is_bot", "is_datacenter", "is_tor", "is_proxy"]

for flag in flags:
    all_coordinates = []

    with open(input_file, "r") as csvfile:
        csv_reader = csv.reader(csvfile)
        
        for row in csv_reader:
            if flag in row[3:]:
                latitude, longitude = float(row[1]), float(row[2])
                all_coordinates.append((latitude, longitude))

    fig, ax = plt.subplots(figsize=(15, 20))
    world.boundary.plot(ax=ax, linewidth=1)

    for lat, lon in all_coordinates:
        plt.scatter(lon, lat, c='blue', marker='o', s=30)

    plt.title(f"All IPs with {flag} flag true", fontsize=14)
    ax.set_aspect('equal', 'box')

    output_file_path = f"Results/focsec/{flag}_map.jpeg"
    plt.savefig(output_file_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"Map for {flag} saved as {output_file_path}")
