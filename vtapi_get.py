import requests
import sys

url = 'https://www.virustotal.com/vtapi/v2/file/report'
# My api key # Don't use this key on anything program else.
api_key = '0f839cbc51dbca7de87e34c963743592b03b47d4230a0c96316f89ba512e2f57'
resource = sys.argv[1]
params = {'apikey': api_key, 'resource': resource}
response = requests.get(url, params=params)
print(response.json())
