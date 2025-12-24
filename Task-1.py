import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://quotes.toscrape.com/page/"
quotes_data = []

for page in range(1, 6):
    response = requests.get(base_url + str(page))
    soup = BeautifulSoup(response.text, "html.parser")
    
    quotes = soup.find_all("div", class_="quote")
    
    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text

        tags = [tag.text for tag in quote.find_all("a", class_="tag")]
        tags_str = ", ".join(tags)

        quotes_data.append({
            "Quote": text,
            "Author": author,
            "Tags": tags_str
    })

df = pd.DataFrame(quotes_data)
df.to_csv("quotes.csv", index=False)