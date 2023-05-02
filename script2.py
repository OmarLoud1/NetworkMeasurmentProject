import requests
import json
import csv
import os
import dns.resolver

def script2(input_file_path, output_file_path):
    api_key = 'opcgtveqnugh'

    with open(input_file_path) as file:
        lines = [line.rstrip() for line in file]

    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    with open(output_file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for line in lines:
            reversed_ip = ".".join(reversed(line.split(".")))
            query = f"{api_key}.{reversed_ip}.dnsbl.httpbl.org"

            try:
                answers = dns.resolver.resolve(query, "A")
                result = str(answers[0]).split('.')[1:]
                csv_writer.writerow([line] + result)
            except:
                print("no record")

folders = ['Legal', 'Illegal']
for folder in folders:
    input_folder_path = f'IPS/{folder}'
    output_folder_path = f'Results/httpbl/{folder}'
    for file_name in os.listdir(input_folder_path):
        input_file_path = f'{input_folder_path}/{file_name}'
        output_file_path = f'{output_folder_path}/{file_name}.csv'
        script2(input_file_path, output_file_path)
