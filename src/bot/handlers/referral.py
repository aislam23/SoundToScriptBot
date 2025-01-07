from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from ...database.models import User

router = Router()

@router.message(Command("referral"))
async def handle_referral(message: Message, session: AsyncSession):
    """Обработчик команды /referral"""
    # Получаем информацию о боте
    bot_info = await message.bot.get_me()
    
    # Получаем количество рефералов пользователя
    referrals_count = await session.scalar(
        select(func.count(User.id))
        .where(User.referrer_id == message.from_user.id)
    )
    
    # Формируем текст сообщения
    referral_text = (
        "🤝 Реферальная программа\n\n"
        "Приглашайте друзей и получайте бонусы!\n\n"
        f"👥 Ваши приглашенные: {referrals_count}\n\n"
        "🔗 Ваша реферальная ссылка:\n"
        f"t.me/{bot_info.username}?start={message.from_user.id}\n\n"
        "📋 Инструкция:\n"
        "1. Отправьте свою реферальную ссылку друзьям\n"
        "2. Когда они перейдут по ссылке и начнут использовать бота,\n"
        "   вы будете получать бонусы\n"
        "3. Чем больше активных рефералов, тем больше бонусов!\n\n"
        "📊 Статистику можно посмотреть командой /stats"
    )
    
    await message.answer(referral_text) 