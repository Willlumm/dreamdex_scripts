from requests_html import HTMLSession

session = HTMLSession()
result = session.get('https://www.theworldofpokemon.com/habitats/habitat_0.html')
result.html.render()
# about = r.html.search("Habitat Info")
print(result.html.text)
# with open("test_render.html", "w", encoding="utf-8") as file:
#    file.writelines(result.text)
session.close()