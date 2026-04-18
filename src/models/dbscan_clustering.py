import pandas as pd
from sklearn.cluster import DBSCAN

class AlertClustering:
    def cluster_alerts(self, df: pd.DataFrame) -> pd.DataFrame:
        if "request_count" not in df.columns or "failed_logins" not in df.columns:
            df["cluster_id"] = -1
            return df

        features = df[["request_count", "failed_logins"]].fillna(0).values
        clusterer = DBSCAN(eps=3, min_samples=2)
        df["cluster_id"] = clusterer.fit_predict(features)
        return df
