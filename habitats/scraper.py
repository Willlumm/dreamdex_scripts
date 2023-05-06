import pandas as pd
import re
from requests_html import HTMLSession

data = []
session = HTMLSession()
for i in range(387, 388):
    result = session.get('https://www.theworldofpokemon.com/entryPages/entryPage_387.html')
    result.html.render()
    species = result.html.find("#entry-name", first=True).text
    habitat = result.html.find("#Habitat", first=True).text
    data.append((species, habitat))
session.close()
df = pd.DataFrame(data, columns=["species", "habitat"])
df.to_csv("habitats/habitats.csv")
