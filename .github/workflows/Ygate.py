#Applying Pauli Y gate on a single qubit
from qiskit import QuantumCircuit, Aer, execute

# Create a Quantum Circuit with one qubit
qc = QuantumCircuit(1)

# Apply Pauli Y gate to the qubit
qc.y(0)

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator).result()
counts = result.get_counts(qc)
print(counts)

#Applying Pauli Y gate to a qubit and measuring it
from qiskit import QuantumCircuit, Aer, execute

# Create a Quantum Circuit with one qubit
qc = QuantumCircuit(1, 1)

# Apply Pauli Y gate to the qubit
qc.y(0)

# Measure the qubit
qc.measure(0, 0)

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator).result()
counts = result.get_counts(qc)
print(counts)

#Applying Pauli Y gate to multiple qubits
from qiskit import QuantumCircuit, Aer, execute

# Create a Quantum Circuit with three qubits
qc = QuantumCircuit(3)

# Apply Pauli Y gate to each qubit
for qubit in range(3):
    qc.y(qubit)

# Simulate the circuit
simulator = Aer.get_backend('statevector_simulator')
result = execute(qc, simulator).result()
statevector = result.get_statevector()
print(statevector)

#Applying Pauli Y gate controlled by another qubit
from qiskit import QuantumCircuit, Aer, execute

# Create a Quantum Circuit with two qubits
qc = QuantumCircuit(2)

# Apply Pauli Y gate controlled by qubit 0, target qubit is 1
qc.cy(0, 1)

# Simulate the circuit
simulator = Aer.get_backend('statevector_simulator')
result = execute(qc, simulator).result()
statevector = result.get_statevector()
print(statevector)

#Applying Pauli Y gate followed by Pauli Y gate on a single qubit
from qiskit import QuantumCircuit, Aer, execute

# Create a Quantum Circuit with one qubit
qc = QuantumCircuit(1)

# Apply Pauli Y gate followed by another Pauli Y gate
qc.y(0)
qc.y(0)

# Simulate the circuit
simulator = Aer.get_backend('statevector_simulator')
result = execute(qc, simulator).result()
statevector = result.get_statevector()
print(statevector)
