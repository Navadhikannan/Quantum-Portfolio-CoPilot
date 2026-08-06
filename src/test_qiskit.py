from qiskit_optimization import QuadraticProgram

def main():
    qp = QuadraticProgram("Portfolio_Test")

    # Create 5 binary variables
    for i in range(5):
        qp.binary_var(name=f"x{i}")

    print("=" * 50)
    print("Quadratic Program Created Successfully")
    print("=" * 50)

    print(qp.prettyprint())


if __name__ == "__main__":
    main()