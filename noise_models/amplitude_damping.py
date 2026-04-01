from qutip import *
import numpy as np

def amplitude_damping(gamma):
    sm = destroy(2)
    return np.sqrt(gamma) * sm