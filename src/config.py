
# General Settings
# ==========================================================

# Random seed for reproducible results
RANDOM_SEED = 42

# Number of synthetic assets
NUM_ASSETS = 30

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

MAX_EQUITY = 0.60
MAX_BOND = 0.40
MAX_ETF = 0.30
MAX_COMMODITY = 0.20
MIN_CASH = 0.05

# ==========================================================
# Optimization Settings
# ==========================================================

OPTIMIZER = "SLSQP"

MAX_ITERATIONS = 500

TOLERANCE = 1e-8

# ==========================================================
# File Paths
# ==========================================================

DATA_FOLDER = "data"

ASSET_DATA_FILE = "synthetic_assets.csv"
CORRELATION_FILE = "correlation_matrix.csv"
COVARIANCE_FILE = "covariance_matrix.csv"

RESULT_FOLDER = "results"
OUTPUT_PORTFOLIO = "optimized_portfolio.csv"