import matplotlib.pyplot as plt

def plot_grape_results(pulse, fidelity_history):
    plt.figure()
    plt.plot(pulse)
    plt.title("GRAPE Optimized Pulse")
    plt.xlabel("Time Step")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.savefig("results/plots/grape_optimized_pulse.png")
    # plt.show()

    plt.figure()
    plt.plot(fidelity_history)
    plt.title("Fidelity During GRAPE Optimization")
    plt.xlabel("Iteration")
    plt.ylabel("Fidelity")
    plt.grid(True)
    plt.savefig("results/plots/grape_fidelity_history.png")
    # plt.show()