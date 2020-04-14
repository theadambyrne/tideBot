import requests
from bs4 import BeautifulSoup

url = "https://www.tidetimes.org.uk/dingle-harbour-tide-times"
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/81.0.4044.92 Chrome/81.0.4044.92 Safari/537.36"}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

headlines = soup.find(id="hightide")
print(headlines.get_text())
