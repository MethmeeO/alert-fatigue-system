import pandas as pd

def clean_logs(df):
    """Remove nulls & duplicates"""
    
    df = df.dropna()
    df = df.drop_duplicates()

    return df