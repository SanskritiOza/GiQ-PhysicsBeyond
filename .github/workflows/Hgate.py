#This program will create a quantum circuit with multiple qubits and apply the Hadamard gate to each qubit
from qiskit import QuantumCircuit, Aer, execute

# Define the number of qubits
num_qubits = 5

# Create a quantum circuit with the specified number of qubits
qc = QuantumCircuit(num_qubits)

# Apply Hadamard gate to each qubit
for qubit in range(num_qubits):
    qc.h(qubit)

# Visualize the circuit
print(qc)

# Simulate the circuit
simulator = Aer.get_backend('statevector_simulator')
result = execute(qc, simulator).result()
statevector = result.get_statevector()

# Print the final statevector
print("\nFinal Statevector:")
print(statevector)
