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
from simulation.lindblad_solver import lindblad_evolution
from utils.file_utils import ensure_directory

def compare_fidelity_with_without_control(pulse, noise_ops):
    """
    Compare system fidelity with and without control pulse.

    Physics:
    This function evaluates how control pulses improve
    qubit performance under noise and decoherence.

    Two simulations are performed:
        1. Evolution without control pulse
        2. Evolution with optimized control pulse

    The fidelity over time is plotted for both cases to show
    whether the control pulse improves quantum state preservation.

    This is used in quantum control and noise mitigation research.

    Parameters
    ----------
    pulse : array
        Control pulse amplitudes.
    noise_ops : list
        Collapse operators representing noise.

    Returns
    -------
    None
        Displays fidelity comparison plot.
    """
    N = len(pulse)
    T = 5
    tlist = np.linspace(0, T, N)

    sx = sigmax()
    sz = sigmaz()
    psi0 = basis(2, 0)
    target = ket2dm(basis(2, 1))

    # Without control
    H = 0.5 * sx
    states_no_control = lindblad_evolution(H, psi0, noise_ops, tlist)
    fid_no = [fidelity(s, target) for s in states_no_control]

    # With control
    H_list = []
    for i in range(N):
        H = 0.5 * sx + pulse[i] * sz
        H_list.append(H)

    result = mesolve(H_list, psi0, tlist, noise_ops, [])
    fid_control = [fidelity(s, target) for s in result.states]

    plt.figure()
    plt.plot(tlist, fid_no, label="No Control")
    plt.plot(tlist, fid_control, label="With Optimal Control")
    plt.xlabel("Time")
    plt.ylabel("Fidelity")
    plt.title("Fidelity Improvement with Optimal Control")
    plt.legend()
    plt.grid(True)
    ensure_directory("results/plots")
    plt.savefig("results/plots/fidelity_comparison.png")
    # plt.show()