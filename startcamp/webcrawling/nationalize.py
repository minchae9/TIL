import requests

name = 'Dorothy'
url = f'https://api.nationalize.io/?name={name}'
response = requests.get(url).json()

print(response)
print(response['country'])
