import logging
import os

# Настройка логирования в файл
LOG_FILE = "my_app.log"
LOG_SIZE_LIMIT = 100 * 1024 * 1024  # 100 МБ


def setup_logging():
    """Настройка логирования в файл и консоль с очисткой файла каждые 100 МБ."""
    # Создаем обработчик для файла
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(logging.INFO)  # Уровень логирования для файла
    file_handler.setFormatter(
    logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    )

    # Создаем обработчик для консоли
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # Уровень логирования для консоли
    console_handler.setFormatter(
    logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    )

    # Создаем корневой логгер
    logger = logging.getLogger()
    logger.setLevel(logging.INFO) # Уровень логирования для корневого логгера

    # Добавляем обработчики к корневому логгеру
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

# Проверяем размер файла и очищаем его, если он превышает 100 МБ
    if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) >= LOG_SIZE_LIMIT:
        with open(LOG_FILE, 'w'):
            pass  # Очищаем файл, записывая в него пустую строку