from qutip import *
import numpy as np

def depolarizing_noise(gamma):
    '''
    Depolarizing noise model.

    Physics:
    Depolarizing noise randomly applies Pauli errors X, Y, Z,
    pushing the qubit towards a maximally mixed state.

    Collapse Operator:
        sqrt(gamma) * sigma_x
        sqrt(gamma) * sigma_y
        sqrt(gamma) * sigma_z

    Parameters
    ----------
    gamma : float
        Depolarizing rate.
    
    Returns
    -------
    qutip.Qobj
        List of collapse operators for depolarizing noise
    '''
    return [
        np.sqrt(gamma) * sigmax(),
        np.sqrt(gamma) * sigmay(),
        np.sqrt(gamma) * sigmaz()
    ]