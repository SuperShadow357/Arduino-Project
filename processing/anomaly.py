def is_anomaly(current, previous, config):
    if current < config["dark_threshold"]:
        return True
    if current > config["bright_threshold"]:
        return True
    if previous is not None:
        if abs(current - previous) > config["sudden_change_threshold"]:
            return True
    return False
