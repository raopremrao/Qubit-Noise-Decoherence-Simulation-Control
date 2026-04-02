import numpy as np
from qutip import *
import matplotlib.pyplot as plt

def grape_optimize(noise_ops, target_state, iterations=100, N=100, T=5):
    dt = T / N
    tlist = np.linspace(0, T, N)

    sx = sigmax()
    sz = sigmaz()

    psi0 = basis(2, 0)

    # Initialize pulse
    pulse = np.zeros(N)

    learning_rate = 0.1

    fidelity_history = []

    for it in range(iterations):
        # Forward evolution
        states = [psi0]
        for i in range(N):
            H = 0.5 * sx + pulse[i] * sz
            U = (-1j * H * dt).expm()
            states.append(U * states[-1])

        final_state = states[-1]
        fid = fidelity(final_state, target_state)
        fidelity_history.append(fid)

        # Backward evolution
        lambdas = [target_state]
        for i in reversed(range(N)):
            H = 0.5 * sx + pulse[i] * sz
            U = (-1j * H * dt).expm()
            lambdas.append(U.dag() * lambdas[-1])

        lambdas.reverse()

        # Gradient update
        for i in range(N):
            grad = (lambdas[i+1].dag() * (1j * sz * dt) * states[i]).tr().real
            pulse[i] += learning_rate * grad

        # Clip pulse
        pulse = np.clip(pulse, -3, 3)

        print(f"Iteration {it}, Fidelity {fid}")

    return pulse, fidelity_history