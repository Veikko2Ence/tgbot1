import logging

logger = logging.getLogger("logs_bot")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")


console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter) 
logger.addHandler(console_handler)

file_handler = logging.FileHandler("bot_logs.log", encoding="utf-8")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)