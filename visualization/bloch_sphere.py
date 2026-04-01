from qutip import Bloch

def plot_bloch(states):
    b = Bloch()
    for rho in states:
        b.add_states(rho)
    b.show()