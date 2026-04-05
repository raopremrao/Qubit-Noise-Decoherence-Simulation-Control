# Qubit Noise, Decoherence Simulation & Control

## Overview

This project simulates how noise and decoherence affect a single qubit and explores simple control pulse methods to improve fidelity. The simulation is based on open quantum system dynamics using the Lindblad master equation. An interactive Streamlit dashboard is included to visualize qubit behavior under different noise models.

The project focuses on understanding:

* Quantum noise
* Decoherence (T1 and T2)
* Qubit state evolution
* Fidelity degradation due to noise
* Simple control pulses for error reduction
* Visualization of qubit states on the Bloch sphere

---

## Noise Models Implemented

The simulator includes the following quantum noise channels:

1. **Amplitude Damping**

   * Models energy relaxation (T1 decay)
   * Qubit decays from |1⟩ to |0⟩

2. **Phase Damping**

   * Models loss of phase coherence (T2 dephasing)
   * Does not change population, only phase

3. **Depolarizing Noise**

   * Random Pauli errors (X, Y, Z)
   * Pushes qubit toward a mixed state

---

## Decoherence Simulation

The project includes simulation of:

* **T1 Relaxation**
* **T2 Dephasing**
* Density matrix evolution
* Bloch sphere trajectory
* Bloch vector components over time

The system evolution is simulated using the Lindblad master equation.

---

## Control Pulse Simulation

Simple control pulses are implemented to study their effect on qubit fidelity:

* Constant pulse
* Sinusoidal pulse
* Gaussian pulse

These pulses modify the Hamiltonian and can improve fidelity under noise in some cases.

---

## Streamlit Interactive Simulator

The project includes an interactive Streamlit dashboard where users can:

* Select noise type
* Adjust noise strength
* Change simulation time
* Enable/disable control pulse
* Choose control pulse type
* View Bloch sphere trajectory
* View fidelity vs time
* View density matrix heatmap
* View Bloch vector components
* View fidelity vs noise strength
* Compare noise models

This allows interactive exploration of qubit noise and decoherence.

---

## Tools & Libraries Used

* Python
* NumPy
* Matplotlib
* QuTiP
* Qiskit
* Streamlit

---

## Features

* Open quantum system simulation
* Lindblad master equation simulation
* Quantum noise modeling
* Decoherence simulation (T1, T2)
* Fidelity analysis
* Bloch sphere visualization
* Density matrix visualization
* Control pulse simulation
* Interactive Streamlit dashboard

---

## Project Structure

```
project/
│
├── app/
│   └── streamlit_app.py
│
├── simulation/
├── noise_models/
├── control/
├── visualization/
├── theory/
├── results/
│   ├── plots/
│   └── data/
│
├── notebooks/
│   └── experiments.ipynb
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Run the Streamlit App

From the project root directory:

```bash
streamlit run app/streamlit_app.py
```

---

## Educational Purpose

This project is intended for learning and experimentation with:

* Quantum noise
* Decoherence
* Open quantum systems
* Quantum state visualization
* Basic quantum control concepts

---

## Future Improvements

Possible future extensions:

* Multi-qubit noise simulation
* Gate fidelity simulation
* Dynamical decoupling
* Optimal control algorithms
* Parameter sweep heatmaps
* Monte Carlo noise simulation
* Randomized benchmarking simulation

---

## Author

Project developed as a quantum computing simulation and visualization project focusing on noise, decoherence, and simple control techniques.
