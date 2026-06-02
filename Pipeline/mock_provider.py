import pandas as pd
import numpy as np

def generate_mock_data(days=30):

    np.random.seed(42)

    df = pd.DataFrame({
        "temperature": np.random.uniform(20, 42, days),
        "humidity": np.random.uniform(10, 95, days),
        "wind_speed": np.random.uniform(5, 50, days),
        "rainfall": np.random.uniform(0, 30, days)
    })

    return df