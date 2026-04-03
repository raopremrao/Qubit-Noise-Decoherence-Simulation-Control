# Lindblad Master Equation

The Lindblad master equation describes the evolution of an open quantum system interacting with an environment.

The density matrix evolves as:

$$dρ/dt = -i[H, ρ] + Σ (L ρ L^† - 1/2 {L^†L, ρ})$$

Where:
H = System Hamiltonian
L = Collapse operators
ρ = Density matrix

This equation models decoherence and noise in quantum systems.

In this project, we simulate qubit evolution under noise using the Lindblad equation.