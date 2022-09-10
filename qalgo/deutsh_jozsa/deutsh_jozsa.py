from qiskit import QuantumCircuit
from qiskit.circuit import Gate

def DeutshJozsaConstantOracleCircuit(n: int, a: bool) -> Gate:
    oracle_circuit = QuantumCircuit(n + 1) 
    if a:
        oracle_circuit.x(n)

    return oracle_circuit

def DeutshJozsaBalancedOracleCircuit(n: int, 
    bstring: int) -> QuantumCircuit:
        oracle_circuit = QuantumCircuit(n + 1) 

        for i in range(n):
            if (bstring >> i) & 1:
                oracle_circuit.x(i)

        for i in range(n):
            oracle_circuit.cx(i, n)

        for i in range(n):
            if (bstring >> i) & 1:
                oracle_circuit.x(i)

        return oracle_circuit

def DeutshJozsaConstantOracle(n: int, a: bool) -> Gate:
    return DeutshJozsaConstantOracleCircuit(n, 
        a).to_gate(label = r"$U_f$")

def DeutshJozsaBalancedOracle(n: int, bstring: int) -> Gate:
    return DeutshJozsaBalancedOracleCircuit(n, 
        bstring).to_gate(label = r"$U_f$")

def DeutshJozsaCircuit(n: int, oracle: Gate) -> QuantumCircuit:
    circuit = QuantumCircuit(n + 1, n + 1)
    circuit.x(n)
    circuit.h([i for i in range(0, n + 1)])

    circuit.append(oracle, [i for i in range(0, n + 1)])

    circuit.h([i for i in range(0, n)])

    circuit.measure([i for i in range(0, n)], 
        [i for i in range(0, n)])

    return circuit
