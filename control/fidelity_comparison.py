import numpy as np
import matplotlib.pyplot as plt
from qutip import *
from simulation.lindblad_solver import lindblad_evolution

def compare_fidelity_with_without_control(pulse, noise_ops):
    N = len(pulse)
    T = 5
    tlist = np.linspace(0, T, N)

    sx = sigmax()
    sz = sigmaz()
    psi0 = basis(2, 0)
    target = ket2dm(basis(2, 1))

    # Without control
    H = 0.5 * sx
    states_no_control = lindblad_evolution(H, psi0, noise_ops, tlist)
    fid_no = [fidelity(s, target) for s in states_no_control]

    # With control
    H_list = []
    for i in range(N):
        H = 0.5 * sx + pulse[i] * sz
        H_list.append(H)

    result = mesolve(H_list, psi0, tlist, noise_ops, [])
    fid_control = [fidelity(s, target) for s in result.states]

    plt.figure()
    plt.plot(tlist, fid_no, label="No Control")
    plt.plot(tlist, fid_control, label="With Optimal Control")
    plt.xlabel("Time")
    plt.ylabel("Fidelity")
    plt.title("Fidelity Improvement with Optimal Control")
    plt.legend()
    plt.grid(True)
    plt.savefig("results/plots/fidelity_comparison.png")
    # plt.show()