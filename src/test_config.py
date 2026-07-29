from config import *

print("=" * 50)
print("Configuration Test")
print("=" * 50)

print(f"Random Seed        : {RANDOM_SEED}")
print(f"Number of Assets   : {NUM_ASSETS}")
print(f"Risk Aversion      : {RISK_AVERSION}")
print(f"Max Asset Weight   : {MAX_WEIGHT}")
print(f"Optimizer          : {OPTIMIZER}")
print(f"Result Folder      : {RESULT_FOLDER}")

print("\nConfiguration loaded successfully.")