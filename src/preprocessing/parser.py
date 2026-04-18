import re

def parse_log_line(line, source="app"):
    try:
        line = line.strip()
        if "|" not in line:
            return None

        timestamp_part, message_part = line.split("|", 1)

        user_match = re.search(r"user=([^\s]+)", message_part)
        ip_match = re.search(r"ip=([^\s]+)", message_part)
        endpoint_match = re.search(r"endpoint=([^\s]+)", message_part)

        event_type = "GET_REQUEST"
        if "LOGIN_SUCCESS" in message_part:
            event_type = "login_success"
        elif "LOGIN_FAILED" in message_part:
            event_type = "login_failed"
        elif "OR 1=1" in message_part:
            event_type = "sqli_attempt"

        return {
            "timestamp": timestamp_part.strip(),
            "ip": ip_match.group(1) if ip_match else "0.0.0.0",
            "user": user_match.group(1) if user_match else "anonymous",
            "event_type": event_type,
            "endpoint": endpoint_match.group(1) if endpoint_match else "unknown",
            "source": source
        }

    except:
        return None