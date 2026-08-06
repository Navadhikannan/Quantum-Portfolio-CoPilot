# Quantum Portfolio Optimization

## Overview

The Quantum Portfolio Optimization module extends the classical portfolio optimization approach by formulating the portfolio selection problem as a Quadratic Unconstrained Binary Optimization (QUBO) problem and solving it using the Quantum Approximate Optimization Algorithm (QAOA).

Unlike the classical optimizer, which computes continuous portfolio weights, the quantum optimizer selects an optimal subset of assets using binary decision variables. This approach demonstrates the application of quantum computing techniques to combinatorial optimization problems in finance.

---

# Quantum Optimization Objective

The optimization aims to:

- Maximize Expected Portfolio Return
- Minimize Portfolio Risk
- Minimize Transaction Cost
- Select a fixed number of assets

Each asset is represented by a binary decision variable.

```
xi = 1   Asset is selected

xi = 0   Asset is not selected
```

---

# QUBO Formulation

The portfolio optimization problem is transformed into a Quadratic Unconstrained Binary Optimization (QUBO) model.

The objective function is expressed as:

Q = βΣ − diag(αR − γC)

Where:

- **Σ** = Covariance Matrix (Risk)
- **R** = Expected Return
- **C** = Transaction Cost
- **α** = Return Weight
- **β** = Risk Weight
- **γ** = Transaction Cost Weight

The QUBO formulation combines these objectives into a single optimization problem that can be solved by a quantum optimization algorithm.

---

# Portfolio Model

The QUBO model is converted into a Quadratic Program using the Qiskit Optimization library.

The model consists of:

- Binary decision variables
- Objective function
- Asset selection constraint

Example constraint:

```
x₁ + x₂ + x₃ + ... + x₁₅ = 4
```

This ensures that exactly four assets are selected.

---

# Quantum Optimization Algorithm

The optimization problem is solved using the Quantum Approximate Optimization Algorithm (QAOA).

QAOA is a hybrid quantum-classical algorithm designed for solving combinatorial optimization problems.

The algorithm alternates between:

- Problem Hamiltonian
- Mixing Hamiltonian

A classical optimizer updates the circuit parameters until the objective function converges.

---

# Classical Optimizer

The QAOA circuit parameters are optimized using the COBYLA optimizer.

Reasons for selecting COBYLA:

- Gradient-free optimization
- Efficient for quantum circuits
- Suitable for noisy optimization landscapes
- Commonly used with QAOA

---

# Quantum Simulation

The project executes QAOA locally using the Qiskit Statevector Sampler.

This provides an ideal quantum simulation environment without requiring access to physical quantum hardware.

---

# Workflow

The quantum optimization process consists of the following steps:

1. Load the asset dataset.
2. Build the Quadratic Program.
3. Convert the model into a QUBO formulation.
4. Configure the QAOA algorithm.
5. Execute quantum optimization.
6. Decode the selected assets.
7. Save the optimized portfolio.
8. Compare with the classical solution.

---

# Output

The Quantum Optimization module generates:

- Quantum Portfolio (`quantum_portfolio.csv`)
- Selected Assets
- Objective Function Value
- Execution Time

---

# Advantages

- Suitable for combinatorial optimization.
- Binary asset selection.
- Hybrid quantum-classical optimization.
- Scalable QUBO formulation.
- Modular implementation using Qiskit.

---

# Current Implementation

The current implementation includes:

- 15 quantum optimization assets
- Binary portfolio selection
- QUBO formulation
- QAOA optimization
- COBYLA optimizer
- Statevector simulation
- Streamlit visualization

---

# Limitations

The current implementation is designed for simulation and demonstration purposes.

Current limitations include:

- Executes on a quantum simulator rather than physical quantum hardware.
- Uses a subset of 15 assets for efficient simulation.
- Does not include sector diversification constraints in the quantum optimization model.
- Uses synthetic financial data instead of live market data.

---

# Summary

The Quantum Portfolio Optimization module demonstrates how quantum computing techniques can be applied to financial portfolio optimization. By transforming the portfolio selection problem into a QUBO model and solving it using QAOA, the project provides a practical comparison between classical and quantum optimization methods while showcasing the potential of hybrid quantum-classical computing.