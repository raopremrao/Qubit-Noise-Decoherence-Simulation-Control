import numpy as np
from qutip import *

def phase_damping(gamma):
    sz = sigmaz()
    return np.sqrt(gamma) * sz