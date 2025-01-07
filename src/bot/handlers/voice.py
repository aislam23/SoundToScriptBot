import os
import whisper
from aiogram import Router, F
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession
from ...database.models import User, VoiceMessage
from ..utils.voice import download_voice_message

router = Router()
model = whisper.load_model("base")

@router.message(F.voice)
async def handle_voice(message: Message, session: AsyncSession):
    """Обработчик голосовых сообщений"""
    # Отправляем сообщение о начале обработки
    status_message = await message.answer("🎵 Получено голосовое сообщение\n⏳ Начинаю обработку...")
    
    try:
        # Скачиваем голосовое сообщение
        voice_path = await download_voice_message(message.voice, message.bot)
        
        # Конвертируем в текст
        result = model.transcribe(voice_path)
        text = result["text"].strip()
        
        # Сохраняем в базу данных
        voice_msg = VoiceMessage(
            user_id=message.from_user.id,
            file_id=message.voice.file_id,
            duration=message.voice.duration,
            text_result=text
        )
        session.add(voice_msg)
        await session.commit()
        
        # Отправляем результат
        await status_message.edit_text(
            f"✅ Голосовое сообщение успешно преобразовано в текст:\n\n{text}"
        )
        
        # Удаляем временный файл
        os.remove(voice_path)
        
    except Exception as e:
        await status_message.edit_text(
            "❌ Произошла ошибка при обработке голосового сообщения.\n"
            "Пожалуйста, попробуйте еще раз."
        )
        raise e 