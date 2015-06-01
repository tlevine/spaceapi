DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

def earlier_later(day, hour, radius):
    yd, yh = clock_time(day, hour - 24)
    td, th = clock_time(day, hour + 24)

    ed, eh = clock_time(day, hour - radius)
    ld, lh = clock_time(day, hour + radius)

    return {
        'yesterday_day': yd,
        'yesterday_hour': yh,
        'tomorrow_day': td,
        'tomorrow_hour': th,
        'earlier_day': ed,
        'earlier_hour': eh,
        'later_day': ld,
        'later_hour': lh,
    }

def clock_time(day, hour):
    if 0 <= hour <= 23:
        return day, hour
    
    i = DAYS.index(day)
    if hour < 0:
        return DAYS[(i - 1) % 7], hour + 24
    
    if hour > 23:
        return DAYS[(i + 1) % 7], hour - 24
