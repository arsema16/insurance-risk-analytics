import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_loss_ratio_by_province(df, save_path=None):
    """Plot loss ratio by province."""
    province_lr = df.groupby("Province")["LossRatio"].mean().sort_values()
    plt.figure(figsize=(10, 6))
    province_lr.plot(kind="bar")
    plt.title("Loss Ratio by Province")
    plt.xlabel("Province")
    plt.ylabel("Loss Ratio")
    plt.xticks(rotation=45)
    if save_path:
        plt.savefig(save_path)
    plt.show()


def plot_claim_frequency_by_vehicle(df, save_path=None):
    """Plot claim frequency by vehicle type."""
    claim_freq = (
        df.groupby("VehicleType")
        .apply(lambda x: (x["TotalClaims"] > 0).sum() / len(x) * 100)
        .sort_values(ascending=False)
    )
    plt.figure(figsize=(10, 6))
    claim_freq.plot(kind="bar")
    plt.title("Claim Frequency by Vehicle Type")
    plt.xlabel("Vehicle Type")
    plt.ylabel("Claim Frequency (%)")
    plt.xticks(rotation=45)
    if save_path:
        plt.savefig(save_path)
    plt.show()
