"""
Quantum Noise & Decoherence Simulation Project

This module is part of the open quantum system simulation framework.
It models qubit noise, decoherence, and control using Lindblad dynamics.

Author: T PREM
Project: Quantum Noise and Control Simulator
"""

import numpy as np

# Simulation parameters
TIME_STEPS = 200
TOTAL_TIME = 5

T = 5
N = 80

# Noise parameters
gamma_amplitude = 0.2
gamma_phase = 0.15
gamma_depolarizing = 0.1

# Initial State
psi0 = np.array([1, 0])
