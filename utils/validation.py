import numpy as np
from qutip import Qobj

def validate_noise_strength(gamma):
    if not isinstance(gamma, (int, float)):
        raise TypeError("Noise strength gamma must be a number.")
    if gamma < 0:
        raise ValueError("Noise strength gamma must be >= 0.")

def validate_time_list(tlist):
    if not isinstance(tlist, np.ndarray):
        raise TypeError("tlist must be a list or numpy array.")
    if len(tlist) < 2:
        raise ValueError("tlist must contain multiple time points.")
    if np.any(np.diff(tlist) <= 0):
        raise ValueError("tlist must be strictly increasing.")
    
def validate_quantum_state(state):
    if not isinstance(state, Qobj):
        raise TypeError("Quantum state must be a Qobj.")

def validate_collapse_ops(c_ops):
    if not isinstance(c_ops, list):
        raise TypeError("Collapse operators must be provided as a list.")