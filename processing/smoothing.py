def moving_average(values, window):
    if not values:
        return None
    recent = values[-window:]
    return sum(recent) / len(recent)
