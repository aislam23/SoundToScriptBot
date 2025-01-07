from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from ...database.models import User, VoiceMessage

router = Router()

@router.message(Command("stats"))
async def handle_stats(message: Message, session: AsyncSession):
    """Обработчик команды /stats"""
    # Получаем статистику пользователя
    voice_count = await session.scalar(
        select(func.count(VoiceMessage.id))
        .where(VoiceMessage.user_id == message.from_user.id)
    )
    
    # Получаем количество рефералов
    referrals_count = await session.scalar(
        select(func.count(User.id))
        .where(User.referrer_id == message.from_user.id)
    )
    
    # Получаем общее время голосовых сообщений
    total_duration = await session.scalar(
        select(func.sum(VoiceMessage.duration))
        .where(VoiceMessage.user_id == message.from_user.id)
    ) or 0
    
    # Получаем дату регистрации пользователя
    user = await session.scalar(
        select(User).where(User.id == message.from_user.id)
    )
    
    # Формируем сообщение со статистикой
    stats_text = (
        "📊 Ваша статистика:\n\n"
        f"🎤 Обработано голосовых сообщений: {voice_count}\n"
        f"⏱ Общая длительность: {total_duration // 60} мин. {total_duration % 60} сек.\n"
        f"👥 Приглашено пользователей: {referrals_count}\n"
        f"📅 Дата регистрации: {user.created_at.strftime('%d.%m.%Y')}\n"
        f"🕒 Последняя активность: {user.last_activity.strftime('%d.%m.%Y %H:%M')}\n\n"
        "🔗 Чтобы получить вашу реферальную ссылку,\n"
        "используйте команду /referral"
    )
    
    await message.answer(stats_text) 