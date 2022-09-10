"""
MIT License

Copyright (c) 2022 Adi Salimgereyev

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

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
