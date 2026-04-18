import pandas as pd

class RiskScoring:
    def calculate_risk(self, df: pd.DataFrame) -> pd.DataFrame:
        if "final_anomaly" not in df.columns:
            df["risk_score"] = 0
            return df

        # Simple risk score: base on anomaly and failed logins
        df["risk_score"] = (df["final_anomaly"] * 5) + df.get("failed_logins", 0)
        return df

    def classify_risk(self, df: pd.DataFrame) -> pd.DataFrame:
        def get_level(score):
            if score >= 8:
                return "high"
            elif score >= 4:
                return "medium"
            else:
                return "low"

        df["risk_level"] = df["risk_score"].apply(get_level)
        return df
