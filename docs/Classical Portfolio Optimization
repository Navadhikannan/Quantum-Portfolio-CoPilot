# Classical Portfolio Optimization

## Overview

The Classical Portfolio Optimization module determines the optimal allocation of investment weights among financial assets using mathematical optimization techniques. The objective is to maximize the expected portfolio return while minimizing the associated investment risk under predefined portfolio constraints.

This module serves as the baseline for evaluating the performance of the Quantum Portfolio Optimization approach.

---

# Objective

The optimization problem is formulated to:

- Maximize Expected Portfolio Return
- Minimize Portfolio Risk
- Satisfy Portfolio Constraints

The optimization objective is represented as:

Objective = Portfolio Risk − λ × Portfolio Return

where:

- Portfolio Risk is calculated using the covariance matrix.
- Portfolio Return is calculated using the expected asset returns.
- λ (Risk Aversion) controls the balance between return and risk.

---

# Input Data

The optimizer receives the following inputs:

## Asset Dataset

The synthetic dataset contains:

- Asset ID
- Asset Name
- Asset Class
- Expected Return
- Transaction Cost

## Covariance Matrix

The covariance matrix represents the relationship between asset returns and is used to estimate overall portfolio risk.

---

# Portfolio Constraints

The optimization is performed subject to the following constraints:

## Weight Constraint

The total portfolio weight must equal 100%.

Σ wi = 1

---

## Individual Asset Limits

Each asset weight must satisfy:

Minimum Weight ≤ wi ≤ Maximum Weight

---

## Asset-Class Constraints

The portfolio allocation follows predefined limits for each asset class.

Example:

| Asset Class | Minimum | Maximum |
|-------------|---------|---------|
| Equity      | 30%     | 60%     |
| Bond        | 10%     | 40%     |
| ETF         | 5%      | 30%     |
| Commodity   | 0%      | 20%     |
| Cash        | 5%      | 10%     |

---

# Optimization Algorithm

The optimization uses the Sequential Least Squares Programming (SLSQP) algorithm available in the SciPy optimization library.

Reasons for selecting SLSQP:

- Supports equality constraints.
- Supports inequality constraints.
- Supports variable bounds.
- Efficient for continuous optimization problems.
- Widely used in financial portfolio optimization.

---

# Workflow

The classical optimization process consists of the following steps:

1. Load the asset dataset.
2. Load the covariance matrix.
3. Validate the input data.
4. Initialize equal portfolio weights.
5. Define the objective function.
6. Apply portfolio constraints.
7. Execute the SLSQP optimizer.
8. Compute portfolio performance metrics.
9. Save the optimized portfolio.

---

# Output

The optimizer produces:

- Optimized Portfolio (`optimized_portfolio.csv`)
- Portfolio Return
- Portfolio Risk
- Sharpe Ratio

---

# Advantages

- Fast execution.
- Stable convergence.
- Handles multiple constraints.
- Produces continuous asset weights.
- Well-established optimization technique.

---

# Limitations

- Performance may decrease as the number of assets and constraints increases.
- Can converge to local optima depending on the optimization landscape.
- Requires continuous decision variables and does not directly solve binary portfolio selection problems.

---

# Summary

The Classical Portfolio Optimization module provides an efficient baseline solution using the SLSQP algorithm. Its results are compared against the Quantum Portfolio Optimization module to evaluate the effectiveness of QAOA for portfolio selection.