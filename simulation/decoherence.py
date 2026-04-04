"""
Quantum Noise & Decoherence Simulation Project

This module is part of the open quantum system simulation framework.
It models qubit noise, decoherence, and control using Lindblad dynamics.

Author: T PREM
Project: Quantum Noise and Control Simulator
"""

import numpy as np
import matplotlib.pyplot as plt
from qutip import *
from utils.file_utils import ensure_directory

def simulate_T1(T1=2, total_time=5):
    tlist = np.linspace(0, total_time, 200)

    H = 0 * sigmaz()
    psi0 = basis(2, 1) # Excited state

    gamma = 1 / T1
    c_ops = [np.sqrt(gamma) * destroy(2)]

    result = mesolve(H, psi0, tlist, c_ops, [])

    excited_pop = [expect(basis(2, 1)*basis(2, 1).dag(), state) for state in result.states]

    plt.figure()
    plt.plot(tlist, excited_pop)
    plt.xlabel("Time")
    plt.ylabel("Excited State Population")
    plt.title("T1 Relaxation")
    plt.grid(True)
    ensure_directory("results/plots")
    plt.savefig("results/plots/T1_relaxation.png")
    # plt.show()


def simulate_T2(T2=1, total_time=5):

    tlist = np.linspace(0, total_time, 200)

    H = 0 * sigmaz()
    psi0 = (basis(2, 0) + basis(2, 1)).unit()

    gamma = 1 / T2
    c_ops = [np.sqrt(gamma) * sigmaz()]

    result = mesolve(H, psi0, tlist, c_ops, [])

    coherence = [abs(state[0, 1]) for state in result.states]

    plt.figure()
    plt.plot(tlist, coherence)
    plt.xlabel("Time")
    plt.ylabel("Coherence |ρ01|")
    plt.title("T2 Dephasing")
    plt.grid(True)
    ensure_directory("results/plots")
    plt.savefig("results/plots/T2_dephasing.png")
    # plt.show()