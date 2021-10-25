import requests
from pprint import pprint

response = requests.get('http://127.0.0.1:8000/api/v1/json-3/') # 응답객체 받음
# pprint(response.json())  # 파싱

data = response.json()  # 하나의 큰 리스트에 딕셔너리가 들어가 있는 형태라 접근 가능
pprint(data[0])