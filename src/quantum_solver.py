"""
quantum_solver.py
 
Part 1
-------
Load the portfolio model and convert it to a QUBO.
"""
 
import time

import pandas as pd

from config import (
    ASSET_DATA_FILE,
    QUANTUM_RESULTS_FILE,
    QUANTUM_NUM_ASSETS,
)
 
from portfolio_model import (
    build_portfolio_model,
)
 
from qiskit_optimization.converters import (
    QuadraticProgramToQubo,
)
 
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit_optimization.minimum_eigensolvers import QAOA
from qiskit_optimization.optimizers import COBYLA
 
from qiskit.primitives import StatevectorSampler
 
 
# ---------------------------------------------------------
# Build Portfolio Model
# ---------------------------------------------------------
 
def load_portfolio_model():
    """
    Build the QuadraticProgram defined in
    portfolio_model.py.
    """
 
    model = build_portfolio_model()
 
    print("✓ Portfolio model loaded")
 
    return model
 
 
# ---------------------------------------------------------
# Convert to QUBO
# ---------------------------------------------------------
 
def convert_to_qubo(model):
    """
    Convert QuadraticProgram to QUBO.
    """
 
    converter = QuadraticProgramToQubo()
 
    qubo = converter.convert(model)
 
    print("✓ QUBO conversion completed")
 
    return qubo, converter
 
 
# ---------------------------------------------------------
# Display Information
# ---------------------------------------------------------
 
def display_qubo_summary(qubo):
 
    print("\n" + "=" * 60)
    print("Quantum Portfolio Solver")
    print("=" * 60)
 
    print(f"Problem Name      : {qubo.name}")
    print(f"Binary Variables  : {qubo.get_num_binary_vars()}")
    print(f"Constraints       : {qubo.get_num_linear_constraints()}")
 
    # Full prettyprint() is omitted here on purpose for large problems
    # (30 assets => hundreds of lines of output that bury real errors).
    # Uncomment once the solver is confirmed working end-to-end:
    # print("\nQUBO Model")
    # print("-" * 60)
    # print(qubo.prettyprint())
 
 
# ---------------------------------------------------------
# Create QAOA Solver
# ---------------------------------------------------------
 
def create_qaoa_solver():
    """
    Configure the QAOA optimizer.
 
    NOTE: We use qiskit.primitives.StatevectorSampler instead of
    qiskit_aer's AerSimulator + SamplerV2 + generate_preset_pass_manager
    combo. That combo triggers a known upstream bug (Qiskit/qiskit-aer#2015)
    where AerSimulator's generated Target doesn't correctly declare
    non-unitary instructions like "measure"/"reset", causing
    HighLevelSynthesis to fail trying to synthesize them.
 
    StatevectorSampler is qiskit's own exact local simulator, needs no
    hardware-basis transpilation, and is what the official qiskit-algorithms
    QAOA tutorial uses for local runs. No pass_manager is needed at all.
    """
 
    sampler = StatevectorSampler(seed=123)
 
    optimizer = COBYLA(
        maxiter=100,
    )
 
    qaoa = QAOA(
        sampler=sampler,
        optimizer=optimizer,
        reps=2,
    )
 
    solver = MinimumEigenOptimizer(qaoa)
 
    print("✓ QAOA solver initialized")
 
    return solver
 
 
# ---------------------------------------------------------
# Solve QUBO
# ---------------------------------------------------------
 
def solve_qubo(
    solver,
    qubo,
):
    """
    Solve the optimization problem.
    """
 
    print("Running QAOA...")
 
    result = solver.solve(qubo)
 
    print("✓ Optimization completed")
 
    return result

# ---------------------------------------------------------
# Decode Solution
# ---------------------------------------------------------

def decode_solution(result):
    """
    Extract selected asset indices from the QAOA result.
    """

    selected_indices = []

    for i, value in enumerate(result.x):
        if value > 0.5:
            selected_indices.append(i)

    return selected_indices


# ---------------------------------------------------------
# Save Quantum Portfolio
# ---------------------------------------------------------

def save_quantum_portfolio(selected_indices):
    """
    Save selected assets to CSV.
    """

    assets = pd.read_csv(ASSET_DATA_FILE)

    # Keep the same quantum subset
    assets = assets.iloc[:QUANTUM_NUM_ASSETS].reset_index(drop=True)

    portfolio = assets.iloc[selected_indices].copy()

    portfolio["Weight"] = (
        1.0 / len(portfolio)
    )

    portfolio.to_csv(
        QUANTUM_RESULTS_FILE,
        index=False,
    )

    print(
        f"\n✓ Quantum portfolio saved to {QUANTUM_RESULTS_FILE}"
    )

    return portfolio


# ---------------------------------------------------------
# Display Portfolio
# ---------------------------------------------------------

def display_portfolio(portfolio):

    print("\nSelected Quantum Assets")
    print("-" * 45)

    print(
        portfolio[
            [
                "Asset_ID",
                "Asset_Name",
                "Asset_Class",
                "Expected_Return",
                "Weight",
            ]
        ]
    )

 
 
# ---------------------------------------------------------
# Main
# ---------------------------------------------------------
 
def main():

    start = time.time()

    model = load_portfolio_model()

    qubo, converter = convert_to_qubo(model)

    display_qubo_summary(qubo)

    solver = create_qaoa_solver()

    result = solve_qubo(
        solver,
        qubo,
    )

    elapsed = time.time() - start

    print("\n" + "=" * 60)
    print("Optimization Result")
    print("=" * 60)

    print(result.prettyprint())

    # Decode selected assets
    selected = decode_solution(result)

    # Save portfolio
    portfolio = save_quantum_portfolio(selected)

    # Display portfolio
    display_portfolio(portfolio)

    print(f"\nExecution Time : {elapsed:.3f} sec")
# ---------------------------------------------------------
 
if __name__ == "__main__":
    main()
 
 