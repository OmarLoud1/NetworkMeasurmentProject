import requests
import json
from ipaddress import ip_address
import httpbl
import 


with open("IPS/Illegal/DrMerco") as file:
    lines = [line.rstrip() for line in file]

for line in lines:


    api_key = 'opcgtveqnugh'



    ip_address = line

    bl = httpbl.HttpBL('opcgtveqnugh')
    response = bl.query(line)

    print('Threat Score: {}'.format(response))


    # response = requests.get(url)

    # result = response.text
    # print(result)   
