import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"

try:
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    print("Status Code:", response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")
    headlines = []

    for tag in soup.find_all(['h2', 'h3']):
        title = tag.get_text(strip=True)
        if title and len(title) > 10:
            headlines.append(title)

    with open("Headlines.txt", "w", encoding="utf-8") as f:
        for i, line in enumerate(headlines, start=1):
            f.write(f"{i}. {line}\n")

    print(f"\n{len(headlines)} headlines saved successfully in 'Headlines.txt'!")
except requests.exceptions.RequestException as e:
    print("Error fetching the webpage:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
