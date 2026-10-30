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
def analyze_logs(parsed_logs):
    error_counts = {}

    for log in parsed_logs:
        if log["level"] == "ERROR":
            message = log["message"]

            if message in error_counts:
                error_counts[message] += 1
            else:
                error_counts[message] = 1

    return error_counts