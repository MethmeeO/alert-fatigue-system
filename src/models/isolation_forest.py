import pandas as pd
from sklearn.ensemble import IsolationForest

class IsolationForestModel:
    def __init__(self):
        self.model = IsolationForest(
            n_estimators=100,
            contamination=0.1,
            random_state=42
        )

    def train(self, df):
        features = df[["request_count", "failed_logins"]]
        self.model.fit(features)

    def predict(self, df):
        features = df[["request_count", "failed_logins"]]
        
        df["anomaly_score_if"] = self.model.decision_function(features)
        df["anomaly_label_if"] = self.model.predict(features)

        # Convert: -1 = anomaly → 1, 1 = normal → 0
        df["anomaly_label_if"] = df["anomaly_label_if"].apply(lambda x: 1 if x == -1 else 0)

        return df