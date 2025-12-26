import logging
from services.fivel_client import fivel_client
from config import get_settings

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

settings = get_settings()


def main() -> None:
    logger.info("Starting the application")
    fivel_client = fivel_client(settings.API_511_KEY)

    

    print(fivel_client.get_stop_predictions("13909"))


if __name__ == "__main__":
    main()
