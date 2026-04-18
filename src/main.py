import pandas as pd
import os
import sys

# PATH FIX (important)
sys.path.append(os.getcwd())

# Preprocessing
from src.preprocessing.parser import parse_log_line
from src.preprocessing.cleaner import clean_logs
from src.preprocessing.normalizer import normalize_timestamp
from src.preprocessing.feature_extractor import extract_features

# Models
from src.models.detection_pipeline import DetectionPipeline
from src.models.risk_scoring import RiskScoring
from src.models.dbscan_clustering import AlertClustering
from src.threat_intel import check_ip

# LOG FILE PATHS

LOG_FILES = [
    "logs/app.log",
    "logs/auth.log",
    "logs/waf.log"
]

SOURCES = ["app", "auth", "waf"]


def run_pipeline():

    
    # STEP 1: LOAD LOGS

    print("\n" + "-"*40)
    print(" STEP 1: LOADING RAW LOG DATA")
    print("-"*40)

    lines = []

    for file, source in zip(LOG_FILES, SOURCES):
        try:
            if os.path.exists(file):
                with open(file, "r") as f:
                    for line in f:
                        lines.append((line.strip(), source))
                print(f"✅ Loaded: {file}")
            else:
                print(f"⚠️ Warning: {file} not found")
        except Exception as e:
            print(f"❌ Error reading {file}: {e}")

    if not lines:
        print("❌ No logs collected. Pipeline stopping.")
        return

    # STEP 2: PARSE LOGS
  
    parsed_logs = []

    for line, source in lines:
        parsed = parse_log_line(line, source)
        if parsed:
            parsed_logs.append(parsed)

    if not parsed_logs:
        print("❌ No valid logs found after parsing.")
        return

    df = pd.DataFrame(parsed_logs)

    # Add threat intelligence check
    df["threat_score"] = df["ip"].apply(check_ip)

    print("\n" + "-"*40)
    print(" STEP 2: PARSED LOGS")
    print("-"*40)
    print(df[['timestamp', 'user', 'ip', 'endpoint', 'event_type', 'source']].head().to_string(index=False))

  
    # STEP 3: PREPROCESSING + FEATURES
    
    df = clean_logs(df)
    df = normalize_timestamp(df)
    df = extract_features(df)

    print("\n" + "-"*40)
    print(" STEP 3: FEATURES CREATED")
    print("-"*40)

    feature_cols = ['request_count', 'failed_logins', 'endpoint_hits', 'session_duration']

    # Safe print (prevents crash)
    available_cols = [col for col in feature_cols if col in df.columns]
    print(df[available_cols].head().to_string(index=False))

  
    # STEP 4: ANOMALY DETECTION

    print("\n" + "-"*40)
    print(" STEP 4: ANOMALY DETECTION")
    print("-"*40)

    detector = DetectionPipeline()
    df = detector.run(df)

    print("✅ ML Detection Complete")

  
    # STEP 5: RISK SCORING
  
    risk_engine = RiskScoring()
    df = risk_engine.calculate_risk(df)
    df = risk_engine.classify_risk(df)

    print("\n Risk Output:")
    print(df[['risk_score', 'risk_level']].head().to_string(index=False))

    # STEP 6: DBSCAN CLUSTERING
    
    cluster = AlertClustering()
    df = cluster.cluster_alerts(df)

    print("\n Clustering Output:")
    print(df[['cluster_id', 'risk_level']].head().to_string(index=False))

    # STEP 7: SAVE OUTPUT
    
    if not os.path.exists("data"):
        os.makedirs("data")

    output_path = "data/final_output.csv"
    df.to_csv(output_path, index=False)

    print("\n" + "-"*40)
    print("✅ HEIST Pipeline completed successfully!")
    print(f"📁 Output saved to: {output_path}")
    print("-"*40 + "\n")


if __name__ == "__main__":
    run_pipeline()










# ---- 1st cheaking code -----
""" 
import pandas as pd
import os
import sys

# ==============================================================
# 🚀 PATH BRIDGE (Fixes ModuleNotFoundError)
# ==============================================================
# This tells Python to look in the current folder for your modules
sys.path.append(os.getcwd())

# Now we can import your custom modules using the folder name
from src.preprocessing.parser import parse_log_line
from src.preprocessing.cleaner import clean_logs
from src.preprocessing.normalizer import normalize_timestamp
from src.preprocessing.feature_extractor import extract_features

from src.models.detection_pipeline import DetectionPipeline
from src.models.risk_scoring import RiskScoring
from src.models.dbscan_clustering import AlertClustering

# ==============================
# LOG FILE PATHS
# ==============================
# Removing "../" because you should run this from the project root
LOG_FILES = [
    "logs/app.log",
    "logs/auth.log",
    "logs/logs/waf.log"
]

SOURCES = ["app", "auth", "waf"]

def run_pipeline():
    # 1. READ ALL LOG FILES
    lines = []
    for file, source in zip(LOG_FILES, SOURCES):
        try:
            if os.path.exists(file):
                with open(file, "r") as f:
                    for line in f:
                        lines.append((line.strip(), source))
                print(f"✅ Loaded: {file}")
            else:
                print(f"⚠️ Warning: {file} not found")
        except Exception as e:
            print(f"❌ Error reading {file}: {e}")

    if not lines:
        print("❌ No logs collected. Pipeline stopping.")
        return

    # 2. PARSE LOGS
    parsed_logs = []
    for line, source in lines:
        parsed = parse_log_line(line, source)
        if parsed:
            parsed_logs.append(parsed)

    if not parsed_logs:
        print("❌ No valid logs found after parsing.")
        return

    df = pd.DataFrame(parsed_logs)

    # 3-5. PREPROCESSING
    df = clean_logs(df)
    df = normalize_timestamp(df)
    df = extract_features(df)

    # 6. ANOMALY DETECTION
    detector = DetectionPipeline()
    df = detector.run(df)

    # 7. RISK SCORING
    risk_engine = RiskScoring()
    df = risk_engine.calculate_risk(df)
    df = risk_engine.classify_risk(df)

    # 8. ALERT CLUSTERING (DBSCAN)
    cluster = AlertClustering()
    df = cluster.cluster_alerts(df)

    # 9. SAVE OUTPUT
    if not os.path.exists("data"):
        os.makedirs("data")
    
    output_path = "data/final_output.csv"
    df.to_csv(output_path, index=False)

    print("\n✅ HEIST Pipeline completed successfully!")
    print(f"📁 Final results saved to: {output_path}")

if __name__ == "__main__":
    run_pipeline() """