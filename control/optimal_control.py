"""
Quantum Noise & Decoherence Simulation Project

This module is part of the open quantum system simulation framework.
It models qubit noise, decoherence, and control using Lindblad dynamics.

Author: T PREM
Project: Quantum Noise and Control Simulator
"""

import numpy as np
from qutip import *
from scipy.optimize import minimize

def optimize_pulse(noise_ops, target_state):
    """
    Optimize control pulse to maximize quantum state fidelity.

    Physics:
    The goal is to find a control pulse u(t) such that the final
    quantum state is as close as possible to the target state.

    The system evolves under:
        H(t) = H0 + u(t) Hc

    The optimization minimizes the cost function:
        Cost = 1 - Fidelity

    This is a basic quantum optimal control problem used in
    quantum gate design and noise mitigation.

    Parameters
    ----------
    noise_ops : list
        Collapse operators representing noise.
    target_state : qutip.Qobj
        Desired target quantum state.

    Returns
    -------
    pulse : array
        Optimized pulse amplitudes.
    """

    if not isinstance(noise_ops, list):
        raise TypeError("noise_ops must be a list of collapse operators.")
    if not isinstance(target_state, Qobj):
        raise TypeError("target_state must be a Qobj.")

    N = 80
    T = 5
    tlist = np.linspace(0, T, N)

    sx = sigmax()
    sz = sigmaz()
    psi0 = basis(2, 0)

    def fidelity_cost(pulse):

        if len(pulse) == 0:
            raise ValueError("Pulse array cannot be empty.")

        pulse = np.clip(pulse, -5, 5)  # limit amplitude

        H_list = []
        for i in range(N):
            H = 0.5 * sx + pulse[i] * sz
            H_list.append(H)

        result = mesolve(H_list, psi0, tlist, noise_ops, [])
        final_state = result.states[-1]

        fid = fidelity(final_state, target_state)

        # smoothness penalty
        smooth_penalty = np.sum(np.diff(pulse)**2)

        return 1 - fid + 0.01 * smooth_penalty

    initial_pulse = np.zeros(N)

    result = minimize(
        fidelity_cost,
        initial_pulse,
        method='Powell'
    )

    return np.clip(result.x, -5, 5)