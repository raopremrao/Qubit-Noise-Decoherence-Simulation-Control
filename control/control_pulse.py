import numpy as np

def control_hamiltonian(t, args):
    omega = args['omega']
    return omega * np.cos(t)