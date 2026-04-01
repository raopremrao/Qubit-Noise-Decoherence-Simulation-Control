import numpy as np
from qutip import *

def lindblad_evolution(H, psi0, c_ops, tlist):
    # 1. Convert initial state to density matrix
    rho0 = ket2dm(psi0)

    # 2. Solve the master equation
    result = mesolve(H,rho0, tlist, c_ops, [])

    # 3. Return the states
    return result.states