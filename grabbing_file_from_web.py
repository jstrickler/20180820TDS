#!/usr/bin/env python

import requests

URL = "https://tdstelecom.com/"

response = requests.get(URL)

for header_name, header_value in response.headers.items():
    print(header_name, header_value)
print('-' * 60)

print(response.content.decode())

URL = 'http://kbase.tds.local/CMS/modules/Outages/load_outages_by_exchange_xml.php'

response = requests.get(URL)

if response.status_code == requests.codes.OK:
    print(response.content)
else:
    print("womp womp")

