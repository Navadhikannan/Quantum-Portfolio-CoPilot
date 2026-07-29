from pathlib import Path
import random

import numpy as np
import pandas as pd


# Configuration


random.seed(42)
np.random.seed(42)

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

NUM_ASSETS = 30


# Asset Configuration


ASSET_CONFIG = {
    "Equity": {
        "count": 12,
        "return_range": (0.09, 0.15),
        "volatility_range": (0.15, 0.28),
        "cost_range": (0.004, 0.010),
        "liquidity_range": (7, 10),
        "sectors": [
            "Technology",
            "Healthcare",
            "Finance",
            "Energy",
            "Consumer",
            "Industrial",
        ],
    },
    "Bond": {
        "count": 6,
        "return_range": (0.03, 0.06),
        "volatility_range": (0.03, 0.08),
        "cost_range": (0.001, 0.003),
        "liquidity_range": (8, 10),
        "sectors": [
            "Government",
            "Corporate",
        ],
    },
    "ETF": {
        "count": 5,
        "return_range": (0.06, 0.10),
        "volatility_range": (0.08, 0.15),
        "cost_range": (0.002, 0.005),
        "liquidity_range": (8, 10),
        "sectors": [
            "Diversified",
        ],
    },
    "Commodity": {
        "count": 4,
        "return_range": (0.05, 0.11),
        "volatility_range": (0.10, 0.20),
        "cost_range": (0.003, 0.007),
        "liquidity_range": (6, 9),
        "sectors": [
            "Gold",
            "Silver",
            "Oil",
            "Agriculture",
        ],
    },
    "Cash": {
        "count": 3,
        "return_range": (0.01, 0.03),
        "volatility_range": (0.00, 0.01),
        "cost_range": (0.000, 0.001),
        "liquidity_range": (10, 10),
        "sectors": [
            "Cash",
        ],
    },
}


# Generate Synthetic Assets


assets = []
asset_id = 1

for asset_class, config in ASSET_CONFIG.items():

    for _ in range(config["count"]):

        asset = {
            "Asset_ID": f"A{asset_id:02}",
            "Asset_Name": f"{asset_class}_{asset_id}",
            "Asset_Class": asset_class,
            "Sector": random.choice(config["sectors"]),
            "Expected_Return": round(
                random.uniform(*config["return_range"]), 4
            ),
            "Volatility": round(
                random.uniform(*config["volatility_range"]), 4
            ),
            "Transaction_Cost": round(
                random.uniform(*config["cost_range"]), 4
            ),
            "Liquidity_Score": random.randint(
                *config["liquidity_range"]
            ),
        }

        assets.append(asset)
        asset_id += 1


# Create Asset DataFrame


df = pd.DataFrame(assets)


# Save Synthetic Dataset


asset_file = DATA_DIR / "synthetic_assets.csv"
df.to_csv(asset_file, index=False)


# Generate Correlation Matrix


random_matrix = np.random.uniform(
    low=-0.30,
    high=0.90,
    size=(NUM_ASSETS, NUM_ASSETS),
)

# Make matrix symmetric
correlation_matrix = (
    random_matrix + random_matrix.T
) / 2

# Set diagonal = 1
np.fill_diagonal(correlation_matrix, 1.0)

correlation_df = pd.DataFrame(
    correlation_matrix,
    index=df["Asset_ID"],
    columns=df["Asset_ID"],
)

correlation_file = DATA_DIR / "correlation_matrix.csv"
correlation_df.to_csv(correlation_file)


# Preview


print("=" * 60)
print("Synthetic Portfolio Dataset Generated Successfully")
print("=" * 60)

print(df.head())

print("\nTotal Assets       :", len(df))
print("Asset Dataset      :", asset_file)
print("Correlation Matrix :", correlation_file)