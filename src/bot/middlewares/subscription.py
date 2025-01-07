from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from ..utils.subscription import check_subscription
from ...config.config import settings

class SubscriptionMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        # Пропускаем команду /start
        if isinstance(event, Message) and event.text and event.text.startswith('/start'):
            return await handler(event, data)
            
        # Проверяем подписку
        is_subscribed = await check_subscription(event.from_user.id)
        if not is_subscribed:
            await event.answer(
                f"❗️ Для использования бота необходимо подписаться на канал {settings.CHANNEL_USERNAME}\n"
                "После подписки повторите действие."
            )
            return
            
        return await handler(event, data) 