from aiogram import Dispatcher
from .subscription import SubscriptionMiddleware
from ...database.database import DatabaseMiddleware

def register_middlewares(dp: Dispatcher):
    """Регистрирует все middleware"""
    # Добавляем сессию базы данных в middleware
    dp.message.middleware(DatabaseMiddleware())
    dp.callback_query.middleware(DatabaseMiddleware())
    
    # Добавляем проверку подписки
    dp.message.middleware(SubscriptionMiddleware())
    dp.callback_query.middleware(SubscriptionMiddleware()) 