import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------

st.set_page_config(
    page_title="Quantum Portfolio CoPilot",
    page_icon="⚛️",
    layout="wide",
)
st.title("⚛️ Quantum Portfolio CoPilot")

st.caption(
    "Classical Portfolio Optimization vs Quantum Portfolio Optimization using QAOA"
)

st.markdown("""
This dashboard compares the performance of a **Classical Portfolio Optimizer**
and a **Quantum Portfolio Optimizer (QAOA)**.

It provides portfolio metrics, comparison charts, and selected asset allocations
to demonstrate the application of quantum computing in financial optimization.
""")

st.divider()

# ----------------------------------------------------
# About Project
# ----------------------------------------------------

with st.expander("ℹ️ About this Project"):

    st.markdown("""
### 🎯 Objective

Compare **Classical Portfolio Optimization** with
**Quantum Portfolio Optimization (QAOA)** for asset selection.

### 🛠 Technologies Used

- Python
- Qiskit
- Streamlit
- Plotly
- Pandas
- NumPy
- SciPy

### ✨ Features

- 📊 Classical Portfolio Optimization
- ⚛️ Quantum Portfolio Optimization (QAOA)
- 🔄 QUBO Formulation
- 📈 Portfolio Performance Comparison
- 🥧 Asset Allocation Visualization
- 📥 Downloadable Results

### 📁 Output Files

- `optimized_portfolio.csv`
- `quantum_portfolio.csv`
- `comparison_results.csv`
""")
    
# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

st.sidebar.title("⚛️ Quantum Portfolio CoPilot")

st.sidebar.markdown("""
### Navigation

- 🏠 Dashboard
- 📈 Classical Portfolio
- ⚛️ Quantum Portfolio
- 📊 Comparison
- ℹ️ About Project
""")

st.sidebar.divider()

st.sidebar.info(
    """
    **Project**

    Classical vs Quantum Portfolio Optimization

    Built using:

    - Python
    - Qiskit
    - Streamlit
    - Plotly
    """
)

# ----------------------------------------------------
# Project Statistics
# ----------------------------------------------------

st.sidebar.divider()

st.sidebar.subheader("📊 Project Statistics")

st.sidebar.metric(
    "Total Assets",
    "30"
)

st.sidebar.metric(
    "Quantum Assets",
    "15"
)

st.sidebar.metric(
    "Selected Assets",
    "4"
)

st.sidebar.metric(
    "Quantum Algorithm",
    "QAOA"
)

# ----------------------------------------------------
# Load Data
# ----------------------------------------------------

comparison = pd.read_csv("results/comparison_results.csv")
classical = pd.read_csv("results/optimized_portfolio.csv")
quantum = pd.read_csv("results/quantum_portfolio.csv")

# ----------------------------------------------------
# KPI Metrics
# ----------------------------------------------------

st.subheader("📊 Portfolio Metrics")

c_return = comparison.iloc[0]["Classical"]
q_return = comparison.iloc[0]["Quantum"]

c_risk = comparison.iloc[1]["Classical"]
q_risk = comparison.iloc[1]["Quantum"]

c_sharpe = comparison.iloc[2]["Classical"]
q_sharpe = comparison.iloc[2]["Quantum"]

c_assets = int(comparison.iloc[3]["Classical"])
q_assets = int(comparison.iloc[3]["Quantum"])

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "📈 Expected Return",
        f"{q_return:.4f}",
        f"{(q_return-c_return):+.4f} vs Classical"
    )

with col2:
    st.metric(
        "📉 Portfolio Risk",
        f"{q_risk:.4f}",
        f"{(q_risk-c_risk):+.4f} vs Classical"
    )

with col3:
    st.metric(
        "⚖️ Sharpe Ratio",
        f"{q_sharpe:.4f}",
        f"{(q_sharpe-c_sharpe):+.4f}"
    )

col4, col5 = st.columns(2)

with col4:
    st.metric(
        "💼 Classical Assets",
        c_assets
    )

with col5:
    st.metric(
        "⚛️ Quantum Assets",
        q_assets
    )


st.divider()

st.subheader("🏆 Performance Summary")

left, right = st.columns(2)

with left:

    if q_return > c_return:
        st.success("✅ Quantum achieved a higher expected return.")
    else:
        st.success("✅ Classical achieved a higher expected return.")

    if c_risk < q_risk:
        st.success("✅ Classical portfolio has lower risk.")
    else:
        st.success("✅ Quantum portfolio has lower risk.")

with right:

    if q_sharpe > c_sharpe:
        st.success("✅ Quantum has a better Sharpe Ratio.")
    else:
        st.success("✅ Classical has a better Sharpe Ratio.")

    if c_assets > q_assets:
        st.success("✅ Classical portfolio is more diversified.")
    else:
        st.success("✅ Quantum portfolio is more diversified.")


# ----------------------------------------------------
# Comparison Table
# ----------------------------------------------------

st.divider()

st.subheader("📋 Comparison Results")

st.dataframe(
    comparison,
    use_container_width=True
)

