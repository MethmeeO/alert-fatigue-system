import time
import random

LOG_FILE = "logs/app.log"

users = ["admin", "guest", "user1"]
ips = ["10.10.10.10", "192.168.1.100", "172.16.0.5"]

def generate_brute_force():
    print("🔥 Simulating Brute Force Attack...")

    with open(LOG_FILE, "a") as f:
        for i in range(20):
            user = random.choice(users)
            ip = random.choice(ips)

            log = f"2026-04-01 12:00:{i:02d} | LOGIN_FAILED user={user} ip={ip} endpoint=/login\n"
            f.write(log)

            time.sleep(0.2)

def generate_scan():
    print("🔍 Simulating Endpoint Scan...")

    endpoints = ["/admin", "/config", "/db", "/secret"]

    with open(LOG_FILE, "a") as f:
        for i in range(20):
            ep = random.choice(endpoints)
            log = f"2026-04-01 12:01:{i:02d} | GET_REQUEST user=hacker ip=10.10.10.10 endpoint={ep}\n"
            f.write(log)

            time.sleep(0.2)

if __name__ == "__main__":
    generate_brute_force()
    generate_scan()