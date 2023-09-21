from bs4 import BeautifulSoup
import requests

WEBSITE = "http://www.srikanthtechnologies.com"
resp = requests.get(WEBSITE)
contents = resp.text

soup = BeautifulSoup(contents, 'html.parser')
links = set()

for a in soup.find_all("a"):
    href = a['href']
    if href == "#":
        continue

    if not href.startswith("http"):
        href = WEBSITE + "/" + href

    links.add(href)

for link in links:
    print(link)
