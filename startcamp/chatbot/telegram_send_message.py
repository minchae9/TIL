import requests

# 기본 설정
TOKEN = "1887719492:AAGoyH4eGo2514dnwAyjrp80Hios50qFKnk"
APP_URL = f"https://api.telegram.org/bot{TOKEN}"


# chat_id 가져오기
UPDATES_URL = f"{APP_URL}/getUpdates"
response = requests.get(UPDATES_URL).json()


chat_id = response.get('result')[0].get('message').get('chat').get('id')
# print(chat_id)

text = "냐옹냐옹~"

message_url = f"{APP_URL}/sendMessage?chat_id={chat_id}&text={text}"

requests.get(message_url)