# Set up logger function so we can log to two files
import logging

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def setup_logger(name, log_file, level=logging.INFO):
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    new_logger = logging.getLogger(name)
    new_logger.setLevel(level)
    new_logger.addHandler(handler)

    return new_logger

my_logger = setup_logger('my_logger', 'src/logging.log', level=logging.WARNING)
info_logger = setup_logger('info_logger', 'src/info.log', level=logging.INFO)