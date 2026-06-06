from datetime import datetime
from .knowledge import CONSCIOUSNESS, MISSIONS, EXCEPTIONS

def reduce_to_1_9(n:int)->int:
    while n > 9:
        n = sum(int(x) for x in str(n))
    return n

def parse_date(value:str):
    value = value.strip().replace('-', '.').replace('/', '.')
    dt = datetime.strptime(value, '%d.%m.%Y')
    return dt

def calculate(value:str):
    dt = parse_date(value)
    consciousness = reduce_to_1_9(dt.day)
    digits = f'{dt.day:02d}{dt.month:02d}{dt.year:04d}'
    mission = reduce_to_1_9(sum(int(x) for x in digits))
    c = CONSCIOUSNESS[consciousness]
    m = MISSIONS[mission]
    return {
        'birth_date': dt.strftime('%d.%m.%Y'),
        'consciousness': consciousness,
        'mission': mission,
        'is_exception': (consciousness, mission) in EXCEPTIONS,
        'consciousness_data': c,
        'mission_data': m,
    }
