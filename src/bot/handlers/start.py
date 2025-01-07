from datetime import datetime
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ...database.models import User
from ...config.config import settings

router = Router()

@router.message(CommandStart())
async def handle_start(message: Message, session: AsyncSession):
    """Обработчик команды /start"""
    # Проверяем, существует ли пользователь
    user = await session.scalar(
        select(User).where(User.id == message.from_user.id)
    )
    
    # Если пользователь новый
    if not user:
        # Проверяем реферальный код
        referrer_id = None
        if message.text.startswith('/start '):
            try:
                referrer_id = int(message.text.split()[1])
            except (ValueError, IndexError):
                pass
        
        # Создаем нового пользователя
        user = User(
            id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            referrer_id=referrer_id
        )
        session.add(user)
        await session.commit()
    
    # Обновляем время последней активности
    user.last_activity = datetime.utcnow()
    await session.commit()
    
    # Получаем информацию о боте
    bot_info = await message.bot.get_me()
    
    # Формируем приветственное сообщение
    welcome_text = (
        f"👋 Привет, {message.from_user.first_name}!\n\n"
        "🎙 Я бот для преобразования голосовых сообщений в текст.\n\n"
        f"❗️ Для использования бота необходимо подписаться на канал {settings.CHANNEL_USERNAME}\n\n"
        "📝 Просто отправь мне голосовое сообщение, и я преобразую его в текст.\n\n"
        "🔗 Твоя реферальная ссылка:\n"
        f"t.me/{bot_info.username}?start={message.from_user.id}\n\n"
        "Команды:\n"
        "/help - Получить справку\n"
        "/referral - Информация о реферальной программе\n"
        "/stats - Ваша статистика"
    )
    
    await message.answer(welcome_text) 