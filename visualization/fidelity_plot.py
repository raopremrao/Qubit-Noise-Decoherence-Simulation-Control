import matplotlib.pyplot as plt
from qutip import fidelity

def plot_fidelity(states, target):
    fids = [fidelity(states, target) for states in states]

    plt.figure()  # create new figure
    plt.plot(fids)
    plt.xlabel("Time")
    plt.ylabel("Fidelity")
    plt.title("Fidelity vs Time")
    plt.grid(True)
    plt.savefig("results/plots/fidelity_vs_time.png")
    # plt.show()