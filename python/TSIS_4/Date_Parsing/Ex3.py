from datetime import datetime

def without_microseconds() -> datetime:
    now = datetime.now()
    now = now.replace(microsecond=0)

    return now

print(without_microseconds())