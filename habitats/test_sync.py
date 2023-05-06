from requests_html import HTMLSession
from requests_html import AsyncHTMLSession

session = HTMLSession()

async def get_async():
    r = await session.get('https://python.org/')
    return r

result = session.get('https://pythonclock.org')
result.html.render()
print(result.html.search('Python 2.7 will retire in...{}Enable Guido Mode')[0])