from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("help"))
async def handle_help(message: Message):
    """Обработчик команды /help"""
    help_text = (
        "🤖 Помощь по использованию бота:\n\n"
        "1️⃣ Для начала работы подпишитесь на канал @baldfrombrowser\n\n"
        "2️⃣ Отправьте голосовое сообщение, и я преобразую его в текст\n\n"
        "3️⃣ Используйте команды:\n"
        "   /start - Начать работу с ботом\n"
        "   /help - Получить эту справку\n"
        "   /referral - Информация о реферальной программе\n"
        "   /stats - Ваша статистика использования\n\n"
        "4️⃣ Приглашайте друзей и получайте бонусы!\n\n"
        "❓ Если у вас возникли проблемы, попробуйте:\n"
        "• Убедиться, что вы подписаны на канал\n"
        "• Проверить качество интернет-соединения\n"
        "• Отправить голосовое сообщение заново\n\n"
        "🎯 Бот поддерживает голосовые сообщения длительностью до 30 минут"
    )
    
    await message.answer(help_text) 