import numpy as np
import pandas as pd

from config import (
    ASSET_DATA_FILE,
    COVARIANCE_FILE,
    QUBO_MATRIX_FILE,
    QUBO_SETTINGS,
    QUANTUM_NUM_ASSETS,
)


# ==========================================================
# Load Data
# ==========================================================

def load_data():
    """Load asset dataset and covariance matrix."""

    assets = pd.read_csv(
        ASSET_DATA_FILE
    )

    covariance = pd.read_csv(
        COVARIANCE_FILE,
        index_col=0
    )

    # Quantum optimization uses only the first N assets
    assets = assets.iloc[:QUANTUM_NUM_ASSETS]

    covariance = covariance.iloc[
        :QUANTUM_NUM_ASSETS,
        :QUANTUM_NUM_ASSETS
    ]

    return assets, covariance


# ==========================================================
# Build QUBO Matrix
# ==========================================================

def build_qubo_matrix(
    expected_returns,
    covariance_matrix,
    transaction_costs,
):
    """
    Build the QUBO matrix.

    Objective:

        Maximize Expected Return
        Minimize Portfolio Risk
        Minimize Transaction Cost

    Q = βΣ − diag(αR − γC)
    """

    return_weight = QUBO_SETTINGS["return_weight"]
    risk_weight = QUBO_SETTINGS["risk_weight"]
    transaction_cost_weight = QUBO_SETTINGS["transaction_cost_weight"]

    # Risk term
    qubo = risk_weight * covariance_matrix.copy()

    # Diagonal reward/penalty
    diagonal = (
        return_weight * expected_returns
        - transaction_cost_weight * transaction_costs
    )

    qubo -= np.diag(diagonal)

    return qubo


# ==========================================================
# Save QUBO Matrix
# ==========================================================

def save_qubo_matrix(
    qubo_matrix,
    asset_ids,
):
    """Save QUBO matrix to CSV."""

    qubo_df = pd.DataFrame(
        qubo_matrix,
        index=asset_ids,
        columns=asset_ids,
    )

    qubo_df.to_csv(QUBO_MATRIX_FILE)

    print(f"✓ QUBO matrix saved to {QUBO_MATRIX_FILE}")


# ==========================================================
# Display Summary
# ==========================================================

def display_summary(
    assets,
    qubo_matrix,
):
    """Display matrix information."""

    print("\nQUBO Summary")
    print("-" * 35)

    print(f"Number of Assets : {len(assets)}")
    print(f"Matrix Shape     : {qubo_matrix.shape}")
    print(f"Matrix Type      : {type(qubo_matrix).__name__}")

    print("\nFirst 5 Diagonal Values")

    diagonal = np.diag(qubo_matrix)

    for i in range(min(5, len(diagonal))):
        print(f"{assets.iloc[i]['Asset_ID']} : {diagonal[i]:.6f}")


# ==========================================================
# Main
# ==========================================================

def main():

    assets, covariance = load_data()

    expected_returns = assets["Expected_Return"].values

    transaction_costs = assets["Transaction_Cost"].values

    qubo_matrix = build_qubo_matrix(
        expected_returns,
        covariance.values,
        transaction_costs,
    )

    save_qubo_matrix(
        qubo_matrix,
        assets["Asset_ID"],
    )

    display_summary(
        assets,
        qubo_matrix,
    )


# ==========================================================
# Entry Point
# ==========================================================

if __name__ == "__main__":
    main()