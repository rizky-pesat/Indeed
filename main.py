import carishopee
from bs4 import BeautifulSoup

import requests
#generating url form product

url = carishopee.get_url('payung magic')
print(url)


#Create Beautifoulsoup
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
cards = soup.find_all('div','col-xs-2-4 shopee-search-item-result__item')

print(len(cards))



