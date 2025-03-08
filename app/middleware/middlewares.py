# import logging
# from aiogram.types import Message, Update
# from aiogram.dispatcher.middlewares.base import BaseMiddleware
# from utils.logger import logger  

# class LoggingMiddleware(BaseMiddleware):
#     async def __call__(self, handler, event: Update, data: dict):
#         if isinstance(event, Message):  
#             user = event.from_user
#             logger.info(f"Сообщение от {user.id} (@{user.username}): {event.text}")
#         return await handler(event, data)
