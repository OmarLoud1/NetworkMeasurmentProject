

import requests
import json
import csv
import os



def script5(input_file_path, output_file_path):
    api_key = "tja_ylILVBXoQFf2Q4E1gmMIS2nO5Xm69rAeVgc2"
    headers = {'accept': 'application/json', 'Authorization': f'Bearer {api_key}'}

    with open(input_file_path) as file:
        lines = [line.rstrip() for line in file]

    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    with open(output_file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for line in lines:
            ip = line
            response = requests.get(f'https://dublin.api.threatjammer.com/v1/asn/{ip}', headers=headers)
            data = json.loads(response.text)

            if data and data.get("score", 0) != 0:
                row = [ip, data["score"]]
                csv_writer.writerow(row)

folders = ['Legal', 'Illegal']
for folder in folders:
    input_folder_path = f'IPS/{folder}'
    output_folder_path = f'Results/threatjammer/{folder}'
    for file_name in os.listdir(input_folder_path):
        input_file_path = f'{input_folder_path}/{file_name}'
        output_file_path = f'{output_folder_path}/{file_name}.csv'
        script5(input_file_path, output_file_path)
