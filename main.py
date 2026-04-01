import numpy as np
from qutip import *
from simulation.lindblad_solver import lindblad_evolution
from noise_models.amplitude_damping import amplitude_damping
from noise_models.phase_damping import phase_damping
from visualization.bloch_sphere import plot_bloch
from visualization.fidelity_plot import plot_fidelity


# Time
tlist = np.linspace(0, 5, 200)

# Hamiltonian
H = 0.5 * sigmax()

# Initial state
psi0 = basis(2, 0)

# Noise Operators
c_ops = [
    amplitude_damping(0.2),
    phase_damping(0.1)
]

# Evolution
states = lindblad_evolution(H, psi0, c_ops, tlist)

# Target state
target = basis(2, 1)

# Plots
plot_bloch(states)
plot_fidelity(states, ket2dm(target))