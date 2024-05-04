import requests
from bs4 import BeautifulSoup

url = "https://g2a.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
title = soup.title.string
print("Webpage title:", title)