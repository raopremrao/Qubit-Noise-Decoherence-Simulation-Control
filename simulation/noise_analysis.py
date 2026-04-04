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
from noise_models.amplitude_damping import amplitude_damping
from noise_models.phase_damping import phase_damping
from noise_models.depolarizing_noise import depolarizing_noise
from utils.file_utils import ensure_directory

def fidelity_vs_noise(noise_type="amplitude"):
    tlist = np.linspace(0, 5, 200)
    H = 0.5 * sigmax()
    psi0 = basis(2, 0)
    target = ket2dm(basis(2, 1))

    noise_values = np.linspace(0, 1, 20)
    fidelities = []

    for g in noise_values:
        if noise_type == "amplitude":
            c_ops = [amplitude_damping(g)]
        elif noise_type == "phase":
            c_ops = [phase_damping(g)]
        elif noise_type == "depolarizing":
            c_ops = depolarizing_noise(g)

        states = lindblad_evolution(H, psi0, c_ops, tlist)
        final_state = states[-1]
        fidelities.append(fidelity(final_state, target))

    plt.figure()
    plt.plot(noise_values, fidelities)
    plt.xlabel("Noise Strength")
    plt.ylabel("Fidelity")
    plt.title(f"Fidelity vs {noise_type} noise")
    plt.grid(True)
    ensure_directory("results/plots")
    plt.savefig(f"results/plots/{noise_type}_noise.png")
    # plt.show()


def compare_noise_models():
    tlist = np.linspace(0, 5, 200)
    H = 0.5 * sigmax()
    psi0 = basis(2, 0)
    target = ket2dm(basis(2, 1))

    noise_values = np.linspace(0, 1, 20)

    amp_fid = []
    phase_fid = []
    depol_fid = []

    for g in noise_values:
        states = lindblad_evolution(H, psi0, [amplitude_damping(g)], tlist)
        amp_fid.append(fidelity(states[-1], target))

        states = lindblad_evolution(H, psi0, [phase_damping(g)], tlist)
        phase_fid.append(fidelity(states[-1], target))

        states = lindblad_evolution(H, psi0, depolarizing_noise(g), tlist)
        depol_fid.append(fidelity(states[-1], target))

    plt.figure()
    plt.plot(noise_values, amp_fid, label="Amplitude Damping")
    plt.plot(noise_values, phase_fid, label="Phase Damping")
    plt.plot(noise_values, depol_fid, label="Depolarizing Noise")

    plt.xlabel("Noise Strength")
    plt.ylabel("Fidelity")
    plt.title("Fidelity vs Noise Type")
    plt.legend()
    plt.grid(True)
    ensure_directory("results/plots")
    plt.savefig("results/plots/compare_noise_models.png")
    # plt.show()