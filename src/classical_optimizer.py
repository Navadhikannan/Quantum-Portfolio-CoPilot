import numpy as np
import pandas as pd

from config import (
    ASSET_DATA_FILE,
    COVARIANCE_FILE
)


def load_data():
    """Load asset information and covariance matrix."""

    assets = pd.read_csv(ASSET_DATA_FILE)
    covariance = pd.read_csv(COVARIANCE_FILE, index_col=0)

    return assets, covariance


def validate_data(assets, covariance):
    """Basic validation of loaded data."""

    if assets.empty:
        raise ValueError("Asset dataset is empty.")

    if covariance.empty:
        raise ValueError("Covariance matrix is empty.")

    if len(assets) != covariance.shape[0]:
        raise ValueError(
            "Number of assets and covariance matrix size do not match."
        )

    print("Data validation successful.")


def calculate_return(weights, expected_returns):
    """Calculate expected portfolio return."""

    return np.dot(weights, expected_returns)


def calculate_risk(weights, covariance_matrix):
    """Calculate portfolio risk (standard deviation)."""

    variance = np.dot(weights.T, np.dot(covariance_matrix, weights))
    return np.sqrt(variance)


def main():

    assets, covariance = load_data()

    validate_data(assets, covariance)

    num_assets = len(assets)

    weights = np.ones(num_assets) / num_assets

    expected_returns = assets["Expected_Return"].values

    portfolio_return = calculate_return(weights, expected_returns)

    portfolio_risk = calculate_risk(weights, covariance.values)

    print("\nEqual Weight Portfolio")
    print("-" * 30)
    print(f"Assets            : {num_assets}")
    print(f"Expected Return   : {portfolio_return:.4f}")
    print(f"Portfolio Risk    : {portfolio_risk:.4f}")


if __name__ == "__main__":
    main()