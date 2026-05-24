import pandas as pd


def load_data(filepath):
    """Load insurance data from CSV file."""
    return pd.read_csv(filepath)


def load_and_prepare(filepath):
    """Load data and create derived metrics."""
    df = pd.read_csv(filepath)
    df["TransactionDate"] = pd.to_datetime(df["TransactionDate"])
    df["LossRatio"] = df["TotalClaims"] / df["TotalPremium"]
    df["Margin"] = df["TotalPremium"] - df["TotalClaims"]
    return df
