
# General Settings
# ==========================================================

# Random seed for reproducible results
RANDOM_SEED = 42

# Number of synthetic assets
NUM_ASSETS = 30

# Classical optimization uses all assets
CLASSICAL_NUM_ASSETS = 30

# Quantum optimization uses a subset
QUANTUM_NUM_ASSETS = 15

# ==========================================================
# Portfolio Constraints
# ==========================================================

# Portfolio weights must sum to 100%
TOTAL_WEIGHT = 1.0

# Minimum and maximum allocation allowed per asset
MIN_WEIGHT = 0.0
MAX_WEIGHT = 0.20

# Allow negative weights (short selling)?
ALLOW_SHORT_SELLING = False

# ==========================================================
# Risk Preference
# ==========================================================

# Higher value = lower risk portfolio
# Lower value = higher return portfolio
RISK_AVERSION = 0.50

# ==========================================================
# Asset Class Allocation Limits
# ==========================================================

ASSET_CLASS_LIMITS = {
    "Equity": {"min": 0.30, "max": 0.60},
    "Bond": {"min": 0.10, "max": 0.40},
    "ETF": {"min": 0.05, "max": 0.30},
    "Commodity": {"min": 0.00, "max": 0.20},
    "Cash": {"min": 0.05, "max": 0.10},
}

# ==========================================================
# Optimization Settings
# ==========================================================

OPTIMIZER = "SLSQP"

MAX_ITERATIONS = 500

TOLERANCE = 1e-8

# ==========================================================
# QUBO Settings
# ==========================================================

QUBO_SETTINGS = {
    # Portfolio objective weights
    "return_weight": 1.00,
    "risk_weight": 0.50,
    "transaction_cost_weight": 0.20,

    # Quantum optimization parameters
    "risk_aversion": 0.50,

    # Penalty parameters
    "constraint_penalty": 10.0,
    "selection_penalty": 5.0,
}

# ==========================================================
# File Paths
# ==========================================================

DATA_FOLDER = "data"
RESULT_FOLDER = "results"

ASSET_DATA_FILE = f"{DATA_FOLDER}/synthetic_assets.csv"
CORRELATION_FILE = f"{DATA_FOLDER}/correlation_matrix.csv"
COVARIANCE_FILE = f"{DATA_FOLDER}/covariance_matrix.csv"

OUTPUT_PORTFOLIO = f"{RESULT_FOLDER}/optimized_portfolio.csv"
QUBO_MATRIX_FILE = f"{DATA_FOLDER}/qubo_matrix.csv"
QUANTUM_RESULTS_FILE = f"{RESULT_FOLDER}/quantum_portfolio.csv"