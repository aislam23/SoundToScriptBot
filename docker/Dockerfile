# Базовый образ
FROM docker.io/library/python:3.11-slim as base

# Настройка переменных окружения для pip и Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONOPTIMIZE=2 \
    PIP_NO_CACHE_DIR=0 \
    PIP_DEFAULT_TIMEOUT=100 \
    DOCKER_CLIENT_TIMEOUT=120 \
    COMPOSE_HTTP_TIMEOUT=120

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Установка рабочей директории
WORKDIR /app

# Установка зависимостей Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Создание директорий
RUN mkdir -p data temp

# Образ для разработки
FROM base as development
# В режиме разработки исходный код монтируется через volume

# Образ для продакшена
FROM base as production
# В продакшене копируем исходный код
COPY src/ src/

# Запуск бота
CMD ["python", "-m", "src.bot.main"] 