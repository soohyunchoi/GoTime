import httpx
import asyncio
from google.transit import gtfs_realtime_pb2

class fivel_client:
    key: str
    client: httpx.AsyncClient
    BASE_URL: str = "http://api.511.org/transit"
    def __init__(self, key) -> None:
        self.key = key
        self.client = httpx.AsyncClient(timeout=10.0)

    async def get_stop_predictions(self, stop_id: str, agency: str = "SF") -> list[dict]:
        url=f"{self.BASE_URL}/StopMonitoring?api_key={self.key}&agency={agency}&stopCode={stop_id}&format=json"
        response = await self.client.get(url, headers={"Accept-Encoding": "gzip"})

        feed = gtfs_realtime_pb2.FeedMessage()
        feed.ParseFromString(response.content)

        return response.json()
    
    async def close(self):
        await self.client.aclose()