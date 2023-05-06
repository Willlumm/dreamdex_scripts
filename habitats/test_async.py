from requests_html import HTMLSession
from requests_html import AsyncHTMLSession

session = AsyncHTMLSession()

async def get_async():
    r = await session.get('https://python.org/')
    return r

result = session.run(get_async)
# r.html.render()
# r.html.search('Python 2.7 will retire in...{}Enable Guido Mode')[0]
# r.text