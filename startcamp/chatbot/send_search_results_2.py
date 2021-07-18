## 자습
import requests

# 기본 설정
TOKEN = "1887719492:AAGoyH4eGo2514dnwAyjrp80Hios50qFKnk"
API_URL = f"https://api.telegram.org/bot{TOKEN}/"

# chat_id 가져오기
UPDATES_URL = f'{API_URL}getUpdates'
response = requests.get(UPDATES_URL).json()
chat_id = response.get('result')[0].get('message').get('chat').get('id')

# 입력 텍스트 가져오기
input = response.get('result')[-1].get('message').get('text')
# print(input)

# text 가져오기
# 1. 쇼핑 검색
naver_client_id = 'O3_vMhmVLMBGdzFQ9Y0t'
naver_client_secret = '3mn8qqU92B'
URL = "https://openapi.naver.com/v1/search/shop.json?query="

headers = {
    'X-Naver-Client-Id': naver_client_id,
    'X-Naver-Client-Secret': naver_client_secret
}

query = input

product = requests.get(URL+query, headers = headers).json()['items'][5]
#print(product)

product_name = product['title']
product_price = product['lprice']
product_link = product['link']

#2. 메시지 텍스트 만들기
text = f'{product_name}\n{product_price}\n{product_link}'

message_url = f'{API_URL}sendMessage?chat_id={chat_id}&text={text}'
requests.get(message_url)


