import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

os.makedirs("Level-1", exist_ok=True)

base_url = "https://www.scrapethissite.com/pages/forms/?page_num="
hockey_data = []

for page in range(1, 4):
    print(f"Scraping page {page}...")
    response = requests.get(base_url + str(page))
    soup = BeautifulSoup(response.text, "html.parser")
    
    table = soup.find("table", class_="table")
    rows = table.find_all("tr", class_="team")

    for row in rows:
        hockey_data.append({
            "Team Name": row.find("td", class_="name").text.strip(),
            "Year": row.find("td", class_="year").text.strip(),
            "Wins": row.find("td", class_="wins").text.strip(),
            "Losses": row.find("td", class_="losses").text.strip(),
            "OT Losses": row.find("td", class_="ot-losses").text.strip(),
            "Win %": row.find("td", class_="pct").text.strip(),
            "GF": row.find("td", class_="gf").text.strip(),
            "GA": row.find("td", class_="ga").text.strip(),
            "Diff": row.find("td", class_="diff").text.strip()
        })

df = pd.DataFrame(hockey_data)
df.to_csv("Level-1/hockey_teams.csv", index=False)
print(f"Successfully scraped {len(df)} records across 3 pages.")