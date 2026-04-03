# Quantum Noise Models

This project simulates three types of noise:

## 1. Amplitude Damping
Represents energy loss from excited state to ground state.
Related to T1 relaxation.

Collapse operator:
$$ L = \sqrt{\gamma} * \sigma_{-} $$

## 2. Phase Damping
Represents loss of phase coherence.
Related to T2 dephasing.

Collapse operator:
$$L = \sqrt{\gamma} * \sigma_z$$

## 3. Depolarizing Noise
Randomly applies Pauli errors X, Y, Z.

This models random quantum errors in quantum computers.