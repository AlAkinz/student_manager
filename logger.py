"""
logger.py — настройка логирования для всего проекта.

Логи пишутся в файл LOGS/LOG и одновременно выводятся в консоль.
Уровни: INFO, ERROR, CRITICAL
"""

import logging
import os

# Папка и файл для логов
LOGS_DIR  = os.path.join(os.path.dirname(__file__), "LOGS")
LOG_FILE  = os.path.join(LOGS_DIR, "LOG")

# Создаём папку LOGS, если её ещё нет
os.makedirs(LOGS_DIR, exist_ok=True)

# Формат записи: время — уровень — сообщение
LOG_FORMAT = "%(asctime)s  [%(levelname)-8s]  %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def get_logger(name: str) -> logging.Logger:
    """
    Вернуть логгер с заданным именем.
    Все логгеры пишут в один общий файл LOGS/LOG.
    """
    logger = logging.getLogger(name)

    # Чтобы не добавлять обработчики повторно при повторном вызове
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)

    # Обработчик — запись в файл
    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # Обработчик — вывод в консоль
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
