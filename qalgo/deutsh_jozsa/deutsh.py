from qiskit import QuantumCircuit
from qiskit.circuit import Gate

def DeutshConstantOracleCircuit(a: bool) -> Gate:
    oracle_circuit = QuantumCircuit(2) 
    if a:
        oracle_circuit.x(1)

    return oracle_circuit

def DeutshConstantOracle(a: bool) -> Gate:
    return DeutshConstantOracleCircuit(a).to_gate(label = r"$U_f$")

def DeutshCircuit(oracle: Gate) -> QuantumCircuit:
    circuit = QuantumCircuit(2, 2)
    circuit.x(1)
    circuit.h([0, 1])

    circuit.append(oracle, [0, 1])

    circuit.h(0)
    circuit.measure(0, 0)

    return circuit
