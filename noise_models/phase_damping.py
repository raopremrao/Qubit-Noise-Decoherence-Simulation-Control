import numpy as np
from qutip import *

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
    sz = sigmaz()
    return np.sqrt(gamma) * sz