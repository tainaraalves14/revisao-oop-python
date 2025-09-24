from abc import ABC, abstractmethod

class AsyncAPIClient(ABC):
    @abstractmethod
    async def get_data(self):
        pass

class TwitterClient(AsyncAPIClient):
    async def get_data(self):
        await asyncio.sleep(1)
        return {"tweets": ["tweet1", "tweet2"]}

class GitHubClient(AsyncAPIClient):
    async def get_data(self):
        await asyncio.sleep(1)
        return {"repos": ["repo1", "repo2"]}

async def main():
    clients = [TwitterClient(), GitHubClient()]
    results = await asyncio.gather(*(client.get_data() for client in clients))
    print(results)

asyncio.run(main())
