"""
Quantum Noise & Decoherence Simulation Project

This module is part of the open quantum system simulation framework.
It models qubit noise, decoherence, and control using Lindblad dynamics.

Author: T PREM
Project: Quantum Noise and Control Simulator
"""

import numpy as np
from qutip import *

def run_controlled_simulation(pulse_function, noise_ops):
    '''
    Simulate qubit evolution under a time-dependent control pulse.

    Hamiltonian:
        H(t) = H0 + u(t) * Hc
    
    where:
        H0 = base Hamiltonian
        u(t) = control pulse
        Hc = control Hamiltonian
    
    Control pulses are used in quantum control to: 
        - Implement quantum gates
        - Reduce decoherence
        - Improve fidelity
        - Perform optimal control

    Parameters
    ----------
    pulse_function : function
        Function defining control pulse u(t).
    noise_ops : list
        Collapse operators representing noise.

    Returns
    -------
    tlist : array
        Time points.
    states : list
        System states over time.
    '''
    tlist = np.linspace(0, 5, 200)

    sx = sigmax()
    sz = sigmaz()

    def H_t(t, args):
        return 0.5 * sx + pulse_function(t) * sz
    
    H = QobjEvo(H_t)
    psi0 = basis(2, 0)

    result = mesolve(H, psi0, tlist, noise_ops, [])

    return tlist, result.states