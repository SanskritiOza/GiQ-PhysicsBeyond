#Applying Pauli Z gate to a single qubit
from qiskit import QuantumCircuit, Aer, execute

# Create a quantum circuit with one qubit
qc = QuantumCircuit(1)

# Apply Pauli Z gate to the qubit
qc.z(0)

# Visualize the circuit
print(qc.draw())

# Simulate the circuit
backend = Aer.get_backend('statevector_simulator')
result = execute(qc, backend).result()
statevector = result.get_statevector()
print("Final statevector:", statevector)


#Applying Pauli Z gate to multiple qubits
from qiskit import QuantumCircuit, Aer, execute

# Create a quantum circuit with two qubits
qc = QuantumCircuit(2)

# Apply Pauli Z gate to both qubits
qc.z(0)
qc.z(1)

# Visualize the circuit
print(qc.draw())

# Simulate the circuit
backend = Aer.get_backend('statevector_simulator')
result = execute(qc, backend).result()
statevector = result.get_statevector()
print("Final statevector:", statevector)


#Using Pauli Z gate in a circuit with other gates
from qiskit import QuantumCircuit, Aer, execute

# Create a quantum circuit with two qubits
qc = QuantumCircuit(2)

# Apply Hadamard gate to the first qubit
qc.h(0)

# Apply Pauli Z gate to the second qubit
qc.z(1)

# Apply CNOT gate with the first qubit as control and second qubit as target
qc.cx(0, 1)

# Visualize the circuit
print(qc.draw())

# Simulate the circuit
backend = Aer.get_backend('statevector_simulator')
result = execute(qc, backend).result()
statevector = result.get_statevector()
print("Final statevector:", statevector)


#Using Pauli Z gate for measurement
from qiskit import QuantumCircuit, Aer, execute

# Create a quantum circuit with one qubit
qc = QuantumCircuit(1, 1)

# Apply Pauli Z gate to the qubit
qc.z(0)

# Measure the qubit
qc.measure(0, 0)

# Visualize the circuit
print(qc.draw())

# Simulate the circuit
backend = Aer.get_backend('qasm_simulator')
result = execute(qc, backend, shots=1024).result()
counts = result.get_counts()
print("Measurement outcome:", counts)


#Using Pauli Z gate for conditional operations

from qiskit import QuantumCircuit, Aer, execute

# Create a quantum circuit with two qubits
qc = QuantumCircuit(2, 2)

# Apply Pauli Z gate to the first qubit
qc.z(0)

# Apply conditional X gate to the second qubit based on the state of the first qubit
qc.x(1).c_if(0, 1)  # Apply X gate if first qubit is |1>

# Measure both qubits
qc.measure([0, 1], [0, 1])

# Visualize the circuit
print(qc.draw())

# Simulate the circuit
backend = Aer.get_backend('qasm_simulator')
result = execute(qc, backend, shots=1024).result()
counts = result.get_counts()
print("Measurement outcome:", counts)
