import numpy as np
import matplotlib.pyplot as plt
from qutip import *

def fidelity_with_grape(pulse, noise_ops, T=5):
    N = len(pulse)
    dt = T / N
    sx = sigmax()
    sz = sigmaz()

    psi0 = basis(2, 0)
    states = [psi0]

    for i in range(N):
        H = 0.5 * sx + pulse[i] * sz
        U = (-1j * H * dt).expm()
        states.append(U * states[-1])

    target = basis(2,1)
    fids = [fidelity(s, target) for s in states]

    plt.figure()
    plt.plot(fids)
    plt.title("Fidelity with GRAPE Pulse")
    plt.xlabel("Time Step")
    plt.ylabel("Fidelity")
    plt.grid(True)
    plt.show()