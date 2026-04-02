import numpy as np
import matplotlib.pyplot as plt
from qutip import *

def simulate_T1(T1=2, total_time=5):
    tlist = np.linspace(0, total_time, 200)

    H = 0 * sigmaz()
    psi0 = basis(2, 1) # Excited state

    gamma = 1 / T1
    c_ops = [np.sqrt(gamma) * destroy(2)]

    result = mesolve(H, psi0, tlist, c_ops, [])

    excited_pop = [expect(basis(2, 1)*basis(2, 1).dag(), state) for state in result.states]

    plt.figure()
    plt.plot(tlist, excited_pop)
    plt.xlabel("Time")
    plt.ylabel("Excited State Population")
    plt.title("T1 Relaxtion")
    plt.grid(True)
    plt.show()