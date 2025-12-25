# # from qiskit import Quantumqcuit, QuantumRegister, ClassicalRegister
# # # from qiskit_aer import AerSimulator

# # # for plotting
# # from matplotlib import pyplot as plt

# # qc = Quantumqcuit(2);
# # # print(qc);
# # #superposition state
# # qc.h(0);
# # # print(qc)
# # qc.cx(0,1)
# # # print(qc)

# # qc.draw("mpl")

# from qiskit import QuantumCircuit
# from qiskit.quantum_info import SparsePauliOp
# from qiskit.transpiler import generate_preset_pass_manager
# from qiskit_ibm_runtime import EstimatorV2 as Estimator
 
# # Create a new circuit with two qubits
# qc = QuantumCircuit(2)
 
# # Add a Hadamard gate to qubit 0
# qc.h(0)
 
# # Perform a controlled-X gate on qubit 1, controlled by qubit 0
# qc.cx(0, 1)
 
# # Return a drawing of the circuit using MatPlotLib ("mpl").
# # These guides are written by using Jupyter notebooks, which
# # display the output of the last line of each cell.
# # If you're running this in a script, use `print(qc.draw())` to
# # print a text drawing.
# qc.draw("mpl")


from qiskit import QuantumCircuit, ClassicalRegister
from matplotlib import pyplot as plt

c = ClassicalRegister(2)
circ = QuantumCircuit(2, 2)

circ.h(0)
circ.measure(0, 0)
circ.cx(0, 1)

circ.draw()
plt.show()
    