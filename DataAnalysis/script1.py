import requests
import json
import csv
import os

def script1(input_file_path, output_file_path):
    api_key = ''
    headers = {'Authorization': api_key}

    with open(input_file_path) as file:
        lines = [line.rstrip() for line in file]

    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    with open(output_file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for line in lines:
            ip = line
            response = requests.get(f'https://api.focsec.com/v1/ip/{ip}', headers=headers)
            data = json.loads(response.text)

            true_fields = [key for key, value in data.items() if value is True and key != 'is_in_european_union']

            if true_fields:
                row = [ip] + true_fields
                csv_writer.writerow(row)

folders = ['Legal', 'Illegal']
for folder in folders:
    input_folder_path = f'IPS/{folder}'
    output_folder_path = f'Results/focsec/{folder}'
    for file_name in os.listdir(input_folder_path):
        input_file_path = f'{input_folder_path}/{file_name}'
        output_file_path = f'{output_folder_path}/{file_name}.csv'
        script1(input_file_path, output_file_path)
