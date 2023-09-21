from bs4 import BeautifulSoup
import requests

WEBSITE = "https://www.tiobe.com/tiobe-index/"
resp = requests.get(WEBSITE)
contents = resp.text

soup = BeautifulSoup(contents, 'html.parser')
table = soup.find(id="top20")
print(table)
