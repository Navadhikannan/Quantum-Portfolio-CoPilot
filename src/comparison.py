import pandas as pd

from config import (
    OUTPUT_PORTFOLIO,
    QUANTUM_RESULTS_FILE,
)

# Load Portfolios


def load_portfolios():
    """Load classical and quantum portfolio CSV files."""

    classical = pd.read_csv(OUTPUT_PORTFOLIO)
    quantum = pd.read_csv(QUANTUM_RESULTS_FILE)

    return classical, quantum

# Portfolio Metrics


def portfolio_metrics(portfolio):
    """Calculate portfolio statistics."""

    expected_return = (
        portfolio["Expected_Return"] *
        portfolio["Weight"]
    ).sum()

    portfolio_risk = (
        (
            portfolio["Volatility"] ** 2 *
            portfolio["Weight"]
        ).sum()
    ) ** 0.5

    sharpe_ratio = (
        expected_return / portfolio_risk
        if portfolio_risk != 0
        else 0
    )

    return {
        "Expected Return": expected_return,
        "Portfolio Risk": portfolio_risk,
        "Sharpe Ratio": sharpe_ratio,
        "Selected Assets": len(portfolio),
    }

# Comparison Table

def create_comparison_table(
    classical_metrics,
    quantum_metrics,
):
    """Create comparison DataFrame."""

    comparison = pd.DataFrame({
        "Metric": classical_metrics.keys(),
        "Classical": classical_metrics.values(),
        "Quantum": quantum_metrics.values(),
    })

    return comparison

# Display Comparison

def display_results(comparison):

    print("\n")
    print("=" * 65)
    print(" Classical vs Quantum Portfolio Comparison")
    print("=" * 65)

    print(
        comparison.to_string(index=False)
    )



# Main


def main():

    classical, quantum = load_portfolios()

    classical_metrics = portfolio_metrics(
        classical
    )

    quantum_metrics = portfolio_metrics(
        quantum
    )

    comparison = create_comparison_table(
        classical_metrics,
        quantum_metrics,
    )

    # Save comparison results
    comparison.to_csv(
        "results/comparison_results.csv",
        index=False
    )

    print(
        "\n✓ Comparison saved to results/comparison_results.csv"
    )

    display_results(comparison)

# Entry Point


if __name__ == "__main__":
    main()