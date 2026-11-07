import random
from datetime import datetime, timedelta

levels = ["INFO", "WARN", "ERROR", "DEBUG"]
endpoints = ["/api/v1/users", "/api/v1/auth", "/health", "/dashboard", "/api/v1/orders"]
status_codes = [200, 201, 400, 401, 404, 500]

start_time = datetime.now() - timedelta(hours=5)

with open("sample.log", "w") as f:
    for i in range(1, 1001):
        timestamp = (start_time + timedelta(seconds=i * 2)).strftime("%Y-%m-%d %H:%M:%S")
        level = random.choice(levels)
        endpoint = random.choice(endpoints)
        status = random.choice(status_codes)
        latency = random.randint(12, 450)
        f.write(f"[{timestamp}] {level} {endpoint} - Status: {status} - {latency}ms\n")

print("Generated 1000 lines in sample.log")
