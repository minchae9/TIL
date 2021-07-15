import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/exchangeDetail.nhn?marketindexCd=FX_USDKRW'
response = requests.get(url).text
data = BeautifulSoup(response, 'html.parser')
exchange = data.select_one('#content > div.spot > div.today > p.no_today')
result = exchange.text

print(f'현재  원/달러 환율은 {result}입니다')
