"""
An asynchronous COVID-19 statistics API wrapper
"""

import aiohttp

from aiocovidapi.Summary import Summary


class COVID19APIClient:
    def __init__(self):
        self._base_url = "https://api.covid19api.com/"
        self._session = aiohttp.ClientSession()

    async def close(self):
        await self._session.close()

    async def summary(self):
        async with self._session.get(self._base_url + "summary") as response:
            response_contents = await response.json()
            return Summary(response_contents)
