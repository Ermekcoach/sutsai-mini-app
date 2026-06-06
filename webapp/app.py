import os, sqlite3
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from data.calc import calculate

load_dotenv()
app = FastAPI(title='Сюцай-разбор')
BASE_DIR = Path(__file__).resolve().parent
ROOT = BASE_DIR.parent
DB_PATH = Path(os.getenv('DB_PATH', ROOT / 'data' / 'users.db'))
DB_PATH.parent.mkdir(parents=True, exist_ok=True)
BRAND_NAME = os.getenv('BRAND_NAME', 'Ермек Исламович')
CONSULTATION_LINK = os.getenv('CONSULTATION_LINK', 'https://t.me/ermekcoach_bot')

app.mount('/static', StaticFiles(directory=BASE_DIR / 'static'), name='static')

def init_db():
    with sqlite3.connect(DB_PATH) as con:
        con.execute('''CREATE TABLE IF NOT EXISTS leads(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tg_user_id TEXT,
            username TEXT,
            full_name TEXT,
            birth_date TEXT,
            consciousness INTEGER,
            mission INTEGER,
            request_text TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )''')
init_db()

@app.get('/')
def index():
    return FileResponse(BASE_DIR / 'static' / 'index.html')

@app.get('/config')
def config():
    return {'brand_name': BRAND_NAME, 'consultation_link': CONSULTATION_LINK}

@app.post('/api/calculate')
async def api_calculate(request: Request):
    data = await request.json()
    try:
        result = calculate(data.get('birth_date', ''))
        return result
    except Exception:
        return JSONResponse({'error': 'Введите дату в формате ДД.ММ.ГГГГ'}, status_code=400)

@app.post('/api/lead')
async def api_lead(request: Request):
    data = await request.json()
    result = calculate(data.get('birth_date', ''))
    tg = data.get('telegram_user') or {}
    with sqlite3.connect(DB_PATH) as con:
        con.execute('''INSERT INTO leads(tg_user_id, username, full_name, birth_date, consciousness, mission, request_text)
                       VALUES(?,?,?,?,?,?,?)''', (
            str(tg.get('id','')), tg.get('username',''), tg.get('first_name',''),
            result['birth_date'], result['consciousness'], result['mission'], data.get('request_text','')
        ))
    return {'ok': True}
