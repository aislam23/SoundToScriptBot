# SoundToScriptBot

Telegram бот для преобразования голосовых сообщений в текст с системой рефералов.

## Функциональность

- Преобразование голосовых сообщений в текст
- Система подписки на канал
- Реферальная система
- Статистика использования

## Технологии

- Python 3.11
- aiogram 3.x
- SQLAlchemy
- OpenAI Whisper
- Docker

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/aislam23/SoundToScriptBot.git
cd SoundToScriptBot
```

2. Создайте файл .env с необходимыми переменными окружения:
```bash
# Telegram Bot settings
BOT_TOKEN=your_bot_token_here
CHANNEL_USERNAME=@your_channel

# Database settings
DATABASE_URL=sqlite+aiosqlite:///data/bot_database.db

# Logging
LOG_LEVEL=INFO

# Rate limiting
RATE_LIMIT=1
```

3. Запустите бота через Docker Compose:

Для разработки:
```bash
docker-compose -f docker/docker-compose.dev.yml up --build
```

Для продакшена:
```bash
docker-compose -f docker/docker-compose.yml up --build
```

## Команды бота

- `/start` - Начать работу с ботом
- `/help` - Получить справку
- `/referral` - Информация о реферальной программе
- `/stats` - Ваша статистика использования

## Структура проекта

```
project/
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── src/
│   ├── bot/
│   │   ├── handlers/
│   │   ├── keyboards/
│   │   ├── middlewares/
│   │   ├── filters/
│   │   └── utils/
│   ├── database/
│   └── config/
└── requirements.txt
```

## Лицензия

MIT 