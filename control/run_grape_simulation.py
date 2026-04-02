import numpy as np
import matplotlib.pyplot as plt
from qutip import *
from control.grape_optimization import grape_optimize

def run_grape(noise_ops):
    target = basis(2, 1)

    pulse, fidelity_history = grape_optimize(noise_ops, target)

    return pulse, fidelity_history