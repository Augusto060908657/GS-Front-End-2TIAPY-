def calculate_fire_risk(df):

    risk = (
        df["temperature"] * 0.4 +
        df["wind_speed"] * 0.3 +
        (100 - df["humidity"]) * 0.2 +
        (30 - df["rainfall"]) * 0.1
    )

    df["risk_score"] = risk.clip(0, 100)

    def classify(score):

        if score < 30:
            return "Baixo"

        if score < 60:
            return "Médio"

        if score < 80:
            return "Alto"

        return "Crítico"

    df["risk_level"] = df["risk_score"].apply(classify)

    return df
    