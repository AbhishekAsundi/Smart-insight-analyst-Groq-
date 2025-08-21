import pandas as pd
import numpy as np

class DataAgent:
    def run(self, df):
        """Profile the dataset."""
        numeric = df.select_dtypes(include=np.number).describe().to_dict()
        categorical = df.select_dtypes(exclude=np.number).describe().to_dict()
        nulls = df.isnull().sum().to_dict()
        sample = df.head(10).to_dict(orient="records")
        return {"numeric": numeric, "categorical": categorical, "nulls": nulls, "sample": sample}
