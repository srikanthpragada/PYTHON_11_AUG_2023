from bs4 import BeautifulSoup
import requests

WEBSITE = "https://www.tiobe.com/tiobe-index/"
resp = requests.get(WEBSITE)
contents = resp.text

soup = BeautifulSoup(contents, 'html.parser')
table = soup.find(id="top20")

for row in table.tbody.find_all('tr')[:10]:
    cols = row.find_all('td')
    print(cols[4].text)

