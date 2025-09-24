import asyncio
import aiohttp

class WebScraper:
    def __init__(self, urls):
        self.urls = urls

    async def fetch(self, session, url):
        async with session.get(url) as response:
            return await response.text()

    async def scrape_all(self):
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch(session, url) for url in self.urls]
            results = await asyncio.gather(*tasks)
            return results

# Uso
urls = ["https://example.com", "https://httpbin.org/get"]
scraper = WebScraper(urls)
data = asyncio.run(scraper.scrape_all())
print(data)
