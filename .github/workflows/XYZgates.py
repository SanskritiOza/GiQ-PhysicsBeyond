#Simple circuit applying Pauli-X, Pauli-Y, and Pauli-Z gates to a single qubit

from qiskit import QuantumCircuit, Aer, execute

# Create a Quantum Circuit with one qubit
qc = QuantumCircuit(1)

# Apply Pauli-X gate
qc.x(0)

# Apply Pauli-Y gate
qc.y(0)

# Apply Pauli-Z gate
qc.z(0)

# Visualize the circuit
print(qc.draw())

# Execute the circuit on the Aer simulator
backend = Aer.get_backend('statevector_simulator')
result = execute(qc, backend).result()
statevector = result.get_statevector()
print("Final statevector:", statevector)

#apply Pauli gates to multiple qubits
from qiskit import QuantumCircuit, Aer, execute

# Create a Quantum Circuit with two qubits
qc = QuantumCircuit(2)

# Apply Pauli-X gate to the first qubit
qc.x(0)

# Apply Pauli-Y gate to the second qubit
qc.y(1)

# Apply Pauli-Z gate to both qubits
qc.z(0)
qc.z(1)

# Apply CNOT gate
qc.cx(0, 1)

# Visualize the circuit
print(qc.draw())

# Execute the circuit on the Aer simulator
backend = Aer.get_backend('statevector_simulator')
result = execute(qc, backend).result()
statevector = result.get_statevector()
print("Final statevector:", statevector)
