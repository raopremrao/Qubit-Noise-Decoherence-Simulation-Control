"""
Quantum Noise & Decoherence Simulation Project

This module is part of the open quantum system simulation framework.
It models qubit noise, decoherence, and control using Lindblad dynamics.

Author: T PREM
Project: Quantum Noise and Control Simulator
"""

import matplotlib.pyplot as plt

def plot_optimal_pulse(pulse):
    plt.figure()
    plt.plot(pulse)
    plt.xlabel("Time Step")
    plt.ylabel("Pulse Amplitude")
    plt.title("Optimized Control Pulse")
    plt.grid(True)
    plt.savefig("results/plots/optimal_pulse.png")
    # plt.show()