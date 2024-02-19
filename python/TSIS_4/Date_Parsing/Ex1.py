from datetime import datetime, timedelta

def five_day_substruct() -> datetime:
    todays_day = datetime.now()
    substruct_time = timedelta(days=5, hours=0, minutes=0)
    new_time = todays_day - substruct_time

    return new_time
