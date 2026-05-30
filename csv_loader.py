
import pandas as pd

def load_sales(path):
    df = pd.read_csv(path)
    return {
        "rows": len(df)
    }
