<p align="center">
  <img src="assets/banner.png" alt="Quantum Portfolio CoPilot Banner" width="100%">
</p>

<h1 align="center">⚛️ Quantum Portfolio CoPilot</h1>

<p align="center">
A Hybrid Classical–Quantum Portfolio Optimization Framework using QAOA
</p>

<p align="center">
Python • Qiskit • SciPy • Streamlit • Plotly
</p>

---

# 📖 Project Overview

Quantum Portfolio CoPilot is a hybrid portfolio optimization framework that compares **Classical Portfolio Optimization** with **Quantum Portfolio Optimization** using the **Quantum Approximate Optimization Algorithm (QAOA)**.

The project demonstrates how financial portfolio optimization problems can be formulated as a **Quadratic Unconstrained Binary Optimization (QUBO)** problem and solved using **Qiskit**. An interactive **Streamlit Dashboard** provides a visual comparison of the optimization results.

---

# ✨ Features

- 📈 Classical Portfolio Optimization (SLSQP)
- ⚛️ Quantum Portfolio Optimization (QAOA)
- 🔄 QUBO Matrix Construction
- 📊 Portfolio Performance Comparison
- 📉 Risk Analysis
- 🥧 Portfolio Allocation Charts
- 🖥 Interactive Streamlit Dashboard
- 📄 Project Documentation
- 📥 Exportable CSV Results

---

# 🏗️ System Architecture

<p align="center">
  <img src="assets/architecture.png" alt="System Architecture" width="100%">
</p>

The project follows a modular hybrid architecture integrating classical optimization, QUBO formulation, quantum optimization, comparison, and dashboard visualization.

---

# 🔄 Project Workflow

<p align="center">
<img src="assets/workflow.png"> alt="Quantum Portfolio CoPilot Workflow" width="100%">
</p>

The workflow begins with synthetic dataset generation, performs classical optimization, transforms the problem into a QUBO model, executes quantum optimization using QAOA, compares the results, and visualizes them through the Streamlit dashboard.

---

# 🛠 Technology Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| Quantum Computing | Qiskit |
| Optimization | SciPy |
| Dashboard | Streamlit |
| Visualization | Plotly |
| Data Processing | Pandas, NumPy |

---

# 📂 Project Structure

```text
Quantum-Portfolio-CoPilot/
│
├── assets/
│   ├── banner.png
│   ├── architecture.png
│   ├── workflow.png
│   └── dashboard.png
│
├── data/
│
├── docs/
│   ├── 01_Project_Overview.md
│   ├── 02_System_Architecture.md
│   ├── 03_Classical_Optimization.md
│   ├── 04_Quantum_Optimization.md
│   ├── 05_Dashboard.md
│   ├── 06_Project_Workflow.md
│   └── Quantum_Portfolio_CoPilot_Dashboard.pdf
│
├── results/
│
├── src/
│
├── dashboard.py
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/Quantum-Portfolio-CoPilot.git

cd Quantum-Portfolio-CoPilot
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

### Generate Dataset

```bash
python src/dataset_generator.py
```

### Classical Portfolio Optimization

```bash
python src/classical_optimizer.py
```

### Build QUBO Matrix

```bash
python src/qubo_builder.py
```

### Quantum Portfolio Optimization

```bash
python src/quantum_solver.py
```

### Compare Results

```bash
python src/comparison.py
```

### Launch Dashboard

```bash
python -m streamlit run dashboard.py
```

---

# 📊 Dashboard Preview

<p align="center">
  <img src="assets/dashboard.png" alt="Dashboard Preview" width="100%">
</p>

The Streamlit dashboard provides:

- Portfolio Metrics
- Performance Summary
- Expected Return Comparison
- Portfolio Risk Comparison
- Sharpe Ratio Comparison
- Portfolio Allocation Charts
- Portfolio Tables
- Downloadable Results

---

# 📈 Output Files

| File | Description |
|------|-------------|
| optimized_portfolio.csv | Classical optimization results |
| quantum_portfolio.csv | Quantum optimization results |
| comparison_results.csv | Classical vs Quantum comparison |
| qubo_matrix.csv | Generated QUBO matrix |

---

# 📚 Documentation

The complete project documentation is available in the **docs/** folder.

- 📘 Project Overview
- 🏗 System Architecture
- 📈 Classical Optimization
- ⚛️ Quantum Optimization
- 📊 Dashboard Documentation
- 🔄 Project Workflow
- 📄 Dashboard PDF

---

# 📄 License

This project is licensed under the MIT License.

---


⭐ If you found this project useful, consider giving it a star on GitHub.