"""
Quantum Noise & Decoherence Simulation Project

This module is part of the open quantum system simulation framework.
It models qubit noise, decoherence, and control using Lindblad dynamics.

Author: T PREM
Project: Quantum Noise and Control Simulator
"""

"""
State Evolution Module

This module contains functions for simulating quantum state evolution
under different Hamiltonians, noise models, and control pulses.
"""

import numpy as np
from qutip import *
from simulation.lindblad_solver import lindblad_evolution

def evolve_state(H, psi0, c_ops, T=5, steps=200):
    """
    Simulate quantum state evolution under a Hamiltonian and noise.

    Physics:
    The system evolves according to the Lindblad master equation:
            drho/dt = -i[H, rho] + sum (L rho L^dagger - 0.5 {L^dagger L, rho})
        
    Parameters
    ----------
    H : qutip.Qobj
        System Hamiltonian.
    psi0 : qutip.Qobj
        Initial state.
    c_ops : list
        Collapse operators representing noise.
    T : float
        Total simulation time.
    steps : int
        Number of time steps.

    Returns
    -------
    tlist : array
        Time points.
    states : list
        Density matrices over time.
    """

    tlist = np.linspace(0, T, steps)
    states = lindblad_evolution(H, psi0, c_ops, tlist)
    return tlist, states

def evolve_without_noise(H, psi0, T=5, steps=200):
    """
    Simulate unitary evolution without noise.

    Schrodinger equation:
        d|psi>/dt = -i H |psi>

    Used for comparison with noisy evolution.
    """

    tlist = np.linspace(0, T, steps)
    result = sesolve(H, psi0, tlist)
    return tlist, result.states

def compute_bloch_components(states):
    """
    Compute Bloch sphere components for a list of states.

    Bloch vector:
        x = <sigma_x>
        y = <sigma_y>
        z = <sigma_z>

    Returns
    -------
    bx, by, bz : array
        Bloch vector components over time.
    """

    bx = []
    by = []
    bz = []

    for rho in states:
        bx.append(expect(sigmax(), rho))
        by.append(expect(sigmay(), rho))
        bz.append(expect(sigmaz(), rho))

    return bx, by, bz

def compute_fidelity_over_time(states, target):
    """
    Compute fidelity between evolving states and target state.

    Fidelity:
        F = |<sigma_target | sigma>|^2
    """
    return [fidelity(state, target) for state in states]