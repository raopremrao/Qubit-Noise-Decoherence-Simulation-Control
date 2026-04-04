"""
Quantum Noise & Decoherence Simulation Project

This module is part of the open quantum system simulation framework.
It models qubit noise, decoherence, and control using Lindblad dynamics.

Author: T PREM
Project: Quantum Noise and Control Simulator
"""
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
from control.control_pulse import constant_pulse, sinusoidal_pulse, gaussian_pulse
from control.controlled_evolution import run_controlled_simulation
from utils.logger import log



log("Simulation started by streamlit")

st.set_page_config(page_title="Quantum Noise Simulator", layout="wide")

st.title("Quantum Qubit Noise & Control Simulator")

st.markdown("""
## Physics Background

This simulator models qubit evolution under noise and control using the Lindblad master equation.

The density matrix evolves as:

$$dρ/dt = -i[H, ρ] + Σ (L ρ L^† - 1/2 {L^†L, ρ})$$

Noise models included:
- Amplitude damping (T1 relaxation)
- Phase damping (T2 dephasing)
- Depolarizing noise

The simulator visualizes:
- Bloch sphere trajectory
- Fidelity vs time
- Density matrix
- Noise effects
- Control pulse effects
""")

# Sidebar
st.sidebar.header("Simulation Parameters")

noise_type = st.sidebar.selectbox(
    "Noise Type",
    ["Amplitude Damping", "Phase Damping", "Depolarizing"]
)

noise_strength = st.sidebar.slider(
    "Noise Strength",
    min_value=0.0, 
    max_value=1.0, 
    value=0.2,
    step=0.01
)

time = st.sidebar.slider(
    "Simulation Time", 
    min_value=1, 
    max_value=10, 
    value=5
)

if noise_strength > 0.8:
    st.warning("High noise regime - fidelity may drop quickly.")

use_control = st.sidebar.checkbox("Enable Control Pulse")
pulse_type = st.sidebar.selectbox("Control Pulse Type", ["Constant", "Sinusodial", "Gaussian"])

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

# With Control
try:
    if use_control:
        if pulse_type == "Constant":
            pulse_func = constant_pulse
        elif pulse_type == "Sinusodial":
            pulse_func = sinusoidal_pulse
        else:
            pulse_func = gaussian_pulse
    
        tlist, states = run_controlled_simulation(pulse_func, c_ops)
    else:
        states = lindblad_evolution(H, psi0, c_ops, tlist)
    
    target = ket2dm(basis(2, 1))
    fids = [fidelity(state, target) for state in states]

except Exception as e:
    st.error(f"Simulation error: {e}")
    st.stop()
    log(f"Simulation error: {e}")

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

# Fidelity vs Noise Strength
st.subheader("Fidelity vs Noise Strength")

noise_vals = np.linspace(0, 1, 20)
fid_noise = []

# H_noise = 0 * sigmaz() # No Driving Hamiltonian

for g in noise_vals:
    if noise_type == "Amplitude Damping":
        c_ops_temp = [amplitude_damping(g)]
    elif noise_type == "Phase Damping":
        c_ops_temp = [phase_damping(g)]
    else:
        c_ops_temp = depolarizing_noise(g)

    if use_control:
        _, states_temp = run_controlled_simulation(pulse_func, c_ops_temp)
    else:
        states_temp = lindblad_evolution(H, psi0, c_ops_temp, tlist)
        
    fid_noise.append(fidelity(states_temp[-1], target))

fig3, ax = plt.subplots()
ax.plot(noise_vals, fid_noise)
ax.axvline(x=noise_strength, color='r', linestyle='--', label=f'Current: {noise_strength}')
ax.set_xlabel("Noise Strength")
ax.set_ylabel("Fidelity")
ax.grid(True)
ax.set_title("Fidelity vs Noise Strength")
ax.legend()
st.pyplot(fig3)

# Download Plot
# st.download_button(
#     label="Download Fidelity Plot",
#     data=open("results/plots/fidelity_plot.png", "rb").read(),
#     file_name="fidelity_plot.png"
# )