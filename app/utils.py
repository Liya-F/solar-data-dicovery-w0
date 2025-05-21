import pandas as pd

def load_data():
    paths = {
        "Benin": "data/benin_clean.csv",
        "Togo": "data/togo_clean.csv",
        "Sierra Leone": "data/sierraleone_clean.csv"
    }
    dfs = {}
    for name, path in paths.items():
        df = pd.read_csv(path)
        df['Country'] = name
        dfs[name] = df
    return pd.concat(dfs.values(), ignore_index=True)

def get_summary_table(df):
    return df.groupby("Country")[["GHI", "DNI", "DHI"]].agg(["mean", "median", "std"]).round(2)
