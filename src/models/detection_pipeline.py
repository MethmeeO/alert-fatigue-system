import pandas as pd
from models.isolation_forest import IsolationForestModel
from models.autoencoder import AutoencoderModel

class DetectionPipeline:
    def __init__(self):
        self.if_model = IsolationForestModel()
        self.ae_model = None

    def run(self, df):
        # Step 1: Train Isolation Forest
        self.if_model.train(df)
        df = self.if_model.predict(df)

        # Step 2: Prepare data for Autoencoder
        features = df[["request_count", "failed_logins"]].values

        self.ae_model = AutoencoderModel(input_dim=features.shape[1])
        self.ae_model.train(features)

        # Step 3: Reconstruction error
        errors = self.ae_model.get_reconstruction_error(features)
        df["reconstruction_error"] = errors

        # Step 4: Final anomaly decision
        threshold = errors.mean() + 2 * errors.std()

        df["final_anomaly"] = df.apply(
            lambda row: 1 if (row["anomaly_label_if"] == 1 and row["reconstruction_error"] > threshold) else 0,
            axis=1
        )

        return df