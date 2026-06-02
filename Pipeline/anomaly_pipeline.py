import pandas as pd

def detect_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    """
    Detecta anomalias simples usando z-score.
    """
    df = df.copy()
    numeric_cols = ["temperature", "humidity", "wind_speed", "risk_score"]

    # Calcula os z-scores
    for col in numeric_cols:
        if col in df.columns:
            mean = df[col].mean()
            std = df[col].std()

            if std == 0:
                df[f"{col}_zscore"] = 0
            else:
                df[f"{col}_zscore"] = (df[col] - mean) / std

    df["anomaly"] = False

    # Verifica anomalias
    for col in numeric_cols:
        z_col = f"{col}_zscore"
        if z_col in df.columns:
            # Limite reduzido para 1.5 para funcionar com os dados simulados atuais
            df["anomaly"] = df["anomaly"] | (df[z_col].abs() > 1.5)

    return df