# Return & Risk Charts

st.divider()

st.subheader("📊 Portfolio Comparison Charts")

return_df = comparison[
    comparison["Metric"] == "Expected Return"
]

risk_df = comparison[
    comparison["Metric"] == "Portfolio Risk"
]

fig_return = px.bar(
    return_df,
    x="Metric",
    y=["Classical", "Quantum"],
    barmode="group",
    title="📈 Expected Return Comparison",
    color_discrete_sequence=["#2563EB", "#7C3AED"],
)

fig_return.update_layout(
    height=400,
    legend_title="Portfolio",
    xaxis_title="",
    yaxis_title="Return",
)

fig_risk = px.bar(
    risk_df,
    x="Metric",
    y=["Classical", "Quantum"],
    barmode="group",
    title="📉 Portfolio Risk Comparison",
    color_discrete_sequence=["#2563EB", "#7C3AED"],
)

fig_risk.update_layout(
    height=400,
    legend_title="Portfolio",
    xaxis_title="",
    yaxis_title="Risk",
)

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        fig_return,
        use_container_width=True,
    )

with col2:
    st.plotly_chart(
        fig_risk,
        use_container_width=True,
    )

    # ----------------------------------------------------
# Sharpe Ratio Chart
# ----------------------------------------------------

sharpe_df = comparison[
    comparison["Metric"] == "Sharpe Ratio"
]

fig_sharpe = px.bar(
    sharpe_df,
    x="Metric",
    y=["Classical", "Quantum"],
    barmode="group",
    title="Sharpe Ratio Comparison",
    color_discrete_sequence=["#2563EB", "#7C3AED"],
)

st.plotly_chart(
    fig_sharpe,
    use_container_width=True,
)

# ----------------------------------------------------
# Portfolio Allocation
# ----------------------------------------------------

st.divider()

st.subheader("🥧 Portfolio Allocation")

pie_col1, pie_col2 = st.columns(2)

# ==========================
# Classical Portfolio
# ==========================

with pie_col1:

    st.markdown("### 💼 Classical Portfolio")

    fig_classical = px.pie(
        classical,
        names="Asset_Class",
        values="Weight",
        title="Classical Asset Allocation",
        hole=0.45,
        color_discrete_sequence=px.colors.qualitative.Set2,
    )

    fig_classical.update_traces(
        textposition="inside",
        textinfo="percent+label",
    )

    st.plotly_chart(
        fig_classical,
        use_container_width=True,
    )

# ==========================
# Quantum Portfolio
# ==========================

with pie_col2:

    st.markdown("### ⚛️ Quantum Portfolio")

    fig_quantum = px.pie(
        quantum,
        names="Asset_Class",
        values="Weight",
        title="Quantum Asset Allocation",
        hole=0.45,
        color_discrete_sequence=px.colors.qualitative.Bold,
    )

    fig_quantum.update_traces(
        textposition="inside",
        textinfo="percent+label",
    )

    st.plotly_chart(
        fig_quantum,
        use_container_width=True,
    )


# ----------------------------------------------------
# Portfolio Tables
# ----------------------------------------------------

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("💼 Classical Portfolio")

    st.dataframe(
        classical[
            [
                "Asset_ID",
                "Asset_Name",
                "Asset_Class",
                "Expected_Return",
                "Weight",
            ]
        ],
        use_container_width=True,
    )

with right:
    st.subheader("⚛️ Quantum Portfolio")

    st.dataframe(
        quantum[
            [
                "Asset_ID",
                "Asset_Name",
                "Asset_Class",
                "Expected_Return",
                "Weight",
            ]
        ],
        use_container_width=True,
    )

    # ----------------------------------------------------
# Download Results
# ----------------------------------------------------

st.divider()

st.subheader("📥 Download Project Results")

download1, download2, download3 = st.columns(3)

# Classical Portfolio
with download1:

    with open(
        "results/optimized_portfolio.csv",
        "rb",
    ) as file:

        st.download_button(
            label="⬇ Classical Portfolio",
            data=file,
            file_name="optimized_portfolio.csv",
            mime="text/csv",
        )

# Quantum Portfolio
with download2:

    with open(
        "results/quantum_portfolio.csv",
        "rb",
    ) as file:

        st.download_button(
            label="⬇ Quantum Portfolio",
            data=file,
            file_name="quantum_portfolio.csv",
            mime="text/csv",
        )

# Comparison Results
with download3:

    with open(
        "results/comparison_results.csv",
        "rb",
    ) as file:

        st.download_button(
            label="⬇ Comparison Results",
            data=file,
            file_name="comparison_results.csv",
            mime="text/csv",
        )

        st.divider()

st.markdown(
    """
    <div style="text-align:center; color:gray;">
        <h4>⚛️ Quantum Portfolio CoPilot</h4>
        <p>Version 2.0</p>
        <p>Developed by Navadhikannan</p>
        <p>Built with Python • Qiskit • Streamlit • Plotly</p>
    </div>
    """,
    unsafe_allow_html=True,
)