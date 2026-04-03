import numpy as np

def control_hamiltonian(t, args):
    omega = args['omega']
    return omega * np.cos(t)

# For Controlled Pulse:

def constant_pulse(t, A=1):
    """
    Constant control pulse.

    Represents constant driving field applied to qubit.
    """
    return A

def sinusoidal_pulse(t, A=1, w=2):
    """
    Sinusoidal control pulse.

    Used in driven qubit control and Rabi oscillations.
    """
    return A * np.sin(w * t)

def gaussian_pulse(t, A=1, mu=2.5, sigma=1):
    """
    Gaussian Control pulse.

    Commonly used in quantum gate implementation
    and pulse shaping for superconducting qubits.
    """
    return A * np.exp(-(t - mu)**2 / (2 * sigma**2))