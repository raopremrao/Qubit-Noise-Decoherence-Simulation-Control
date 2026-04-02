import numpy as np
from qutip import *
from scipy.optimize import minimize

def optimize_pulse(noise_ops, target_state):
    N = 80
    T = 5
    tlist = np.linspace(0, T, N)

    sx = sigmax()
    sz = sigmaz()
    psi0 = basis(2, 0)

    def fidelity_cost(pulse):
        pulse = np.clip(pulse, -5, 5)  # limit amplitude

        H_list = []
        for i in range(N):
            H = 0.5 * sx + pulse[i] * sz
            H_list.append(H)

        result = mesolve(H_list, psi0, tlist, noise_ops, [])
        final_state = result.states[-1]

        fid = fidelity(final_state, target_state)

        # smoothness penalty
        smooth_penalty = np.sum(np.diff(pulse)**2)

        return 1 - fid + 0.01 * smooth_penalty

    initial_pulse = np.zeros(N)

    result = minimize(
        fidelity_cost,
        initial_pulse,
        method='Powell'
    )

    return np.clip(result.x, -5, 5)