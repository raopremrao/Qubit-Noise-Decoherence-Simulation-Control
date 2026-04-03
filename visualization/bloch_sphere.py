"""
Quantum Noise & Decoherence Simulation Project

This module is part of the open quantum system simulation framework.
It models qubit noise, decoherence, and control using Lindblad dynamics.

Author: T PREM
Project: Quantum Noise and Control Simulator
"""

from qutip import Bloch

def plot_bloch(states):
    b = Bloch()
    for rho in states:
        b.add_states(rho)
    # b.show()