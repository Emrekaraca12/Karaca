def date_difference_in_seconds(date1, date2):
    from datetime import datetime
    dt1 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
    dt2 = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
    
    time_difference = dt2 - dt1

    difference_in_seconds = time_difference.total_seconds()
    
    return difference_in_seconds