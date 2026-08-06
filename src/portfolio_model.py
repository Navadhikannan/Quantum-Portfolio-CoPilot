import pandas as pd

from qiskit_optimization import QuadraticProgram

from config import (
    ASSET_DATA_FILE,
    COVARIANCE_FILE,
    QUBO_SETTINGS,
    QUANTUM_NUM_ASSETS,
)


# Configuration


NUM_SELECTED_ASSETS = 4



# Load Dataset

def load_data():
    """Load asset dataset and covariance matrix."""

    assets = pd.read_csv(ASSET_DATA_FILE)

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


# Create Optimization Model


def create_model():
    """Create an empty Quadratic Program."""

    model = QuadraticProgram("Quantum_Portfolio")

    return model



# Add Binary Variables


def add_binary_variables(model, num_assets):
    """
    Create one binary variable for each asset.
    """

    for i in range(num_assets):
        model.binary_var(name=f"x{i}")



# Build Objective Function


def build_objective(
    model,
    assets,
    covariance,
):
    """
    Objective:

    Maximize Return
    Minimize Risk
    Minimize Transaction Cost
    """

    return_weight = QUBO_SETTINGS["return_weight"]
    risk_weight = QUBO_SETTINGS["risk_weight"]
    transaction_cost_weight = QUBO_SETTINGS["transaction_cost_weight"]

    linear = {}

    quadratic = {}

    expected_returns = assets["Expected_Return"].values
    transaction_costs = assets["Transaction_Cost"].values

    num_assets = len(assets)

    # Linear coefficients
    for i in range(num_assets):

        linear[f"x{i}"] = -(
            return_weight * expected_returns[i]
        ) + (
            transaction_cost_weight * transaction_costs[i]
        )

    # Quadratic coefficients
    for i in range(num_assets):

        for j in range(i, num_assets):

            quadratic[(f"x{i}", f"x{j}")] = (
                risk_weight * covariance.iloc[i, j]
            )

    model.minimize(
        linear=linear,
        quadratic=quadratic,
    )



# Add Portfolio Constraint


def build_constraints(
    model,
    num_assets,
):
    """
    Select exactly NUM_SELECTED_ASSETS assets.
    """

    linear_constraint = {}

    for i in range(num_assets):
        linear_constraint[f"x{i}"] = 1

    model.linear_constraint(
        linear=linear_constraint,
        sense="==",
        rhs=NUM_SELECTED_ASSETS,
        name="asset_selection",
    )



# Display Summary

def display_summary(
    assets,
    model,
):
    """Display model information."""

    print("=" * 60)
    print("Quantum Portfolio Optimization Model")
    print("=" * 60)

    print(f"Number of Assets      : {len(assets)}")
    print(f"Binary Variables      : {model.get_num_binary_vars()}")
    print(f"Linear Constraints    : {model.get_num_linear_constraints()}")

    print("\nOptimization Model")
    print("-" * 60)

    print(model.prettyprint())


def build_portfolio_model():
    """Build and return the portfolio optimization model."""

    assets, covariance = load_data()

    model = create_model()

    add_binary_variables(
        model,
        len(assets),
    )

    build_objective(
        model,
        assets,
        covariance,
    )

    build_constraints(
        model,
        len(assets),
    )

    return model



# Main


def main():
    assets, _ = load_data()

    model = build_portfolio_model()

    display_summary(
        assets,
        model,
    )

# Entry Point


if __name__ == "__main__":
    main()