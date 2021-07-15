import requests

name = 'Dorothy'
url = f'https://api.agify.io/?name={name}'
response = requests.get(url).json()

print(response)
print(response['age'])