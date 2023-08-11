## utils.py

import logging
from typing import Any

def setup_logger(name: str, log_file: str, level: int = logging.INFO) -> logging.Logger:
    """
    Setup logger with specified name, log file and level.

    Parameters:
    name (str): The name of the logger.
    log_file (str): The file to which the log should be written.
    level (int): The level of the log.

    Returns:
    logging.Logger: The logger object.
    """
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

def print_progress(iteration: int, total: int, prefix: str = '', suffix: str = '', decimals: int = 1, length: int = 100, fill: str = '█') -> None:
    """
    Print progress bar for long running operations.

    Parameters:
    iteration (int): Current iteration.
    total (int): Total iterations.
    prefix (str): Prefix string.
    suffix (str): Suffix string.
    decimals (int): Positive number of decimals in percent complete.
    length (int): Character length of bar.
    fill (str): Bar fill character.

    Returns:
    None
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = '\r')
    if iteration == total: 
        print()

def safe_cast(val: Any, to_type: type, default: Any = None) -> Any:
    """
    Safely cast the value to a type. If the cast fails, returns the default value.

    Parameters:
    val (Any): The value to be casted.
    to_type (type): The type to cast the value to.
    default (Any): The default value to return if the cast fails.

    Returns:
    Any: The casted value or the default value if the cast fails.
    """
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default
