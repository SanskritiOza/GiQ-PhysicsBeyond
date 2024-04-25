#Circuit 1: Entanglement Generation
from qiskit import QuantumCircuit

# Create a quantum circuit with 2 qubits
qc = QuantumCircuit(2)

# Apply a Hadamard gate on qubit 0
qc.h(0)

# Apply a CNOT gate with control qubit 0 and target qubit 1
qc.cx(0, 1)

# Display the circuit
print(qc.draw())

#Circuit 2: Quantum Teleportation
from qiskit import QuantumCircuit

# Create a quantum circuit with 3 qubits
qc = QuantumCircuit(3)

# Apply a Hadamard gate on qubit 0
qc.h(0)

# Apply a CNOT gate with control qubit 0 and target qubit 1
qc.cx(0, 1)

# Apply a CNOT gate with control qubit 1 and target qubit 2
qc.cx(1, 2)

# Display the circuit
print(qc.draw())

#Circuit 3: Grover's Algorithm
from qiskit import QuantumCircuit

# Create a quantum circuit with 3 qubits
qc = QuantumCircuit(3)

# Apply a Hadamard gate on all qubits
qc.h(range(3))

# Apply a CNOT gate with control qubit 0 and target qubit 1
qc.cx(0, 1)

# Apply a CNOT gate with control qubit 0 and target qubit 2
qc.cx(0, 2)

# Apply a Hadamard gate on all qubits again
qc.h(range(3))

# Apply X gate on all qubits
qc.x(range(3))

# Apply a CNOT gate with control qubit 1 and target qubit 2
qc.cx(1, 2)

# Apply a Hadamard gate on all qubits
qc.h(range(3))

# Apply X gate on all qubits
qc.x(range(3))

# Apply a CNOT gate with control qubit 0 and target qubit 1
qc.cx(0, 1)

# Apply a CNOT gate with control qubit 0 and target qubit 2
qc.cx(0, 2)

# Apply a Hadamard gate on all qubits
qc.h(range(3))

# Apply X gate on all qubits
qc.x(range(3))

# Display the circuit
print(qc.draw())
