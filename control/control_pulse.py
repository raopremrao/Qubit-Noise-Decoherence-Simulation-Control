import numpy as np

# def control_hamiltonian(t, args):
#     omega = args['omega']
#     return omega * np.cos(t)

def constant_pulse(t, A=1):
    return A

def sinusodial_pulse(t, A=1, w=2):
    return A * np.sin(w * t)

def gaussian_pulse(t, A=1, mu=2.5, sigma=1):
    return A * np.exp(-(t - mu)**2 / (2 * sigma**2))