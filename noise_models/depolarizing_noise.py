from qutip import *
import numpy as np

def depolarizing_noise(gamma):
    return [
        np.sqrt(gamma) * sigmax(),
        np.sqrt(gamma) * sigmay(),
        np.sqrt(gamma) * sigmaz()
    ]