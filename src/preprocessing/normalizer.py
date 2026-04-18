import pandas as pd

def normalize_timestamp(df):
    """Convert timestamps to datetime format"""
    
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors='coerce')
    
    return df