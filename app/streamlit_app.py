import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from qutip import *

from noise_models.amplitude_damping import amplitude_damping
from noise_models.phase_damping import phase_damping
from noise_models.depolarizing_noise import depolarizing_noise
from simulation.lindblad_solver import lindblad_evolution

st.set_page_config(page_title="Quantum Noise Simulator", layout="wide")

st.title("Quantum Qubit Noise & Control Simulator")

# Sidebar
st.sidebar.header("Simulation Parameters")

noise_type = st.sidebar.selectbox(
    "Noise Type",
    ["Amplitude Damping", "Phase Damping", "Depolarizing"]
)

noise_strength = st.sidebar.slider("Noise Strength", 0.0, 1.0, 0.2)

time = st.sidebar.slider("Simulation Time", 1, 10, 5)

# Simulation
tlist = np.linspace(0, time, 200)
H = 0.5 * sigmax()
psi0 = basis(2, 0)

if noise_type == "Amplitude Damping":
    c_ops = [amplitude_damping(noise_strength)]
elif noise_type == "Phase Damping":
    c_ops = [phase_damping(noise_strength)]
else:
    c_ops = depolarizing_noise(noise_strength)

states = lindblad_evolution(H, psi0, c_ops, tlist)

target = basis(2, 1)
fids = [fidelity(state, target) for state in states]

# Layout
col1, col2 = st.columns(2)

# Fidelity plot
with col1:
    st.subheader("Fidelity vs Time")
    fig1, ax = plt.subplots()
    ax.plot(tlist, fids)
    ax.set_xlabel("Time")
    ax.set_ylabel("Fidelity")
    ax.grid(True)
    st.pyplot(fig1)

# Bloch sphere
with col2:
    st.subheader("Bloch Sphere Trajectory")
    fig2 = plt.figure()
    b = Bloch(fig=fig2)
    for state in states:
        b.add_states(state)
    b.render()
    st.pyplot(fig2)

# Density matrix
st.subheader("Final Density Matrix")
st.write(states[-1])

# rho = states[-1].full()
# 
# st.write("Matrix Form:")
# st.dataframe(rho)

