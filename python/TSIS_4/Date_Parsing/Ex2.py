from datetime import datetime, timedelta

def days() -> None:
    todays_day = datetime.now()
    one_day = timedelta(days=1, hours=0, minutes=0)
    print(f"Yesterday - {todays_day - one_day}")
    print(f"Today - {todays_day}")
    print(f'Tomorrow {todays_day + one_day}')

    return None

days()