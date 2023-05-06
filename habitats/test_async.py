from requests_html import HTMLSession
from requests_html import AsyncHTMLSession

session = AsyncHTMLSession()

async def get_result():
    result = await session.get('https://www.theworldofpokemon.com/entryPages/entryPage_387.html')
    await result.html.arender()
    print(result.html.text)

session.run(get_result)