def earlier_later(day, hour, radius):
    ed, eh = clock_time(day, hour - radius)
    ld, lh = clock_time(day, hour + radius)
    return {
        'earlier_day': ed,
        'earlier_hour': eh,
        'later_day': ld,
        'later_hour': lh,
    }

def clock_time(day, hour):
    if 0 <= hour <= 23:
        return day, hour
    
    i = DAYS.index(day)
    if i == 0:
        i = i + len(DAYS)

    if hour < 0:
        return DAYS[i - 1], hour + 24
    
    if hour > 23:
        return DAYS[i + 1], hour - 24
