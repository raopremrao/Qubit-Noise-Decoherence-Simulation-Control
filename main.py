"""
Quantum Noise & Decoherence Simulation Project

This module is part of the open quantum system simulation framework.
It models qubit noise, decoherence, and control using Lindblad dynamics.

Author: T PREM
Project: Quantum Noise and Control Simulator
"""

import numpy as np
from qutip import *
from simulation.lindblad_solver import lindblad_evolution
from noise_models.amplitude_damping import amplitude_damping
from noise_models.phase_damping import phase_damping
from visualization.bloch_sphere import plot_bloch
from visualization.fidelity_plot import plot_fidelity
from simulation.decoherence import simulate_T1, simulate_T2
from simulation.noise_analysis import fidelity_vs_noise, compare_noise_models
from control.control_analysis import compare_control_pulse
from control.optimal_control import optimize_pulse
from control.plot_optimal_pulse import plot_optimal_pulse
from control.fidelity_comparison import compare_fidelity_with_without_control
from utils.logger import log



log("Simulation started by main.py")
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

# Plot
# plot_bloch(states)
plot_fidelity(states, ket2dm(target))

simulate_T1()
simulate_T2()

fidelity_vs_noise("amplitude")
fidelity_vs_noise("phase")
fidelity_vs_noise("depolarizing")

compare_noise_models()

compare_control_pulse()


noise = [amplitude_damping(0.2)]
target = ket2dm(basis(2, 1))

pulse = optimize_pulse(noise, target)
# print(pulse)
plot_optimal_pulse(pulse)


compare_fidelity_with_without_control(pulse, noise)


log("Simulation Completed")