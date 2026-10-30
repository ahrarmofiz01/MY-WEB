def parse_log(log):

    parts = log.split()

    timestamp = parts[0] + " " + parts[1]
    level = parts[2]
    message = " ".join(parts[3:])

    return {
        "timestamp": timestamp,
        "level": level,
        "message": message
    }