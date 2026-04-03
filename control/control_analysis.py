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
from noise_models.amplitude_damping import amplitude_damping
from control.controlled_evolution import run_controlled_simulation
from control.control_pulse import constant_pulse, sinusoidal_pulse, gaussian_pulse

def compare_control_pulse():
    """
    Compare different control pulse shapes and their effect on fidelity.

    Physics:
    Different control pulse shapes (constant, sinusoidal, gaussian)
    affect qubit evolution differently.

    The system evolves under:
        H(t) = H0 + u(t) Hc

    where u(t) is the control pulse.

    This function compares fidelity vs time for:
        - Constant pulse
        - Sinusoidal pulse
        - Gaussian pulse

    This analysis is useful in quantum control,
    pulse shaping, and gate optimization.

    Returns
    -------
    None
        Displays fidelity comparison plots.
    """
    noise = [amplitude_damping(0.2)]
    target = ket2dm(basis(2,1))

    pulses = {
        "Constant": constant_pulse,
        "Sinusodial": sinusoidal_pulse,
        "Gaussian": gaussian_pulse
    }

    plt.figure()

    for name, pulse in pulses.items():
        tlist, states = run_controlled_simulation(pulse, noise)
        fids = [fidelity(state, target) for state in states]
        plt.plot(tlist, fids, label=name)

    plt.xlabel("Time")
    plt.ylabel("Fidelity")
    plt.title("Fidelity with Control Pulses")
    plt.legend()
    plt.grid(True)
    plt.savefig("results/plots/fidelity_with_control_pulses.png")
    # plt.show()