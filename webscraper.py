
import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"  
response = requests.get(URL)
print("Status Code:", response.status_code) 

soup = BeautifulSoup(response.text, "html.parser")

headlines = []

for tag in soup.find_all(['h2', 'h3']):
    title = tag.get_text(strip=True)
    if title and len(title) > 10:   
        headlines.append(title)

with open("news_headlines.txt", "w", encoding="utf-8") as f:
    for i, line in enumerate(headlines, start=1):
        f.write(f"{i}. {line}\n")

print(f"\n✅ {len(headlines)} headlines saved successfully in 'news_headlines.txt'!")
