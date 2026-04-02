import numpy as np
from qutip import *
from scipy.optimize import minimize

def optimize_pulse(noise_ops, target_states):
    N = 50
    T = 5
    dt = T / N

    sx = sigmax()
    sz = sigmaz()

    psi0 = basis(2, 0)
    tlist = np.linspace(0, T, N)

    def fidelity_cost(pulse):
        H_list = []

        for i in range(N):
            H = 0.5 * sx + pulse[i] * sz
            H_list.append(H)
        
        result = mesolve(H_list, psi0, tlist, noise_ops, [])
        # print(f"Results: {result}")
        final_state = result.states[-1]
        # print(f"final state: {final_state}")

        fid = fidelity(final_state, target_states)
        return 1 - fid # minimize
    
    initial_pulse = np.random.rand(N)

    result = minimize(fidelity_cost, initial_pulse, method='Powell')

    # print(f"Optimization Results: {result}")

    return result.x