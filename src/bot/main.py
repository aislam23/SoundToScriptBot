import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand

from ..config.config import settings
from ..database.database import init_models
from .handlers import register_handlers
from .middlewares import register_middlewares

# Настройка логирования
logging.basicConfig(level=settings.LOG_LEVEL)
logger = logging.getLogger(__name__)

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Начать работу с ботом"),
        BotCommand(command="/help", description="Получить справку"),
        BotCommand(command="/referral", description="Ваша реферальная ссылка"),
        BotCommand(command="/stats", description="Ваша статистика")
    ]
    await bot.set_my_commands(commands)

async def main():
    # Инициализация бота и диспетчера
    bot = Bot(token=settings.BOT_TOKEN.get_secret_value())
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    
    # Регистрация middleware
    register_middlewares(dp)
    
    # Регистрация хендлеров
    register_handlers(dp)
    
    # Установка команд бота
    await set_commands(bot)
    
    # Инициализация моделей базы данных
    await init_models()
    
    try:
        logger.info("Бот запущен")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        logger.info("Бот остановлен")

if __name__ == "__main__":
    asyncio.run(main()) 