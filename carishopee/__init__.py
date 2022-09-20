
import requests
from bs4 import BeautifulSoup

#generating url form product

def get_url(product_name):
    product_name = product_name.replace(' ','%20')
    template = 'https://shopee.co.id/search?keyword={}'
    url = template.format(product_name)
    return url