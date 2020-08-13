import requests
import json
requests_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=abc321'

response = requests.get(requests_url)

print(response)

print(response.status_code)
print(type(response.text))  # < string

parsed_response = json.loads(response.text)

print(type(parsed_response))  # > dict
print(parsed_response.keys())
