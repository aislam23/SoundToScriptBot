import os
from aiogram import Bot
from aiogram.types import Voice

async def download_voice_message(voice: Voice, bot: Bot) -> str:
    """Скачивает голосовое сообщение и возвращает путь к файлу"""
    # Создаем директорию для временных файлов, если её нет
    os.makedirs("temp", exist_ok=True)
    
    # Получаем информацию о файле
    file = await bot.get_file(voice.file_id)
    file_path = file.file_path
    
    # Формируем путь для сохранения
    save_path = f"temp/{voice.file_id}.ogg"
    
    # Скачиваем файл
    await bot.download_file(file_path, save_path)
    
    return save_path 