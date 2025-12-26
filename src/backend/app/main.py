import logging
from backend.app.services.redis_client import RedisClient
from services.fivel_client import FivelClient
from config import get_settings

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

settings = get_settings()


def main() -> None:
    logger.info("Starting the application")
    fivel_client = FivelClient(settings.API_511_KEY)
    redis_client = RedisClient(settings.REDIS_URL)

    print(fivel_client.get_stop_predictions("13909"))


if __name__ == "__main__":
    main()
