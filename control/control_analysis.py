import numpy as np
import matplotlib.pyplot as plt
from qutip import *
from noise_models.amplitude_damping import amplitude_damping
from control.controlled_evolution import run_controlled_simulation
from control.control_pulse import constant_pulse, sinusoidal_pulse, gaussian_pulse

def compare_control_pulse():
    noise = [amplitude_damping(0.2)]
    target = ket2dm(basis(2,1))

    pulses = {
        "Constant": constant_pulse,
        "Sinusodial": sinusoidal_pulse,
        "Gaussian": gaussian_pulse
    }

    plt.figure()

    for name, pulse in pulses.items():
        tlist, states = run_controlled_simulation(pulse, noise)
        fids = [fidelity(state, target) for state in states]
        plt.plot(tlist, fids, label=name)

    plt.xlabel("Time")
    plt.ylabel("Fidelity")
    plt.title("Fidelity with Control Pulses")
    plt.legend()
    plt.grid(True)
    plt.savefig("results/plots/fidelity_with_control_pulses.png")
    # plt.show()