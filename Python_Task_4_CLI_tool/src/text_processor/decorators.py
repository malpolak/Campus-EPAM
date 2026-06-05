import time

from text_processor.logger import setup_logger

logger = setup_logger()

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        results = func(*args, **kwargs)

        end = time.time()
        logger.info(f"{func.__name__} executed in {end - start:.4f} seconds")

        return results

    return wrapper

