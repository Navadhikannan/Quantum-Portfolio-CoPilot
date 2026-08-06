# Dashboard

## Overview

The Quantum Portfolio CoPilot dashboard is developed using **Streamlit** to provide an interactive interface for visualizing and comparing the results of Classical Portfolio Optimization and Quantum Portfolio Optimization.

The dashboard allows users to analyze portfolio performance, compare optimization results, visualize asset allocations, and download generated result files.

---

# Dashboard Features

The dashboard includes the following components:

- Portfolio Metrics
- Performance Summary
- Comparison Table
- Return Comparison Chart
- Risk Comparison Chart
- Sharpe Ratio Comparison
- Portfolio Allocation Pie Charts
- Classical Portfolio Table
- Quantum Portfolio Table
- Download Results
- Project Information

---

# Dashboard Layout

The dashboard is organized into the following sections:

## 1. Header

The header provides the project title and a brief description of the application.

Information displayed:

- Project Name
- Project Description
- About Project (Expandable Section)

---

## 2. Sidebar

The sidebar provides project-related information and quick statistics.

Contents:

- Navigation
- Technologies Used
- Total Assets
- Quantum Assets
- Selected Assets
- Quantum Algorithm

---

## 3. Portfolio Metrics

Key Performance Indicators (KPIs) are displayed at the top of the dashboard.

Metrics include:

- Expected Return
- Portfolio Risk
- Sharpe Ratio
- Number of Classical Assets
- Number of Quantum Assets

These metrics provide a quick comparison between the two optimization methods.

---

## 4. Performance Summary

The dashboard highlights the better-performing optimization method for:

- Expected Return
- Portfolio Risk
- Sharpe Ratio
- Portfolio Diversification

This section allows users to quickly identify the strengths of each optimization approach.

---

## 5. Comparison Table

A tabular comparison is provided for the following metrics:

|-----------------|
| Metric          |
|-----------------|
| Expected Return |
| Portfolio Risk  |
| Sharpe Ratio    |
| Selected Assets |
|-----------------|

The table compares Classical and Quantum optimization results side by side.

---

## 6. Performance Charts

Interactive Plotly charts visualize:

### Expected Return Comparison

Compares the expected portfolio return obtained by the classical and quantum optimizers.

### Portfolio Risk Comparison

Displays the portfolio risk for both optimization approaches.

### Sharpe Ratio Comparison

Compares the risk-adjusted performance of the two portfolios.

---

## 7. Portfolio Allocation

Pie charts visualize the asset allocation for:

- Classical Portfolio
- Quantum Portfolio

These charts illustrate how assets are distributed across different asset classes.

---

## 8. Portfolio Tables

Detailed portfolio information is displayed separately for:

### Classical Portfolio

Includes:

- Asset ID
- Asset Name
- Asset Class
- Portfolio Weight

### Quantum Portfolio

Includes:

- Asset ID
- Asset Name
- Asset Class
- Portfolio Weight

---

## 9. Download Section

Users can download:

- Classical Portfolio Results
- Quantum Portfolio Results
- Comparison Results

All files are exported in CSV format.

---

# Technologies Used

The dashboard is developed using:

- Streamlit
- Plotly
- Pandas

---

# Dashboard Workflow

The dashboard performs the following operations:

1. Load generated CSV result files.
2. Calculate portfolio metrics.
3. Display key performance indicators.
4. Visualize portfolio comparisons.
5. Present asset allocation charts.
6. Display detailed portfolio tables.
7. Allow users to download optimization results.

---

# Summary

The dashboard provides a user-friendly interface for comparing Classical Portfolio Optimization with Quantum Portfolio Optimization. It integrates performance metrics, interactive visualizations, portfolio allocation charts, and downloadable reports into a single application, making the optimization results easy to interpret and analyze.