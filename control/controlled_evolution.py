import numpy as np
from qutip import *
from simulation.lindblad_solver import lindblad_evolution

def run_controlled_simulation(pulse_function, noise_ops):
    tlist = np.linspace(0, 5, 200)

    sx = sigmax()
    sz = sigmaz()

    def H_t(t, args):
        return 0.5 * sx + pulse_function(t) * sz
    
    H = QobjEvo(H_t)

    psi0 = basis(2, 0)

    result = mesolve(H, psi0, tlist, noise_ops, [])

    return tlist, result.states