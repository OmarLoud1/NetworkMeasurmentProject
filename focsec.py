import requests
import json

api_key = '2cf0ad6ba3c84f1687beda2a81ff911e'
headers = {'Authorization': api_key}

with open("IPS/Illegal/DrMerco") as file:
    lines = [line.rstrip() for line in file]

for line in lines:
    ip = line
    response = requests.get(f'https://api.focsec.com/v1/ip/{ip}', headers=headers)
    data = json.loads(response.text)

    true_fields = [key for key, value in data.items() if value is True]

    if true_fields:
        print(f"IP: {ip}")
        for field in true_fields:
            print(f"{field}: True")
        print("\n")
    else:
        print(f"IP: {ip} - No true values\n")
