import requests
import json
import csv
import os

def script3(input_file_path, output_file_path):
    with open(input_file_path) as file:
        lines = [line.rstrip() for line in file]

    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    with open(output_file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for line in lines:
            url = 'https://api.abuseipdb.com/api/v2/check'
            querystring = {'ipAddress': line}
            headers = {
                'Accept': 'application/json',
                'Key': 'fc248444343aad6fb38e5b6276290e4e7b73de9740561cc88f2d55452ae8db48c15635e96935c25b'
            }

            response = requests.request(method='GET', url=url, headers=headers, params=querystring)
            decodedResponse = json.loads(response.text)
            data = decodedResponse.get('data', None)

            if data:
                abuse_confidence_score = data['abuseConfidenceScore']
                if(abuse_confidence_score != 0):
                     csv_writer.writerow([line, abuse_confidence_score])


folders = ['Legal', 'Illegal']
for folder in folders:
    input_folder_path = f'IPS/{folder}'
    output_folder_path = f'Results/abuseipdb/{folder}'
    for file_name in os.listdir(input_folder_path):
        input_file_path = f'{input_folder_path}/{file_name}'
        output_file_path = f'{output_folder_path}/{file_name}.csv'
        script3(input_file_path, output_file_path)
