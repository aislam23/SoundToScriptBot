from aiogram import Dispatcher
from . import start, voice, stats, help, referral

def register_handlers(dp: Dispatcher):
    """Регистрирует все обработчики"""
    dp.include_router(start.router)
    dp.include_router(voice.router)
    dp.include_router(stats.router)
    dp.include_router(help.router)
    dp.include_router(referral.router) 