# 🏗️ System Architecture

## Overview

The Quantum Portfolio CoPilot follows a hybrid classical–quantum architecture that combines conventional portfolio optimization techniques with quantum optimization using the Quantum Approximate Optimization Algorithm (QAOA). The workflow begins with synthetic financial data generation, followed by separate classical and quantum optimization pipelines. The outputs from both approaches are compared and visualized through an interactive Streamlit dashboard.

---

## System Architecture Diagram

<p align="center">
  <img src="../assets/architecture.png" alt="Quantum Portfolio CoPilot Architecture" width="100%">
</p>

---

## Architecture Components

### 1. Synthetic Dataset Generation

The project begins by generating a synthetic financial dataset containing:

- Asset information
- Expected returns
- Transaction costs
- Correlation matrix
- Covariance matrix

These datasets are used by both the classical and quantum optimization pipelines.

---

### 2. Classical Portfolio Optimization

The classical optimizer uses the Sequential Least Squares Programming (SLSQP) algorithm to determine the optimal asset allocation.

Features:

- Expected return maximization
- Portfolio risk minimization
- Budget constraints
- Asset-class allocation constraints
- Weight bounds

Output:

- `optimized_portfolio.csv`

---

### 3. Portfolio Performance Evaluation

The optimized portfolio is evaluated using:

- Expected Return
- Portfolio Risk
- Sharpe Ratio
- Asset Allocation

These metrics provide the benchmark for comparison with the quantum solution.

---

### 4. QUBO Construction

The portfolio optimization problem is transformed into a Quadratic Unconstrained Binary Optimization (QUBO) formulation.

The QUBO objective combines:

- Expected Return
- Portfolio Risk
- Transaction Cost

Output:

- `qubo_matrix.csv`

---

### 5. Portfolio Model

The QUBO formulation is converted into a Quadratic Program using Qiskit Optimization.

The model includes:

- Binary decision variables
- Objective function
- Asset selection constraint

---

### 6. Quantum Optimization

The Quadratic Program is converted into a QUBO problem and solved using the Quantum Approximate Optimization Algorithm (QAOA).

Components:

- Statevector Sampler
- COBYLA Optimizer
- QAOA

---

### 7. Quantum Portfolio Results

The quantum optimizer selects the optimal portfolio and exports the selected assets.

Output:

- `quantum_portfolio.csv`

---

### 8. Portfolio Comparison

The classical and quantum portfolios are compared using:

- Expected Return
- Portfolio Risk
- Sharpe Ratio
- Number of Selected Assets

Output:

- `comparison_results.csv`

---

### 9. Streamlit Dashboard

The final results are presented using an interactive Streamlit dashboard.

The dashboard provides:

- Portfolio metrics
- Performance comparison
- Bar charts
- Asset allocation pie charts
- Portfolio tables
- Downloadable results

---

## Summary

The hybrid architecture integrates classical optimization with quantum optimization to demonstrate how QAOA can be applied to portfolio selection problems. The modular design enables independent execution of each stage while providing a unified workflow for data generation, optimization, comparison, and visualization.