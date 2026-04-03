from qutip import *
import numpy as np

def amplitude_damping(gamma):
    '''
    Amplitude damping noise model.

    Physics:
    Amplitude damping represents energy relaxation  (T1 decay),
    where the qubit decays from |1> -> |0>.

    Collapse operator:
        L = sqrt(gamma) * sigma_minus

    Parameters
    ----------
    gamma : float
        Damping rate (related to T1 time).

    Returns
    -------
    qutip.Qobj
        Collapse operator for amplitude damping.
    '''

    sm = destroy(2)
    return np.sqrt(gamma) * sm