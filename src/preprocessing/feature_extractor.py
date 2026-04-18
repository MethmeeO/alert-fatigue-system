import pandas as pd

def extract_features(df):

    # Request frequency per IP
    request_freq = df.groupby("ip").size().reset_index(name="request_count")

    # Failed login attempts per user
    failed_logins = df[df["event_type"] == "login_failed"] \
        .groupby("user").size().reset_index(name="failed_logins")

    # Endpoint usage
    endpoint_usage = df.groupby(["user", "endpoint"]) \
        .size().reset_index(name="endpoint_hits")

    # Merge all
    df = df.merge(request_freq, on="ip", how="left")
    df = df.merge(failed_logins, on="user", how="left")
    df = df.merge(endpoint_usage, on=["user", "endpoint"], how="left")

    # Fill missing
    df["failed_logins"] = df["failed_logins"].fillna(0)

    # SESSION BEHAVIOR
    df = df.sort_values(by=["user", "timestamp"])
    df["session_duration"] = df.groupby("user")["timestamp"].diff().dt.seconds
    df["session_duration"] = df["session_duration"].fillna(0)

    return df