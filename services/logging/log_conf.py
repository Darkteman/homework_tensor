from loguru import logger

logger.add(
    'services/logging/debag.log',
    format='{time} {level} {message}',
    level='INFO',
    rotation='1 MB',
    compression='zip'
)
