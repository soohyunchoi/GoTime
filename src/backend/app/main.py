import logging
from config import get_settings

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

settings = get_settings()


def main() -> None:
    logger.info("Starting the application")


if __name__ == "__main__":
    main()
