import requests
import json


with open("IPS/Illegal/DrMerco") as file:
    lines = [line.rstrip() for line in file]

for line in lines:

    # Defining the api-endpoint
    url = 'https://api.abuseipdb.com/api/v2/check'

    querystring = {
        'ipAddress': line
    }

    headers = {
        'Accept': 'application/json',
        'Key': 'fc248444343aad6fb38e5b6276290e4e7b73de9740561cc88f2d55452ae8db48c15635e96935c25b'
    }

    response = requests.request(method='GET', url=url, headers=headers, params=querystring)

    # Formatted output
    decodedResponse = json.loads(response.text)
    #print(json.dumps(decodedResponse, sort_keys=True, indent=4))
    print(decodedResponse["data"]['abuseConfidenceScore'])