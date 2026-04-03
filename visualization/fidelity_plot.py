"""
Quantum Noise & Decoherence Simulation Project

This module is part of the open quantum system simulation framework.
It models qubit noise, decoherence, and control using Lindblad dynamics.

Author: T PREM
Project: Quantum Noise and Control Simulator
"""

import matplotlib.pyplot as plt
from qutip import fidelity

def plot_fidelity(states, target):
    fids = [fidelity(state, target) for state in states]

    plt.figure()  # create new figure
    plt.plot(fids)
    plt.xlabel("Time")
    plt.ylabel("Fidelity")
    plt.title("Fidelity vs Time")
    plt.grid(True)
    plt.savefig("results/plots/fidelity_vs_time.png")
    # plt.show()