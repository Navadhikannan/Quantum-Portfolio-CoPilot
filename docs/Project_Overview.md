# Quantum Portfolio CoPilot

## Project Overview

Quantum Portfolio CoPilot is a hybrid portfolio optimization application that compares Classical Portfolio Optimization with Quantum Portfolio Optimization using the Quantum Approximate Optimization Algorithm (QAOA).

The project demonstrates how quantum computing techniques can be applied to financial portfolio optimization by formulating the portfolio selection problem as a Quadratic Unconstrained Binary Optimization (QUBO) problem and solving it using Qiskit. Alongside the quantum approach, a classical optimization method based on the Sequential Least Squares Programming (SLSQP) algorithm is implemented to provide a performance comparison.

An interactive Streamlit dashboard is included to visualize optimization results, portfolio allocation, performance metrics, and comparisons between the classical and quantum solutions.

---

# Problem Statement

Portfolio optimization is a fundamental problem in finance that aims to maximize investment returns while minimizing risk under a set of investment constraints.

Traditional optimization algorithms become computationally expensive as the number of assets and constraints increases. Quantum optimization algorithms provide an alternative approach by exploring multiple solution states simultaneously and solving combinatorial optimization problems through quantum-inspired techniques.

This project investigates the applicability of QAOA for portfolio optimization and compares its performance with a classical optimization approach.

---

# Objectives

The primary objectives of this project are:

- Design a classical portfolio optimization model using the SLSQP algorithm.
- Develop a QUBO formulation suitable for quantum optimization.
- Implement a Quantum Portfolio Optimizer using QAOA.
- Compare classical and quantum optimization results.
- Visualize portfolio performance through an interactive dashboard.
- Demonstrate the practical use of quantum computing in financial optimization.

---

# Key Features

- Classical Portfolio Optimization
- Quantum Portfolio Optimization using QAOA
- QUBO Model Generation
- Risk and Return Analysis
- Portfolio Performance Comparison
- Interactive Streamlit Dashboard
- Portfolio Allocation Visualization
- Downloadable Optimization Results

---

# Technologies Used

## Programming Language

- Python

## Quantum Computing

- Qiskit
- Qiskit Optimization
- QAOA
- COBYLA Optimizer

## Classical Optimization

- SciPy
- NumPy

## Data Processing

- Pandas

## Visualization

- Plotly
- Streamlit

---

# Project Workflow

The project follows the workflow below:

1. Generate synthetic financial asset data.
2. Perform classical portfolio optimization.
3. Construct the QUBO formulation.
4. Build the Quantum Portfolio Model.
5. Solve the optimization problem using QAOA.
6. Compare classical and quantum results.
7. Visualize the results using the Streamlit dashboard.

---

# Expected Outcomes

The project demonstrates:

- Classical portfolio optimization using mathematical optimization techniques.
- Quantum optimization using QAOA.
- Comparative analysis of classical and quantum portfolio strategies.
- Interactive visualization of optimization results.
- A modular framework that can be extended to larger datasets and future quantum hardware.

---

# Project Status

Current Version: **2.0**

Status: **Completed**

Modules Completed:

- Dataset Generator
- Classical Portfolio Optimizer
- Portfolio Analytics
- QUBO Builder
- Portfolio Model
- Quantum Solver
- Comparison Module
- Interactive Dashboard

---



