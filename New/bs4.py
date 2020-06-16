from bs4 import BeautifulSoup
import requests


url = 'http://mignews.com/mobile'

page = requests.get(url)

print(page.status_code)

new = []
whole = []

soup = BeautifulSoup(page.text, "html.parser")
    
print(soup)