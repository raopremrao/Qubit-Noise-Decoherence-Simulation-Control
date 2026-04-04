"""
Quantum Noise & Decoherence Simulation Project

This module is part of the open quantum system simulation framework.
It models qubit noise, decoherence, and control using Lindblad dynamics.

Author: T PREM
Project: Quantum Noise and Control Simulator
"""

import matplotlib.pyplot as plt
from utils.file_utils import ensure_directory

def plot_optimal_pulse(pulse):
    """
    Plot the optimized control pulse amplitude versus time step.

    Physics:
    The control pulse u(t) modifies the system Hamiltonian:
        H(t) = H0 + u(t) Hc

    The optimized pulse is obtained using numerical optimization
    to maximize state fidelity or minimize decoherence effects.

    This plot shows how the control field amplitude changes over time,
    which is useful for analyzing pulse shaping and quantum control strategies.

    Parameters
    ----------
    pulse : array
        Optimized pulse amplitudes at each time step.

    Returns
    -------
    None
        Displays the pulse amplitude plot.
    """
    plt.figure()
    plt.plot(pulse)
    plt.xlabel("Time Step")
    plt.ylabel("Pulse Amplitude")
    plt.title("Optimized Control Pulse")
    plt.grid(True)
    ensure_directory("results/plots")
    plt.savefig("results/plots/optimal_pulse.png")
    # plt.show()