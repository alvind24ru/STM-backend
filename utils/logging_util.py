import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log",
                    format="%(asctime)s %(levelname)s %(message)s")


def log_info(text: str):
    logging.info(f'{text}')


def log_critical(text: str):
    logging.critical(f'{text}', exc_info=True)
