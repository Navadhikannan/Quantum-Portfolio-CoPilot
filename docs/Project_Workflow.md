# Project Workflow

## Overview

The Quantum Portfolio CoPilot follows a structured workflow that integrates classical optimization and quantum optimization into a single application. Each module performs a dedicated task and passes its output to the next stage, resulting in a complete end-to-end portfolio optimization pipeline.

---

# 🔄 Project Workflow

## Overview

The Quantum Portfolio CoPilot follows a structured hybrid workflow that integrates classical optimization and quantum optimization into a single portfolio optimization framework.

---

## Workflow Diagram

<p align="center">
  <img src="assets/workflow.png">
       alt="Quantum Portfolio CoPilot Workflow"
       width="100%">
</p>

---

## Workflow Description

The project executes the following stages sequentially:

1. **Synthetic Dataset Generation**
   - Generate asset information
   - Generate expected returns
   - Generate transaction costs
   - Generate correlation matrix
   - Generate covariance matrix

2. **Classical Portfolio Optimization**
   - Apply the SLSQP optimization algorithm
   - Calculate optimal portfolio weights
   - Evaluate portfolio performance

3. **QUBO Construction**
   - Convert the portfolio optimization problem into a Quadratic Unconstrained Binary Optimization (QUBO) formulation

4. **Quantum Portfolio Optimization**
   - Build the Quadratic Program
   - Convert to QUBO
   - Execute QAOA
   - Optimize using COBYLA
   - Sample using the Statevector Sampler

5. **Portfolio Comparison**
   - Compare expected return
   - Compare portfolio risk
   - Compare Sharpe ratio
   - Compare selected assets

6. **Interactive Dashboard**
   - Display portfolio metrics
   - Visualize comparison charts
   - Show asset allocation
   - Export optimization results

   

# Workflow Stages

The project execution consists of the following stages:

## Stage 1 – Synthetic Dataset Generation

The workflow begins by generating a synthetic financial dataset containing information about multiple investment assets.

The generated dataset includes:

- Asset ID
- Asset Name
- Asset Class
- Expected Return
- Transaction Cost
- Correlation Matrix
- Covariance Matrix

Output Files:

- `synthetic_assets.csv`
- `correlation_matrix.csv`
- `covariance_matrix.csv`

---

## Stage 2 – Classical Portfolio Optimization

The generated dataset is processed using the Sequential Least Squares Programming (SLSQP) optimizer.

The optimizer determines the portfolio weights while satisfying:

- Total weight constraint
- Individual asset weight limits
- Asset-class allocation constraints

Output File:

- `optimized_portfolio.csv`

---

## Stage 3 – Portfolio Performance Evaluation

The optimized portfolio is evaluated using standard financial metrics.

The calculated metrics include:

- Expected Return
- Portfolio Risk
- Sharpe Ratio

These metrics are later used for comparison with the quantum optimization results.

---

## Stage 4 – QUBO Construction

The portfolio optimization problem is transformed into a Quadratic Unconstrained Binary Optimization (QUBO) formulation.

The QUBO model combines:

- Expected Return
- Portfolio Risk
- Transaction Cost

Output File:

- `qubo_matrix.csv`

---

## Stage 5 – Quantum Portfolio Model

The QUBO formulation is converted into a Quadratic Program using the Qiskit Optimization library.

The optimization model includes:

- Binary decision variables
- Objective function
- Asset selection constraint

---

## Stage 6 – Quantum Optimization

The Quantum Approximate Optimization Algorithm (QAOA) is executed using:

- Statevector Sampler
- COBYLA Optimizer

The optimization process identifies the optimal subset of assets according to the defined objective function.

Output File:

- `quantum_portfolio.csv`

---

## Stage 7 – Portfolio Comparison

The results from the classical and quantum optimization modules are compared.

The comparison includes:

- Expected Return
- Portfolio Risk
- Sharpe Ratio
- Number of Selected Assets

Output File:

- `comparison_results.csv`

---

## Stage 8 – Dashboard Visualization

The generated CSV files are loaded into the Streamlit dashboard.

The dashboard presents:

- Portfolio Metrics
- Performance Summary
- Comparison Charts
- Portfolio Allocation Pie Charts
- Portfolio Tables
- Downloadable Results

---

# Input Files

The project uses the following input files:

|         File            |    Description    |
|------------------------|--------------------|
| synthetic_assets.csv   | Asset dataset      |
| covariance_matrix.csv  | Covariance matrix  |
| correlation_matrix.csv | Correlation matrix |

---

# Output Files

The project generates:

|         File            |        Description             |
|-------------------------|--------------------------------|
| optimized_portfolio.csv | Classical optimization results |
| qubo_matrix.csv         | QUBO matrix                    |
| quantum_portfolio.csv   | Quantum optimization results   |
| comparison_results.csv  | Performance comparison         |

---

# End-to-End Execution

The overall workflow is summarized below:

1. Generate the synthetic financial dataset.
2. Perform classical portfolio optimization.
3. Evaluate classical portfolio performance.
4. Construct the QUBO formulation.
5. Build the quantum optimization model.
6. Execute QAOA.
7. Generate the quantum portfolio.
8. Compare classical and quantum results.
9. Visualize the results through the Streamlit dashboard.

---

# Summary

The modular workflow enables seamless integration of classical optimization, quantum optimization, performance analysis, and interactive visualization. The architecture also allows future extensions with larger datasets, additional optimization techniques, and execution on quantum hardware.