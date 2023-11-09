import requests
import json
from ipaddress import ip_address
import httpbl
import dns.resolver


api_key = 'opcgtveqnugh'
ip = '2.1.9.127'
with open("IPS/Illegal/DrMerco") as file:
    lines = [line.rstrip() for line in file]

for line in lines:


    api_key = 'opcgtveqnugh'

    url = 'opcgtveqnugh.2.1.9.127.dnsbl.httpbl.org'

    reversed_ip = ".".join(reversed(line.split(".")))
    query = f"{api_key}.{reversed_ip}.dnsbl.httpbl.org"

    try:
        print(query)
        answers = dns.resolver.resolve(query, "A")
        print(str(answers[0]))
    except:
        print("ip not referenced")





    # response = requests.get(url)

    # result = response.text
    # print(result)   
