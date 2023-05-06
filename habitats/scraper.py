import pandas as pd
import re
from requests_html import HTMLSession

data = []
session = HTMLSession()
print("Scraping...")
for i in range(0, 1009):
    result = session.get("https://www.theworldofpokemon.com/entryPages/entryPage_f{i}.html")
    result.html.render()
    species = result.html.find("#entry-name", first=True).text
    habitat = result.html.find("#Habitat", first=True).text
    data.append((species, habitat))
    if i % 100 == 0:
        print(f"{i} of 1009 complete...")
session.close()
df = pd.DataFrame(data, columns=["species", "habitat"])
df.to_csv("habitats/habitats.csv")
