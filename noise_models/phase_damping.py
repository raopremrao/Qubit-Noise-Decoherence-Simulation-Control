"""
Quantum Noise & Decoherence Simulation Project

This module is part of the open quantum system simulation framework.
It models qubit noise, decoherence, and control using Lindblad dynamics.

Author: T PREM
Project: Quantum Noise and Control Simulator
"""

import numpy as np
from qutip import *
from utils.validation import validate_noise_strength

def phase_damping(gamma):
    '''
    Phase damping (dephasing) noise model.

    Physics:
    Phase damping causes loss of coherence without energy loss.
    Related to T2 dephasing time.

    Collapse operator:
        L = sqrt(gamma) * sigma_z

    Parameters
    ----------
    gamma : float
        Damping rate (related to T2 time).
    
    Returns
    -------
    qutip.Qobj
        Collapse operator for phase damping.
    '''

    # Validation:
    validate_noise_strength(gamma)

    sz = sigmaz()
    return np.sqrt(gamma) * sz