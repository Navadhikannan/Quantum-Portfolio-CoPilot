import numpy as np
import pandas as pd
from scipy.optimize import minimize

from config import (
    ASSET_DATA_FILE,
    COVARIANCE_FILE,
    MAX_WEIGHT,
    MIN_WEIGHT,
    TOTAL_WEIGHT,
    RISK_AVERSION,
    OUTPUT_PORTFOLIO
)


def load_data():
    """Load asset dataset and covariance matrix."""

    assets = pd.read_csv(ASSET_DATA_FILE)
    covariance = pd.read_csv(COVARIANCE_FILE, index_col=0)

    return assets, covariance


def validate_data(assets, covariance):
    """Validate input files."""

    if assets.empty:
        raise ValueError("Asset dataset is empty.")

    if covariance.empty:
        raise ValueError("Covariance matrix is empty.")

    if len(assets) != covariance.shape[0]:
        raise ValueError(
            "Asset count and covariance matrix size do not match."
        )

    print("✓ Data validation successful.")


def calculate_return(weights, expected_returns):
    """Calculate portfolio expected return."""

    return np.dot(weights, expected_returns)


def calculate_risk(weights, covariance_matrix):
    """Calculate portfolio risk."""

    variance = np.dot(weights.T, np.dot(covariance_matrix, weights))
    return np.sqrt(variance)


def objective_function(weights, expected_returns, covariance_matrix):
    """
    Objective:
    Minimize risk while maximizing return.
    """

    portfolio_return = calculate_return(weights, expected_returns)
    portfolio_risk = calculate_risk(weights, covariance_matrix)

    return portfolio_risk - (RISK_AVERSION * portfolio_return)


def optimize_portfolio(expected_returns, covariance_matrix):
    """Run classical portfolio optimization."""

    num_assets = len(expected_returns)

    initial_weights = np.ones(num_assets) / num_assets

    bounds = [
        (MIN_WEIGHT, MAX_WEIGHT)
        for _ in range(num_assets)
    ]

    constraints = (
        {
            "type": "eq",
            "fun": lambda w: np.sum(w) - TOTAL_WEIGHT
        },
    )

    result = minimize(
        objective_function,
        initial_weights,
        args=(expected_returns, covariance_matrix),
        method="SLSQP",
        bounds=bounds,
        constraints=constraints
    )

    return result


def save_results(assets, weights):
    """Save optimized portfolio."""

    portfolio = assets.copy()

    portfolio["Weight"] = weights

    portfolio.to_csv(OUTPUT_PORTFOLIO, index=False)

    print(f"✓ Portfolio saved to {OUTPUT_PORTFOLIO}")


def print_summary(result, portfolio_return, portfolio_risk):
    """Display optimization summary."""

    print("\nOptimized Portfolio")
    print("-" * 35)

    print(f"Optimization Success : {result.success}")
    print(f"Status Message       : {result.message}")
    print(f"Expected Return      : {portfolio_return:.4f}")
    print(f"Portfolio Risk       : {portfolio_risk:.4f}")


def main():

    assets, covariance = load_data()

    validate_data(assets, covariance)

    expected_returns = assets["Expected_Return"].values

    optimization = optimize_portfolio(
        expected_returns,
        covariance.values
    )

    if not optimization.success:
        raise RuntimeError(
            f"Optimization failed: {optimization.message}"
        )

    optimal_weights = optimization.x

    portfolio_return = calculate_return(
        optimal_weights,
        expected_returns
    )

    portfolio_risk = calculate_risk(
        optimal_weights,
        covariance.values
    )

    save_results(
        assets,
        optimal_weights
    )

    print_summary(
        optimization,
        portfolio_return,
        portfolio_risk
    )


if __name__ == "__main__":
    main()