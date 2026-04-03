"""
Quantum Noise & Decoherence Simulation Project

This module is part of the open quantum system simulation framework.
It models qubit noise, decoherence, and control using Lindblad dynamics.

Author: T PREM
Project: Quantum Noise and Control Simulator
"""

import numpy as np
from qutip import *

def lindblad_evolution(H, psi0, c_ops, tlist):
    '''
    Simulate open quantum system evolution using Lindblad master equation.

    Physics:
    The density matrix evolution is governed by the Lindblad master equation:

            drho/dt = -i[H, rho] + sum_k (L_k rho L_k^dagger - 0.5 * {L_k^dagger L_k, rho})

    Where:
        H       : System Hamiltonian
        L_K     : Collapse (noise) operators
        rho     : Density matrix

    This equation models decoherence and noise in quantum systems.
    
    Parameters
    ----------
    H : qutip.Qobj
        Hamiltonian of the system.
    psi0 : qutip.Qobj
        Initial state vector (ket).
    c_ops : list
        List of collapse operators representing noise.
    tlist : array
        Time points for simulation.

    Returns
    -------
    states : list
        List of density matrices representing system evolution.
    '''

    # 1. Convert initial state to density matrix
    rho0 = ket2dm(psi0)

    # 2. Solve the master equation
    result = mesolve(H,rho0, tlist, c_ops, [])

    # 3. Return the states(density matrices)
    return result.states