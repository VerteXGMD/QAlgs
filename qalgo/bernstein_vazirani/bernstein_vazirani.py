from qiskit import QuantumCircuit
from qiskit.circuit import Gate

def BernsteinVaziraniOracleCircuit(n: int, bstring: int) -> QuantumCircuit:
        oracle_circuit = QuantumCircuit(n + 1) 

        for i in range(n):
            if (bstring >> i) & 1:
                oracle_circuit.cx(i, n)

        return oracle_circuit

def BernsteinVaziraniOracle(n: int, bstring: int) -> Gate:
    return BernsteinVaziraniOracleCircuit(n, bstring).to_gate(label = r"$U_f$")

def BernsteinVaziraniCircuit(n: int, oracle: Gate) -> QuantumCircuit:
    circuit = QuantumCircuit(n + 1, n + 1)
    circuit.x(n)
    circuit.h([i for i in range(0, n + 1)])

    circuit.append(oracle, [i for i in range(0, n + 1)])

    circuit.h([i for i in range(0, n)])

    circuit.measure([i for i in range(0, n)], 
        [i for i in range(0, n)])

    return circuit
