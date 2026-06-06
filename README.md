# Сюцай-разбор Ермека Исламовича — Telegram Mini App

## Что внутри
- `bot/bot.py` — Telegram-бот с кнопкой открытия приложения.
- `webapp/app.py` — веб-приложение FastAPI.
- `webapp/static/` — красивый интерфейс для клиентов.
- `data/knowledge.py` — база описаний ЧС и миссий.
- `data/calc.py` — расчет даты рождения.

## Локальный запуск
1. Установите Python 3.10+
2. Скопируйте `.env.example` в `.env`
3. Заполните BOT_TOKEN, ADMIN_ID, CONSULTATION_LINK, WEBAPP_URL
4. Установите зависимости:

```bash
pip install -r requirements.txt
```

5. Запустите веб-приложение:

```bash
uvicorn webapp.app:app --host 0.0.0.0 --port 8000
```

6. В другом окне запустите бота:

```bash
python bot/bot.py
```

## Важно для Telegram Mini App
Telegram открывает Mini App только по HTTPS-ссылке. Для теста можно использовать ngrok:

```bash
ngrok http 8000
```

Полученную HTTPS-ссылку вставьте в `.env` как WEBAPP_URL.
Также в BotFather используйте `/setmenubutton` или кнопку в боте.

