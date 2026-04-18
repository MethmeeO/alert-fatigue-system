import os
from datetime import datetime

LOG_FILE = "../../logs/app.log"

def collect_log(message):
    """Simulates syslog log collection"""
    
    log_entry = f"{datetime.utcnow()} | {message}\n"
    
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)

    print("Log collected:", log_entry.strip())


if __name__ == "__main__":
    # Simulated logs
    collect_log("LOGIN_SUCCESS user=admin ip=192.168.1.10 endpoint=/login")
    collect_log("LOGIN_FAILED user=admin ip=192.168.1.10 endpoint=/login")
    collect_log("GET_REQUEST user=guest ip=192.168.1.15 endpoint=/home")