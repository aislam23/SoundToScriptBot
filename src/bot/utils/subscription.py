from aiogram import Bot
from ...config.config import settings

async def check_subscription(user_id: int) -> bool:
    """Проверяет подписку пользователя на канал"""
    bot = Bot(token=settings.BOT_TOKEN.get_secret_value())
    try:
        member = await bot.get_chat_member(
            chat_id=settings.CHANNEL_USERNAME,
            user_id=user_id
        )
        return member.status in ["creator", "administrator", "member"]
    except Exception:
        return False
    finally:
        await bot.session.close() 