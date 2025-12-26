from apscheduler.schedulers.asyncio import AsyncIOScheduler

from backend.app.services.fivel_client import FivelClient
import redis
import os

from backend.app.services.redis_client import RedisClient

class MuniPoller:
    scheduler: AsyncIOScheduler
    def __init__(self, fivel_client: FivelClient, redis_client: RedisClient) -> None:
        self.scheduler = AsyncIOScheduler()
        self.fivel_client = fivel_client
        self.redis_client = redis_client

    async def poll_muni(self, stop_id) -> None:
        arrivals = await self.fivel_client.get_stop_predictions(stop_id)
        print(arrivals)
    
    def add_stop_job(self, stop_id: str):
        self.scheduler.add_job(self.poll_muni, 'interval', seconds=30, stop_id=stop_id)

    def start(self) -> None:
        self.scheduler.start()

    def stop(self) -> None:
        self.scheduler.shutdown()