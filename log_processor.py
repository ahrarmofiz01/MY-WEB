import re
def parse_log(log):
    parts = log.split()

    if len(parts) < 4:
        return None

    timestamp = parts[0] + " " + parts[1]
    level = parts[2]
    message = " ".join(parts[3:])

    return {
        "timestamp": timestamp,
        "level": level,
        "message": message
    }
def fingerprint_error(message):
    fingerprint = re.sub(r"user \d+", "user <ID>", message)

    return fingerprint
def analyze_logs(parsed_logs):
    error_counts = {}

    for log in parsed_logs:
        if log["level"] == "ERROR":
            message = log["message"]
            fingerprint = fingerprint_error(message)
            if fingerprint in error_counts:
                error_counts[fingerprint] += 1
            else:
                error_counts[fingerprint] = 1

    return error_counts

  
