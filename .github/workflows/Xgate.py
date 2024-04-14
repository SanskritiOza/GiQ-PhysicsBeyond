#Pauli X gate on a Single Qubit

from qiskit import QuantumCircuit, Aer, execute

# Create a quantum circuit with one qubit
qc = QuantumCircuit(1, 1)

# Apply Pauli-X gate to the qubit
qc.x(0)

# Measure the qubit
qc.measure(0, 0)

# Execute the circuit on the local simulator
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend)
result = job.result()

# Get the counts
counts = result.get_counts(qc)
print(counts)

#Pauli X gate on a Multiple Qubit

from qiskit import QuantumCircuit, Aer, execute

# Create a quantum circuit with three qubits
qc = QuantumCircuit(3, 3)

# Apply Pauli-X gate to each qubit
for qubit in range(3):
    qc.x(qubit)

# Measure the qubits
for qubit in range(3):
    qc.measure(qubit, qubit)

# Execute the circuit on the local simulator
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend)
result = job.result()

# Get the counts
counts = result.get_counts(qc)
print(counts)

#Pauli-X Gate followed by Hadamard Gate

from qiskit import QuantumCircuit, Aer, execute

# Create a quantum circuit with one qubit
qc = QuantumCircuit(1, 1)

# Apply Pauli-X gate followed by Hadamard gate
qc.x(0)
qc.h(0)

# Measure the qubit
qc.measure(0, 0)

# Execute the circuit on the local simulator
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend)
result = job.result()

# Get the counts
counts = result.get_counts(qc)
print(counts)

#Pauli-X Gate in a Superposition State

from qiskit import QuantumCircuit, Aer, execute

# Create a quantum circuit with one qubit
qc = QuantumCircuit(1, 1)

# Apply Hadamard gate to create a superposition state
qc.h(0)

# Apply Pauli-X gate
qc.x(0)

# Measure the qubit
qc.measure(0, 0)

# Execute the circuit on the local simulator
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend)
result = job.result()

# Get the counts
counts = result.get_counts(qc)
print(counts)

#Pauli-X Gate with Controlled-NOT (CNOT) Gate

from qiskit import QuantumCircuit, Aer, execute

# Create a quantum circuit with two qubits
qc = QuantumCircuit(2, 2)

# Apply Pauli-X gate to the first qubit
qc.x(0)

# Apply Controlled-NOT gate with the first qubit as control and the second qubit as target
qc.cx(0, 1)

# Measure both qubits
qc.measure([0, 1], [0, 1])

# Execute the circuit on the local simulator
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend)
result = job.result()

# Get the counts
counts = result.get_counts(qc)
print(counts)

