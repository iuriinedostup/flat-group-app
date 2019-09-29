import sys
import logging

logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.StreamHandler(sys.stderr)],
    format=' %(asctime)s %(levelname)s | %(message)s'
)


def get_logger(name):
    return logging.getLogger(name)
