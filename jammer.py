
import requests
import json
import csv
import os

def script5(input_file_path, output_file_path):
    api_key = "tja_ylILVBXoQFf2Q4E1gmMIS2nO5Xm69rAeVgc2"
    headers = {'accept': 'application/json', 'Authorization': f'Bearer {api_key}'}

    with open(input_file_path) as file:
        lines = [line.rstrip() for line in file]

 
    ip = "211.210.79.220"
    response = requests.get(f'https://dublin.api.threatjammer.com/v1/asn/{ip}', headers=headers)
    data = json.loads(response.text)
    print(format(data))